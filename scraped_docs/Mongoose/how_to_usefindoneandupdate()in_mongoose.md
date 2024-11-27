# How to UsefindOneAndUpdate()in Mongoose


# How to UsefindOneAndUpdate()in Mongoose

[How to UsefindOneAndUpdate()in Mongoose](#how-to-use-code>findoneandupdate()</code>-in-mongoose)

`findOneAndUpdate()`

ThefindOneAndUpdate()function in Mongoosehas a wide variety of use cases.You should usesave()to update documents where possible, for bettervalidationandmiddlewaresupport.
However, there are some cases where you need to usefindOneAndUpdate(). In this tutorial, you'll see how to usefindOneAndUpdate(), and learn when you need to use it.

[findOneAndUpdate()function in Mongoose](../api/query.html#query_Query-findOneAndUpdate)

`findOneAndUpdate()`
[You should usesave()to update documents where possible](https://masteringjs.io/tutorials/mongoose/update)

`save()`
[validation](../validation.html)

[middleware](../middleware.html)

[findOneAndUpdate()](https://masteringjs.io/tutorials/mongoose/findoneandupdate)

`findOneAndUpdate()`
`findOneAndUpdate()`

Getting StartedAtomic UpdatesUpsertTheincludeResultMetadataOptionUpdating Discriminator Keys

- Getting Started

- Atomic Updates

- Upsert

- TheincludeResultMetadataOption

`includeResultMetadata`
- Updating Discriminator Keys


## Getting Started

[Getting Started](#getting-started)


As the name implies,findOneAndUpdate()finds the first document that matches a givenfilter, applies anupdate, and returns the document.
ThefindOneAndUpdate()function has the following signature:

`findOneAndUpdate()`
`filter`
`update`
`findOneAndUpdate()`

```javascript
functionfindOneAndUpdate(filter, update, options) {}
```


By default,findOneAndUpdate()returns the document as it wasbeforeupdatewas applied.
In the following example,docinitially only hasnameand_idproperties.findOneAndUpdate()adds anageproperty, but the result offindOneAndUpdate()doesnothave anageproperty.

`findOneAndUpdate()`
`update`
`doc`
`name`
`_id`
`findOneAndUpdate()`
`age`
`findOneAndUpdate()`
`age`

```javascript
constCharacter= mongoose.model('Character',newmongoose.Schema({name:String,age:Number}));const_id =newmongoose.Types.ObjectId('0'.repeat(24));letdoc =awaitCharacter.create({ _id,name:'Jean-Luc Picard'});
doc;// { name: 'Jean-Luc Picard', _id: ObjectId('000000000000000000000000') }constfilter = {name:'Jean-Luc Picard'};constupdate = {age:59};// The result of `findOneAndUpdate()` is the document _before_ `update` was applieddoc =awaitCharacter.findOneAndUpdate(filter, update);
doc;// { name: 'Jean-Luc Picard', _id: ObjectId('000000000000000000000000') }doc =awaitCharacter.findOne(filter);
doc.age;// 59
```


You should set thenewoption totrueto return the documentafterupdatewas applied.

`new`
`true`
`update`

```javascript
constfilter = {name:'Jean-Luc Picard'};constupdate = {age:59};// `doc` is the document _after_ `update` was applied because of// `new: true`constdoc =awaitCharacter.findOneAndUpdate(filter, update, {new:true});
doc.name;// 'Jean-Luc Picard'doc.age;// 59
```


Mongoose'sfindOneAndUpdate()is slightly different fromthe MongoDB Node.js driver'sfindOneAndUpdate()because it returns the document itself, not aresult object.

`findOneAndUpdate()`
[the MongoDB Node.js driver'sfindOneAndUpdate()](http://mongodb.github.io/node-mongodb-native/3.1/api/Collection.html#findOneAndUpdate)

`findOneAndUpdate()`
[result object](http://mongodb.github.io/node-mongodb-native/3.1/api/Collection.html#~findAndModifyWriteOpResult)


As an alternative to thenewoption, you can also use thereturnOriginaloption.returnOriginal: falseis equivalent tonew: true. ThereturnOriginaloption
exists for consistency with thethe MongoDB Node.js driver'sfindOneAndUpdate(),
which has the same option.

`new`
`returnOriginal`
`returnOriginal: false`
`new: true`
`returnOriginal`
[the MongoDB Node.js driver'sfindOneAndUpdate()](http://mongodb.github.io/node-mongodb-native/3.1/api/Collection.html#findOneAndUpdate)

`findOneAndUpdate()`

```javascript
constfilter = {name:'Jean-Luc Picard'};constupdate = {age:59};// `doc` is the document _after_ `update` was applied because of// `returnOriginal: false`constdoc =awaitCharacter.findOneAndUpdate(filter, update, {returnOriginal:false});
doc.name;// 'Jean-Luc Picard'doc.age;// 59
```


## Atomic Updates

[Atomic Updates](#atomic-updates)


With the exception of anunindexed upsert,findOneAndUpdate()is atomic. That means you can assume the document doesn't change between when MongoDB finds the document and when it updates the document,unlessyou're doing anupsert.

[unindexed upsert](https://www.mongodb.com/docs/manual/reference/method/db.collection.findAndModify/#upsert-with-unique-index)

[findOneAndUpdate()is atomic](https://www.mongodb.com/docs/manual/core/write-operations-atomicity/#atomicity)

`findOneAndUpdate()`
[upsert](#upsert)


For example, if you're usingsave()to update a document, the document can change in MongoDB in between when you load the document usingfindOne()and when you save the document usingsave()as show below. For many use cases, thesave()race condition is a non-issue. But you can work around it withfindOneAndUpdate()(ortransactions) if you need to.

`save()`
`findOne()`
`save()`
`save()`
`findOneAndUpdate()`
[transactions](../transactions.html)


```javascript
constfilter = {name:'Jean-Luc Picard'};constupdate = {age:59};letdoc =awaitCharacter.findOne({name:'Jean-Luc Picard'});// Document changed in MongoDB, but not in MongooseawaitCharacter.updateOne(filter, {name:'Will Riker'});// This will update `doc` age to `59`, even though the doc changed.doc.age= update.age;awaitdoc.save();

doc =awaitCharacter.findOne();
doc.name;// Will Rikerdoc.age;// 59
```


## Upsert

[Upsert](#upsert)


Using theupsertoption, you can usefindOneAndUpdate()as a find-and-upsertoperation. An upsert behaves like a normalfindOneAndUpdate()if it finds a document that matchesfilter. But, if no document matchesfilter, MongoDB will insert one by combiningfilterandupdateas shown below.

`upsert`
`findOneAndUpdate()`
[upsert](https://www.mongodb.com/docs/manual/reference/method/db.collection.update/#db.collection.update)

`findOneAndUpdate()`
`filter`
`filter`
`filter`
`update`

```javascript
constfilter = {name:'Will Riker'};constupdate = {age:29};awaitCharacter.countDocuments(filter);// 0constdoc =awaitCharacter.findOneAndUpdate(filter, update, {new:true,upsert:true// Make this update into an upsert});
doc.name;// Will Rikerdoc.age;// 29
```


## TheincludeResultMetadataOption

`includeResultMetadata`

Mongoose transforms the result offindOneAndUpdate()by default: it
returns the updated document. That makes it difficult to check whether
a document was upserted or not. In order to get the updated document
and check whether MongoDB upserted a new document in the same operation,
you can set theincludeResultMetadataflag to make Mongoose return the raw result
from MongoDB.

`findOneAndUpdate()`
`includeResultMetadata`

```javascript
constfilter = {name:'Will Riker'};constupdate = {age:29};awaitCharacter.countDocuments(filter);// 0constres =awaitCharacter.findOneAndUpdate(filter, update, {new:true,upsert:true,// Return additional properties about the operation, not just the documentincludeResultMetadata:true});

res.valueinstanceofCharacter;// true// The below property will be `false` if MongoDB upserted a new// document, and `true` if MongoDB updated an existing object.res.lastErrorObject.updatedExisting;// false
```


Here's what theresobject from the above example looks like:

`res`

```javascript
{ lastErrorObject:
   { n: 1,
     updatedExisting: false,
     upserted: 5e6a9e5ec6e44398ae2ac16a },
  value:
   { _id: 5e6a9e5ec6e44398ae2ac16a,
     name: 'Will Riker',
     __v: 0,
     age: 29 },
  ok: 1 }
```


## Updating Discriminator Keys

[Updating Discriminator Keys](#updating-discriminator-keys)


Mongoose prevents updating thediscriminator keyusingfindOneAndUpdate()by default.
For example, suppose you have the following discriminator models.

[discriminator key](../discriminators.html#discriminator-keys)

`findOneAndUpdate()`

```javascript
consteventSchema =newmongoose.Schema({time:Date});constEvent= db.model('Event', eventSchema);constClickedLinkEvent=Event.discriminator('ClickedLink',newmongoose.Schema({url:String})
);constSignedUpEvent=Event.discriminator('SignedUp',newmongoose.Schema({username:String})
);
```


Mongoose will remove__t(the default discriminator key) from theupdateparameter, if__tis set.
This is to prevent unintentional updates to the discriminator key; for example, if you're passing untrusted user input to theupdateparameter.
However, you can tell Mongoose to allow updating the discriminator key by setting theoverwriteDiscriminatorKeyoption totrueas shown below.

`__t`
`update`
`__t`
`update`
`overwriteDiscriminatorKey`
`true`

```javascript
letevent =newClickedLinkEvent({time:Date.now(),url:'google.com'});awaitevent.save();

event =awaitClickedLinkEvent.findByIdAndUpdate(
  event._id,
  {__t:'SignedUp'},
  {overwriteDiscriminatorKey:true,new:true}
);
event.__t;// 'SignedUp', updated discriminator key
```


[Source](https://mongoosejs.com/docs/tutorials/findoneandupdate.html)