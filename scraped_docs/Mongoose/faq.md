# FAQ


# FAQ

[FAQ](#faq)


Q. I get an errorconnect ECONNREFUSED ::1:27017when connecting tolocalhost. Why?

[Q](#localhost-ipv6)

`connect ECONNREFUSED ::1:27017`
`localhost`

The easy solution is to replacelocalhostwith127.0.0.1.

`localhost`
`127.0.0.1`

The reason why this error happens is that Node.js 18 and up prefer IPv6 addresses over IPv4 by default.
And, most Linux and OSX machines have a::1     localhostentry in/etc/hostsby default.
That means that Node.js 18 will assume thatlocalhostmeans the IPv6::1address.
And MongoDB doesn't accept IPv6 connections by default.

`::1     localhost`
`/etc/hosts`
`localhost`
`::1`

You can also fix this error byenabling IPv6 support on your MongoDB server.

[enabling IPv6 support on your MongoDB server](https://www.mongodb.com/docs/manual/core/security-mongodb-configuration/)


Q. Operation...timed out after 10000 ms. What gives?

[Q](#operation-buffering-timed-out)

`...`

A. At its core, this issue stems from not connecting to MongoDB.
You can use Mongoose before connecting to MongoDB, but you must connect at some point. For example:


```javascript
awaitmongoose.createConnection(mongodbUri).asPromise();constTest= mongoose.model('Test', schema);awaitTest.findOne();// Will throw "Operation timed out" error because didn't call `mongoose.connect()`
```


```javascript
awaitmongoose.connect(mongodbUri);constdb = mongoose.createConnection();constTest= db.model('Test', schema);awaitTest.findOne();// Will throw "Operation timed out" error because `db` isn't connected to MongoDB
```


Q. I am able to connect locally but when I try to connect to MongoDB Atlas I get this error. What gives?

[Q](#not-local)


You must ensure that you have whitelisted your ip onmongodbto allow Mongoose to connect.
You can allow access from all ips with0.0.0.0/0.

[mongodb](https://www.mongodb.com/docs/atlas/security/ip-access-list/)

`0.0.0.0/0`

Q. x.$__y is not a function. What gives?

[Q](#not-a-function)


A. This issue is a result of having multiple versions of mongoose installed that are incompatible with each other.
Runnpm list | grep "mongoose"to find and remedy the problem.
If you're storing schemas or models in a separate npm package, please list Mongoose inpeerDependenciesrather thandependenciesin your separate package.

`npm list | grep "mongoose"`
`peerDependencies`
`dependencies`

Q. I declared a schema property asuniquebut I can still save duplicates. What gives?

[Q](#unique-doesnt-work)

`unique`

A. Mongoose doesn't handleuniqueon its own:{ name: { type: String, unique: true } }is just a shorthand for creating aMongoDB unique index onname.
For example, if MongoDB doesn't already have a unique index onname, the below code will not error despite the fact thatuniqueis true.

`unique`
`{ name: { type: String, unique: true } }`
[MongoDB unique index onname](https://www.mongodb.com/docs/manual/core/index-unique/)

`name`
`name`
`unique`

```javascript
constschema =newmongoose.Schema({name: {type:String,unique:true}
});constModel= db.model('Test', schema);// No error, unless index was already builtawaitModel.create([{name:'Val'}, {name:'Val'}]);
```


However, if you wait for the index to build using theModel.on('index')event, attempts to save duplicates will correctly error.

`Model.on('index')`

```javascript
constschema =newmongoose.Schema({name: {type:String,unique:true}
});constModel= db.model('Test', schema);// Wait for model's indexes to finish. The `init()`// function is idempotent, so don't worry about triggering an index rebuild.awaitModel.init();// Throws a duplicate key errorawaitModel.create([{name:'Val'}, {name:'Val'}]);
```


MongoDB persists indexes, so you only need to rebuild indexes if you're starting
with a fresh database or you randb.dropDatabase(). In a production environment,
you shouldcreate your indexes using the MongoDB shellrather than relying on mongoose to do it for you. Theuniqueoption for schemas is
convenient for development and documentation, but mongoose isnotan index management solution.

`db.dropDatabase()`
[create your indexes using the MongoDB shell](https://www.mongodb.com/docs/manual/reference/method/db.collection.createIndex/)

`unique`

Q. When I have a nested property in a schema, mongoose adds empty objects by default. Why?

[Q](#nested-properties)


```javascript
constschema =newmongoose.Schema({nested: {prop:String}
});constModel= db.model('Test', schema);// The below prints `{ _id: /* ... */, nested: {} }`, mongoose assigns// `nested` to an empty object `{}` by default.console.log(newModel());
```


A. This is a performance optimization. These empty objects are not saved
to the database, nor are they in the resulttoObject(), nor do they show
up inJSON.stringify()output unless you turn off theminimizeoption.

`toObject()`
`JSON.stringify()`
[minimizeoption](guide.html#minimize)

`minimize`

The reason for this behavior is that Mongoose's change detection
and getters/setters are based onObject.defineProperty().
In order to support change detection on nested properties without incurring
the overhead of runningObject.defineProperty()every time a document is created,
mongoose defines properties on theModelprototype when the model is compiled.
Because mongoose needs to define getters and setters fornested.prop,nestedmust always be defined as an object on a mongoose document, even ifnestedis undefined on the underlyingPOJO.

[Object.defineProperty()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)

`Object.defineProperty()`
`Object.defineProperty()`
`Model`
`nested.prop`
`nested`
`nested`
[POJO](guide.html#minimize)


Q. I'm using an arrow function for avirtual,middleware,getter/setter, ormethodand the value ofthisis wrong.

[Q](#arrow-functions)

[virtual](guide.html#virtuals)

[middleware](middleware.html)

[getter](api/schematype.html#schematype_SchemaType-get)

[setter](api/schematype.html#schematype_SchemaType-set)

[method](guide.html#methods)

`this`

A. Arrow functionshandle thethiskeyword differently than conventional functions.
Mongoose getters/setters depend onthisto give you access to the document that you're writing to, but this functionality does not work with arrow functions. Donotuse arrow functions for mongoose getters/setters unless do not intend to access the document in the getter/setter.

[handle thethiskeyword differently than conventional functions](https://masteringjs.io/tutorials/fundamentals/arrow#why-not-arrow-functions)

`this`
`this`

```javascript
// Do **NOT** use arrow functions as shown below unless you're certain// that's what you want. If you're reading this FAQ, odds are you should// just be using a conventional function.constschema =newmongoose.Schema({propWithGetter: {type:String,get:v=>{// Will **not** be the doc, do **not** use arrow functions for getters/settersconsole.log(this);returnv;
    }
  }
});// `this` will **not** be the doc, do **not** use arrow functions for methodsschema.method.arrowMethod=() =>this;
schema.virtual('virtualWithArrow').get(() =>{// `this` will **not** be the doc, do **not** use arrow functions for virtualsconsole.log(this);
});
```


Q. I have an embedded property namedtypelike this:

[Q](#type-key)

`type`

```javascript
constholdingSchema =newSchema({// You might expect `asset` to be an object that has 2 properties,// but unfortunately `type` is special in mongoose so mongoose// interprets this schema to mean that `asset` is a stringasset: {type:String,ticker:String}
});
```


But mongoose gives me a CastError telling me that it can't cast an object
to a string when I try to save aHoldingwith anassetobject. Why
is this?

`Holding`
`asset`

```javascript
Holding.create({asset: {type:'stock',ticker:'MDB'} }).catch(error=>{// Cast to String failed for value "{ type: 'stock', ticker: 'MDB' }" at path "asset"console.error(error);
});
```


A. Thetypeproperty is special in mongoose, so when you saytype: String, mongoose interprets it as a type declaration. In the
above schema, mongoose thinksassetis a string, not an object. Do
this instead:

`type`
`type: String`
`asset`

```javascript
constholdingSchema =newSchema({// This is how you tell mongoose you mean `asset` is an object with// a string property `type`, as opposed to telling mongoose that `asset`// is a string.asset: {type: {type:String},ticker:String}
});
```


Q. I'm populating a nested property under an array like the below code:

[Q](#populate_sort_order)


```javascript
newSchema({arr: [{child: {ref:'OtherModel',type:Schema.Types.ObjectId}
  }]
});
```


.populate({ path: 'arr.child', options: { sort: 'name' } })won't sort byarr.child.name?

`.populate({ path: 'arr.child', options: { sort: 'name' } })`
`arr.child.name`

A. Seethis GitHub issue. It's a known issue but one that's exceptionally difficult to fix.

[this GitHub issue](https://github.com/Automattic/mongoose/issues/2202)


Q. All function calls on my models hang, what am I doing wrong?

[Q](#model_functions_hanging)


A. By default, mongoose will buffer your function calls until it can
connect to MongoDB. Read thebuffering section of the connection docsfor more information.

[buffering section of the connection docs](connections.html#buffering)


Q. How can I enable debugging?

[Q](#enable_debugging)


A. Set thedebugoption:

`debug`

```javascript
// all executed methods log output to consolemongoose.set('debug',true);// disable colors in debug modemongoose.set('debug', {color:false});// get mongodb-shell friendly output (ISODate)mongoose.set('debug', {shell:true});
```


For more debugging options (streams, callbacks), see the'debug' option under.set().

['debug' option under.set()](api/mongoose.html#mongoose_Mongoose-set)

`.set()`

Q. Mysave()callback never executes. What am I doing wrong?

[Q](#callback_never_executes)

`save()`

A. Allcollectionactions (insert, remove, queries, etc.) are queued
until Mongoose successfully connects to MongoDB. It is likely you haven't called Mongoose'sconnect()orcreateConnection()function yet.

`collection`
`connect()`
`createConnection()`

In Mongoose 5.11, there is abufferTimeoutMSoption (set to 10000 by default) that configures how long
Mongoose will allow an operation to stay buffered before throwing an error.

`bufferTimeoutMS`

If you want to opt out of Mongoose's buffering mechanism across your entire
application, set the globalbufferCommandsoption to false:

`bufferCommands`

```javascript
mongoose.set('bufferCommands',false);
```


Instead of opting out of Mongoose's buffering mechanism, you may want to instead reducebufferTimeoutMSto make Mongoose only buffer for a short time.

`bufferTimeoutMS`

```javascript
// If an operation is buffered for more than 500ms, throw an error.mongoose.set('bufferTimeoutMS',500);
```


Q. Should I create/destroy a new connection for each database operation?

[Q](#creating_connections)


A. No. Open your connection when your application starts up and leave
it open until the application shuts down.


Q. Why do I get "OverwriteModelError: Cannot overwrite .. model once
compiled" when I use nodemon / a testing framework?

[Q](#overwrite-model-error)


A.mongoose.model('ModelName', schema)requires 'ModelName' to be
unique, so you can access the model by usingmongoose.model('ModelName').
If you putmongoose.model('ModelName', schema);in amochabeforeEach()hook, this code will
attempt to create a new model named 'ModelName' beforeeverytest,
and so you will get an error. Make sure you only create a new model with
a given nameonce. If you need to create multiple models with the
same name, create a new connection and bind the model to the connection.

`mongoose.model('ModelName', schema)`
`mongoose.model('ModelName')`
`mongoose.model('ModelName', schema);`
[mochabeforeEach()hook](https://masteringjs.io/tutorials/mocha/beforeeach)

`beforeEach()`

```javascript
constmongoose =require('mongoose');constconnection = mongoose.createConnection(/* ... */);// use mongoose.SchemaconstkittySchema = mongoose.Schema({name:String});// use connection.modelconstKitten= connection.model('Kitten', kittySchema);
```


Q. How can I change mongoose's default behavior of initializing an array path to an empty array so that I can require real data on document creation?

[Q](#array-defaults)


A. You can set the default of the array toundefined.

`undefined`

```javascript
constCollectionSchema=newSchema({field1: {type: [String],default:void0}
});
```


Q. How can I initialize an array path tonull?

[Q](#initialize-array-path-null)

`null`

A. You can set the default of the array tonull.

[null](https://masteringjs.io/tutorials/fundamentals/null)

`null`

```javascript
constCollectionSchema=newSchema({field1: {type: [String],default:null}
});
```


Q. Why does my aggregate $match fail to return the document that my find query returns when working with dates?

[Q](#aggregate-casting)


A. Mongoose does not cast aggregation pipeline stages because with $project,
$group, etc. the type of a property may change during the aggregation. If you want
to query by date using the aggregation framework, you're responsible for ensuring
that you're passing in a valid date.


Q. Why don't in-place modifications to date objects
(e.g.date.setMonth(1);) get saved?

[Q](#date_changes)

`date.setMonth(1);`

```javascript
doc.createdAt.setDate(2011,5,1);
doc.save();// createdAt changes won't get saved!
```


A. Mongoose currently doesn't watch for in-place updates to date
objects. If you have need for this feature, feel free to discuss onthis GitHub issue.
There are several workarounds:

[this GitHub issue](https://github.com/Automattic/mongoose/issues/3738)


```javascript
doc.createdAt.setDate(2011,5,1);
doc.markModified('createdAt');
doc.save();// Worksdoc.createdAt=newDate(2011,5,1).setHours(4);
doc.save();// Works
```


Q. Why does callingsave()multiple times on the same document in parallel only let
the first save call succeed and return ParallelSaveErrors for the rest?

[Q](#parallel_saves)

`save()`

A. Due to the asynchronous nature of validation and middleware in general, callingsave()multiple times in parallel on the same doc could result in conflicts. For example,
validating, and then subsequently invalidating the same path.

`save()`

Q. Why isany12 character string successfully cast to an ObjectId?

[Q](#objectid-validation)


A. Technically, any 12 character string is a validObjectId.
Consider using a regex like/^[a-f0-9]{24}$/to test whether a string is exactly 24 hex characters.

[ObjectId](https://www.mongodb.com/docs/manual/reference/bson-types/#objectid)

`/^[a-f0-9]{24}$/`

Q. Why do keys in Mongoose Maps have to be strings?

[Q](#map-keys-strings)


A. Because the Map eventually gets stored in MongoDB where the keys must be strings.


Q. I am usingModel.find(...).populate(...)with thelimitoption, but getting fewer results than the limit. What gives?

[Q](#limit-vs-perDocumentLimit)

`Model.find(...).populate(...)`
`limit`

A. In order to avoid executing a separate query for each document returned from thefindquery, Mongoose
instead queries using (numDocuments * limit) as the limit. If you need the correct limit, you should use theperDocumentLimitoption (new in Mongoose 5.9.0). Just keep in
mind that populate() will execute a separate query for each document.

`find`
[perDocumentLimit](populate.html#limit-vs-perDocumentLimit)


Q. My query/update seems to execute twice. Why is this happening?

[Q](#duplicate-query)


A. The most common cause of duplicate queries ismixing callbacks and promises with queries.
That's because passing a callback to a query function, likefind()orupdateOne(),
immediately executes the query, and callingthen()executes the query again.

`find()`
`updateOne()`
[then()](https://masteringjs.io/tutorials/fundamentals/then)

`then()`

Mixing promises and callbacks can lead to duplicate entries in arrays.
For example, the below code inserts 2 entries into thetagsarray, *notjust 1.

`tags`

```javascript
constBlogPost= mongoose.model('BlogPost',newSchema({title:String,tags: [String]
}));// Because there's both `await` **and** a callback, this `updateOne()` executes twice// and thus pushes the same string into `tags` twice.constupdate = {$push: {tags: ['javascript'] } };awaitBlogPost.updateOne({title:'Introduction to Promises'}, update,(err, res) =>{console.log(res);
});
```


Something to add?


If you'd like to contribute to this page, pleasevisit iton github and use theEditbutton to send a pull request.

[visit it](https://github.com/Automattic/mongoose/tree/master/docs/faq.md)

[Edit](https://github.com/blog/844-forking-with-the-edit-button)


[Source](https://mongoosejs.com/docs/faq.html#overwrite-model-error)