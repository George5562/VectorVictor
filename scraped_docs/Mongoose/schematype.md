# SchemaType


# SchemaType

[Mongoose](mongoose.html)

[Schema](schema.html)

[Connection](connection.html)

[Document](document.html)

[Model](model.html)

[Query](query.html)

[QueryCursor](querycursor.html)

[Aggregate](aggregate.html)

[AggregationCursor](aggregationcursor.html)

[SchemaType](schematype.html)


SchemaType()SchemaType.cast()SchemaType.checkRequired()SchemaType.get()SchemaType.prototype.cast()SchemaType.prototype.castFunction()SchemaType.prototype.default()SchemaType.prototype.doValidate()SchemaType.prototype.get()SchemaType.prototype.getEmbeddedSchemaType()SchemaType.prototype.immutable()SchemaType.prototype.index()SchemaType.prototype.isRequiredSchemaType.prototype.pathSchemaType.prototype.ref()SchemaType.prototype.required()SchemaType.prototype.select()SchemaType.prototype.set()SchemaType.prototype.sparse()SchemaType.prototype.text()SchemaType.prototype.transform()SchemaType.prototype.unique()SchemaType.prototype.validate()SchemaType.prototype.validateAll()SchemaType.prototype.validatorsSchemaType.set()

- SchemaType()

`SchemaType()`
- SchemaType.cast()

`SchemaType.cast()`
- SchemaType.checkRequired()

`SchemaType.checkRequired()`
- SchemaType.get()

`SchemaType.get()`
- SchemaType.prototype.cast()

`SchemaType.prototype.cast()`
- SchemaType.prototype.castFunction()

`SchemaType.prototype.castFunction()`
- SchemaType.prototype.default()

`SchemaType.prototype.default()`
- SchemaType.prototype.doValidate()

`SchemaType.prototype.doValidate()`
- SchemaType.prototype.get()

`SchemaType.prototype.get()`
- SchemaType.prototype.getEmbeddedSchemaType()

`SchemaType.prototype.getEmbeddedSchemaType()`
- SchemaType.prototype.immutable()

`SchemaType.prototype.immutable()`
- SchemaType.prototype.index()

`SchemaType.prototype.index()`
- SchemaType.prototype.isRequired

`SchemaType.prototype.isRequired`
- SchemaType.prototype.path

`SchemaType.prototype.path`
- SchemaType.prototype.ref()

`SchemaType.prototype.ref()`
- SchemaType.prototype.required()

`SchemaType.prototype.required()`
- SchemaType.prototype.select()

`SchemaType.prototype.select()`
- SchemaType.prototype.set()

`SchemaType.prototype.set()`
- SchemaType.prototype.sparse()

`SchemaType.prototype.sparse()`
- SchemaType.prototype.text()

`SchemaType.prototype.text()`
- SchemaType.prototype.transform()

`SchemaType.prototype.transform()`
- SchemaType.prototype.unique()

`SchemaType.prototype.unique()`
- SchemaType.prototype.validate()

`SchemaType.prototype.validate()`
- SchemaType.prototype.validateAll()

`SchemaType.prototype.validateAll()`
- SchemaType.prototype.validators

`SchemaType.prototype.validators`
- SchemaType.set()

`SchemaType.set()`
[VirtualType](virtualtype.html)

[Error](error.html)

[SchemaArray](schemaarray.html)

[SchemaDocumentArray](schemadocumentarray.html)

[SchemaSubdocument](schemasubdocument.html)

[SchemaBoolean](schemaboolean.html)

[SchemaBuffer](schemabuffer.html)

[SchemaNumber](schemanumber.html)

[SchemaObjectId](schemaobjectid.html)

[SchemaString](schemastring.html)

[DocumentArray](documentarray.html)

[Subdocument](subdocument.html)

[ArraySubdocument](arraysubdocument.html)

[Buffer](buffer.html)

[Decimal128](decimal128.html)

[Map](map.html)

[Array](array.html)


SchemaType()SchemaType.cast()SchemaType.checkRequired()SchemaType.get()SchemaType.prototype.cast()SchemaType.prototype.castFunction()SchemaType.prototype.default()SchemaType.prototype.doValidate()SchemaType.prototype.get()SchemaType.prototype.getEmbeddedSchemaType()SchemaType.prototype.immutable()SchemaType.prototype.index()SchemaType.prototype.isRequiredSchemaType.prototype.pathSchemaType.prototype.ref()SchemaType.prototype.required()SchemaType.prototype.select()SchemaType.prototype.set()SchemaType.prototype.sparse()SchemaType.prototype.text()SchemaType.prototype.transform()SchemaType.prototype.unique()SchemaType.prototype.validate()SchemaType.prototype.validateAll()SchemaType.prototype.validatorsSchemaType.set()

- SchemaType()

`SchemaType()`
- SchemaType.cast()

`SchemaType.cast()`
- SchemaType.checkRequired()

`SchemaType.checkRequired()`
- SchemaType.get()

`SchemaType.get()`
- SchemaType.prototype.cast()

`SchemaType.prototype.cast()`
- SchemaType.prototype.castFunction()

`SchemaType.prototype.castFunction()`
- SchemaType.prototype.default()

`SchemaType.prototype.default()`
- SchemaType.prototype.doValidate()

`SchemaType.prototype.doValidate()`
- SchemaType.prototype.get()

`SchemaType.prototype.get()`
- SchemaType.prototype.getEmbeddedSchemaType()

`SchemaType.prototype.getEmbeddedSchemaType()`
- SchemaType.prototype.immutable()

`SchemaType.prototype.immutable()`
- SchemaType.prototype.index()

`SchemaType.prototype.index()`
- SchemaType.prototype.isRequired

`SchemaType.prototype.isRequired`
- SchemaType.prototype.path

`SchemaType.prototype.path`
- SchemaType.prototype.ref()

`SchemaType.prototype.ref()`
- SchemaType.prototype.required()

`SchemaType.prototype.required()`
- SchemaType.prototype.select()

`SchemaType.prototype.select()`
- SchemaType.prototype.set()

`SchemaType.prototype.set()`
- SchemaType.prototype.sparse()

`SchemaType.prototype.sparse()`
- SchemaType.prototype.text()

`SchemaType.prototype.text()`
- SchemaType.prototype.transform()

`SchemaType.prototype.transform()`
- SchemaType.prototype.unique()

`SchemaType.prototype.unique()`
- SchemaType.prototype.validate()

`SchemaType.prototype.validate()`
- SchemaType.prototype.validateAll()

`SchemaType.prototype.validateAll()`
- SchemaType.prototype.validators

`SchemaType.prototype.validators`
- SchemaType.set()

`SchemaType.set()`

### SchemaType()

[SchemaType()](#SchemaType())

`SchemaType()`

path«String»[options]«SchemaTypeOptions»SeeSchemaTypeOptions docs[instance]«String»

- path«String»

`path`
- [options]«SchemaTypeOptions»SeeSchemaTypeOptions docs

`[options]`
- [instance]«String»

`[instance]`

SchemaType constructor. DonotinstantiateSchemaTypedirectly.
Mongoose converts your schema paths into SchemaTypes automatically.

`SchemaType`

#### Example:

[Example:](#example)


```javascript
constschema =newSchema({name:String});
schema.path('name')instanceofSchemaType;// true
```


### SchemaType.cast()

[SchemaType.cast()](#SchemaType.cast())

`SchemaType.cast()`

caster«Function|false»Function that casts arbitrary values to this type, or throws an error if casting failed

- caster«Function|false»Function that casts arbitrary values to this type, or throws an error if casting failed

`caster`

«Function»

- «Function»


Get/set the function used to cast arbitrary values to this type.


#### Example:

[Example:](#example)


```javascript
// Disallow `null` for numbers, and don't try to cast any values to// numbers, so even strings like '123' will cause a CastError.mongoose.Number.cast(function(v) {
  assert.ok(v ===undefined||typeofv ==='number');returnv;
});
```


### SchemaType.checkRequired()

[SchemaType.checkRequired()](#SchemaType.checkRequired())

`SchemaType.checkRequired()`

[fn]«Function»If set, will overwrite the current set function

- [fn]«Function»If set, will overwrite the current set function

`[fn]`

«Function»The inputfnor the already set function

- «Function»The inputfnor the already set function

`fn`

Set & Get thecheckRequiredfunction
Override the function the required validator uses to check whether a value
passes therequiredcheck. Override this on the individual SchemaType.

`checkRequired`
`required`

#### Example:

[Example:](#example)


```javascript
// Use this to allow empty strings to pass the `required` validatormongoose.Schema.Types.String.checkRequired(v=>typeofv ==='string');
```


### SchemaType.get()

[SchemaType.get()](#SchemaType.get())

`SchemaType.get()`

getter«Function»

- getter«Function»

`getter`

«this»

- «this»


Attaches a getter for all instances of this schema type.


#### Example:

[Example:](#example)


```javascript
// Make all numbers round downmongoose.Number.get(function(v) {returnMath.floor(v); });
```


### SchemaType.prototype.cast()

[SchemaType.prototype.cast()](#SchemaType.prototype.cast())

`SchemaType.prototype.cast()`

value«Object»value to castdoc«Document»document that triggers the castinginit«Boolean»

- value«Object»value to cast

`value`
- doc«Document»document that triggers the casting

`doc`
- init«Boolean»

`init`

The function that Mongoose calls to cast arbitrary values to this SchemaType.


### SchemaType.prototype.castFunction()

[SchemaType.prototype.castFunction()](#SchemaType.prototype.castFunction())

`SchemaType.prototype.castFunction()`

caster«Function|false»Function that casts arbitrary values to this type, or throws an error if casting failed

- caster«Function|false»Function that casts arbitrary values to this type, or throws an error if casting failed

`caster`

«Function»

- «Function»


Get/set the function used to cast arbitrary values to this particular schematype instance.
OverridesSchemaType.cast().

`SchemaType.cast()`

#### Example:

[Example:](#example)


```javascript
// Disallow `null` for numbers, and don't try to cast any values to// numbers, so even strings like '123' will cause a CastError.constnumber =newmongoose.Number('mypath', {});
number.cast(function(v) {
  assert.ok(v ===undefined||typeofv ==='number');returnv;
});
```


### SchemaType.prototype.default()

[SchemaType.prototype.default()](#SchemaType.prototype.default())

`SchemaType.prototype.default()`

val«Function|any»The default value to set

- val«Function|any»The default value to set

`val`

«Any,undefined,void»Returns the set default value.

- «Any,undefined,void»Returns the set default value.


Sets a default value for this SchemaType.


#### Example:

[Example:](#example)


```javascript
constschema =newSchema({n: {type:Number,default:10})constM = db.model('M', schema)constm =newM;console.log(m.n)// 10
```


Defaults can be eitherfunctionswhich return the value to use as the default or the literal value itself. Either way, the value will be cast based on its schema type before being set during document creation.

`functions`

#### Example:

[Example:](#example)


```javascript
// values are cast:constschema =newSchema({aNumber: {type:Number,default:4.815162342}})constM = db.model('M', schema)constm =newM;console.log(m.aNumber)// 4.815162342// default unique objects for Mixed types:constschema =newSchema({mixed:Schema.Types.Mixed});
schema.path('mixed').default(function() {return{};
});// if we don't use a function to return object literals for Mixed defaults,// each document will receive a reference to the same object literal creating// a "shared" object instance:constschema =newSchema({mixed:Schema.Types.Mixed});
schema.path('mixed').default({});constM = db.model('M', schema);constm1 =newM;
m1.mixed.added=1;console.log(m1.mixed);// { added: 1 }constm2 =newM;console.log(m2.mixed);// { added: 1 }
```


### SchemaType.prototype.doValidate()

[SchemaType.prototype.doValidate()](#SchemaType.prototype.doValidate())

`SchemaType.prototype.doValidate()`

value«Any»callback«Function»scope«Object»[options]«Object»[options.path]«String»

- value«Any»

`value`
- callback«Function»

`callback`
- scope«Object»

`scope`
- [options]«Object»

`[options]`

[options.path]«String»

- [options.path]«String»

`[options.path]`

«Any»If no validators, returns the output from callingfn, otherwise no return

- «Any»If no validators, returns the output from callingfn, otherwise no return

`fn`

Performs a validation ofvalueusing the validators declared for this SchemaType.

`value`

### SchemaType.prototype.get()

[SchemaType.prototype.get()](#SchemaType.prototype.get())

`SchemaType.prototype.get()`

fn«Function»

- fn«Function»

`fn`

«SchemaType»this

- «SchemaType»this


Adds a getter to this schematype.


#### Example:

[Example:](#example)


```javascript
functiondob(val) {if(!val)returnval;return(val.getMonth() +1) +"/"+ val.getDate() +"/"+ val.getFullYear();
}// defining within the schemaconsts =newSchema({born: {type:Date,get: dob })// or by retreiving its SchemaTypeconsts =newSchema({born:Date})
s.path('born').get(dob)
```


Getters allow you to transform the representation of the data as it travels from the raw mongodb document to the value that you see.


Suppose you are storing credit card numbers and you want to hide everything except the last 4 digits to the mongoose user. You can do so by defining a getter in the following way:


```javascript
functionobfuscate(cc) {return'****-****-****-'+ cc.slice(cc.length-4, cc.length);
}constAccountSchema=newSchema({creditCardNumber: {type:String,get: obfuscate }
});constAccount= db.model('Account',AccountSchema);Account.findById(id,function(err, found) {console.log(found.creditCardNumber);// '****-****-****-1234'});
```


Getters are also passed a second argument, the schematype on which the getter was defined. This allows for tailored behavior based on options passed in the schema.


```javascript
functioninspector(val, priorValue, schematype) {if(schematype.options.required) {returnschematype.path+' is required';
  }else{returnschematype.path+' is not';
  }
}constVirusSchema=newSchema({name: {type:String,required:true,get: inspector },taxonomy: {type:String,get: inspector }
})constVirus= db.model('Virus',VirusSchema);Virus.findById(id,function(err, virus) {console.log(virus.name);// name is requiredconsole.log(virus.taxonomy);// taxonomy is not})
```


### SchemaType.prototype.getEmbeddedSchemaType()

[SchemaType.prototype.getEmbeddedSchemaType()](#SchemaType.prototype.getEmbeddedSchemaType())

`SchemaType.prototype.getEmbeddedSchemaType()`

Returns the embedded schema type, if any. For arrays, document arrays, and maps,getEmbeddedSchemaType()returns the schema type of the array's elements (or map's elements). For other types,getEmbeddedSchemaType()returnsundefined.

`getEmbeddedSchemaType()`
`getEmbeddedSchemaType()`
`undefined`

#### Example:

[Example:](#example)


```javascript
constschema =newSchema({name:String,tags: [String] });
schema.path('name').getEmbeddedSchemaType();// undefinedschema.path('tags').getEmbeddedSchemaType();// SchemaString { path: 'tags', ... }
```


### SchemaType.prototype.immutable()

[SchemaType.prototype.immutable()](#SchemaType.prototype.immutable())

`SchemaType.prototype.immutable()`

bool«Boolean»

- bool«Boolean»

`bool`

«SchemaType»this

- «SchemaType»this


isNew

- isNew

[isNew](/docs/api/document.html#Document.prototype.isNew())


Defines this path as immutable. Mongoose prevents you from changing
immutable paths unless the parent document hasisNew: true.

[isNew: true](/docs/api/document.html#Document.prototype.isNew())

`isNew: true`

#### Example:

[Example:](#example)


```javascript
constschema =newSchema({name: {type:String,immutable:true},age:Number});constModel= mongoose.model('Test', schema);awaitModel.create({name:'test'});constdoc =awaitModel.findOne();

doc.isNew;// falsedoc.name='new name';
doc.name;// 'test', because `name` is immutable
```


Mongoose also prevents changing immutable properties usingupdateOne()andupdateMany()based onstrict mode.

`updateOne()`
`updateMany()`
[strict mode](/docs/guide.html#strict)


#### Example:

[Example:](#example)


```javascript
// Mongoose will strip out the `name` update, because `name` is immutableModel.updateOne({}, {$set: {name:'test2'},$inc: {age:1} });// If `strict` is set to 'throw', Mongoose will throw an error if you// update `name`consterr =awaitModel.updateOne({}, {name:'test2'}, {strict:'throw'}).then(() =>null,err=>err);
err.name;// StrictModeError// If `strict` is `false`, Mongoose allows updating `name` even though// the property is immutable.Model.updateOne({}, {name:'test2'}, {strict:false});
```


### SchemaType.prototype.index()

[SchemaType.prototype.index()](#SchemaType.prototype.index())

`SchemaType.prototype.index()`

options«Object|Boolean|String|Number»

- options«Object|Boolean|String|Number»

`options`

«SchemaType»this

- «SchemaType»this


Declares the index options for this schematype.


#### Example:

[Example:](#example)


```javascript
consts =newSchema({name: {type:String,index:true})consts =newSchema({name: {type:String,index: -1})consts =newSchema({loc: {type: [Number],index:'hashed'})consts =newSchema({loc: {type: [Number],index:'2d',sparse:true})consts =newSchema({loc: {type: [Number],index: {type:'2dsphere',sparse:true}})consts =newSchema({date: {type:Date,index: {unique:true,expires:'1d'}})
s.path('my.path').index(true);
s.path('my.date').index({expires:60});
s.path('my.path').index({unique:true,sparse:true});
```


#### Note:

[Note:](#note)


Indexes are createdin the backgroundby default. Ifbackgroundis set tofalse, MongoDB will not execute any
read/write operations you send until the index build.
Specifybackground: falseto override Mongoose's default.

[in the background](https://www.mongodb.com/docs/manual/core/index-creation/#index-creation-background)

`background`
`false`
`background: false`

### SchemaType.prototype.isRequired

[SchemaType.prototype.isRequired](#SchemaType.prototype.isRequired)

`SchemaType.prototype.isRequired`

«property»

- «property»


True if this SchemaType has a required validator. False otherwise.


#### Example:

[Example:](#example)


```javascript
constschema =newSchema({name: {type:String,required:true} });
schema.path('name').isRequired;// trueschema.path('name').required(false);
schema.path('name').isRequired;// false
```


### SchemaType.prototype.path

[SchemaType.prototype.path](#SchemaType.prototype.path)

`SchemaType.prototype.path`

«property»

- «property»


The path to this SchemaType in a Schema.


#### Example:

[Example:](#example)


```javascript
constschema =newSchema({name:String});
schema.path('name').path;// 'name'
```


### SchemaType.prototype.ref()

[SchemaType.prototype.ref()](#SchemaType.prototype.ref())

`SchemaType.prototype.ref()`

ref«String|Model|Function»either a model name, aModel, or a function that returns a model name or model.

- ref«String|Model|Function»either a model name, aModel, or a function that returns a model name or model.

`ref`

«SchemaType»this

- «SchemaType»this


Set the model that this path refers to. This is the option thatpopulatelooks at to determine the foreign collection it should query.

[populate](/docs/populate.html)


#### Example:

[Example:](#example)


```javascript
constuserSchema =newSchema({name:String});constUser= mongoose.model('User', userSchema);constpostSchema =newSchema({user: mongoose.ObjectId});
postSchema.path('user').ref('User');// Can set ref to a model namepostSchema.path('user').ref(User);// Or a model classpostSchema.path('user').ref(() =>'User');// Or a function that returns the model namepostSchema.path('user').ref(() =>User);// Or a function that returns the model class// Or you can just declare the `ref` inline in your schemaconstpostSchema2 =newSchema({user: {type: mongoose.ObjectId,ref:User}
});
```


### SchemaType.prototype.required()

[SchemaType.prototype.required()](#SchemaType.prototype.required())

`SchemaType.prototype.required()`

required«Boolean|Function|Object»enable/disable the validator, or function that returns required boolean, or options object[options.isRequired]«Boolean|Function»enable/disable the validator, or function that returns required boolean[options.ErrorConstructor]«Function»custom error constructor. The constructor receives 1 parameter, an object containing the validator properties.[message]«String»optional custom error message

- required«Boolean|Function|Object»enable/disable the validator, or function that returns required boolean, or options object

`required`

[options.isRequired]«Boolean|Function»enable/disable the validator, or function that returns required boolean

- [options.isRequired]«Boolean|Function»enable/disable the validator, or function that returns required boolean

`[options.isRequired]`

[options.ErrorConstructor]«Function»custom error constructor. The constructor receives 1 parameter, an object containing the validator properties.

- [options.ErrorConstructor]«Function»custom error constructor. The constructor receives 1 parameter, an object containing the validator properties.

`[options.ErrorConstructor]`
- [message]«String»optional custom error message

`[message]`

«SchemaType»this

- «SchemaType»this


Customized Error MessagesSchemaArray#checkRequiredSchemaBoolean#checkRequiredSchemaBuffer#checkRequiredSchemaNumber#checkRequiredSchemaObjectId#checkRequiredSchemaString#checkRequired

- Customized Error Messages

[Customized Error Messages](/docs/api/error.html#Error.messages)

- SchemaArray#checkRequired

[SchemaArray#checkRequired](/docs/api/schemaarray.html#SchemaArray.prototype.checkRequired())

- SchemaBoolean#checkRequired

[SchemaBoolean#checkRequired](/docs/api/schemaboolean.html#SchemaBoolean.prototype.checkRequired())

- SchemaBuffer#checkRequired

[SchemaBuffer#checkRequired](/docs/api/schemabuffer.html#SchemaBuffer.prototype.checkRequired())

- SchemaNumber#checkRequired

[SchemaNumber#checkRequired](/docs/api/schemanumber.html#SchemaNumber.prototype.checkRequired())

- SchemaObjectId#checkRequired

[SchemaObjectId#checkRequired](/docs/api/schemaobjectid.html#ObjectId.prototype.checkRequired())

- SchemaString#checkRequired

[SchemaString#checkRequired](/docs/api/schemastring.html#SchemaString.prototype.checkRequired())


Adds a required validator to this SchemaType. The validator gets added
to the front of this SchemaType's validators array usingunshift().

`unshift()`

#### Example:

[Example:](#example)


```javascript
consts =newSchema({born: {type:Date,required:true})// or with custom error messageconsts =newSchema({born: {type:Date,required:'{PATH} is required!'})// or with a functionconsts =newSchema({userId:ObjectId,username: {type:String,required:function() {returnthis.userId!=null; }
  }
})// or with a function and a custom messageconsts =newSchema({userId:ObjectId,username: {type:String,required: [function() {returnthis.userId!=null; },'username is required if id is specified']
  }
})// or through the path APIs.path('name').required(true);// with custom error messagings.path('name').required(true,'grrr :( ');// or make a path conditionally required based on a functionconstisOver18 =function() {returnthis.age>=18; };
s.path('voterRegistrationId').required(isOver18);
```


The required validator uses the SchemaType'scheckRequiredfunction to
determine whether a given value satisfies the required validator. By default,
a value satisfies the required validator ifval != null(that is, if
the value is not null nor undefined). However, most built-in mongoose schema
types override the defaultcheckRequiredfunction:

`checkRequired`
`val != null`
`checkRequired`

### SchemaType.prototype.select()

[SchemaType.prototype.select()](#SchemaType.prototype.select())

`SchemaType.prototype.select()`

val«Boolean»

- val«Boolean»

`val`

«SchemaType»this

- «SchemaType»this


Sets defaultselect()behavior for this path.

`select()`

Set totrueif this path should always be included in the results,falseif it should be excluded by default. This setting can be overridden at the query level.

`true`
`false`

#### Example:

[Example:](#example)


```javascript
T = db.model('T',newSchema({x: {type:String,select:true}}));
T.find(..);// field x will always be selected ..// .. unless overridden;T.find().select('-x').exec(callback);
```


### SchemaType.prototype.set()

[SchemaType.prototype.set()](#SchemaType.prototype.set())

`SchemaType.prototype.set()`

fn«Function»

- fn«Function»

`fn`

«SchemaType»this

- «SchemaType»this


Adds a setter to this schematype.


#### Example:

[Example:](#example)


```javascript
functioncapitalize(val) {if(typeofval !=='string') val ='';returnval.charAt(0).toUpperCase() + val.substring(1);
}// defining within the schemaconsts =newSchema({name: {type:String,set: capitalize }});// or with the SchemaTypeconsts =newSchema({name:String})
s.path('name').set(capitalize);
```


Setters allow you to transform the data before it gets to the raw mongodb
document or query.


Suppose you are implementing user registration for a website. Users provide
an email and password, which gets saved to mongodb. The email is a string
that you will want to normalize to lower case, in order to avoid one email
having more than one account -- e.g., otherwise,avenue@q.comcan be registered for 2 accounts viaavenue@q.comandAvEnUe@Q.CoM.

[avenue@q.com](mailto:avenue@q.com)

[avenue@q.com](mailto:avenue@q.com)

[AvEnUe@Q.CoM](mailto:AvEnUe@Q.CoM)


You can set up email lower case normalization easily via a Mongoose setter.


```javascript
functiontoLower(v) {returnv.toLowerCase();
}constUserSchema=newSchema({email: {type:String,set: toLower }
});constUser= db.model('User',UserSchema);constuser =newUser({email:'AVENUE@Q.COM'});console.log(user.email);// 'avenue@q.com'// orconstuser =newUser();
user.email='Avenue@Q.com';console.log(user.email);// 'avenue@q.com'User.updateOne({_id: _id }, {$set: {email:'AVENUE@Q.COM'} });// update to 'avenue@q.com'
```


As you can see above, setters allow you to transform the data before it
stored in MongoDB, or before executing a query.


NOTE: we could have also just used the built-inlowercase: trueSchemaType option instead of defining our own function.

`lowercase: true`

```javascript
newSchema({email: {type:String,lowercase:true}})
```


Setters are also passed a second argument, the schematype on which the setter was defined. This allows for tailored behavior based on options passed in the schema.


```javascript
functioninspector(val, priorValue, schematype) {if(schematype.options.required) {returnschematype.path+' is required';
  }else{returnval;
  }
}constVirusSchema=newSchema({name: {type:String,required:true,set: inspector },taxonomy: {type:String,set: inspector }
})constVirus= db.model('Virus',VirusSchema);constv =newVirus({name:'Parvoviridae',taxonomy:'Parvovirinae'});console.log(v.name);// name is requiredconsole.log(v.taxonomy);// Parvovirinae
```


You can also use setters to modify other properties on the document. If
you're setting a propertynameon a document, the setter will run withthisas the document. Be careful, in mongoose 5 setters will also run
when querying bynamewiththisas the query.

`name`
`this`
`name`
`this`

```javascript
constnameSchema =newSchema({name:String,keywords: [String] });
nameSchema.path('name').set(function(v) {// Need to check if `this` is a document, because in mongoose 5// setters will also run on queries, in which case `this` will be a// mongoose query object.if(thisinstanceofDocument&& v !=null) {this.keywords= v.split(' ');
  }returnv;
});
```


### SchemaType.prototype.sparse()

[SchemaType.prototype.sparse()](#SchemaType.prototype.sparse())

`SchemaType.prototype.sparse()`

bool«Boolean»

- bool«Boolean»

`bool`

«SchemaType»this

- «SchemaType»this


Declares a sparse index.


#### Example:

[Example:](#example)


```javascript
consts =newSchema({name: {type:String,sparse:true} });
s.path('name').index({sparse:true});
```


### SchemaType.prototype.text()

[SchemaType.prototype.text()](#SchemaType.prototype.text())

`SchemaType.prototype.text()`

bool«Boolean»

- bool«Boolean»

`bool`

«SchemaType»this

- «SchemaType»this


Declares a full text index.


### Example:

[Example:](#example)


```javascript
consts =newSchema({ name : {type:String, text :true} })
 s.path('name').index({ text :true});
```


### SchemaType.prototype.transform()

[SchemaType.prototype.transform()](#SchemaType.prototype.transform())

`SchemaType.prototype.transform()`

fn«Function»

- fn«Function»

`fn`

«SchemaType»this

- «SchemaType»this


Defines a custom function for transforming this path when converting a document to JSON.


Mongoose calls this function with one parameter: the currentvalueof the path. Mongoose
then uses the return value in the JSON output.

`value`

#### Example:

[Example:](#example)


```javascript
constschema =newSchema({date: {type:Date,transform:v=>v.getFullYear() }
});constModel= mongoose.model('Test', schema);awaitModel.create({date:newDate('2016-06-01') });constdoc =awaitModel.findOne();

doc.dateinstanceofDate;// truedoc.toJSON().date;// 2016 as a numberJSON.stringify(doc);// '{"_id":...,"date":2016}'
```


### SchemaType.prototype.unique()

[SchemaType.prototype.unique()](#SchemaType.prototype.unique())

`SchemaType.prototype.unique()`

bool«Boolean»

- bool«Boolean»

`bool`

«SchemaType»this

- «SchemaType»this


Declares an unique index.


#### Example:

[Example:](#example)


```javascript
consts =newSchema({name: {type:String,unique:true} });
s.path('name').index({unique:true});
```


NOTE: violating the constraint returns anE11000error from MongoDB when saving, not a Mongoose validation error.

`E11000`

### SchemaType.prototype.validate()

[SchemaType.prototype.validate()](#SchemaType.prototype.validate())

`SchemaType.prototype.validate()`

obj«RegExp|Function|Object»validator function, or hash describing options[obj.validator]«Function»validator function. If the validator function returnsundefinedor a truthy value, validation succeeds. If it returnsfalsy(exceptundefined) or throws an error, validation fails.[obj.message]«String|Function»optional error message. If function, should return the error message as a string[obj.propsParameter=false]«Boolean»If true, Mongoose will pass the validator properties object (with thevalidatorfunction,message, etc.) as the 2nd arg to the validator function. This is disabled by default because many validatorsrely on positional args, so turning this on may cause unpredictable behavior in external validators.[errorMsg]«String|Function»optional error message. If function, should return the error message as a string[type]«String»optional validator type

- obj«RegExp|Function|Object»validator function, or hash describing options

`obj`

[obj.validator]«Function»validator function. If the validator function returnsundefinedor a truthy value, validation succeeds. If it returnsfalsy(exceptundefined) or throws an error, validation fails.

- [obj.validator]«Function»validator function. If the validator function returnsundefinedor a truthy value, validation succeeds. If it returnsfalsy(exceptundefined) or throws an error, validation fails.

`[obj.validator]`
`undefined`
`undefined`

[obj.message]«String|Function»optional error message. If function, should return the error message as a string

- [obj.message]«String|Function»optional error message. If function, should return the error message as a string

`[obj.message]`

[obj.propsParameter=false]«Boolean»If true, Mongoose will pass the validator properties object (with thevalidatorfunction,message, etc.) as the 2nd arg to the validator function. This is disabled by default because many validatorsrely on positional args, so turning this on may cause unpredictable behavior in external validators.

- [obj.propsParameter=false]«Boolean»If true, Mongoose will pass the validator properties object (with thevalidatorfunction,message, etc.) as the 2nd arg to the validator function. This is disabled by default because many validatorsrely on positional args, so turning this on may cause unpredictable behavior in external validators.

`[obj.propsParameter=false]`
`validator`
`message`
- [errorMsg]«String|Function»optional error message. If function, should return the error message as a string

`[errorMsg]`
- [type]«String»optional validator type

`[type]`

«SchemaType»this

- «SchemaType»this


Adds validator(s) for this document path.


Validators always receive the value to validate as their first argument and
must returnBoolean. Returningfalseor throwing an error means
validation failed.

`Boolean`
`false`

The error message argument is optional. If not passed, thedefault generic error message templatewill be used.

[default generic error message template](/docs/api/error.html#Error.messages)


#### Example:

[Example:](#example)


```javascript
// make sure every value is equal to "something"functionvalidator(val) {returnval ==='something';
}newSchema({name: {type:String,validate: validator }});// with a custom error messageconstcustom = [validator,'Uh oh, {PATH} does not equal "something".']newSchema({name: {type:String,validate: custom }});// adding many validators at a timeconstmany = [
    {validator: validator,message:'uh oh'}
  , {validator: anotherValidator,message:'failed'}
]newSchema({name: {type:String,validate: many }});// or utilizing SchemaType methods directly:constschema =newSchema({name:'string'});
schema.path('name').validate(validator,'validation of `{PATH}` failed with value `{VALUE}`');
```


#### Error message templates:

[Error message templates:](#error-message-templates)


Below is a list of supported template keywords:


PATH: The schema path where the error is being triggered.VALUE: The value assigned to the PATH that is triggering the error.KIND: The validation property that triggered the error i.e. required.REASON: The error object that caused this error if there was one.

- PATH: The schema path where the error is being triggered.

- VALUE: The value assigned to the PATH that is triggering the error.

- KIND: The validation property that triggered the error i.e. required.

- REASON: The error object that caused this error if there was one.


If Mongoose's built-in error message templating isn't enough, Mongoose
supports setting themessageproperty to a function.

`message`

```javascript
schema.path('name').validate({validator:function(v) {returnv.length>5; },// `errors['name']` will be "name must have length 5, got 'foo'"message:function(props) {return`${props.path}must have length 5, got '${props.value}'`;
  }
});
```


To bypass Mongoose's error messages and just copy the error message that
the validator throws, do this:


```javascript
schema.path('name').validate({validator:function() {thrownewError('Oops!'); },// `errors['name'].message` will be "Oops!"message:function(props) {returnprops.reason.message; }
});
```


#### Asynchronous validation:

[Asynchronous validation:](#asynchronous-validation)


Mongoose supports validators that return a promise. A validator that returns
a promise is called anasync validator. Async validators run in
parallel, andvalidate()will wait until all async validators have settled.

`validate()`

```javascript
schema.path('name').validate({validator:function(value) {returnnewPromise(function(resolve, reject) {resolve(false);// validation failed});
  }
});
```


You might use asynchronous validators to retreive other documents from the database to validate against or to meet other I/O bound validation needs.


Validation occurspre('save')or whenever you manually executedocument#validate.

`pre('save')`
[document#validate](/docs/api/document.html#Document.prototype.validate())


If validation fails duringpre('save')and no callback was passed to receive the error, anerrorevent will be emitted on your Models associated dbconnection, passing the validation error object along.

`pre('save')`
`error`
[connection](/docs/api/connection.html#Connection())


```javascript
constconn = mongoose.createConnection(..);
conn.on('error', handleError);constProduct= conn.model('Product', yourSchema);constdvd =newProduct(..);
dvd.save();// emits error on the `conn` above
```


If you want to handle these errors at the Model level, add anerrorlistener to your Model as shown below.

`error`

```javascript
// registering an error listener on the Model lets us handle errors more locallyProduct.on('error', handleError);
```


### SchemaType.prototype.validateAll()

[SchemaType.prototype.validateAll()](#SchemaType.prototype.validateAll())

`SchemaType.prototype.validateAll()`

validators«Array<RegExp|Function|Object>»

- validators«Array<RegExp|Function|Object>»

`validators`

Adds multiple validators for this document path.
Callsvalidate()for every element in validators.

`validate()`

### SchemaType.prototype.validators

[SchemaType.prototype.validators](#SchemaType.prototype.validators)

`SchemaType.prototype.validators`

«property»

- «property»


The validators that Mongoose should run to validate properties at this SchemaType's path.


#### Example:

[Example:](#example)


```javascript
constschema =newSchema({name: {type:String,required:true} });
schema.path('name').validators.length;// 1, the `required` validator
```


### SchemaType.set()

[SchemaType.set()](#SchemaType.set())

`SchemaType.set()`

option«String»The name of the option you'd like to set (e.g. trim, lowercase, etc...)value«Any»The value of the option you'd like to set.

- option«String»The name of the option you'd like to set (e.g. trim, lowercase, etc...)

`option`
- value«Any»The value of the option you'd like to set.

`value`

«void,void»

- «void,void»


Sets a default option for this schema type.


#### Example:

[Example:](#example)


```javascript
// Make all strings be trimmed by defaultmongoose.SchemaTypes.String.set('trim',true);
```


[Source](https://mongoosejs.com/docs/api/schematype.html#SchemaType.prototype.immutable)