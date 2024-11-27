# Timestamps


# Timestamps

[Timestamps](#timestamps)


Mongoose schemas support atimestampsoption.
If you settimestamps: true, Mongoose will add two properties of typeDateto your schema:

`timestamps`
`timestamps: true`
`Date`

createdAt: a date representing when this document was createdupdatedAt: a date representing when this document was last updated

- createdAt: a date representing when this document was created

`createdAt`
- updatedAt: a date representing when this document was last updated

`updatedAt`

Mongoose will then setcreatedAtwhen the document is first inserted, and updateupdatedAtwhenever you update the document usingsave(),updateOne(),updateMany(),findOneAndUpdate(),update(),replaceOne(), orbulkWrite().

`createdAt`
`updatedAt`
`save()`
`updateOne()`
`updateMany()`
`findOneAndUpdate()`
`update()`
`replaceOne()`
`bulkWrite()`

```javascript
constuserSchema =newSchema({name:String}, {timestamps:true});constUser= mongoose.model('User', userSchema);letdoc =awaitUser.create({name:'test'});console.log(doc.createdAt);// 2022-02-26T16:37:48.244Zconsole.log(doc.updatedAt);// 2022-02-26T16:37:48.244Zdoc.name='test2';awaitdoc.save();console.log(doc.createdAt);// 2022-02-26T16:37:48.244Zconsole.log(doc.updatedAt);// 2022-02-26T16:37:48.307Zdoc =awaitUser.findOneAndUpdate({_id: doc._id}, {name:'test3'}, {new:true});console.log(doc.createdAt);// 2022-02-26T16:37:48.244Zconsole.log(doc.updatedAt);// 2022-02-26T16:37:48.366Z
```


ThecreatedAtproperty is immutable, and Mongoose overwrites any user-specified updates toupdatedAtby default.

`createdAt`
`updatedAt`

```javascript
letdoc =awaitUser.create({name:'test'});console.log(doc.createdAt);// 2022-02-26T17:08:13.930Zconsole.log(doc.updatedAt);// 2022-02-26T17:08:13.930Zdoc.name='test2';
doc.createdAt=newDate(0);
doc.updatedAt=newDate(0);awaitdoc.save();// Mongoose blocked changing `createdAt` and set its own `updatedAt`, ignoring// the attempt to manually set them.console.log(doc.createdAt);// 2022-02-26T17:08:13.930Zconsole.log(doc.updatedAt);// 2022-02-26T17:08:13.991Z// Mongoose also blocks changing `createdAt` and sets its own `updatedAt`// on `findOneAndUpdate()`, `updateMany()`, and other query operations// **except** `replaceOne()` and `findOneAndReplace()`.doc =awaitUser.findOneAndUpdate(
  {_id: doc._id},
  {name:'test3',createdAt:newDate(0),updatedAt:newDate(0) },
  {new:true}
);console.log(doc.createdAt);// 2022-02-26T17:08:13.930Zconsole.log(doc.updatedAt);// 2022-02-26T17:08:14.008Z
```


Keep in mind thatreplaceOne()andfindOneAndReplace()overwrite all non-_idproperties,includingimmutable properties likecreatedAt.
CallingreplaceOne()orfindOneAndReplace()will update thecreatedAttimestamp as shown below.

`replaceOne()`
`findOneAndReplace()`
`_id`
`createdAt`
`replaceOne()`
`findOneAndReplace()`
`createdAt`

```javascript
// `findOneAndReplace()` and `replaceOne()` without timestamps specified in `replacement`// sets `createdAt` and `updatedAt` to current time.doc =awaitUser.findOneAndReplace(
  {_id: doc._id},
  {name:'test3'},
  {new:true}
);console.log(doc.createdAt);// 2022-02-26T17:08:14.008Zconsole.log(doc.updatedAt);// 2022-02-26T17:08:14.008Z// `findOneAndReplace()` and `replaceOne()` with timestamps specified in `replacement`// sets `createdAt` and `updatedAt` to the values in `replacement`.doc =awaitUser.findOneAndReplace(
  {_id: doc._id},
  {name:'test3',createdAt:newDate('2022-06-01'),updatedAt:newDate('2022-06-01')
  },
  {new:true}
);console.log(doc.createdAt);// 2022-06-01T00:00:00.000Zconsole.log(doc.updatedAt);// 2022-06-01T00:00:00.000Z
```


## Alternate Property Names

[Alternate Property Names](#alternate-property-names)


For the purposes of these docs, we'll always refer tocreatedAtandupdatedAt.
But you can overwrite these property names as shown below.

`createdAt`
`updatedAt`

```javascript
constuserSchema =newSchema({name:String}, {timestamps: {createdAt:'created_at',// Use `created_at` to store the created dateupdatedAt:'updated_at'// and `updated_at` to store the last updated date}
});
```


## Disabling Timestamps

[Disabling Timestamps](#disabling-timestamps)


save(),updateOne(),updateMany(),findOneAndUpdate(),update(),replaceOne(), andbulkWrite()all support atimestampsoption.
Settimestamps: falseto skip setting timestamps for that particular operation.

`save()`
`updateOne()`
`updateMany()`
`findOneAndUpdate()`
`update()`
`replaceOne()`
`bulkWrite()`
`timestamps`
`timestamps: false`

```javascript
letdoc =awaitUser.create({name:'test'});console.log(doc.createdAt);// 2022-02-26T23:28:54.264Zconsole.log(doc.updatedAt);// 2022-02-26T23:28:54.264Zdoc.name='test2';// Setting `timestamps: false` tells Mongoose to skip updating `updatedAt` on this `save()`awaitdoc.save({timestamps:false});console.log(doc.updatedAt);// 2022-02-26T23:28:54.264Z// Similarly, setting `timestamps: false` on a query tells Mongoose to skip updating// `updatedAt`.doc =awaitUser.findOneAndUpdate({_id: doc._id}, {name:'test3'}, {new:true,timestamps:false});console.log(doc.updatedAt);// 2022-02-26T23:28:54.264Z// Below is how you can disable timestamps on a `bulkWrite()`awaitUser.bulkWrite([{updateOne: {filter: {_id: doc._id},update: {name:'test4'},timestamps:false}
}]);
doc =awaitUser.findOne({_id: doc._id});console.log(doc.updatedAt);// 2022-02-26T23:28:54.264Z
```


You can also set thetimestampsoption to an object to configurecreatedAtandupdatedAtseparately.
For example, in the below code, Mongoose setscreatedAtonsave()but skipsupdatedAt.

`timestamps`
`createdAt`
`updatedAt`
`createdAt`
`save()`
`updatedAt`

```javascript
constdoc =newUser({name:'test'});// Tell Mongoose to set `createdAt`, but skip `updatedAt`.awaitdoc.save({timestamps: {createdAt:true,updatedAt:false} });console.log(doc.createdAt);// 2022-02-26T23:32:12.478Zconsole.log(doc.updatedAt);// undefined
```


Disabling timestamps also lets you set timestamps yourself.
For example, suppose you need to correct a document'screatedAtorupdatedAtproperty.
You can do that by settingtimestamps: falseand settingcreatedAtyourself as shown below.

`createdAt`
`updatedAt`
`timestamps: false`
`createdAt`

```javascript
letdoc =awaitUser.create({name:'test'});// To update `updatedAt`, do a `findOneAndUpdate()` with `timestamps: false` and// `updatedAt` set to the value you wantdoc =awaitUser.findOneAndUpdate({_id: doc._id}, {updatedAt:newDate(0) }, {new:true,timestamps:false});console.log(doc.updatedAt);// 1970-01-01T00:00:00.000Z// To update `createdAt`, you also need to set `strict: false` because `createdAt`// is immutabledoc =awaitUser.findOneAndUpdate({_id: doc._id}, {createdAt:newDate(0) }, {new:true,timestamps:false,strict:false});console.log(doc.createdAt);// 1970-01-01T00:00:00.000Z
```


## Timestamps on Subdocuments

[Timestamps on Subdocuments](#timestamps-on-subdocuments)


Mongoose also supports setting timestamps on subdocuments.
Keep in mind thatcreatedAtandupdatedAtfor subdocuments represent when the subdocument was created or updated, not the top level document.
Overwriting a subdocument will also overwritecreatedAt.

`createdAt`
`updatedAt`
`createdAt`

```javascript
constroleSchema =newSchema({value:String}, {timestamps:true});constuserSchema =newSchema({name:String,roles: [roleSchema] });constdoc =awaitUser.create({name:'test',roles: [{value:'admin'}] });console.log(doc.roles[0].createdAt);// 2022-02-27T00:22:53.836Zconsole.log(doc.roles[0].updatedAt);// 2022-02-27T00:22:53.836Z// Overwriting the subdocument also overwrites `createdAt` and `updatedAt`doc.roles[0] = {value:'root'};awaitdoc.save();console.log(doc.roles[0].createdAt);// 2022-02-27T00:22:53.902Zconsole.log(doc.roles[0].updatedAt);// 2022-02-27T00:22:53.902Z// But updating the subdocument preserves `createdAt` and updates `updatedAt`doc.roles[0].value='admin';awaitdoc.save();console.log(doc.roles[0].createdAt);// 2022-02-27T00:22:53.902Zconsole.log(doc.roles[0].updatedAt);// 2022-02-27T00:22:53.909Z
```


## Under the Hood

[Under the Hood](#under-the-hood)


For queries with timestamps, Mongoose adds 2 properties to each update query:


AddupdatedAtto$setAddcreatedAtto$setOnInsert

- AddupdatedAtto$set

`updatedAt`
`$set`
- AddcreatedAtto$setOnInsert

`createdAt`
`$setOnInsert`

For example, if you run the below code:


```javascript
mongoose.set('debug',true);constuserSchema =newSchema({name:String}, {timestamps:true});constUser= mongoose.model('User', userSchema);awaitUser.findOneAndUpdate({}, {name:'test'});
```


You'll see the below output from Mongoose debug mode:


Notice the$setOnInsertforcreatedAtand$setforupdatedAt.
MongoDB's$setOnInsertoperatorapplies the update only if a new document isupserted.
So, for example, if you want toonlysetupdatedAtif a new document is created, you can disable theupdatedAttimestamp and set it yourself as shown below:

`$setOnInsert`
`createdAt`
`$set`
`updatedAt`
[$setOnInsertoperator](https://www.mongodb.com/docs/manual/reference/operator/update/setOnInsert/)

`$setOnInsert`
[upserted](https://masteringjs.io/tutorials/mongoose/upsert)

`updatedAt`
`updatedAt`

```javascript
awaitUser.findOneAndUpdate({}, {$setOnInsert: {updatedAt:newDate() } }, {timestamps: {createdAt:true,updatedAt:false}
});
```


## Updating Timestamps

[Updating Timestamps](#updating-timestamps)


If you need to disable Mongoose's timestamps and update a document's timestamps to a different value usingupdateOne()orfindOneAndUpdate(), you need to do the following:

`updateOne()`
`findOneAndUpdate()`

Set thetimestampsoption tofalseto prevent Mongoose from settingupdatedAt.SetoverwriteImmutabletotrueto allow overwritingcreatedAt, which is an immutable property by default.

- Set thetimestampsoption tofalseto prevent Mongoose from settingupdatedAt.

`timestamps`
`false`
`updatedAt`
- SetoverwriteImmutabletotrueto allow overwritingcreatedAt, which is an immutable property by default.

`overwriteImmutable`
`true`
`createdAt`

```javascript
constcreatedAt =newDate('2011-06-01');// Update a document's `createdAt` to a custom value.// Normally Mongoose would prevent doing this because `createdAt` is immutable.awaitModel.updateOne({_id: doc._id}, { createdAt }, {overwriteImmutable:true,timestamps:false});

doc =awaitModel.collection.findOne({_id: doc._id});
doc.createdAt.valueOf() === createdAt.valueOf();// true
```


[Source](https://mongoosejs.com/docs/timestamps.html)