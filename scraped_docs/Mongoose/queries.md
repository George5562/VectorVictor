# Queries


# Queries

[Queries](#queries)


Mongoosemodelsprovide several static helper functions
forCRUD operations.
Each of these functions returns amongooseQueryobject.

[models](models.html)

[CRUD operations](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

[mongooseQueryobject](api/query.html#Query)

`Query`

Model.deleteMany()Model.deleteOne()Model.find()Model.findById()Model.findByIdAndDelete()Model.findByIdAndRemove()Model.findByIdAndUpdate()Model.findOne()Model.findOneAndDelete()Model.findOneAndReplace()Model.findOneAndUpdate()Model.replaceOne()Model.updateMany()Model.updateOne()

- Model.deleteMany()

`Model.deleteMany()`
- Model.deleteOne()

`Model.deleteOne()`
- Model.find()

`Model.find()`
- Model.findById()

`Model.findById()`
- Model.findByIdAndDelete()

`Model.findByIdAndDelete()`
- Model.findByIdAndRemove()

`Model.findByIdAndRemove()`
- Model.findByIdAndUpdate()

`Model.findByIdAndUpdate()`
- Model.findOne()

`Model.findOne()`
- Model.findOneAndDelete()

`Model.findOneAndDelete()`
- Model.findOneAndReplace()

`Model.findOneAndReplace()`
- Model.findOneAndUpdate()

`Model.findOneAndUpdate()`
- Model.replaceOne()

`Model.replaceOne()`
- Model.updateMany()

`Model.updateMany()`
- Model.updateOne()

`Model.updateOne()`

A mongoose query can be executed in one of two ways. First, if you
pass in acallbackfunction, Mongoose will execute the query asynchronously
and pass the results to thecallback.

`callback`
`callback`

A query also has a.then()function, and thus can be used as a promise.

`.then()`

ExecutingQueries are Not PromisesReferences to other documentsStreamingVersus Aggregation

- Executing

- Queries are Not Promises

- References to other documents

- Streaming

- Versus Aggregation


## Executing

[Executing](#executing)


When executing a query, you specify your query as a JSON document. The JSON document's syntax is the same as theMongoDB shell.

[MongoDB shell](http://www.mongodb.com/docs/manual/tutorial/query-documents/)


```javascript
constPerson= mongoose.model('Person', yourSchema);// find each person with a last name matching 'Ghost', selecting the `name` and `occupation` fieldsconstperson =awaitPerson.findOne({'name.last':'Ghost'},'name occupation');// Prints "Space Ghost is a talk show host".console.log('%s %s is a %s.', person.name.first, person.name.last, person.occupation);
```


Whatpersonis depends on the operation: ForfindOne()it is apotentially-null single document,find()alist of documents,count()the number of documents,update()thenumber of documents affected, etc.
TheAPI docs for Modelsprovide more details.

`person`
`findOne()`
[potentially-null single document](api/model.html#model_Model-findOne)

`find()`
[list of documents](api/model.html#model_Model-find)

`count()`
[the number of documents](api/model.html#model_Model-count)

`update()`
[number of documents affected](api/model.html#model_Model-update)

[API docs for Models](api/model.html)


Now let's look at what happens when noawaitis used:

`await`

```javascript
// find each person with a last name matching 'Ghost'constquery =Person.findOne({'name.last':'Ghost'});// selecting the `name` and `occupation` fieldsquery.select('name occupation');// execute the query at a later timeconstperson =awaitquery.exec();// Prints "Space Ghost is a talk show host."console.log('%s %s is a %s.', person.name.first, person.name.last, person.occupation);
```


In the above code, thequeryvariable is of typeQuery.
AQueryenables you to build up a query using chaining syntax, rather than specifying a JSON object.
The below 2 examples are equivalent.

`query`
[Query](api/query.html)

`Query`

```javascript
// With a JSON docawaitPerson.find({occupation:/host/,'name.last':'Ghost',age: {$gt:17,$lt:66},likes: {$in: ['vaporizing','talking'] }
  }).limit(10).sort({occupation: -1}).select({name:1,occupation:1}).exec();// Using query builderawaitPerson.find({occupation:/host/}).where('name.last').equals('Ghost').where('age').gt(17).lt(66).where('likes').in(['vaporizing','talking']).limit(10).sort('-occupation').select('name occupation').exec();
```


A full list ofQuery helper functions can be found in the API docs.

[Query helper functions can be found in the API docs](api/query.html)


## Queries are Not Promises

[Queries are Not Promises](#queries-are-not-promises)


Mongoose queries arenotpromises.
Queries arethenables, meaning they have a.then()method forasync/awaitas a convenience.
However, unlike promises, calling a query's.then()executes the query, so callingthen()multiple times will throw an error.

[thenables](https://masteringjs.io/tutorials/fundamentals/thenable)

`.then()`
[async/await](http://thecodebarbarian.com/common-async-await-design-patterns-in-node.js.html)

`.then()`
`then()`

```javascript
constq =MyModel.updateMany({}, {isDeleted:true});awaitq.then(() =>console.log('Update 2'));// Throws "Query was already executed: Test.updateMany({}, { isDeleted: true })"awaitq.then(() =>console.log('Update 3'));
```


## References to other documents

[References to other documents](#refs)


There are no joins in MongoDB but sometimes we still want references to
documents in other collections. This is wherepopulationcomes in. Read more about how to include documents from other collections in
your query resultshere.

[population](populate.html)

[here](api/query.html#query_Query-populate)


## Streaming

[Streaming](#streaming)


You canstreamquery results from
MongoDB. You need to call theQuery#cursor()function to return an instance ofQueryCursor.

[stream](http://nodejs.org/api/stream.html)

[Query#cursor()](api/query.html#query_Query-cursor)

[QueryCursor](api/query.html#query_Query-cursor)


```javascript
constcursor =Person.find({occupation:/host/}).cursor();for(letdoc =awaitcursor.next(); doc !=null; doc =awaitcursor.next()) {console.log(doc);// Prints documents one at a time}
```


Iterating through a Mongoose query usingasync iteratorsalso creates a cursor.

[async iterators](https://thecodebarbarian.com/getting-started-with-async-iterators-in-node-js.html)


```javascript
forawait(constdocofPerson.find()) {console.log(doc);// Prints documents one at a time}
```


Cursors are subject tocursor timeouts.
By default, MongoDB will close your cursor after 10 minutes and subsequentnext()calls will result in aMongoServerError: cursor id 123 not founderror.
To override this, set thenoCursorTimeoutoption on your cursor.

[cursor timeouts](https://stackoverflow.com/questions/21853178/when-a-mongodb-cursor-will-expire)

`next()`
`MongoServerError: cursor id 123 not found`
`noCursorTimeout`

```javascript
// MongoDB won't automatically close this cursor after 10 minutes.constcursor =Person.find().cursor().addCursorFlag('noCursorTimeout',true);
```


However, cursors can still time out because ofsession idle timeouts.
So even a cursor withnoCursorTimeoutset will still time out after 30 minutes
of inactivity. You can read more about working around session idle timeouts in theMongoDB documentation.

[session idle timeouts](https://www.mongodb.com/docs/manual/reference/method/cursor.noCursorTimeout/#session-idle-timeout-overrides-nocursortimeout)

`noCursorTimeout`
[MongoDB documentation](https://www.mongodb.com/docs/manual/reference/method/cursor.noCursorTimeout/#session-idle-timeout-overrides-nocursortimeout)


## Versus Aggregation

[Versus Aggregation](#versus-aggregation)


Aggregationcan
do many of the same things that queries can. For example, below is
how you can useaggregate()to find docs wherename.last = 'Ghost':

[Aggregation](api/aggregate.html#aggregate_Aggregate)

`aggregate()`
`name.last = 'Ghost'`

```javascript
constdocs =awaitPerson.aggregate([{$match: {'name.last':'Ghost'} }]);
```


However, just because you can useaggregate()doesn't mean you should.
In general, you should use queries where possible, and only useaggregate()when you absolutely need to.

`aggregate()`
`aggregate()`

Unlike query results, Mongoose doesnothydrate()aggregation results. Aggregation results are always POJOs, not Mongoose
documents.

[hydrate()](api/model.html#model_Model-hydrate)

`hydrate()`

```javascript
constdocs =awaitPerson.aggregate([{$match: {'name.last':'Ghost'} }]);

docs[0]instanceofmongoose.Document;// false
```


Also, unlike query filters, Mongoose also doesn'tcastaggregation pipelines. That means
you're responsible for ensuring the values you pass in to an aggregation
pipeline have the correct type.

[cast](tutorials/query_casting.html)


```javascript
constdoc =awaitPerson.findOne();constidString = doc._id.toString();// Finds the `Person`, because Mongoose casts `idString` to an ObjectIdconstqueryRes =awaitPerson.findOne({_id: idString });// Does **not** find the `Person`, because Mongoose doesn't cast aggregation// pipelines.constaggRes =awaitPerson.aggregate([{$match: {_id: idString } }]);
```


## Sorting

[Sorting](#sorting)


Sortingis how you can ensure your query results come back in the desired order.

[Sorting](/docs/api.html#query_Query-sort)


```javascript
constpersonSchema =newmongoose.Schema({age:Number});constPerson= mongoose.model('Person', personSchema);for(leti =0; i <10; i++) {awaitPerson.create({age: i });
}awaitPerson.find().sort({age: -1});// returns age starting from 10 as the first entryawaitPerson.find().sort({age:1});// returns age starting from 0 as the first entry
```


When sorting with mutiple fields, the order of the sort keys determines what key MongoDB server sorts by first.


```javascript
constpersonSchema =newmongoose.Schema({age:Number,name:String,weight:Number});constPerson= mongoose.model('Person', personSchema);constiterations =5;for(leti =0; i < iterations; i++) {awaitPerson.create({age:Math.abs(2- i),name:'Test'+ i,weight:Math.floor(Math.random() *100) +1});
}awaitPerson.find().sort({age:1,weight: -1});// returns age starting from 0, but while keeping that order will then sort by weight.
```


You can view the output of a single run of this block below.
As you can see, age is sorted from 0 to 2 but when age is equal, sorts by weight.


```javascript
[
  {_id:newObjectId('63a335a6b9b6a7bfc186cb37'),age:0,name:'Test2',weight:67,__v:0},
  {_id:newObjectId('63a335a6b9b6a7bfc186cb35'),age:1,name:'Test1',weight:99,__v:0},
  {_id:newObjectId('63a335a6b9b6a7bfc186cb39'),age:1,name:'Test3',weight:73,__v:0},
  {_id:newObjectId('63a335a6b9b6a7bfc186cb33'),age:2,name:'Test0',weight:65,__v:0},
  {_id:newObjectId('63a335a6b9b6a7bfc186cb3b'),age:2,name:'Test4',weight:62,__v:0}
];
```


## Next Up

[Next Up](#next)


Now that we've coveredQueries, let's take a look atValidation.

`Queries`
[Validation](validation.html)


[Source](https://mongoosejs.com/docs/queries.html#streaming)