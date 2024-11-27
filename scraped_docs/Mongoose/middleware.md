# Middleware


# Middleware

[Middleware](#middleware)


Middleware (also called pre and posthooks) are functions which are passed
control during execution of asynchronous functions. Middleware is specified
on the schema level and is useful for writingplugins.

[plugins](plugins.html)


Types of MiddlewarePreErrors in Pre HooksPostAsynchronous Post HooksDefine Middleware Before Compiling ModelsSave/Validate HooksAccessing Parameters in MiddlewareNaming ConflictsNotes on findAndUpdate() and Query MiddlewareError Handling MiddlewareAggregation HooksSynchronous Hooks

- Types of Middleware

- Pre

- Errors in Pre Hooks

- Post

- Asynchronous Post Hooks

- Define Middleware Before Compiling Models

- Save/Validate Hooks

- Accessing Parameters in Middleware

- Naming Conflicts

- Notes on findAndUpdate() and Query Middleware

- Error Handling Middleware

- Aggregation Hooks

- Synchronous Hooks


## Types of Middleware

[Types of Middleware](#types-of-middleware)


Mongoose has 4 types
of middleware: document middleware, model middleware, aggregate middleware, and query middleware.


Document middleware is supported for the following document functions.
In Mongoose, a document is an instance of aModelclass.
In document middleware functions,thisrefers to the document. To access the model, usethis.constructor.

`Model`
`this`
`this.constructor`

validatesaveupdateOnedeleteOneinit(note: init hooks aresynchronous)

- validate

- save

- updateOne

- deleteOne

- init(note: init hooks aresynchronous)


Query middleware is supported for the following Query functions.
Query middleware executes when you callexec()orthen()on a Query object, orawaiton a Query object.
In query middleware functions,thisrefers to the query.

`exec()`
`then()`
`await`
`this`

countcountDocumentsdeleteManydeleteOneestimatedDocumentCountfindfindOnefindOneAndDeletefindOneAndReplacefindOneAndUpdatereplaceOneupdateOneupdateManyvalidate

- count

- countDocuments

- deleteMany

- deleteOne

- estimatedDocumentCount

- find

- findOne

- findOneAndDelete

- findOneAndReplace

- findOneAndUpdate

- replaceOne

- updateOne

- updateMany

- validate


Aggregate middleware is forMyModel.aggregate().
Aggregate middleware executes when you callexec()on an aggregate object.
In aggregate middleware,thisrefers to theaggregation object.

`MyModel.aggregate()`
`exec()`
`this`
[aggregation object](api/model.html#model_Model-aggregate)


aggregate

- aggregate


Model middleware is supported for the following model functions.
Don't confuse model middleware and document middleware: model middleware hooks intostaticfunctions on aModelclass, document middleware hooks intomethodson aModelclass.
In model middleware functions,thisrefers to the model.

`Model`
`Model`
`this`

bulkWritecreateCollectioninsertMany

- bulkWrite

- createCollection

- insertMany


Here are the possible strings that can be passed topre()

`pre()`

aggregatebulkWritecountcountDocumentscreateCollectiondeleteOnedeleteManyestimatedDocumentCountfindfindOnefindOneAndDeletefindOneAndReplacefindOneAndUpdateinitinsertManyreplaceOnesaveupdateupdateOneupdateManyvalidate

- aggregate

- bulkWrite

- count

- countDocuments

- createCollection

- deleteOne

- deleteMany

- estimatedDocumentCount

- find

- findOne

- findOneAndDelete

- findOneAndReplace

- findOneAndUpdate

- init

- insertMany

- replaceOne

- save

- update

- updateOne

- updateMany

- validate


All middleware types support pre and post hooks.
How pre and post hooks work is described in more detail below.


Note:Mongoose registersupdateOnemiddleware onQuery.prototype.updateOne()by default.
This means that bothdoc.updateOne()andModel.updateOne()triggerupdateOnehooks, butthisrefers to a query, not a document.
To registerupdateOnemiddleware as document middleware, useschema.pre('updateOne', { document: true, query: false }).

`updateOne`
`Query.prototype.updateOne()`
`doc.updateOne()`
`Model.updateOne()`
`updateOne`
`this`
`updateOne`
`schema.pre('updateOne', { document: true, query: false })`

Note:LikeupdateOne, Mongoose registersdeleteOnemiddleware onQuery.prototype.deleteOneby default.
That means thatModel.deleteOne()will triggerdeleteOnehooks, andthiswill refer to a query.
However,doc.deleteOne()doesnotfiredeleteOnequery middleware for legacy reasons.
To registerdeleteOnemiddleware as document middleware, useschema.pre('deleteOne', { document: true, query: false }).

`updateOne`
`deleteOne`
`Query.prototype.deleteOne`
`Model.deleteOne()`
`deleteOne`
`this`
`doc.deleteOne()`
`deleteOne`
`deleteOne`
`schema.pre('deleteOne', { document: true, query: false })`

Note:Thecreate()function firessave()hooks.

[create()](./api/model.html#model_Model-create)

`create()`
`save()`

Note:Query middlewares are not executed on subdocuments.


```javascript
constchildSchema =newmongoose.Schema({name:String});constmainSchema =newmongoose.Schema({child: [childSchema]
});

mainSchema.pre('findOneAndUpdate',function() {console.log('Middleware on parent document');// Will be executed});

childSchema.pre('findOneAndUpdate',function() {console.log('Middleware on subdocument');// Will not be executed});
```


## Pre

[Pre](#pre)


Pre middleware functions are executed one after another, when each
middleware callsnext.

`next`

```javascript
constschema =newSchema({/* ... */});
schema.pre('save',function(next) {// do stuffnext();
});
```


Inmongoose 5.x, instead of callingnext()manually, you can use a
function that returns a promise. In particular, you can useasync/await.

[mongoose 5.x](http://thecodebarbarian.com/introducing-mongoose-5.html#promises-and-async-await-with-middleware)

`next()`
[async/await](http://thecodebarbarian.com/common-async-await-design-patterns-in-node.js.html)

`async/await`

```javascript
schema.pre('save',function() {returndoStuff().then(() =>doMoreStuff());
});// Or, using async functionsschema.pre('save',asyncfunction() {awaitdoStuff();awaitdoMoreStuff();
});
```


If you usenext(), thenext()call doesnotstop the rest of the code in your middleware function from executing. Usethe earlyreturnpatternto prevent the rest of your middleware function from running when you callnext().

`next()`
`next()`
[the earlyreturnpattern](https://www.bennadel.com/blog/2323-use-a-return-statement-when-invoking-callbacks-especially-in-a-guard-statement.htm)

`return`
`next()`

```javascript
constschema =newSchema({/* ... */});
schema.pre('save',function(next) {if(foo()) {console.log('calling next!');// `return next();` will make sure the rest of this function doesn't run/* return */next();
  }// Unless you comment out the `return` above, 'after next' will printconsole.log('after next');
});
```


### Use Cases

[Use Cases](#use-cases)


Middleware are useful for atomizing model logic. Here are some other ideas:


complex validationremoving dependent documents (removing a user removes all their blogposts)asynchronous defaultsasynchronous tasks that a certain action triggers

- complex validation

- removing dependent documents (removing a user removes all their blogposts)

- asynchronous defaults

- asynchronous tasks that a certain action triggers


### Errors in Pre Hooks

[Errors in Pre Hooks](#error-handling)


If any pre hook errors out, mongoose will not execute subsequent middleware
or the hooked function. Mongoose will instead pass an error to the callback
and/or reject the returned promise. There are several ways to report an
error in middleware:


```javascript
schema.pre('save',function(next) {consterr =newError('something went wrong');// If you call `next()` with an argument, that argument is assumed to be// an error.next(err);
});

schema.pre('save',function() {// You can also return a promise that rejectsreturnnewPromise((resolve, reject) =>{reject(newError('something went wrong'));
  });
});

schema.pre('save',function() {// You can also throw a synchronous errorthrownewError('something went wrong');
});

schema.pre('save',asyncfunction() {awaitPromise.resolve();// You can also throw an error in an `async` functionthrownewError('something went wrong');
});// later...// Changes will not be persisted to MongoDB because a pre hook errored outmyDoc.save(function(err) {console.log(err.message);// something went wrong});
```


Callingnext()multiple times is a no-op. If you callnext()with an
errorerr1and then throw an errorerr2, mongoose will reporterr1.

`next()`
`next()`
`err1`
`err2`
`err1`

## Post middleware

[Post middleware](#post)


postmiddleware are executedafterthe hooked method and all of itspremiddleware have completed.

[post](api.html#schema_Schema-post)

`pre`

```javascript
schema.post('init',function(doc) {console.log('%s has been initialized from the db', doc._id);
});
schema.post('validate',function(doc) {console.log('%s has been validated (but not saved yet)', doc._id);
});
schema.post('save',function(doc) {console.log('%s has been saved', doc._id);
});
schema.post('deleteOne',function(doc) {console.log('%s has been deleted', doc._id);
});
```


## Asynchronous Post Hooks

[Asynchronous Post Hooks](#post-async)


If your post hook function takes at least 2 parameters, mongoose will assume the second parameter is anext()function that you will call to trigger the next middleware in the sequence.

`next()`

```javascript
// Takes 2 parameters: this is an asynchronous post hookschema.post('save',function(doc, next) {setTimeout(function() {console.log('post1');// Kick off the second post hooknext();
  },10);
});// Will not execute until the first middleware calls `next()`schema.post('save',function(doc, next) {console.log('post2');next();
});
```


You can also pass an async function topost().
If you pass an async function that takes at least 2 parameters, you are still responsible for callingnext().
However, you can also pass in an async function that takes less than 2 parameters, and Mongoose will wait for the promise to resolve.

`post()`
`next()`

```javascript
schema.post('save',asyncfunction(doc) {awaitnewPromise(resolve=>setTimeout(resolve,1000));console.log('post1');// If less than 2 parameters, no need to call `next()`});

schema.post('save',asyncfunction(doc, next) {awaitnewPromise(resolve=>setTimeout(resolve,1000));console.log('post1');// If there's a `next` parameter, you need to call `next()`.next();
});
```


## Define Middleware Before Compiling Models

[Define Middleware Before Compiling Models](#defining)


Callingpre()orpost()aftercompiling a modeldoesnotwork in Mongoose in general. For example, the belowpre('save')middleware will not fire.

`pre()`
`post()`
[compiling a model](models.html#compiling)

`pre('save')`

```javascript
constschema =newmongoose.Schema({name:String});// Compile a model from the schemaconstUser= mongoose.model('User', schema);// Mongoose will **not** call the middleware function, because// this middleware was defined after the model was compiledschema.pre('save',() =>console.log('Hello from pre save'));constuser =newUser({name:'test'});
user.save();
```


This means that you must add all middleware andpluginsbeforecallingmongoose.model().
The below script will print out "Hello from pre save":

[plugins](plugins.html)

[mongoose.model()](api/mongoose.html#mongoose_Mongoose-model)

`mongoose.model()`

```javascript
constschema =newmongoose.Schema({name:String});// Mongoose will call this middleware function, because this script adds// the middleware to the schema before compiling the model.schema.pre('save',() =>console.log('Hello from pre save'));// Compile a model from the schemaconstUser= mongoose.model('User', schema);constuser =newUser({name:'test'});
user.save();
```


As a consequence, be careful about exporting Mongoose models from the same
file that you define your schema. If you choose to use this pattern, you
must defineglobal pluginsbeforecallingrequire()on your model file.

[global plugins](api/mongoose.html#mongoose_Mongoose-plugin)

`require()`

```javascript
constschema =newmongoose.Schema({name:String});// Once you `require()` this file, you can no longer add any middleware// to this schema.module.exports= mongoose.model('User', schema);
```


## Save/Validate Hooks

[Save/Validate Hooks](#order)


Thesave()function triggersvalidate()hooks, because mongoose
has a built-inpre('save')hook that callsvalidate(). This means
that allpre('validate')andpost('validate')hooks get calledbeforeanypre('save')hooks.

`save()`
`validate()`
`pre('save')`
`validate()`
`pre('validate')`
`post('validate')`
`pre('save')`

```javascript
schema.pre('validate',function() {console.log('this gets printed first');
});
schema.post('validate',function() {console.log('this gets printed second');
});
schema.pre('save',function() {console.log('this gets printed third');
});
schema.post('save',function() {console.log('this gets printed fourth');
});
```


## Accessing Parameters in Middleware

[Accessing Parameters in Middleware](#accessing-parameters-in-middleware)


Mongoose provides 2 ways to get information about the function call that triggered the middleware.
For query middleware, we recommend usingthis, which will be aMongoose Query instance.

`this`
[Mongoose Query instance](api/query.html)


```javascript
constuserSchema =newSchema({name:String,age:Number});
userSchema.pre('findOneAndUpdate',function() {console.log(this.getFilter());// { name: 'John' }console.log(this.getUpdate());// { age: 30 }});constUser= mongoose.model('User', userSchema);awaitUser.findOneAndUpdate({name:'John'}, {$set: {age:30} });
```


For document middleware, likepre('save'), Mongoose passes the 1st parameter tosave()as the 2nd argument to yourpre('save')callback.
You should use the 2nd argument to get access to thesave()call'soptions, because Mongoose documents don't store all the options you can pass tosave().

`pre('save')`
`save()`
`pre('save')`
`save()`
`options`
`save()`

```javascript
constuserSchema =newSchema({name:String,age:Number});
userSchema.pre('save',function(next, options) {
  options.validateModifiedOnly;// true// Remember to call `next()` unless you're using an async function or returning a promisenext();
});constUser= mongoose.model('User', userSchema);constdoc =newUser({name:'John',age:30});awaitdoc.save({validateModifiedOnly:true});
```


## Naming Conflicts

[Naming Conflicts](#naming)


Mongoose has both query and document hooks fordeleteOne().

`deleteOne()`

```javascript
schema.pre('deleteOne',function() {console.log('Removing!'); });// Does **not** print "Removing!". Document middleware for `deleteOne` is not executed by defaultawaitdoc.deleteOne();// Prints "Removing!"awaitModel.deleteOne();
```


You can pass options toSchema.pre()andSchema.post()to switch whether
Mongoose calls yourdeleteOne()hook forDocument.prototype.deleteOne()orQuery.prototype.deleteOne(). Note here that you need to set bothdocumentandqueryproperties in the passed object:

[Schema.pre()](api.html#schema_Schema-pre)

`Schema.pre()`
[Schema.post()](api.html#schema_Schema-post)

`Schema.post()`
`deleteOne()`
[Document.prototype.deleteOne()](api/model.html#Model.prototype.deleteOne())

`Document.prototype.deleteOne()`
[Query.prototype.deleteOne()](api/query.html#Query.prototype.deleteOne())

`Query.prototype.deleteOne()`
`document`
`query`

```javascript
// Only document middlewareschema.pre('deleteOne', {document:true,query:false},function() {console.log('Deleting doc!');
});// Only query middleware. This will get called when you do `Model.deleteOne()`// but not `doc.deleteOne()`.schema.pre('deleteOne', {query:true,document:false},function() {console.log('Deleting!');
});
```


Mongoose also has both query and document hooks forvalidate().
UnlikedeleteOneandupdateOne,validatemiddleware applies toDocument.prototype.validateby default.

`validate()`
`deleteOne`
`updateOne`
`validate`
`Document.prototype.validate`

```javascript
constschema =newmongoose.Schema({name:String});
schema.pre('validate',function() {console.log('Document validate');
});
schema.pre('validate', {query:true,document:false},function() {console.log('Query validate');
});constTest= mongoose.model('Test', schema);constdoc =newTest({name:'foo'});// Prints "Document validate"awaitdoc.validate();// Prints "Query validate"awaitTest.find().validate();
```


## Notes onfindAndUpdate()and Query Middleware

[Notes onfindAndUpdate()and Query Middleware](#notes)

`findAndUpdate()`

Pre and postsave()hooks arenotexecuted onupdate(),findOneAndUpdate(), etc. You can see a more detailed discussion why inthis GitHub issue.
Mongoose 4.0 introduced distinct hooks for these functions.

`save()`
`update()`
`findOneAndUpdate()`
[this GitHub issue](http://github.com/Automattic/mongoose/issues/964)


```javascript
schema.pre('find',function() {console.log(thisinstanceofmongoose.Query);// truethis.start=Date.now();
});

schema.post('find',function(result) {console.log(thisinstanceofmongoose.Query);// true// prints returned documentsconsole.log('find() returned '+JSON.stringify(result));// prints number of milliseconds the query tookconsole.log('find() took '+ (Date.now() -this.start) +' milliseconds');
});
```


Query middleware differs from document middleware in a subtle but
important way: in document middleware,thisrefers to the document
being updated. In query middleware, mongoose doesn't necessarily have
a reference to the document being updated, sothisrefers to thequeryobject rather than the document being updated.

`this`
`this`

For instance, if you wanted to add anupdatedAttimestamp to everyupdateOne()call, you would use the following pre hook.

`updatedAt`
`updateOne()`

```javascript
schema.pre('updateOne',function() {this.set({updatedAt:newDate() });
});
```


Youcannotaccess the document being updated inpre('updateOne')orpre('findOneAndUpdate')query middleware. If you need to access the document
that will be updated, you need to execute an explicit query for the document.

`pre('updateOne')`
`pre('findOneAndUpdate')`

```javascript
schema.pre('findOneAndUpdate',asyncfunction() {constdocToUpdate =awaitthis.model.findOne(this.getQuery());console.log(docToUpdate);// The document that `findOneAndUpdate()` will modify});
```


However, if you definepre('updateOne')document middleware,thiswill be the document being updated. That's becausepre('updateOne')document middleware hooks intoDocument#updateOne()rather thanQuery#updateOne().

`pre('updateOne')`
`this`
`pre('updateOne')`
[Document#updateOne()](api/document.html#document_Document-updateOne)

`Document#updateOne()`
`Query#updateOne()`

```javascript
schema.pre('updateOne', {document:true,query:false},function() {console.log('Updating');
});constModel= mongoose.model('Test', schema);constdoc =newModel();awaitdoc.updateOne({$set: {name:'test'} });// Prints "Updating"// Doesn't print "Updating", because `Query#updateOne()` doesn't fire// document middleware.awaitModel.updateOne({}, {$set: {name:'test'} });
```


## Error Handling Middleware

[Error Handling Middleware](#error-handling-middleware)


Middleware execution normally stops the first time a piece of middleware
callsnext()with an error. However, there is a special kind of post
middleware called "error handling middleware" that executes specifically
when an error occurs. Error handling middleware is useful for reporting
errors and making error messages more readable.

`next()`

Error handling middleware is defined as middleware that takes one extra
parameter: the 'error' that occurred as the first parameter to the function.
Error handling middleware can then transform the error however you want.


```javascript
constschema =newSchema({name: {type:String,// Will trigger a MongoServerError with code 11000 when// you save a duplicateunique:true}
});// Handler **must** take 3 parameters: the error that occurred, the document// in question, and the `next()` functionschema.post('save',function(error, doc, next) {if(error.name==='MongoServerError'&& error.code===11000) {next(newError('There was a duplicate key error'));
  }else{next();
  }
});// Will trigger the `post('save')` error handlerPerson.create([{name:'Axl Rose'}, {name:'Axl Rose'}]);
```


Error handling middleware also works with query middleware. You can
also define a postupdate()hook that will catch MongoDB duplicate key
errors.

`update()`

```javascript
// The same E11000 error can occur when you call `updateOne()`// This function **must** take 4 parameters.schema.post('updateOne',function(passRawResult, error, res, next) {if(error.name==='MongoServerError'&& error.code===11000) {next(newError('There was a duplicate key error'));
  }else{next();// The `updateOne()` call will still error out.}
});constpeople = [{name:'Axl Rose'}, {name:'Slash'}];awaitPerson.create(people);// Throws "There was a duplicate key error"awaitPerson.updateOne({name:'Slash'}, {$set: {name:'Axl Rose'} });
```


Error handling middleware can transform an error, but it can't remove the
error. Even if you callnext()with no error as shown above, the
function call will still error out.

`next()`

## Aggregation Hooks

[Aggregation Hooks](#aggregate)


You can also define hooks for theModel.aggregate()function.
In aggregation middleware functions,thisrefers to theMongooseAggregateobject.
For example, suppose you're implementing soft deletes on aCustomermodel
by adding anisDeletedproperty. To make sureaggregate()calls only look
at customers that aren't soft deleted, you can use the below middleware to
add a$matchstageto the beginning
of eachaggregation pipeline.

[Model.aggregate()function](api/model.html#model_Model-aggregate)

`Model.aggregate()`
`this`
[MongooseAggregateobject](api/aggregate.html#Aggregate)

`Aggregate`
`Customer`
`isDeleted`
`aggregate()`
[$matchstage](api/aggregate.html#aggregate_Aggregate-match)

`$match`
[aggregation pipeline](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)


```javascript
customerSchema.pre('aggregate',function() {// Add a $match state to the beginning of each pipeline.this.pipeline().unshift({$match: {isDeleted: {$ne:true} } });
});
```


TheAggregate#pipeline()functionlets you access the MongoDB aggregation pipeline that Mongoose will send to
the MongoDB server. It is useful for adding stages to the beginning of the
pipeline from middleware.

[Aggregate#pipeline()function](api/aggregate.html#aggregate_Aggregate-pipeline)

`Aggregate#pipeline()`

## Synchronous Hooks

[Synchronous Hooks](#synchronous)


Certain Mongoose hooks are synchronous, which means they donotsupport
functions that return promises or receive anext()callback. Currently,
onlyinithooks are synchronous, because theinit()functionis synchronous. Below is an example of using pre and post init hooks.

`next()`
`init`
[init()function](api/document.html#document_Document-init)

`init()`

```javascript
[require:post init hooks.*success]
```


To report an error in an init hook, you must throw asynchronouserror.
Unlike all other middleware, init middleware doesnothandle promise
rejections.


```javascript
[require:post init hooks.*error]
```


## Next Up

[Next Up](#next)


Now that we've covered middleware, let's take a look at Mongoose's approach
to faking JOINs with its querypopulationhelper.

[population](populate.html)


[Source](https://mongoosejs.com/docs/middleware.html#naming)