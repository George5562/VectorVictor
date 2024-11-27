# Schemas


# Schemas

[Schemas](#schemas)


If you haven't yet done so, please take a minute to read thequickstartto get an idea of how Mongoose works.
If you are migrating from 7.x to 8.x please take a moment to read themigration guide.

[quickstart](index.html)

[migration guide](migrating_to_8.html)


Defining your schemaCreating a modelIdsInstance methodsStaticsQuery HelpersIndexesVirtualsAliasesOptionsWith ES6 ClassesPluggableFurther Reading

- Defining your schema

- Creating a model

- Ids

- Instance methods

- Statics

- Query Helpers

- Indexes

- Virtuals

- Aliases

- Options

- With ES6 Classes

- Pluggable

- Further Reading


## Defining your schema

[Defining your schema](#definition)


Everything in Mongoose starts with a Schema. Each schema maps to a MongoDB
collection and defines the shape of the documents within that collection.


```javascript
importmongoosefrom'mongoose';const{Schema} = mongoose;constblogSchema =newSchema({title:String,// String is shorthand for {type: String}author:String,body:String,comments: [{body:String,date:Date}],date: {type:Date,default:Date.now},hidden:Boolean,meta: {votes:Number,favs:Number}
});
```


If you want to add additional keys later, use theSchema#addmethod.

[Schema#add](api/schema.html#schema_Schema-add)


Each key in our codeblogSchemadefines a property in our documents which
will be cast to its associatedSchemaType.
For example, we've defined a propertytitlewhich will be cast to theStringSchemaType and propertydatewhich will be cast to aDateSchemaType.

`blogSchema`
[SchemaType](api/schematype.html#schematype_SchemaType)

`title`
[String](schematypes.html#strings)

`date`
`Date`

Notice above that if a property only requires a type, it can be specified using
a shorthand notation (contrast thetitleproperty above with thedateproperty).

`title`
`date`

Keys may also be assigned nested objects containing further key/type definitions
like themetaproperty above.  This will happen whenever a key's value is a POJO
that doesn't have atypeproperty.

`meta`
`type`

In these cases, Mongoose only creates actual schema paths for leaves
in the tree. (likemeta.votesandmeta.favsabove),
and the branches do not have actual paths.  A side-effect of this is thatmetaabove cannot have its own validation.  If validation is needed up the tree, a path
needs to be created up the tree - see theSubdocumentssection
for more information on how to do this.  Also read theMixedsubsection of the SchemaTypes guide for some gotchas.

`meta.votes`
`meta.favs`
`meta`
[Subdocuments](subdocs.html)

[Mixed](schematypes.html)


The permitted SchemaTypes are:


StringNumberDateBufferBooleanMixedObjectIdArrayDecimal128MapUUID

- String

- Number

- Date

- Buffer

- Boolean

- Mixed

- ObjectId

- Array

- Decimal128

- Map

- UUID


Read more aboutSchemaTypes here.

[SchemaTypes here](schematypes.html)


Schemas not only define the structure of your document and casting of
properties, they also define documentinstance methods,static Model methods,compound indexes,
and document lifecycle hooks calledmiddleware.

[instance methods](#methods)

[static Model methods](#statics)

[compound indexes](#indexes)

[middleware](middleware.html)


## Creating a model

[Creating a model](#models)


To use our schema definition, we need to convert ourblogSchemainto aModelwe can work with.
To do so, we pass it intomongoose.model(modelName, schema):

`blogSchema`
[Model](models.html)

`mongoose.model(modelName, schema)`

```javascript
constBlog= mongoose.model('Blog', blogSchema);// ready to go!
```


## Ids

[Ids](#ids)


By default, Mongoose adds an_idproperty to your schemas.

`_id`

```javascript
constschema =newSchema();

schema.path('_id');// ObjectId { ... }
```


When you create a new document with the automatically added_idproperty, Mongoose creates a new_idof type ObjectIdto your document.

`_id`
[_idof type ObjectId](https://masteringjs.io/tutorials/mongoose/objectid)

`_id`

```javascript
constModel= mongoose.model('Test', schema);constdoc =newModel();
doc._idinstanceofmongoose.Types.ObjectId;// true
```


You can also overwrite Mongoose's default_idwith your own_id.
Just be careful: Mongoose will refuse to save a top-level document that doesn't have an_id, so you're responsible for setting_idif you define your own_idpath.

`_id`
`_id`
`_id`
`_id`
`_id`

```javascript
constschema =newSchema({_id:Number// <-- overwrite Mongoose's default `_id`});constModel= mongoose.model('Test', schema);constdoc =newModel();awaitdoc.save();// Throws "document must have an _id before saving"doc._id=1;awaitdoc.save();// works
```


Mongoose also adds an_idproperty to subdocuments.
You can disable the_idproperty on your subdocuments as follows.
Mongoose does allow saving subdocuments without an_idproperty.

`_id`
`_id`
`_id`

```javascript
constnestedSchema =newSchema(
  {name:String},
  {_id:false}// <-- disable `_id`);constschema =newSchema({subdoc: nestedSchema,docArray: [nestedSchema]
});constTest= mongoose.model('Test', schema);// Neither `subdoc` nor `docArray.0` will have an `_id`awaitTest.create({subdoc: {name:'test 1'},docArray: [{name:'test 2'}]
});
```


Alternatively, you can disable_idusing the following syntax:

`_id`

```javascript
constnestedSchema =newSchema({_id:false,// <-- disable _idname:String});
```


## Instance methods

[Instance methods](#methods)


Instances ofModelsaredocuments. Documents have
many of their ownbuilt-in instance methods.
We may also define our own custom document instance methods.

`Models`
[documents](documents.html)

[built-in instance methods](api/document.html)


```javascript
// define a schemaconstanimalSchema =newSchema({name:String,type:String},
  {// Assign a function to the "methods" object of our animalSchema through schema options.// By following this approach, there is no need to create a separate TS type to define the type of the instance functions.methods: {findSimilarTypes(cb) {returnmongoose.model('Animal').find({type:this.type}, cb);
      }
    }
  });// Or, assign a function to the "methods" object of our animalSchemaanimalSchema.methods.findSimilarTypes=function(cb) {returnmongoose.model('Animal').find({type:this.type}, cb);
};
```


Now all of ouranimalinstances have afindSimilarTypesmethod available
to them.

`animal`
`findSimilarTypes`

```javascript
constAnimal= mongoose.model('Animal', animalSchema);constdog =newAnimal({type:'dog'});

dog.findSimilarTypes((err, dogs) =>{console.log(dogs);// woof});
```


Overwriting a default mongoose document method may lead to unpredictable results. Seethisfor more details.The example above uses theSchema.methodsobject directly to save an instance method. You can also use theSchema.method()helper as describedhere.Donotdeclare methods using ES6 arrow functions (=>). Arrow functionsexplicitly prevent bindingthis, so your method willnothave access to the document and the above examples will not work.

- Overwriting a default mongoose document method may lead to unpredictable results. Seethisfor more details.

- The example above uses theSchema.methodsobject directly to save an instance method. You can also use theSchema.method()helper as describedhere.

`Schema.methods`
`Schema.method()`
- Donotdeclare methods using ES6 arrow functions (=>). Arrow functionsexplicitly prevent bindingthis, so your method willnothave access to the document and the above examples will not work.

`=>`
`this`

## Statics

[Statics](#statics)


You can also add static functions to your model. There are three equivalent
ways to add a static:


Add a function property to the second argument of the schema-constructor (statics)Add a function property toschema.staticsCall theSchema#static()function

- Add a function property to the second argument of the schema-constructor (statics)

`statics`
- Add a function property toschema.statics

`schema.statics`
- Call theSchema#static()function

`Schema#static()`

```javascript
// define a schemaconstanimalSchema =newSchema({name:String,type:String},
  {// Assign a function to the "statics" object of our animalSchema through schema options.// By following this approach, there is no need to create a separate TS type to define the type of the statics functions.statics: {findByName(name) {returnthis.find({name:newRegExp(name,'i') });
      }
    }
  });// Or, Assign a function to the "statics" object of our animalSchemaanimalSchema.statics.findByName=function(name) {returnthis.find({name:newRegExp(name,'i') });
};// Or, equivalently, you can call `animalSchema.static()`.animalSchema.static('findByBreed',function(breed) {returnthis.find({ breed }); });constAnimal= mongoose.model('Animal', animalSchema);letanimals =awaitAnimal.findByName('fido');
animals = animals.concat(awaitAnimal.findByBreed('Poodle'));
```


Donotdeclare statics using ES6 arrow functions (=>). Arrow functionsexplicitly prevent bindingthis, so the above examples will not work because of the value ofthis.

`=>`
[explicitly prevent bindingthis](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions#No_binding_of_this)

`this`
`this`

## Query Helpers

[Query Helpers](#query-helpers)


You can also add query helper functions, which are like instance methods
but for mongoose queries. Query helper methods let you extend mongoose'schainable query builder API.

[chainable query builder API](queries.html)


```javascript
// define a schemaconstanimalSchema =newSchema({name:String,type:String},
  {// Assign a function to the "query" object of our animalSchema through schema options.// By following this approach, there is no need to create a separate TS type to define the type of the query functions.query: {byName(name) {returnthis.where({name:newRegExp(name,'i') });
      }
    }
  });// Or, Assign a function to the "query" object of our animalSchemaanimalSchema.query.byName=function(name) {returnthis.where({name:newRegExp(name,'i') });
};constAnimal= mongoose.model('Animal', animalSchema);Animal.find().byName('fido').exec((err, animals) =>{console.log(animals);
});Animal.findOne().byName('fido').exec((err, animal) =>{console.log(animal);
});
```


## Indexes

[Indexes](#indexes)


MongoDB supportssecondary indexes.
With mongoose, we define these indexes within ourSchemaatthepathlevelor theschemalevel.
Defining indexes at the schema level is necessary when creatingcompound indexes.

[secondary indexes](http://www.mongodb.com/docs/manual/indexes/)

`Schema`
[at](api/schematype.html#schematype_SchemaType-index)

[the](api/schematype.html#schematype_SchemaType-unique)

[path](api/schematype.html#schematype_SchemaType-sparse)

[level](api/schemadateoptions.html#schemadateoptions_SchemaDateOptions-expires)

`schema`
[compound indexes](https://www.mongodb.com/docs/manual/core/index-compound/)


```javascript
constanimalSchema =newSchema({name:String,type:String,tags: {type: [String],index:true}// path level});

animalSchema.index({name:1,type: -1});// schema level
```


SeeSchemaType#index()for other index options.

[SchemaType#index()](api/schematype.html#schematype_SchemaType-index)


When your application starts up, Mongoose automatically callscreateIndexfor each defined index in your schema.
Mongoose will callcreateIndexfor each index sequentially, and emit an 'index' event on the model when all thecreateIndexcalls succeeded or when there was an error.
While nice for development, it is recommended this behavior be disabled in production since index creation can cause asignificant performance impact.
Disable the behavior by setting theautoIndexoption of your schema tofalse, or globally on the connection by setting the optionautoIndextofalse.

[createIndex](https://www.mongodb.com/docs/manual/reference/method/db.collection.createIndex/#db.collection.createIndex)

`createIndex`
`createIndex`
`createIndex`
[significant performance impact](https://www.mongodb.com/docs/manual/core/index-creation/#index-build-impact-on-database-performance)

`autoIndex`
`false`
`autoIndex`
`false`

```javascript
mongoose.connect('mongodb://user:pass@127.0.0.1:port/database', {autoIndex:false});// ormongoose.createConnection('mongodb://user:pass@127.0.0.1:port/database', {autoIndex:false});// ormongoose.set('autoIndex',false);// oranimalSchema.set('autoIndex',false);// ornewSchema({/* ... */}, {autoIndex:false});
```


Mongoose will emit anindexevent on the model when indexes are done
building or an error occurred.

`index`

```javascript
// Will cause an error because mongodb has an _id index by default that// is not sparseanimalSchema.index({_id:1}, {sparse:true});constAnimal= mongoose.model('Animal', animalSchema);Animal.on('index',error=>{// "_id index cannot be sparse"console.log(error.message);
});
```


See also theModel#ensureIndexesmethod.

[Model#ensureIndexes](api/model.html#model_Model-ensureIndexes)


## Virtuals

[Virtuals](#virtuals)


Virtualsare document properties that
you can get and set but that do not get persisted to MongoDB. The getters
are useful for formatting or combining fields, while setters are useful for
de-composing a single value into multiple values for storage.

[Virtuals](api/schema.html#schema_Schema-virtual)


```javascript
// define a schemaconstpersonSchema =newSchema({name: {first:String,last:String}
});// compile our modelconstPerson= mongoose.model('Person', personSchema);// create a documentconstaxl =newPerson({name: {first:'Axl',last:'Rose'}
});
```


Suppose you want to print out the person's full name. You could do it yourself:


```javascript
console.log(axl.name.first+' '+ axl.name.last);// Axl Rose
```


Butconcatenatingthe first and
last name every time can get cumbersome.
And what if you want to do some extra processing on the name, likeremoving diacritics? Avirtual property getterlets you
define afullNameproperty that won't get persisted to MongoDB.

[concatenating](https://masteringjs.io/tutorials/fundamentals/string-concat)

[removing diacritics](https://www.npmjs.com/package/diacritics)

[virtual property getter](api/virtualtype.html#virtualtype_VirtualType-get)

`fullName`

```javascript
// That can be done either by adding it to schema options:constpersonSchema =newSchema({name: {first:String,last:String}
}, {virtuals: {fullName: {get() {returnthis.name.first+' '+this.name.last;
      }
    }
  }
});// Or by using the virtual method as following:personSchema.virtual('fullName').get(function() {returnthis.name.first+' '+this.name.last;
});
```


Now, mongoose will call your getter function every time you access thefullNameproperty:

`fullName`

```javascript
console.log(axl.fullName);// Axl Rose
```


If you usetoJSON()ortoObject()Mongoose willnotinclude virtuals by default.
Pass{ virtuals: true }totoJSON()ortoObject()to include virtuals.

`toJSON()`
`toObject()`
`{ virtuals: true }`
[toJSON()](api/document.html#document_Document-toJSON)

`toJSON()`
`toObject()`

```javascript
// Convert `doc` to a POJO, with virtuals attacheddoc.toObject({virtuals:true});// Equivalent:doc.toJSON({virtuals:true});
```


The above caveat fortoJSON()also includes the output of callingJSON.stringify()on a Mongoose document, becauseJSON.stringify()callstoJSON().
To include virtuals inJSON.stringify()output, you can either calltoObject({ virtuals: true })on the document before callingJSON.stringify(), or set thetoJSON: { virtuals: true }option on your schema.

`toJSON()`
[JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)

`JSON.stringify()`
[JSON.stringify()callstoJSON()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description)

`JSON.stringify()`
`toJSON()`
`JSON.stringify()`
`toObject({ virtuals: true })`
`JSON.stringify()`
`toJSON: { virtuals: true }`

```javascript
// Explicitly add virtuals to `JSON.stringify()` outputJSON.stringify(doc.toObject({virtuals:true}));// Or, to automatically attach virtuals to `JSON.stringify()` output:constpersonSchema =newSchema({name: {first:String,last:String}
}, {toJSON: {virtuals:true}// <-- include virtuals in `JSON.stringify()`});
```


You can also add a custom setter to your virtual that will let you set both
first name and last name via thefullNamevirtual.

`fullName`

```javascript
// Again that can be done either by adding it to schema options:constpersonSchema =newSchema({name: {first:String,last:String}
}, {virtuals: {fullName: {get() {returnthis.name.first+' '+this.name.last;
      },set(v) {this.name.first= v.substr(0, v.indexOf(' '));this.name.last= v.substr(v.indexOf(' ') +1);
      }
    }
  }
});// Or by using the virtual method as following:personSchema.virtual('fullName').get(function() {returnthis.name.first+' '+this.name.last;
  }).set(function(v) {this.name.first= v.substr(0, v.indexOf(' '));this.name.last= v.substr(v.indexOf(' ') +1);
  });

axl.fullName='William Rose';// Now `axl.name.first` is "William"
```


Virtual property setters are applied before other validation. So the example
above would still work even if thefirstandlastname fields were
required.

`first`
`last`

Only non-virtual properties work as part of queries and for field selection.
Since virtuals are not stored in MongoDB, you can't query with them.


You canlearn more about virtuals here.

[learn more about virtuals here](https://masteringjs.io/tutorials/mongoose/virtuals)


## Aliases

[Aliases](#aliases)


Aliases are a particular type of virtual where the getter and setter
seamlessly get and set another property. This is handy for saving network
bandwidth, so you can convert a short property name stored in the database
into a longer name for code readability.


```javascript
constpersonSchema =newSchema({n: {type:String,// Now accessing `name` will get you the value of `n`, and setting `name` will set the value of `n`alias:'name'}
});// Setting `name` will propagate to `n`constperson =newPerson({name:'Val'});console.log(person);// { n: 'Val' }console.log(person.toObject({virtuals:true}));// { n: 'Val', name: 'Val' }console.log(person.name);// "Val"person.name='Not Val';console.log(person);// { n: 'Not Val' }
```


You can also declare aliases on nested paths. It is easier to use nested
schemas andsubdocuments, but you can also declare
nested path aliases inline as long as you use the full nested pathnested.myPropas the alias.

[subdocuments](subdocs.html)

`nested.myProp`

```javascript
constchildSchema =newSchema({n: {type:String,alias:'name'}
}, {_id:false});constparentSchema =newSchema({// If in a child schema, alias doesn't need to include the full nested pathc: childSchema,name: {f: {type:String,// Alias needs to include the full nested path if declared inlinealias:'name.first'}
  }
});
```


## Options

[Options](#options)


Schemas have a few configurable options which can be passed to the
constructor or to thesetmethod:

`set`

```javascript
newSchema({/* ... */}, options);// orconstschema =newSchema({/* ... */});
schema.set(option, value);
```


Valid options:


autoIndexautoCreatebufferCommandsbufferTimeoutMScappedcollectiondiscriminatorKeyexcludeIndexesid_idminimizereadwriteConcernshardKeystaticsstrictstrictQuerytoJSONtoObjecttypeKeyvalidateBeforeSaveversionKeyoptimisticConcurrencycollationtimeseriesselectPopulatedPathsskipVersioningtimestampsstoreSubdocValidationErrorcollectionOptionsmethodsqueryautoSearchIndexreadConcern

- autoIndex

- autoCreate

- bufferCommands

- bufferTimeoutMS

- capped

- collection

- discriminatorKey

- excludeIndexes

- id

- _id

- minimize

- read

- writeConcern

- shardKey

- statics

- strict

- strictQuery

- toJSON

- toObject

- typeKey

- validateBeforeSave

- versionKey

- optimisticConcurrency

- collation

- timeseries

- selectPopulatedPaths

- skipVersioning

- timestamps

- storeSubdocValidationError

- collectionOptions

- methods

- query

- autoSearchIndex

- readConcern


## option: autoIndex

[option: autoIndex](#autoIndex)


By default, Mongoose'sinit()functioncreates all the indexes defined in your model's schema by callingModel.createIndexes()after you successfully connect to MongoDB. Creating indexes automatically is
great for development and test environments. But index builds can also create
significant load on your production database. If you want to manage indexes
carefully in production, you can setautoIndexto false.

[init()function](api/model.html#model_Model-init)

`init()`
[Model.createIndexes()](api/model.html#model_Model-createIndexes)

`Model.createIndexes()`
`autoIndex`

```javascript
constschema =newSchema({/* ... */}, {autoIndex:false});constClock= mongoose.model('Clock', schema);Clock.ensureIndexes(callback);
```


TheautoIndexoption is set totrueby default. You can change this
default by settingmongoose.set('autoIndex', false);

`autoIndex`
`true`
[mongoose.set('autoIndex', false);](api/mongoose.html#mongoose_Mongoose-set)

`mongoose.set('autoIndex', false);`

## option: autoCreate

[option: autoCreate](#autoCreate)


Before Mongoose builds indexes, it callsModel.createCollection()to create the underlying collection in MongoDB by default.
CallingcreateCollection()sets thecollection's default collationbased on thecollation optionand establishes the collection as
a capped collection if you set thecappedschema option.

`Model.createCollection()`
`createCollection()`
[collection's default collation](https://thecodebarbarian.com/a-nodejs-perspective-on-mongodb-34-collations)

[collation option](#collation)

[cappedschema option](#capped)

`capped`

You can disable this behavior by settingautoCreatetofalseusingmongoose.set('autoCreate', false).
LikeautoIndex,autoCreateis helpful for development and test environments, but you may want to disable it for production to avoid unnecessary database calls.

`autoCreate`
`false`
[mongoose.set('autoCreate', false)](api/mongoose.html#mongoose_Mongoose-set)

`mongoose.set('autoCreate', false)`
`autoIndex`
`autoCreate`

Unfortunately,createCollection()cannot change an existing collection.
For example, if you addcapped: { size: 1024 }to your schema and the existing collection is not capped,createCollection()willnotoverwrite the existing collection.
That is because the MongoDB server does not allow changing a collection's options without dropping the collection first.

`createCollection()`
`capped: { size: 1024 }`
`createCollection()`

```javascript
constschema =newSchema({name:String}, {autoCreate:false,capped: {size:1024}
});constTest= mongoose.model('Test', schema);// No-op if collection already exists, even if the collection is not capped.// This means that `capped` won't be applied if the 'tests' collection already exists.awaitTest.createCollection();
```


## option: bufferCommands

[option: bufferCommands](#bufferCommands)


By default, mongoose buffers commands when the connection goes down until
the driver manages to reconnect. To disable buffering, setbufferCommandsto false.

`bufferCommands`

```javascript
constschema =newSchema({/* ... */}, {bufferCommands:false});
```


The schemabufferCommandsoption overrides the globalbufferCommandsoption.

`bufferCommands`
`bufferCommands`

```javascript
mongoose.set('bufferCommands',true);// Schema option below overrides the above, if the schema option is set.constschema =newSchema({/* ... */}, {bufferCommands:false});
```


## option: bufferTimeoutMS

[option: bufferTimeoutMS](#bufferTimeoutMS)


IfbufferCommandsis on, this option sets the maximum amount of time Mongoose buffering will wait before
throwing an error. If not specified, Mongoose will use 10000 (10 seconds).

`bufferCommands`

```javascript
// If an operation is buffered for more than 1 second, throw an error.constschema =newSchema({/* ... */}, {bufferTimeoutMS:1000});
```


## option: capped

[option: capped](#capped)


Mongoose supports MongoDBscappedcollections. To specify the underlying MongoDB collection becapped, set
thecappedoption to the maximum size of the collection inbytes.

[capped](https://www.mongodb.com/docs/manual/core/capped-collections/)

`capped`
`capped`
[bytes](https://www.mongodb.com/docs/manual/core/capped-collections/#create-a-capped-collection)


```javascript
newSchema({/* ... */}, {capped:1024});
```


Thecappedoption may also be set to an object if you want to pass
additional options likemax.
In this case you must explicitly pass thesizeoption, which is required.

`capped`
[max](https://www.mongodb.com/docs/manual/core/capped-collections/#change-the-maximum-number-of-documents-in-a-capped-collection)

`size`

```javascript
newSchema({/* ... */}, {capped: {size:1024,max:1000,autoIndexId:true} });
```


## option: collection

[option: collection](#collection)


Mongoose by default produces a collection name by passing the model name to
theutils.toCollectionNamemethod.
This method pluralizes the name. Set this option if you need a different name
for your collection.

`utils.toCollectionName`

```javascript
constdataSchema =newSchema({/* ... */}, {collection:'data'});
```


## option: discriminatorKey

[option: discriminatorKey](#discriminatorKey)


When you define adiscriminator, Mongoose adds a path to your
schema that stores which discriminator a document is an instance of. By default, Mongoose
adds an__tpath, but you can setdiscriminatorKeyto overwrite this default.

[discriminator](discriminators.html)

`__t`
`discriminatorKey`

```javascript
constbaseSchema =newSchema({}, {discriminatorKey:'type'});constBaseModel= mongoose.model('Test', baseSchema);constpersonSchema =newSchema({name:String});constPersonModel=BaseModel.discriminator('Person', personSchema);constdoc =newPersonModel({name:'James T. Kirk'});// Without `discriminatorKey`, Mongoose would store the discriminator// key in `__t` instead of `type`doc.type;// 'Person'
```


## option: excludeIndexes

[option: excludeIndexes](#excludeIndexes)


WhenexcludeIndexesistrue, Mongoose will not create indexes from the given subdocument schema.
This option only works when the schema is used in a subdocument path or document array path, Mongoose ignores this option if set on the top-level schema for a model.
Defaults tofalse.

`excludeIndexes`
`true`
`false`

```javascript
constchildSchema1 =Schema({name: {type:String,index:true}
});constchildSchema2 =Schema({name: {type:String,index:true}
}, {excludeIndexes:true});// Mongoose will create an index on `child1.name`, but **not** `child2.name`, because `excludeIndexes`// is true on `childSchema2`constUser=newSchema({name: {type:String,index:true},child1: childSchema1,child2: childSchema2
});
```


## option: id

[option: id](#id)


Mongoose assigns each of your schemas anidvirtual getter by default
which returns the document's_idfield cast to a string, or in the case of
ObjectIds, its hexString. If you don't want anidgetter added to your
schema, you may disable it by passing this option at schema construction time.

`id`
`_id`
`id`

```javascript
// default behaviorconstschema =newSchema({name:String});constPage= mongoose.model('Page', schema);constp =newPage({name:'mongodb.org'});console.log(p.id);// '50341373e894ad16347efe01'// disabled idconstschema =newSchema({name:String}, {id:false});constPage= mongoose.model('Page', schema);constp =newPage({name:'mongodb.org'});console.log(p.id);// undefined
```


## option: _id

[option: _id](#_id)


Mongoose assigns each of your schemas an_idfield by default if one
is not passed into theSchemaconstructor.
The type assigned is anObjectIdto coincide with MongoDB's default behavior. If you don't want an_idadded to your schema at all, you may disable it using this option.

`_id`
[Schema](api/schema.html#schema_Schema)

[ObjectId](api/schema.html#schema_Schema-Types)

`_id`

You canonlyuse this option on subdocuments. Mongoose can't
save a document without knowing its id, so you will get an error if
you try to save a document without an_id.

`_id`

```javascript
// default behaviorconstschema =newSchema({name:String});constPage= mongoose.model('Page', schema);constp =newPage({name:'mongodb.org'});console.log(p);// { _id: '50341373e894ad16347efe01', name: 'mongodb.org' }// disabled _idconstchildSchema =newSchema({name:String}, {_id:false});constparentSchema =newSchema({children: [childSchema] });constModel= mongoose.model('Model', parentSchema);Model.create({children: [{name:'Luke'}] },(error, doc) =>{// doc.children[0]._id will be undefined});
```


## option: minimize

[option: minimize](#minimize)


Mongoose will, by default, "minimize" schemas by removing empty objects.


```javascript
constschema =newSchema({name:String,inventory: {} });constCharacter= mongoose.model('Character', schema);// will store `inventory` field if it is not emptyconstfrodo =newCharacter({name:'Frodo',inventory: {ringOfPower:1} });awaitfrodo.save();letdoc =awaitCharacter.findOne({name:'Frodo'}).lean();
doc.inventory;// { ringOfPower: 1 }// will not store `inventory` field if it is emptyconstsam =newCharacter({name:'Sam',inventory: {} });awaitsam.save();
doc =awaitCharacter.findOne({name:'Sam'}).lean();
doc.inventory;// undefined
```


This behavior can be overridden by settingminimizeoption tofalse. It
will then store empty objects.

`minimize`
`false`

```javascript
constschema =newSchema({name:String,inventory: {} }, {minimize:false});constCharacter= mongoose.model('Character', schema);// will store `inventory` if emptyconstsam =newCharacter({name:'Sam',inventory: {} });awaitsam.save();
doc =awaitCharacter.findOne({name:'Sam'}).lean();
doc.inventory;// {}
```


To check whether an object is empty, you can use the$isEmpty()helper:

`$isEmpty()`

```javascript
constsam =newCharacter({name:'Sam',inventory: {} });
sam.$isEmpty('inventory');// truesam.inventory.barrowBlade=1;
sam.$isEmpty('inventory');// false
```


## option: read

[option: read](#read)


Allows settingquery#readoptions at the
schema level, providing us a way to apply defaultReadPreferencesto all queries derived from a model.

[query#read](api/query.html#query_Query-read)

[ReadPreferences](http://www.mongodb.com/docs/manual/applications/replication/#replica-set-read-preference)


```javascript
constschema =newSchema({/* ... */}, {read:'primary'});// also aliased as 'p'constschema =newSchema({/* ... */}, {read:'primaryPreferred'});// aliased as 'pp'constschema =newSchema({/* ... */}, {read:'secondary'});// aliased as 's'constschema =newSchema({/* ... */}, {read:'secondaryPreferred'});// aliased as 'sp'constschema =newSchema({/* ... */}, {read:'nearest'});// aliased as 'n'
```


The alias of each pref is also permitted so instead of having to type out
'secondaryPreferred' and getting the spelling wrong, we can simply pass 'sp'.


The read option also allows us to specifytag sets. These tell thedriverfrom which members
of the replica-set it should attempt to read. Read more about tag setshereandhere.

[driver](https://github.com/mongodb/node-mongodb-native/)

[here](http://www.mongodb.com/docs/manual/applications/replication/#tag-sets)

[here](https://www.mongodb.com/docs/manual/core/read-preference)


NOTE: you may also specify the driver read preferencestrategyoption when connecting:

[strategy](https://www.mongodb.com/docs/manual/core/read-preference/#read-preference-modes)


```javascript
// pings the replset members periodically to track network latencyconstoptions = {replset: {strategy:'ping'} };
mongoose.connect(uri, options);constschema =newSchema({/* ... */}, {read: ['nearest', {disk:'ssd'}] });
mongoose.model('JellyBean', schema);
```


## option: writeConcern

[option: writeConcern](#writeConcern)


Allows settingwrite concernat the schema level.

[write concern](https://www.mongodb.com/docs/manual/reference/write-concern/)


```javascript
constschema =newSchema({name:String}, {writeConcern: {w:'majority',j:true,wtimeout:1000}
});
```


## option: shardKey

[option: shardKey](#shardKey)


TheshardKeyoption is used when we have asharded MongoDB architecture.
Each sharded collection is given a shard key which must be present in all
insert/update operations. We just need to set this schema option to the same
shard key and we’ll be all set.

`shardKey`
[sharded MongoDB architecture](https://www.mongodb.com/docs/manual/sharding/)


```javascript
newSchema({/* ... */}, {shardKey: {tag:1,name:1} });
```


Note that Mongoose does not send theshardcollectioncommand for you. You
must configure your shards yourself.

`shardcollection`

## option: strict

[option: strict](#strict)


The strict option, (enabled by default), ensures that values passed to our
model constructor that were not specified in our schema do not get saved to
the db.


```javascript
constthingSchema =newSchema({/* ... */})constThing= mongoose.model('Thing', thingSchema);constthing =newThing({iAmNotInTheSchema:true});
thing.save();// iAmNotInTheSchema is not saved to the db// set to false..constthingSchema =newSchema({/* ... */}, {strict:false});constthing =newThing({iAmNotInTheSchema:true});
thing.save();// iAmNotInTheSchema is now saved to the db!!
```


This also affects the use ofdoc.set()to set a property value.

`doc.set()`

```javascript
constthingSchema =newSchema({/* ... */});constThing= mongoose.model('Thing', thingSchema);constthing =newThing;
thing.set('iAmNotInTheSchema',true);
thing.save();// iAmNotInTheSchema is not saved to the db
```


This value can be overridden at the model instance level by passing a second
boolean argument:


```javascript
constThing= mongoose.model('Thing');constthing =newThing(doc,true);// enables strict modeconstthing =newThing(doc,false);// disables strict mode
```


Thestrictoption may also be set to"throw"which will cause errors
to be produced instead of dropping the bad data.

`strict`
`"throw"`

NOTE: Any key/val set on the instance that does not exist in your schema
is always ignored, regardless of schema option.


```javascript
constthingSchema =newSchema({/* ... */});constThing= mongoose.model('Thing', thingSchema);constthing =newThing;
thing.iAmNotInTheSchema=true;
thing.save();// iAmNotInTheSchema is never saved to the db
```


## option: strictQuery

[option: strictQuery](#strictQuery)


Mongoose supports a separatestrictQueryoption to avoid strict mode for query filters.
This is because empty query filters cause Mongoose to return all documents in the model, which can cause issues.

`strictQuery`

```javascript
constmySchema =newSchema({field:Number}, {strict:true});constMyModel= mongoose.model('Test', mySchema);// Mongoose will filter out `notInSchema: 1` because `strict: true`, meaning this query will return// _all_ documents in the 'tests' collectionMyModel.find({notInSchema:1});
```


Thestrictoption does apply to updates.
ThestrictQueryoption isjustfor query filters.

`strict`
`strictQuery`

```javascript
// Mongoose will strip out `notInSchema` from the update if `strict` is// not `false`MyModel.updateMany({}, {$set: {notInSchema:1} });
```


Mongoose has a separatestrictQueryoption to toggle strict mode for thefilterparameter to queries.

`strictQuery`
`filter`

```javascript
constmySchema =newSchema({field:Number}, {strict:true,strictQuery:false// Turn off strict mode for query filters});constMyModel= mongoose.model('Test', mySchema);// Mongoose will not strip out `notInSchema: 1` because `strictQuery` is falseMyModel.find({notInSchema:1});
```


In general, we donotrecommend passing user-defined objects as query filters:


```javascript
// Don't do this!constdocs =awaitMyModel.find(req.query);// Do this instead:constdocs =awaitMyModel.find({name: req.query.name,age: req.query.age}).setOptions({sanitizeFilter:true});
```


In Mongoose 7,strictQueryisfalseby default.
However, you can override this behavior globally:

`strictQuery`
`false`

```javascript
// Set `strictQuery` to `true` to omit unknown fields in queries.mongoose.set('strictQuery',true);
```


## option: toJSON

[option: toJSON](#toJSON)


Exactly the same as thetoObjectoption but only applies when
the document'stoJSONmethodis called.

[toObject](#toObject)

[toJSONmethod](https://thecodebarbarian.com/what-is-the-tojson-function-in-javascript.html)

`toJSON`

```javascript
constschema =newSchema({name:String});
schema.path('name').get(function(v) {returnv +' is my name';
});
schema.set('toJSON', {getters:true,virtuals:false});constM = mongoose.model('Person', schema);constm =newM({name:'Max Headroom'});console.log(m.toObject());// { _id: 504e0cd7dd992d9be2f20b6f, name: 'Max Headroom' }console.log(m.toJSON());// { _id: 504e0cd7dd992d9be2f20b6f, name: 'Max Headroom is my name' }// since we know toJSON is called whenever a js object is stringified:console.log(JSON.stringify(m));// { "_id": "504e0cd7dd992d9be2f20b6f", "name": "Max Headroom is my name" }
```


To see all availabletoJSON/toObjectoptions, readthis.

`toJSON/toObject`
[this](api/document.html#document_Document-toObject)


## option: toObject

[option: toObject](#toObject)


Documents have atoObjectmethod
which converts the mongoose document into a plain JavaScript object. This
method accepts a few options. Instead of applying these options on a
per-document basis, we may declare the options at the schema level and have
them applied to all of the schema's documents by default.

[toObject](api/document.html#document_Document-toObject)


To have all virtuals show up in yourconsole.logoutput, set thetoObjectoption to{ getters: true }:

`console.log`
`toObject`
`{ getters: true }`

```javascript
constschema =newSchema({name:String});
schema.path('name').get(function(v) {returnv +' is my name';
});
schema.set('toObject', {getters:true});constM = mongoose.model('Person', schema);constm =newM({name:'Max Headroom'});console.log(m);// { _id: 504e0cd7dd992d9be2f20b6f, name: 'Max Headroom is my name' }
```


To see all availabletoObjectoptions, readthis.

`toObject`
[this](api/document.html#document_Document-toObject)


## option: typeKey

[option: typeKey](#typeKey)


By default, if you have an object with key 'type' in your schema, mongoose
will interpret it as a type declaration.


```javascript
// Mongoose interprets this as 'loc is a String'constschema =newSchema({loc: {type:String,coordinates: [Number] } });
```


However, for applications likegeoJSON,
the 'type' property is important. If you want to control which key mongoose
uses to find type declarations, set the 'typeKey' schema option.

[geoJSON](http://www.mongodb.com/docs/manual/reference/geojson/)


```javascript
constschema =newSchema({// Mongoose interprets this as 'loc is an object with 2 keys, type and coordinates'loc: {type:String,coordinates: [Number] },// Mongoose interprets this as 'name is a String'name: {$type:String}
}, {typeKey:'$type'});// A '$type' key means this object is a type declaration
```


## option: validateBeforeSave

[option: validateBeforeSave](#validateBeforeSave)


By default, documents are automatically validated before they are saved to
the database. This is to prevent saving an invalid document. If you want to
handle validation manually, and be able to save objects which don't pass
validation, you can setvalidateBeforeSaveto false.

`validateBeforeSave`

```javascript
constschema =newSchema({name:String});
schema.set('validateBeforeSave',false);
schema.path('name').validate(function(value) {returnvalue !=null;
});constM = mongoose.model('Person', schema);constm =newM({name:null});
m.validate(function(err) {console.log(err);// Will tell you that null is not allowed.});
m.save();// Succeeds despite being invalid
```


## option: versionKey

[option: versionKey](#versionKey)


TheversionKeyis a property set on each document when first created by
Mongoose. This keys value contains the internalrevisionof the document. TheversionKeyoption is a string that represents the
path to use for versioning. The default is__v. If this conflicts with
your application you can configure as such:

`versionKey`
[revision](http://aaronheckmann.blogspot.com/2012/06/mongoose-v3-part-1-versioning.html)

`versionKey`
`__v`

```javascript
constschema =newSchema({name:'string'});constThing= mongoose.model('Thing', schema);constthing =newThing({name:'mongoose v3'});awaitthing.save();// { __v: 0, name: 'mongoose v3' }// customized versionKeynewSchema({/* ... */}, {versionKey:'_somethingElse'})constThing= mongoose.model('Thing', schema);constthing =newThing({name:'mongoose v3'});
thing.save();// { _somethingElse: 0, name: 'mongoose v3' }
```


Note that Mongoose's default versioning isnota fulloptimistic concurrencysolution. Mongoose's default versioning only operates on arrays as shown below.

[optimistic concurrency](https://en.wikipedia.org/wiki/Optimistic_concurrency_control)


```javascript
// 2 copies of the same documentconstdoc1 =awaitModel.findOne({ _id });constdoc2 =awaitModel.findOne({ _id });// Delete first 3 comments from `doc1`doc1.comments.splice(0,3);awaitdoc1.save();// The below `save()` will throw a VersionError, because you're trying to// modify the comment at index 1, and the above `splice()` removed that// comment.doc2.set('comments.1.body','new comment');awaitdoc2.save();
```


If you need optimistic concurrency support forsave(), you can set theoptimisticConcurrencyoption.

`save()`
[optimisticConcurrencyoption](#optimisticConcurrency)

`optimisticConcurrency`

Document versioning can also be disabled by setting theversionKeytofalse.DO NOT disable versioning unless youknow what you are doing.

`versionKey`
`false`
[know what you are doing](http://aaronheckmann.blogspot.com/2012/06/mongoose-v3-part-1-versioning.html)


```javascript
newSchema({/* ... */}, {versionKey:false});constThing= mongoose.model('Thing', schema);constthing =newThing({name:'no versioning please'});
thing.save();// { name: 'no versioning please' }
```


Mongooseonlyupdates the version key when you usesave().
If you useupdate(),findOneAndUpdate(), etc. Mongoose willnotupdate the version key. As a workaround, you can use the below middleware.

[save()](api/document.html#document_Document-save)

`save()`
`update()`
`findOneAndUpdate()`

```javascript
schema.pre('findOneAndUpdate',function() {constupdate =this.getUpdate();if(update.__v!=null) {deleteupdate.__v;
  }constkeys = ['$set','$setOnInsert'];for(constkeyofkeys) {if(update[key] !=null&& update[key].__v!=null) {deleteupdate[key].__v;if(Object.keys(update[key]).length===0) {deleteupdate[key];
      }
    }
  }
  update.$inc= update.$inc|| {};
  update.$inc.__v=1;
});
```


## option: optimisticConcurrency

[option: optimisticConcurrency](#optimisticConcurrency)


Optimistic concurrencyis a strategy to ensure
the document you're updating didn't change between when you loaded it usingfind()orfindOne(), and when
you update it usingsave().

[Optimistic concurrency](https://en.wikipedia.org/wiki/Optimistic_concurrency_control)

`find()`
`findOne()`
`save()`

For example, suppose you have aHousemodel that contains a list ofphotos, and astatusthat represents
whether this house shows up in searches. Suppose that a house that has status'APPROVED'must have at least
twophotos. You might implement the logic of approving a house document as shown below:

`House`
`photos`
`status`
`'APPROVED'`
`photos`

```javascript
asyncfunctionmarkApproved(id) {consthouse =awaitHouse.findOne({ _id });if(house.photos.length<2) {thrownewError('House must have at least two photos!');
  }

  house.status='APPROVED';awaithouse.save();
}
```


ThemarkApproved()function looks right in isolation, but there might be a potential issue: what if another
function removes the house's photos between thefindOne()call and thesave()call? For example, the below
code will succeed:

`markApproved()`
`findOne()`
`save()`

```javascript
consthouse =awaitHouse.findOne({ _id });if(house.photos.length<2) {thrownewError('House must have at least two photos!');
}consthouse2 =awaitHouse.findOne({ _id });
house2.photos= [];awaithouse2.save();// Marks the house as 'APPROVED' even though it has 0 photos!house.status='APPROVED';awaithouse.save();
```


If you set theoptimisticConcurrencyoption on theHousemodel's schema, the above script will throw an
error.

`optimisticConcurrency`
`House`

```javascript
constHouse= mongoose.model('House',Schema({status:String,photos: [String]
}, {optimisticConcurrency:true}));consthouse =awaitHouse.findOne({ _id });if(house.photos.length<2) {thrownewError('House must have at least two photos!');
}consthouse2 =awaitHouse.findOne({ _id });
house2.photos= [];awaithouse2.save();// Throws 'VersionError: No matching document found for id "..." version 0'house.status='APPROVED';awaithouse.save();
```


## option: collation

[option: collation](#collation)


Sets a defaultcollationfor every query and aggregation.Here's a beginner-friendly overview of collations.

[collation](https://www.mongodb.com/docs/manual/reference/collation/)

[Here's a beginner-friendly overview of collations](http://thecodebarbarian.com/a-nodejs-perspective-on-mongodb-34-collations)


```javascript
constschema =newSchema({name:String}, {collation: {locale:'en_US',strength:1} });constMyModel= db.model('MyModel', schema);MyModel.create([{name:'val'}, {name:'Val'}]).then(() =>{returnMyModel.find({name:'val'});
  }).then((docs) =>{// `docs` will contain both docs, because `strength: 1` means// MongoDB will ignore case when matching.});
```


## option: timeseries

[option: timeseries](#timeseries)


If you set thetimeseriesoption on a schema, Mongoose will create atimeseries collectionfor any model that you create from that schema.

`timeseries`
[timeseries collection](https://www.mongodb.com/docs/manual/core/timeseries-collections/)


```javascript
constschema =Schema({name:String,timestamp:Date,metadata:Object}, {timeseries: {timeField:'timestamp',metaField:'metadata',granularity:'hours'},autoCreate:false,expireAfterSeconds:86400});// `Test` collection will be a timeseries collectionconstTest= db.model('Test', schema);
```


## option: skipVersioning

[option: skipVersioning](#skipVersioning)


skipVersioningallows excluding paths from versioning (i.e., the internal
revision will not be incremented even if these paths are updated). DO NOT
do this unless you know what you're doing. For subdocuments, include this
on the parent document using the fully qualified path.

`skipVersioning`

```javascript
newSchema({/* ... */}, {skipVersioning: {dontVersionMe:true} });
thing.dontVersionMe.push('hey');
thing.save();// version is not incremented
```


## option: timestamps

[option: timestamps](#timestamps)


Thetimestampsoption tells Mongoose to assigncreatedAtandupdatedAtfields
to your schema. The type assigned isDate.

`timestamps`
`createdAt`
`updatedAt`
[Date](schematypes.html#dates)


By default, the names of the fields arecreatedAtandupdatedAt. Customize
the field names by settingtimestamps.createdAtandtimestamps.updatedAt.

`createdAt`
`updatedAt`
`timestamps.createdAt`
`timestamps.updatedAt`

The waytimestampsworks under the hood is:

`timestamps`

If you create a new document, mongoose simply setscreatedAt, andupdatedAtto the time of creation.If you update a document, mongoose will addupdatedAtto the$setobject.If you setupsert: trueon an update operation, mongoose will use$setOnInsertoperator to addcreatedAtto the document in case theupsertoperation resulted into a new inserted document.

- If you create a new document, mongoose simply setscreatedAt, andupdatedAtto the time of creation.

`createdAt`
`updatedAt`
- If you update a document, mongoose will addupdatedAtto the$setobject.

`updatedAt`
`$set`
- If you setupsert: trueon an update operation, mongoose will use$setOnInsertoperator to addcreatedAtto the document in case theupsertoperation resulted into a new inserted document.

`upsert: true`
`$setOnInsert`
`createdAt`
`upsert`

```javascript
constthingSchema =newSchema({/* ... */}, {timestamps: {createdAt:'created_at'} });constThing= mongoose.model('Thing', thingSchema);constthing =newThing();awaitthing.save();// `created_at` & `updatedAt` will be included// With updates, Mongoose will add `updatedAt` to `$set`awaitThing.updateOne({}, {$set: {name:'Test'} });// If you set upsert: true, Mongoose will add `created_at` to `$setOnInsert` as wellawaitThing.findOneAndUpdate({}, {$set: {name:'Test2'} });// Mongoose also adds timestamps to bulkWrite() operations// See https://mongoosejs.com/docs/api/model.html#model_Model-bulkWriteawaitThing.bulkWrite([
  {insertOne: {document: {name:'Jean-Luc Picard',ship:'USS Stargazer'// Mongoose will add `created_at` and `updatedAt`}
    }
  },
  {updateOne: {filter: {name:'Jean-Luc Picard'},update: {$set: {ship:'USS Enterprise'// Mongoose will add `updatedAt`}
      }
    }
  }
]);
```


By default, Mongoose usesnew Date()to get the current time.
If you want to overwrite the function
Mongoose uses to get the current time, you can set thetimestamps.currentTimeoption. Mongoose will call thetimestamps.currentTimefunction whenever it needs to get
the current time.

`new Date()`
`timestamps.currentTime`
`timestamps.currentTime`

```javascript
constschema =Schema({createdAt:Number,updatedAt:Number,name:String}, {// Make Mongoose use Unix time (seconds since Jan 1, 1970)timestamps: {currentTime:() =>Math.floor(Date.now() /1000) }
});
```


## option: pluginTags

[option: pluginTags](#pluginTags)


Mongoose supports defining global plugins, plugins that apply to all schemas.


```javascript
// Add a `meta` property to all schemasmongoose.plugin(functionmyPlugin(schema) {
  schema.add({meta: {} });
});
```


Sometimes, you may only want to apply a given plugin to some schemas.
In that case, you can addpluginTagsto a schema:

`pluginTags`

```javascript
constschema1 =newSchema({name:String}, {pluginTags: ['useMetaPlugin'] });constschema2 =newSchema({name:String});
```


If you callplugin()with atagsoption, Mongoose will only apply that plugin to schemas that have a matching entry inpluginTags.

`plugin()`
`tags`
`pluginTags`

```javascript
// Add a `meta` property to all schemasmongoose.plugin(functionmyPlugin(schema) {
  schema.add({meta: {} });
}, {tags: ['useMetaPlugin'] });
```


## option: selectPopulatedPaths

[option: selectPopulatedPaths](#selectPopulatedPaths)


By default, Mongoose will automaticallyselect()any populated paths for
you, unless you explicitly exclude them.

`select()`

```javascript
constbookSchema =newSchema({title:'String',author: {type:'ObjectId',ref:'Person'}
});constBook= mongoose.model('Book', bookSchema);// By default, Mongoose will add `author` to the below `select()`.awaitBook.find().select('title').populate('author');// In other words, the below query is equivalent to the aboveawaitBook.find().select('title author').populate('author');
```


To opt out of selecting populated fields by default, setselectPopulatedPathstofalsein your schema.

`selectPopulatedPaths`
`false`

```javascript
constbookSchema =newSchema({title:'String',author: {type:'ObjectId',ref:'Person'}
}, {selectPopulatedPaths:false});constBook= mongoose.model('Book', bookSchema);// Because `selectPopulatedPaths` is false, the below doc will **not**// contain an `author` property.constdoc =awaitBook.findOne().select('title').populate('author');
```


## option: storeSubdocValidationError

[option: storeSubdocValidationError](#storeSubdocValidationError)


For legacy reasons, when there is a validation error in subpath of a
single nested schema, Mongoose will record that there was a validation error
in the single nested schema path as well. For example:


```javascript
constchildSchema =newSchema({name: {type:String,required:true} });constparentSchema =newSchema({child: childSchema });constParent= mongoose.model('Parent', parentSchema);// Will contain an error for both 'child.name' _and_ 'child'newParent({child: {} }).validateSync().errors;
```


Set thestoreSubdocValidationErrortofalseon the child schema to make
Mongoose only reports the parent error.

`storeSubdocValidationError`
`false`

```javascript
constchildSchema =newSchema({name: {type:String,required:true}
}, {storeSubdocValidationError:false});// <-- set on the child schemaconstparentSchema =newSchema({child: childSchema });constParent= mongoose.model('Parent', parentSchema);// Will only contain an error for 'child.name'newParent({child: {} }).validateSync().errors;
```


## option: collectionOptions

[option: collectionOptions](#collectionOptions)


Options likecollationandcappedaffect the options Mongoose passes to MongoDB when creating a new collection.
Mongoose schemas support mostMongoDBcreateCollection()options, but not all.
You can use thecollectionOptionsoption to set anycreateCollection()options; Mongoose will usecollectionOptionsas the default values when callingcreateCollection()for your schema.

[collation](#collation)

`collation`
[capped](#capped)

`capped`
[MongoDBcreateCollection()options](https://www.mongodb.com/docs/manual/reference/method/db.createCollection/)

`createCollection()`
`collectionOptions`
`createCollection()`
`collectionOptions`
`createCollection()`

```javascript
constschema =newSchema({name:String}, {autoCreate:false,collectionOptions: {capped:true,max:1000}
});constTest= mongoose.model('Test', schema);// Equivalent to `createCollection({ capped: true, max: 1000 })`awaitTest.createCollection();
```


## option: autoSearchIndex

[option: autoSearchIndex](#autoSearchIndex)


Similar toautoIndex, except for automatically creates anyAtlas search indexesdefined in your schema.
UnlikeautoIndex, this option defaults to false.

[autoIndex](#autoIndex)

`autoIndex`
[Atlas search indexes](https://www.mongodb.com/docs/atlas/atlas-search/create-index/)

`autoIndex`

```javascript
constschema =newSchema({name:String}, {autoSearchIndex:true});
schema.searchIndex({name:'my-index',definition: {mappings: {dynamic:true} }
});// Will automatically attempt to create the `my-index` search index.constTest= mongoose.model('Test', schema);
```


## option: readConcern

[option: readConcern](#readConcern)


Read concernsare similar towriteConcern, but for read operations likefind()andfindOne().
To set a defaultreadConcern, pass thereadConcernoption to the schema constructor as follows.

[Read concerns](https://www.mongodb.com/docs/manual/reference/read-concern/)

[writeConcern](#writeConcern)

`writeConcern`
`find()`
`findOne()`
`readConcern`
`readConcern`

```javascript
consteventSchema =newmongoose.Schema(
  {name:String},
  {readConcern: {level:'available'}// <-- set default readConcern for all queries}
);
```


## With ES6 Classes

[With ES6 Classes](#es6-classes)


Schemas have aloadClass()methodthat you can use to create a Mongoose schema from anES6 class:

[loadClass()method](api/schema.html#schema_Schema-loadClass)

`loadClass()`
[ES6 class](https://thecodebarbarian.com/an-overview-of-es6-classes)


ES6 class methodsbecomeMongoose methodsES6 class staticsbecomeMongoose staticsES6 getters and settersbecomeMongoose virtuals

- ES6 class methodsbecomeMongoose methods

- ES6 class staticsbecomeMongoose statics

- ES6 getters and settersbecomeMongoose virtuals


Here's an example of usingloadClass()to create a schema from an ES6 class:

`loadClass()`

```javascript
classMyClass{myMethod() {return42; }staticmyStatic() {return42; }getmyVirtual() {return42; }
}constschema =newmongoose.Schema();
schema.loadClass(MyClass);console.log(schema.methods);// { myMethod: [Function: myMethod] }console.log(schema.statics);// { myStatic: [Function: myStatic] }console.log(schema.virtuals);// { myVirtual: VirtualType { ... } }
```


## Pluggable

[Pluggable](#plugins)


Schemas are alsopluggablewhich allows us to package up reusable features into
plugins that can be shared with the community or just between your projects.

[pluggable](plugins.html)


## Further Reading

[Further Reading](#further-reading)


Here's analternative introduction to Mongoose schemas.

[alternative introduction to Mongoose schemas](https://masteringjs.io/tutorials/mongoose/schema)


To get the most out of MongoDB, you need to learn the basics of MongoDB schema design.
SQL schema design (third normal form) was designed tominimize storage costs,
whereas MongoDB schema design is about making common queries as fast as possible.
The6 Rules of Thumb for MongoDB Schema Designblog seriesis an excellent resource for learning the basic rules for making your queries
fast.

[minimize storage costs](https://en.wikipedia.org/wiki/Third_normal_form)

[6 Rules of Thumb for MongoDB Schema Designblog series](https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1)


Users looking to master MongoDB schema design in Node.js should look intoThe Little MongoDB Schema Design Bookby Christian Kvalheim, the original author of theMongoDB Node.js driver.
This book shows you how to implement performant schemas for a laundry list
of use cases, including e-commerce, wikis, and appointment bookings.

[The Little MongoDB Schema Design Book](http://bit.ly/mongodb-schema-design)

[MongoDB Node.js driver](http://npmjs.com/package/mongodb)


## Next Up

[Next Up](#next)


Now that we've coveredSchemas, let's take a look atSchemaTypes.

`Schemas`
[SchemaTypes](schematypes.html)


[Source](https://mongoosejs.com/docs/guide.html#methods)