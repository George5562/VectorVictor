# Transactions in Mongoose


# Transactions in Mongoose

[Transactions in Mongoose](#transactions-in-mongoose)


Transactionslet you execute multiple operations in isolation and potentially undo all the operations if one of them fails.
This guide will get you started using transactions with Mongoose.

[Transactions](https://www.mongodb.com/transactions)


## Getting Started with Transactions

[Getting Started with Transactions](#getting-started-with-transactions)


If you haven't already, import mongoose:


```javascript
importmongoosefrom'mongoose';
```


To create a transaction, you first need to create a session usingMongoose#startSessionorConnection#startSession().

[Mongoose#startSession](api/mongoose.html#mongoose_Mongoose-startSession)

`Mongoose#startSession`
[Connection#startSession()](api/connection.html#connection_Connection-startSession)

`Connection#startSession()`

```javascript
// Using Mongoose's default connectionconstsession =awaitmongoose.startSession();// Using custom connectionconstdb =awaitmongoose.createConnection(mongodbUri).asPromise();constsession =awaitdb.startSession();
```


In practice, you should use either thesession.withTransaction()helperor Mongoose'sConnection#transaction()function to run a transaction. Thesession.withTransaction()helper handles:

[session.withTransaction()helper](https://mongodb.github.io/node-mongodb-native/3.2/api/ClientSession.html#withTransaction)

`session.withTransaction()`
`Connection#transaction()`
`session.withTransaction()`

Creating a transactionCommitting the transaction if it succeedsAborting the transaction if your operation throwsRetrying in the event of atransient transaction error.

- Creating a transaction

- Committing the transaction if it succeeds

- Aborting the transaction if your operation throws

- Retrying in the event of atransient transaction error.


```javascript
letsession =null;returnCustomer.createCollection().then(() =>Customer.startSession()).// The `withTransaction()` function's first parameter is a function// that returns a promise.then(_session=>{
    session = _session;returnsession.withTransaction(() =>{returnCustomer.create([{name:'Test'}], {session: session });
    });
  }).then(() =>Customer.countDocuments()).then(count=>assert.strictEqual(count,1)).then(() =>session.endSession());
```


For more information on theClientSession#withTransaction()function, please seethe MongoDB Node.js driver docs.

`ClientSession#withTransaction()`
[the MongoDB Node.js driver docs](https://mongodb.github.io/node-mongodb-native/3.2/api/ClientSession.html#withTransaction)


Mongoose'sConnection#transaction()function is a wrapper aroundwithTransaction()that
integrates Mongoose change tracking with transactions.
For example, suppose yousave()a document in a transaction that later fails.
The changes in that document are not persisted to MongoDB.
TheConnection#transaction()function informs Mongoose change tracking that thesave()was rolled back, and marks all fields that were changed in the transaction as modified.

`Connection#transaction()`
`withTransaction()`
`save()`
`Connection#transaction()`
`save()`

```javascript
constdoc =newPerson({name:'Will Riker'});awaitdb.transaction(asyncfunctionsetRank(session) {
  doc.name='Captain';awaitdoc.save({ session });
  doc.isNew;// false// Throw an error to abort the transactionthrownewError('Oops!');
}, {readPreference:'primary'}).catch(() =>{});// true, `transaction()` reset the document's state because the// transaction was aborted.doc.isNew;
```


## Note About Parallelism in Transactions

[Note About Parallelism in Transactions](#note-about-parallelism-in-transactions)


Running operations in parallel isnot supportedduring a transaction. The use ofPromise.all,Promise.allSettled,Promise.race, etc. to parallelize operations inside a transaction is
undefined behaviour and should be avoided.

`Promise.all`
`Promise.allSettled`
`Promise.race`

## With Mongoose Documents andsave()

[With Mongoose Documents andsave()](#with-mongoose-documents-and-save)

`save()`

If you get aMongoose documentfromfindOne()orfind()using a session, the document will
keep a reference to the session and use that session forsave().

[Mongoose document](documents.html)

[findOne()](api/model.html#model_Model-findOne)

`findOne()`
[find()](api/model.html#model_Model-find)

`find()`
[save()](api/document.html#document_Document-save)

`save()`

To get/set the session associated with a given document, usedoc.$session().

[doc.$session()](api/document.html#document_Document-$session)

`doc.$session()`

```javascript
constUser= db.model('User',newSchema({name:String}));letsession =null;returnUser.createCollection().then(() =>db.startSession()).then(_session=>{
    session = _session;returnUser.create({name:'foo'});
  }).then(() =>{
    session.startTransaction();returnUser.findOne({name:'foo'}).session(session);
  }).then(user=>{// Getter/setter for the session associated with this document.assert.ok(user.$session());
    user.name='bar';// By default, `save()` uses the associated sessionreturnuser.save();
  }).then(() =>User.findOne({name:'bar'})).// Won't find the doc because `save()` is part of an uncommitted transactionthen(doc=>assert.ok(!doc)).then(() =>session.commitTransaction()).then(() =>session.endSession()).then(() =>User.findOne({name:'bar'})).then(doc=>assert.ok(doc));
```


## With the Aggregation Framework

[With the Aggregation Framework](#with-the-aggregation-framework)


TheModel.aggregate()function also supports transactions. Mongoose
aggregations have asession()helperthat sets thesessionoption.
Below is an example of executing an aggregation within a transaction.

`Model.aggregate()`
[session()helper](api/aggregate.html#aggregate_Aggregate-session)

`session()`
[sessionoption](api/aggregate.html#aggregate_Aggregate-option)

`session`

```javascript
constEvent= db.model('Event',newSchema({createdAt:Date}),'Event');letsession =null;returnEvent.createCollection().then(() =>db.startSession()).then(_session=>{
    session = _session;
    session.startTransaction();returnEvent.insertMany([
      {createdAt:newDate('2018-06-01') },
      {createdAt:newDate('2018-06-02') },
      {createdAt:newDate('2017-06-01') },
      {createdAt:newDate('2017-05-31') }
    ], {session: session });
  }).then(() =>Event.aggregate([
    {$group: {_id: {month: {$month:'$createdAt'},year: {$year:'$createdAt'}
        },count: {$sum:1}
      }
    },
    {$sort: {count: -1,'_id.year': -1,'_id.month': -1} }
  ]).session(session)).then(res=>assert.deepEqual(res, [
    {_id: {month:6,year:2018},count:2},
    {_id: {month:6,year:2017},count:1},
    {_id: {month:5,year:2017},count:1}
  ])).then(() =>session.commitTransaction()).then(() =>session.endSession());
```


## Using AsyncLocalStorage

[Using AsyncLocalStorage](#asynclocalstorage)


One major pain point with transactions in Mongoose is that you need to remember to set thesessionoption on every operation.
If you don't, your operation will execute outside of the transaction.
Mongoose 8.4 is able to set thesessionoperation on all operations within aConnection.prototype.transaction()executor function using Node'sAsyncLocalStorage API.
Set thetransactionAsyncLocalStorageoption usingmongoose.set('transactionAsyncLocalStorage', true)to enable this feature.

`session`
`session`
`Connection.prototype.transaction()`
[AsyncLocalStorage API](https://nodejs.org/api/async_context.html#class-asynclocalstorage)

`transactionAsyncLocalStorage`
`mongoose.set('transactionAsyncLocalStorage', true)`

```javascript
mongoose.set('transactionAsyncLocalStorage',true);constTest= mongoose.model('Test', mongoose.Schema({name:String}));constdoc =newTest({name:'test'});// Save a new doc in a transaction that abortsawaitconnection.transaction(async() => {awaitdoc.save();// Notice no session herethrownewError('Oops');
}).catch(() =>{});// false, `save()` was rolled backawaitTest.exists({_id: doc._id});
```


WithtransactionAsyncLocalStorage, you no longer need to pass sessions to every operation.
Mongoose will add the session by default under the hood.

`transactionAsyncLocalStorage`

## Advanced Usage

[Advanced Usage](#advanced-usage)


Advanced users who want more fine-grained control over when they commit or abort transactions
can usesession.startTransaction()to start a transaction:

`session.startTransaction()`

```javascript
constCustomer= db.model('Customer',newSchema({name:String}));letsession =null;returnCustomer.createCollection().then(() =>db.startSession()).then(_session=>{
    session = _session;// Start a transactionsession.startTransaction();// This `create()` is part of the transaction because of the `session`// option.returnCustomer.create([{name:'Test'}], {session: session });
  }).// Transactions execute in isolation, so unless you pass a `session`// to `findOne()` you won't see the document until the transaction// is committed.then(() =>Customer.findOne({name:'Test'})).then(doc=>assert.ok(!doc)).// This `findOne()` will return the doc, because passing the `session`// means this `findOne()` will run as part of the transaction.then(() =>Customer.findOne({name:'Test'}).session(session)).then(doc=>assert.ok(doc)).// Once the transaction is committed, the write operation becomes// visible outside of the transaction.then(() =>session.commitTransaction()).then(() =>Customer.findOne({name:'Test'})).then(doc=>assert.ok(doc)).then(() =>session.endSession());
```


You can also usesession.abortTransaction()to abort a transaction:

`session.abortTransaction()`

```javascript
letsession =null;returnCustomer.createCollection().then(() =>Customer.startSession()).then(_session=>{
    session = _session;
    session.startTransaction();returnCustomer.create([{name:'Test'}], {session: session });
  }).then(() =>Customer.create([{name:'Test2'}], {session: session })).then(() =>session.abortTransaction()).then(() =>Customer.countDocuments()).then(count=>assert.strictEqual(count,0)).then(() =>session.endSession());
```


[Source](https://mongoosejs.com/docs/transactions.html)