# SchemaTypes


# SchemaTypes

[SchemaTypes](#schematypes)


SchemaTypes handle definition of pathdefaults,validation,getters,setters,field selection defaultsforqueries,
and other general characteristics for Mongoose document properties.

[defaults](api/schematype.html#schematype_SchemaType-default)

[validation](api/schematype.html#schematype_SchemaType-validate)

[getters](#getters)

[setters](api/schematype.html#schematype_SchemaType-set)

[field selection defaults](api/schematype.html#schematype_SchemaType-select)

[queries](api/query.html)


What is a SchemaType?ThetypeKeySchemaType OptionsUsage NotesGettersCustom TypesTheschema.path()FunctionFurther Reading

- What is a SchemaType?

- ThetypeKey

`type`
- SchemaType Options

- Usage Notes

- Getters

- Custom Types

- Theschema.path()Function

`schema.path()`
- Further Reading


## What is a SchemaType?

[What is a SchemaType?](#what-is-a-schematype)


You can think of a Mongoose schema as the configuration object for a
Mongoose model. A SchemaType is then a configuration object for an individual
property. A SchemaType says what type a given
path should have, whether it has any getters/setters, and what values are
valid for that path.


```javascript
constschema =newSchema({name:String});
schema.path('name')instanceofmongoose.SchemaType;// trueschema.path('name')instanceofmongoose.Schema.Types.String;// trueschema.path('name').instance;// 'String'
```


A SchemaType is different from a type. In other words,mongoose.ObjectId !== mongoose.Types.ObjectId.
A SchemaType is just a configuration object for Mongoose. An instance of
themongoose.ObjectIdSchemaType doesn't actually create MongoDB ObjectIds,
it is just a configuration for a path in a schema.

`mongoose.ObjectId !== mongoose.Types.ObjectId`
`mongoose.ObjectId`

The following are all the valid SchemaTypes in Mongoose. Mongoose plugins
can also add custom SchemaTypes likeint32.
Check outMongoose's plugins searchto find plugins.

[int32](http://plugins.mongoosejs.io/plugins/int32)

[Mongoose's plugins search](http://plugins.mongoosejs.io)


StringNumberDateBufferBooleanMixedObjectIdArrayDecimal128MapSchemaUUIDBigInt

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

- Schema

- UUID

- BigInt


### Example

[Example](#example)


```javascript
constschema =newSchema({name:String,binary:Buffer,living:Boolean,updated: {type:Date,default:Date.now},age: {type:Number,min:18,max:65},mixed:Schema.Types.Mixed,_someId:Schema.Types.ObjectId,decimal:Schema.Types.Decimal128,array: [],ofString: [String],ofNumber: [Number],ofDates: [Date],ofBuffer: [Buffer],ofBoolean: [Boolean],ofMixed: [Schema.Types.Mixed],ofObjectId: [Schema.Types.ObjectId],ofArrays: [[]],ofArrayOfNumbers: [[Number]],nested: {stuff: {type:String,lowercase:true,trim:true}
  },map:Map,mapOfString: {type:Map,of:String}
});// example useconstThing= mongoose.model('Thing', schema);constm =newThing;
m.name='Statue of Liberty';
m.age=125;
m.updated=newDate;
m.binary=Buffer.alloc(0);
m.living=false;
m.mixed= {any: {thing:'i want'} };
m.markModified('mixed');
m._someId=newmongoose.Types.ObjectId;
m.array.push(1);
m.ofString.push('strings!');
m.ofNumber.unshift(1,2,3,4);
m.ofDates.addToSet(newDate);
m.ofBuffer.pop();
m.ofMixed= [1, [],'three', {four:5}];
m.nested.stuff='good';
m.map=newMap([['key','value']]);
m.save(callback);
```


## ThetypeKey

[ThetypeKey](#type-key)

`type`

typeis a special property in Mongoose schemas. When Mongoose finds
a nested property namedtypein your schema, Mongoose assumes that
it needs to define a SchemaType with the given type.

`type`
`type`

```javascript
// 3 string SchemaTypes: 'name', 'nested.firstName', 'nested.lastName'constschema =newSchema({name: {type:String},nested: {firstName: {type:String},lastName: {type:String}
  }
});
```


As a consequence,you need a little extra work to define a property namedtypein your schema.
For example, suppose you're building a stock portfolio app, and you
want to store the asset'stype(stock, bond, ETF, etc.). Naively,
you might define your schema as shown below:

[you need a little extra work to define a property namedtypein your schema](faq.html#type-key)

`type`
`type`

```javascript
constholdingSchema =newSchema({// You might expect `asset` to be an object that has 2 properties,// but unfortunately `type` is special in Mongoose so mongoose// interprets this schema to mean that `asset` is a stringasset: {type:String,ticker:String}
});
```


However, when Mongoose seestype: String, it assumes that you meanassetshould be a string, not an object with a propertytype.
The correct way to define an object with a propertytypeis shown
below.

`type: String`
`asset`
`type`
`type`

```javascript
constholdingSchema =newSchema({asset: {// Workaround to make sure Mongoose knows `asset` is an object// and `asset.type` is a string, rather than thinking `asset`// is a string.type: {type:String},ticker:String}
});
```


## SchemaType Options

[SchemaType Options](#schematype-options)


You can declare a schema type using the type directly, or an object with
atypeproperty.

`type`

```javascript
constschema1 =newSchema({test:String// `test` is a path of type String});constschema2 =newSchema({// The `test` object contains the "SchemaType options"test: {type:String}// `test` is a path of type string});
```


In addition to the type property, you can specify additional properties
for a path. For example, if you want to lowercase a string before saving:


```javascript
constschema2 =newSchema({test: {type:String,lowercase:true// Always convert `test` to lowercase}
});
```


You can add any property you want to your SchemaType options. Many plugins
rely on custom SchemaType options. For example, themongoose-autopopulateplugin automatically populates paths if you setautopopulate: truein your
SchemaType options. Mongoose comes with support for several built-in
SchemaType options, likelowercasein the above example.

[mongoose-autopopulate](http://plugins.mongoosejs.io/plugins/autopopulate)

`autopopulate: true`
`lowercase`

Thelowercaseoption only works for strings. There are certain options
which apply for all schema types, and some that apply for specific schema
types.

`lowercase`

### All Schema Types

[All Schema Types](#all-schema-types)


required: boolean or function, if true adds arequired validatorfor this propertydefault: Any or function, sets a default value for the path. If the value is a function, the return value of the function is used as the default.select: boolean, specifies defaultprojectionsfor queriesvalidate: function, adds avalidator functionfor this propertyget: function, defines a custom getter for this property usingObject.defineProperty().set: function, defines a custom setter for this property usingObject.defineProperty().alias: string, mongoose >= 4.10.0 only. Defines avirtualwith the given name that gets/sets this path.immutable: boolean, defines path as immutable. Mongoose prevents you from changing immutable paths unless the parent document hasisNew: true.transform: function, Mongoose calls this function when you callDocument#toJSON()function, including when youJSON.stringify()a document.

- required: boolean or function, if true adds arequired validatorfor this property

`required`
- default: Any or function, sets a default value for the path. If the value is a function, the return value of the function is used as the default.

`default`
- select: boolean, specifies defaultprojectionsfor queries

`select`
- validate: function, adds avalidator functionfor this property

`validate`
- get: function, defines a custom getter for this property usingObject.defineProperty().

`get`
`Object.defineProperty()`
- set: function, defines a custom setter for this property usingObject.defineProperty().

`set`
`Object.defineProperty()`
- alias: string, mongoose >= 4.10.0 only. Defines avirtualwith the given name that gets/sets this path.

`alias`
- immutable: boolean, defines path as immutable. Mongoose prevents you from changing immutable paths unless the parent document hasisNew: true.

`immutable`
`isNew: true`
- transform: function, Mongoose calls this function when you callDocument#toJSON()function, including when youJSON.stringify()a document.

`transform`
`Document#toJSON()`
`JSON.stringify()`

```javascript
constnumberSchema =newSchema({integerOnly: {type:Number,get:v=>Math.round(v),set:v=>Math.round(v),alias:'i'}
});constNumber= mongoose.model('Number', numberSchema);constdoc =newNumber();
doc.integerOnly=2.001;
doc.integerOnly;// 2doc.i;// 2doc.i=3.001;
doc.integerOnly;// 3doc.i;// 3
```


### Indexes

[Indexes](#indexes)


You can also defineMongoDB indexesusing schema type options.

[MongoDB indexes](https://www.mongodb.com/docs/manual/indexes/)


index: boolean, whether to define anindexon this property.unique: boolean, whether to define aunique indexon this property.sparse: boolean, whether to define asparse indexon this property.

- index: boolean, whether to define anindexon this property.

`index`
- unique: boolean, whether to define aunique indexon this property.

`unique`
- sparse: boolean, whether to define asparse indexon this property.

`sparse`

```javascript
constschema2 =newSchema({test: {type:String,index:true,unique:true// Unique index. If you specify `unique: true`// specifying `index: true` is optional if you do `unique: true`}
});
```


### String

[String](#string-validators)


lowercase: boolean, whether to always call.toLowerCase()on the valueuppercase: boolean, whether to always call.toUpperCase()on the valuetrim: boolean, whether to always call.trim()on the valuematch: RegExp, creates avalidatorthat checks if the value matches the given regular expressionenum: Array, creates avalidatorthat checks if the value is in the given array.minLength: Number, creates avalidatorthat checks if the value length is not less than the given numbermaxLength: Number, creates avalidatorthat checks if the value length is not greater than the given numberpopulate: Object, sets defaultpopulate options

- lowercase: boolean, whether to always call.toLowerCase()on the value

`lowercase`
`.toLowerCase()`
- uppercase: boolean, whether to always call.toUpperCase()on the value

`uppercase`
`.toUpperCase()`
- trim: boolean, whether to always call.trim()on the value

`trim`
`.trim()`
- match: RegExp, creates avalidatorthat checks if the value matches the given regular expression

`match`
- enum: Array, creates avalidatorthat checks if the value is in the given array.

`enum`
- minLength: Number, creates avalidatorthat checks if the value length is not less than the given number

`minLength`
- maxLength: Number, creates avalidatorthat checks if the value length is not greater than the given number

`maxLength`
- populate: Object, sets defaultpopulate options

`populate`

### Number

[Number](#number-validators)


min: Number, creates avalidatorthat checks if the value is greater than or equal to the given minimum.max: Number, creates avalidatorthat checks if the value is less than or equal to the given maximum.enum: Array, creates avalidatorthat checks if the value is strictly equal to one of the values in the given array.populate: Object, sets defaultpopulate options

- min: Number, creates avalidatorthat checks if the value is greater than or equal to the given minimum.

`min`
- max: Number, creates avalidatorthat checks if the value is less than or equal to the given maximum.

`max`
- enum: Array, creates avalidatorthat checks if the value is strictly equal to one of the values in the given array.

`enum`
- populate: Object, sets defaultpopulate options

`populate`

### Date

[Date](#date)


min: Date, creates avalidatorthat checks if the value is greater than or equal to the given minimum.max: Date, creates avalidatorthat checks if the value is less than or equal to the given maximum.expires: Number or String, creates a TTL index with the value expressed in seconds.

- min: Date, creates avalidatorthat checks if the value is greater than or equal to the given minimum.

`min`
- max: Date, creates avalidatorthat checks if the value is less than or equal to the given maximum.

`max`
- expires: Number or String, creates a TTL index with the value expressed in seconds.

`expires`

### ObjectId

[ObjectId](#objectid)


populate: Object, sets defaultpopulate options

- populate: Object, sets defaultpopulate options

`populate`

## Usage Notes

[Usage Notes](#usage-notes)


### String

[String](#strings)


To declare a path as a string, you may use either theStringglobal
constructor or the string'String'.

`String`
`'String'`

```javascript
constschema1 =newSchema({name:String});// name will be cast to stringconstschema2 =newSchema({name:'String'});// EquivalentconstPerson= mongoose.model('Person', schema2);
```


If you pass an element that has atoString()function, Mongoose will call it,
unless the element is an array or thetoString()function is strictly equal toObject.prototype.toString().

`toString()`
`toString()`
`Object.prototype.toString()`

```javascript
newPerson({name:42}).name;// "42" as a stringnewPerson({name: {toString:() =>42} }).name;// "42" as a string// "undefined", will get a cast error if you `save()` this documentnewPerson({name: {foo:42} }).name;
```


### Number

[Number](#numbers)


To declare a path as a number, you may use either theNumberglobal
constructor or the string'Number'.

`Number`
`'Number'`

```javascript
constschema1 =newSchema({age:Number});// age will be cast to a Numberconstschema2 =newSchema({age:'Number'});// EquivalentconstCar= mongoose.model('Car', schema2);
```


There are several types of values that will be successfully cast to a Number.


```javascript
newCar({age:'15'}).age;// 15 as a NumbernewCar({age:true}).age;// 1 as a NumbernewCar({age:false}).age;// 0 as a NumbernewCar({age: {valueOf:() =>83} }).age;// 83 as a Number
```


If you pass an object with avalueOf()function that returns a Number, Mongoose will
call it and assign the returned value to the path.

`valueOf()`

The valuesnullandundefinedare not cast.

`null`
`undefined`

NaN, strings that cast to NaN, arrays, and objects that don't have avalueOf()function
will all result in aCastErroronce validated, meaning that it will not throw on initialization, only when validated.

`valueOf()`
[CastError](validation.html#cast-errors)


### Dates

[Dates](#dates)


Built-inDatemethodsarenothooked intothe mongoose change tracking logic which in English means that if you use aDatein your document and modify it with a method likesetMonth(), mongoose will be unaware of this change anddoc.save()will not persist this modification. If you must modifyDatetypes using built-in methods, tell mongoose about the change withdoc.markModified('pathToYourDate')before saving.

[Built-inDatemethods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)

`Date`
[nothooked into](https://github.com/Automattic/mongoose/issues/1598)

`Date`
`setMonth()`
`doc.save()`
`Date`
`doc.markModified('pathToYourDate')`

```javascript
constAssignment= mongoose.model('Assignment', {dueDate:Date});constdoc =awaitAssignment.findOne();
doc.dueDate.setMonth(3);awaitdoc.save();// THIS DOES NOT SAVE YOUR CHANGEdoc.markModified('dueDate');awaitdoc.save();// works
```


### Buffer

[Buffer](#buffers)


To declare a path as a Buffer, you may use either theBufferglobal
constructor or the string'Buffer'.

`Buffer`
`'Buffer'`

```javascript
constschema1 =newSchema({binData:Buffer});// binData will be cast to a Bufferconstschema2 =newSchema({binData:'Buffer'});// EquivalentconstData= mongoose.model('Data', schema2);
```


Mongoose will successfully cast the below values to buffers.


```javascript
constfile1 =newData({binData:'test'});// {"type":"Buffer","data":[116,101,115,116]}constfile2 =newData({binData:72987});// {"type":"Buffer","data":[27]}constfile4 =newData({binData: {type:'Buffer',data: [1,2,3]}});// {"type":"Buffer","data":[1,2,3]}
```


### Mixed

[Mixed](#mixed)


An "anything goes" SchemaType. Mongoose will not do any casting on mixed paths.
You can define a mixed path usingSchema.Types.Mixedor by passing an empty
object literal. The following are equivalent.

`Schema.Types.Mixed`

```javascript
constAny=newSchema({any: {} });constAny=newSchema({any:Object});constAny=newSchema({any:Schema.Types.Mixed});constAny=newSchema({any: mongoose.Mixed});
```


Since Mixed is a schema-less type, you can change the value to anything else you
like, but Mongoose loses the ability to auto detect and save those changes.
To tell Mongoose that the value of a Mixed type has changed, you need to
calldoc.markModified(path), passing the path to the Mixed type you just changed.

`doc.markModified(path)`

To avoid these side-effects, aSubdocumentpath may be used
instead.

[Subdocument](subdocs.html)


```javascript
person.anything= {x: [3,4, {y:'changed'}] };
person.markModified('anything');
person.save();// Mongoose will save changes to `anything`.
```


### ObjectIds

[ObjectIds](#objectids)


AnObjectIdis a special type typically used for unique identifiers. Here's how
you declare a schema with a pathdriverthat is an ObjectId:

[ObjectId](https://www.mongodb.com/docs/manual/reference/method/ObjectId/)

`driver`

```javascript
constmongoose =require('mongoose');constcarSchema =newmongoose.Schema({driver: mongoose.ObjectId});
```


ObjectIdis a class, and ObjectIds are objects. However, they are
often represented as strings. When you convert an ObjectId to a string
usingtoString(), you get a 24-character hexadecimal string:

`ObjectId`
`toString()`

```javascript
constCar= mongoose.model('Car', carSchema);constcar =newCar();
car.driver=newmongoose.Types.ObjectId();typeofcar.driver;// 'object'car.driverinstanceofmongoose.Types.ObjectId;// truecar.driver.toString();// Something like "5e1a0651741b255ddda996c4"
```


### Boolean

[Boolean](#booleans)


Booleans in Mongoose areplain JavaScript booleans.
By default, Mongoose casts the below values totrue:

[plain JavaScript booleans](https://www.w3schools.com/js/js_booleans.asp)

`true`

true'true'1'1''yes'

- true

`true`
- 'true'

`'true'`
- 1

`1`
- '1'

`'1'`
- 'yes'

`'yes'`

Mongoose casts the below values tofalse:

`false`

false'false'0'0''no'

- false

`false`
- 'false'

`'false'`
- 0

`0`
- '0'

`'0'`
- 'no'

`'no'`

Any other value causes aCastError.
You can modify what values Mongoose converts to true or false using theconvertToTrueandconvertToFalseproperties, which areJavaScript sets.

[CastError](validation.html#cast-errors)

`convertToTrue`
`convertToFalse`
[JavaScript sets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)


```javascript
constM = mongoose.model('Test',newSchema({b:Boolean}));console.log(newM({b:'nay'}).b);// undefined// Set { false, 'false', 0, '0', 'no' }console.log(mongoose.Schema.Types.Boolean.convertToFalse);

mongoose.Schema.Types.Boolean.convertToFalse.add('nay');console.log(newM({b:'nay'}).b);// false
```


### Arrays

[Arrays](#arrays)


Mongoose supports arrays ofSchemaTypesand arrays ofsubdocuments. Arrays of SchemaTypes are
also calledprimitive arrays, and arrays of subdocuments are also calleddocument arrays.

[SchemaTypes](api/schema.html#schema_Schema-Types)

[subdocuments](subdocs.html)


```javascript
constToySchema=newSchema({name:String});constToyBoxSchema=newSchema({toys: [ToySchema],buffers: [Buffer],strings: [String],numbers: [Number]// ... etc});
```


Arrays are special because they implicitly have a default value of[](empty array).

`[]`

```javascript
constToyBox= mongoose.model('ToyBox',ToyBoxSchema);console.log((newToyBox()).toys);// []
```


To overwrite this default, you need to set the default value toundefined

`undefined`

```javascript
constToyBoxSchema=newSchema({toys: {type: [ToySchema],default:undefined}
});
```


Note: specifying an empty array is equivalent toMixed. The following all create arrays ofMixed:

`Mixed`
`Mixed`

```javascript
constEmpty1=newSchema({any: [] });constEmpty2=newSchema({any:Array});constEmpty3=newSchema({any: [Schema.Types.Mixed] });constEmpty4=newSchema({any: [{}] });
```


### Maps

[Maps](#maps)


AMongooseMapis a subclass ofJavaScript'sMapclass.
In these docs, we'll use the terms 'map' andMongooseMapinterchangeably.
In Mongoose, maps are how you create a nested document with arbitrary keys.

`MongooseMap`
[JavaScript'sMapclass](http://thecodebarbarian.com/the-80-20-guide-to-maps-in-javascript.html)

`Map`
`MongooseMap`

Note: In Mongoose Maps, keys must be strings in order to store the document in MongoDB.


```javascript
constuserSchema =newSchema({// `socialMediaHandles` is a map whose values are strings. A map's// keys are always strings. You specify the type of values using `of`.socialMediaHandles: {type:Map,of:String}
});constUser= mongoose.model('User', userSchema);// Map { 'github' => 'vkarpov15', 'twitter' => '@code_barbarian' }console.log(newUser({socialMediaHandles: {github:'vkarpov15',twitter:'@code_barbarian'}
}).socialMediaHandles);
```


The above example doesn't explicitly declaregithubortwitteras paths,
but, sincesocialMediaHandlesis a map, you can store arbitrary key/value
pairs. However, sincesocialMediaHandlesis a map, youmustuse.get()to get the value of a key and.set()to set the value of a key.

`github`
`twitter`
`socialMediaHandles`
`socialMediaHandles`
`.get()`
`.set()`

```javascript
constuser =newUser({socialMediaHandles: {}
});// Gooduser.socialMediaHandles.set('github','vkarpov15');// Works toouser.set('socialMediaHandles.twitter','@code_barbarian');// Bad, the `myspace` property will **not** get saveduser.socialMediaHandles.myspace='fail';// 'vkarpov15'console.log(user.socialMediaHandles.get('github'));// '@code_barbarian'console.log(user.get('socialMediaHandles.twitter'));// undefineduser.socialMediaHandles.github;// Will only save the 'github' and 'twitter' propertiesuser.save();
```


Map types are stored asBSON objects in MongoDB.
Keys in a BSON object are ordered, so this means theinsertion orderproperty of maps is maintained.

[BSON objects in MongoDB](https://en.wikipedia.org/wiki/BSON#Data_types_and_syntax)

[insertion order](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#Description)


Mongoose supports a special$*syntax topopulateall elements in a map.
For example, suppose yoursocialMediaHandlesmap contains aref:

`$*`
[populate](populate.html)

`socialMediaHandles`
`ref`

```javascript
constuserSchema =newSchema({socialMediaHandles: {type:Map,of:newSchema({handle:String,oauth: {type:ObjectId,ref:'OAuth'}
    })
  }
});constUser= mongoose.model('User', userSchema);
```


To populate everysocialMediaHandlesentry'soauthproperty, you should populate
onsocialMediaHandles.$*.oauth:

`socialMediaHandles`
`oauth`
`socialMediaHandles.$*.oauth`

```javascript
constuser =awaitUser.findOne().populate('socialMediaHandles.$*.oauth');
```


### UUID

[UUID](#uuid)


Mongoose also supports a UUID type that stores UUID instances asNode.js buffers.
We recommend usingObjectIdsrather than UUIDs for unique document ids in Mongoose, but you may use UUIDs if you need to.

[Node.js buffers](https://thecodebarbarian.com/an-overview-of-buffers-in-node-js.html)

[ObjectIds](#objectids)


In Node.js, a UUID is represented as an instance ofbson.Binarytype with agetterthat converts the binary to a string when you access it.
Mongoose stores UUIDs asbinary data with subtype 4 in MongoDB.

`bson.Binary`
[getter](./tutorials/getters-setters.html)

[binary data with subtype 4 in MongoDB](https://www.mongodb.com/docs/manual/reference/bson-types/#binary-data)


```javascript
constauthorSchema =newSchema({_id:Schema.Types.UUID,// Can also do `_id: 'UUID'`name:String});constAuthor= mongoose.model('Author', authorSchema);constbookSchema =newSchema({authorId: {type:Schema.Types.UUID,ref:'Author'}
});constBook= mongoose.model('Book', bookSchema);constauthor =newAuthor({name:'Martin Fowler'});console.log(typeofauthor._id);// 'string'console.log(author.toObject()._idinstanceofmongoose.mongo.BSON.Binary);// trueconstbook =newBook({authorId:'09190f70-3d30-11e5-8814-0f4df9a59c41'});
```


To create UUIDs, we recommend usingNode's built-in UUIDv4 generator.

[Node's built-in UUIDv4 generator](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions)


```javascript
const{ randomUUID } =require('crypto');constschema =newmongoose.Schema({docId: {type:'UUID',default:() =>randomUUID()
  }
});
```


### BigInt

[BigInt](#bigint)


Mongoose supportsJavaScript BigIntsas a SchemaType.
BigInts are stored as64-bit integers in MongoDB (BSON type "long").

[JavaScript BigInts](https://thecodebarbarian.com/an-overview-of-bigint-in-node-js.html)

[64-bit integers in MongoDB (BSON type "long")](https://www.mongodb.com/docs/manual/reference/bson-types/)


```javascript
constquestionSchema =newSchema({answer:BigInt});constQuestion= mongoose.model('Question', questionSchema);constquestion =newQuestion({answer:42n});typeofquestion.answer;// 'bigint'
```


## Getters

[Getters](#getters)


Getters are like virtuals for paths defined in your schema. For example,
let's say you wanted to store user profile pictures as relative paths and
then add the hostname in your application. Below is how you would structure
youruserSchema:

`userSchema`

```javascript
constroot ='https://s3.amazonaws.com/mybucket';constuserSchema =newSchema({name:String,picture: {type:String,get:v=>`${root}${v}`}
});constUser= mongoose.model('User', userSchema);constdoc =newUser({name:'Val',picture:'/123.png'});
doc.picture;// 'https://s3.amazonaws.com/mybucket/123.png'doc.toObject({getters:false}).picture;// '/123.png'
```


Generally, you only use getters on primitive paths as opposed to arrays
or subdocuments. Because getters override what accessing a Mongoose path returns,
declaring a getter on an object may remove Mongoose change tracking for
that path.


```javascript
constschema =newSchema({arr: [{url:String}]
});constroot ='https://s3.amazonaws.com/mybucket';// Bad, don't do this!schema.path('arr').get(v=>{returnv.map(el=>Object.assign(el, {url: root + el.url}));
});// Laterdoc.arr.push({key:String});
doc.arr[0];// 'undefined' because every `doc.arr` creates a new array!
```


Instead of declaring a getter on the array as shown above, you should
declare a getter on theurlstring as shown below. If you need to declare
a getter on a nested document or array, be very careful!

`url`

```javascript
constschema =newSchema({arr: [{url:String}]
});constroot ='https://s3.amazonaws.com/mybucket';// Good, do this instead of declaring a getter on `arr`schema.path('arr.0.url').get(v=>`${root}${v}`);
```


## Schemas

[Schemas](#schemas)


To declare a path as anotherschema,
settypeto the sub-schema's instance.

[schema](guide.html#definition)

`type`

To set a default value based on the sub-schema's shape, simply set a default value,
and the value will be cast based on the sub-schema's definition before being set
during document creation.


```javascript
constsubSchema =newmongoose.Schema({// some schema definition here});constschema =newmongoose.Schema({data: {type: subSchema,default: {}
  }
});
```


## Creating Custom Types

[Creating Custom Types](#customtypes)


Mongoose can also be extended withcustom SchemaTypes. Search thepluginssite for compatible types likemongoose-long,mongoose-int32,
andmongoose-function.

[custom SchemaTypes](customschematypes.html)

[plugins](http://plugins.mongoosejs.io)

[mongoose-long](https://github.com/aheckmann/mongoose-long)

[mongoose-int32](https://github.com/vkarpov15/mongoose-int32)

[mongoose-function](https://github.com/aheckmann/mongoose-function)


Read more about creating custom SchemaTypeshere.

[here](customschematypes.html)


## Theschema.path()Function

[Theschema.path()Function](#path)

`schema.path()`

Theschema.path()function returns the instantiated schema type for a
given path.

`schema.path()`

```javascript
constsampleSchema =newSchema({name: {type:String,required:true} });console.log(sampleSchema.path('name'));// Output looks like:/**
 * SchemaString {
 *   enumValues: [],
  *   regExp: null,
  *   path: 'name',
  *   instance: 'String',
  *   validators: ...
  */
```


You can use this function to inspect the schema type for a given path,
including what validators it has and what the type is.


## Further Reading

[Further Reading](#further-reading)


An Introduction to Mongoose SchemaTypesMongoose Schema Types

- An Introduction to Mongoose SchemaTypes

- Mongoose Schema Types


## Next Up

[Next Up](#next-up)


Now that we've coveredSchemaTypes, let's take a look atConnections.

`SchemaTypes`
[Connections](connections.html)


[Source](https://mongoosejs.com/docs/schematypes.html#maps)