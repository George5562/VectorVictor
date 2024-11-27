# Models


# Models

[Models](#models)


Modelsare fancy constructors compiled fromSchemadefinitions. An instance of a model is called adocument. Models are responsible for creating and
reading documents from the underlying MongoDB database.

[Models](api/model.html)

`Schema`
[document](documents.html)


Compiling your first modelConstructing DocumentsQueryingDeletingUpdatingChange StreamsViews

- Compiling your first model

- Constructing Documents

- Querying

- Deleting

- Updating

- Change Streams

- Views


## Compiling your first model

[Compiling your first model](#compiling)


When you callmongoose.model()on a schema, Mongoosecompilesa model
for you.

`mongoose.model()`

```javascript
constschema =newmongoose.Schema({name:String,size:String});constTank= mongoose.model('Tank', schema);
```


The first argument is thesingularname of the collection your model is
for.Mongoose automatically looks for the plural, lowercased version of your model name.Thus, for the example above, the model Tank is for thetankscollection
in the database.


Note:The.model()function makes a copy ofschema. Make sure that
you've added everything you want toschema, including hooks,
before calling.model()!

`.model()`
`schema`
`schema`
`.model()`

## Constructing Documents

[Constructing Documents](#constructing-documents)


An instance of a model is called adocument. Creating
them and saving to the database is easy.

[document](documents.html)


```javascript
constTank= mongoose.model('Tank', yourSchema);constsmall =newTank({size:'small'});awaitsmall.save();// orawaitTank.create({size:'small'});// or, for inserting large batches of documentsawaitTank.insertMany([{size:'small'}]);
```


Note that no tanks will be created/removed until the connection your model
uses is open. Every model has an associated connection. When you usemongoose.model(), your model will use the default mongoose connection.

`mongoose.model()`

```javascript
awaitmongoose.connect('mongodb://127.0.0.1/gettingstarted');
```


If you create a custom connection, use that connection'smodel()function
instead.

`model()`

```javascript
constconnection = mongoose.createConnection('mongodb://127.0.0.1:27017/test');constTank= connection.model('Tank', yourSchema);
```


## Querying

[Querying](#querying)


Finding documents is easy with Mongoose, which supports therichquery syntax of MongoDB.
Documents can be retrieved using amodel'sfind,findById,findOne, orwherestatic functions.

[rich](https://www.mongodb.com/docs/manual/reference/method/js-cursor/)

`model`
[find](api/model.html#model_Model-find)

[findById](api/model.html#model_Model-findById)

[findOne](api/model.html#model_Model-findOne)

[where](api/model.html#model_Model-where)


```javascript
awaitTank.find({size:'small'}).where('createdDate').gt(oneYearAgo).exec();
```


See the chapter onqueriesfor more details on how to use theQueryapi.

[queries](queries.html)

[Query](api/query.html)


## Deleting

[Deleting](#deleting)


Models have staticdeleteOne()anddeleteMany()functions
for removing all documents matching the givenfilter.

`deleteOne()`
`deleteMany()`
`filter`

```javascript
awaitTank.deleteOne({size:'large'});
```


## Updating

[Updating](#updating)


Eachmodelhas its ownupdatemethod for modifying documents in the
database without returning them to your application. See theAPIdocs for more detail.

`model`
`update`
[API](api/model.html#model_Model-updateOne)


```javascript
// Updated at most one doc, `res.nModified` contains the number// of docs that MongoDB updatedawaitTank.updateOne({size:'large'}, {name:'T-90'});
```


If you want to update a single document in the db and return it to your
application, usefindOneAndUpdateinstead.

[findOneAndUpdate](api/model.html#model_Model-findOneAndUpdate)


## Change Streams

[Change Streams](#change-streams)


Change streamsprovide
a way for you to listen to all inserts and updates going through your
MongoDB database. Note that change streams donotwork unless you're
connected to aMongoDB replica set.

[Change streams](https://www.mongodb.com/docs/manual/changeStreams/)

[MongoDB replica set](https://www.mongodb.com/docs/manual/replication/)


```javascript
asyncfunctionrun() {// Create a new mongoose modelconstpersonSchema =newmongoose.Schema({name:String});constPerson= mongoose.model('Person', personSchema);// Create a change stream. The 'change' event gets emitted when there's a// change in the databasePerson.watch().on('change',data=>console.log(newDate(), data));// Insert a doc, will trigger the change stream handler aboveconsole.log(newDate(),'Inserting doc');awaitPerson.create({name:'Axl Rose'});
}
```


The output from the aboveasync functionwill look like what you see below.

[async function](http://thecodebarbarian.com/80-20-guide-to-async-await-in-node.js.html)


You can read more aboutchange streams in mongoose in this blog post.

[change streams in mongoose in this blog post](http://thecodebarbarian.com/a-nodejs-perspective-on-mongodb-36-change-streams.html#change-streams-in-mongoose)


## Views

[Views](#views)


MongoDB Viewsare essentially read-only collections that contain data computed from other collections usingaggregations.
In Mongoose, you should define a separate Model for each of your Views.
You can also create a View usingcreateCollection().

[MongoDB Views](https://www.mongodb.com/docs/manual/core/views)

[aggregations](api/aggregate.html)

[createCollection()](api/model.html#model_Model-createCollection)

`createCollection()`

The following example shows how you can create a newRedactedUserView on aUserModel that hides potentially sensitive information, like name and email.

`RedactedUser`
`User`

```javascript
// Make sure to disable `autoCreate` and `autoIndex` for Views,// because you want to create the collection manually.constuserSchema =newSchema({name:String,email:String,roles: [String]
}, {autoCreate:false,autoIndex:false});constUser= mongoose.model('User', userSchema);constRedactedUser= mongoose.model('RedactedUser', userSchema);// First, create the User model's underlying collection...awaitUser.createCollection();// Then create the `RedactedUser` model's underlying collection// as a View.awaitRedactedUser.createCollection({viewOn:'users',// Set `viewOn` to the collection name, **not** model name.pipeline: [
    {$set: {name: {$concat: [{$substr: ['$name',0,3] },'...'] },email: {$concat: [{$substr: ['$email',0,3] },'...'] }
      }
    }
  ]
});awaitUser.create([
  {name:'John Smith',email:'john.smith@gmail.com',roles: ['user'] },
  {name:'Bill James',email:'bill@acme.co',roles: ['user','admin'] }
]);// [{ _id: ..., name: 'Bil...', email: 'bil...', roles: ['user', 'admin'] }]console.log(awaitRedactedUser.find({roles:'admin'}));
```


Note that Mongoose doesnotcurrently enforce that Views are read-only.
If you attempt tosave()a document from a View, you will get an error from the MongoDB server.

`save()`

## Yet more

[Yet more](#yet-more)


TheAPI docscover many additional methods available likecount,mapReduce,aggregate, and more.

[API docs](api/model.html#model_Model)

[count](api/model.html#model_Model-count)

[mapReduce](api/model.html#model_Model-mapReduce)

[aggregate](api/model.html#model_Model-aggregate)


## Next Up

[Next Up](#next-up)


Now that we've coveredModels, let's take a look atDocuments.

`Models`
[Documents](documents.html)


[Source](https://mongoosejs.com/docs/models.html)