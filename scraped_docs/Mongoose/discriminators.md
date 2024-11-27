# Discriminators


# Discriminators

[Discriminators](#discriminators)


## Themodel.discriminator()function

[Themodel.discriminator()function](#the-code>model.discriminator()</code>-function)

`model.discriminator()`

Discriminators are a schema inheritance mechanism. They enable
you to have multiple models with overlapping schemas on top of the
same underlying MongoDB collection.


Suppose you wanted to track different types of events in a single
collection. Every event will have a timestamp, but events that
represent clicked links should have a URL. You can achieve this
using themodel.discriminator()function. This function takes
3 parameters, a model name, a discriminator schema and an optional
key (defaults to the model name). It returns a model whose schema
is the union of the base schema and the discriminator schema.

`model.discriminator()`

```javascript
constoptions = {discriminatorKey:'kind'};consteventSchema =newmongoose.Schema({time:Date}, options);constEvent= mongoose.model('Event', eventSchema);// ClickedLinkEvent is a special type of Event that has// a URL.constClickedLinkEvent=Event.discriminator('ClickedLink',newmongoose.Schema({url:String}, options));// When you create a generic event, it can't have a URL field...constgenericEvent =newEvent({time:Date.now(),url:'google.com'});
assert.ok(!genericEvent.url);// But a ClickedLinkEvent canconstclickedEvent =newClickedLinkEvent({time:Date.now(),url:'google.com'});
assert.ok(clickedEvent.url);
```


## Discriminators save to the Event model's collection

[Discriminators save to the Event model's collection](#discriminators-save-to-the-event-model#39;s-collection)


Suppose you created another discriminator to track events where
a new user registered. TheseSignedUpEventinstances will be
stored in the same collection as generic events andClickedLinkEventinstances.

`SignedUpEvent`
`ClickedLinkEvent`

```javascript
constevent1 =newEvent({time:Date.now() });constevent2 =newClickedLinkEvent({time:Date.now(),url:'google.com'});constevent3 =newSignedUpEvent({time:Date.now(),user:'testuser'});awaitPromise.all([event1.save(), event2.save(), event3.save()]);constcount =awaitEvent.countDocuments();
assert.equal(count,3);
```


## Discriminator keys

[Discriminator keys](#discriminator-keys)


The way Mongoose tells the difference between the different discriminator models is by the 'discriminator key', which is__tby default.
Mongoose adds a String path called__tto your schemas that it uses to track which discriminator this document is an instance of.

`__t`
`__t`

```javascript
constevent1 =newEvent({time:Date.now() });constevent2 =newClickedLinkEvent({time:Date.now(),url:'google.com'});constevent3 =newSignedUpEvent({time:Date.now(),user:'testuser'});

assert.ok(!event1.__t);
assert.equal(event2.__t,'ClickedLink');
assert.equal(event3.__t,'SignedUp');
```


## Updating the discriminator key

[Updating the discriminator key](#updating-the-discriminator-key)


By default, Mongoose doesn't let you update the discriminator key.save()will throw an error if you attempt to update the discriminator key.
AndfindOneAndUpdate(),updateOne(), etc. will strip out discriminator key updates.

`save()`
`findOneAndUpdate()`
`updateOne()`

```javascript
letevent =newClickedLinkEvent({time:Date.now(),url:'google.com'});awaitevent.save();

event.__t='SignedUp';// ValidationError: ClickedLink validation failed: __t: Cast to String failed for value "SignedUp" (type string) at path "__t"awaitevent.save();

event =awaitClickedLinkEvent.findByIdAndUpdate(event._id, {__t:'SignedUp'}, {new:true});
event.__t;// 'ClickedLink', update was a no-op
```


To update a document's discriminator key, usefindOneAndUpdate()orupdateOne()with theoverwriteDiscriminatorKeyoption set as follows.

`findOneAndUpdate()`
`updateOne()`
`overwriteDiscriminatorKey`

```javascript
letevent =newClickedLinkEvent({time:Date.now(),url:'google.com'});awaitevent.save();

event =awaitClickedLinkEvent.findByIdAndUpdate(
  event._id,
  {__t:'SignedUp'},
  {overwriteDiscriminatorKey:true,new:true}
);
event.__t;// 'SignedUp', updated discriminator key
```


## Embedded discriminators in arrays

[Embedded discriminators in arrays](#embedded-discriminators-in-arrays)


You can also define discriminators on embedded document arrays.
Embedded discriminators are different because the different discriminator types are stored in the same document array (within a document) rather than the same collection.
In other words, embedded discriminators let you store subdocuments matching different schemas in the same array.


As a general best practice, make sure you declare any hooks on your schemasbeforeyou use them.
You shouldnotcallpre()orpost()after callingdiscriminator().

`pre()`
`post()`
`discriminator()`

```javascript
consteventSchema =newSchema({message:String},
  {discriminatorKey:'kind',_id:false});constbatchSchema =newSchema({events: [eventSchema] });// `batchSchema.path('events')` gets the mongoose `DocumentArray`// For TypeScript, use `schema.path<Schema.Types.DocumentArray>('events')`constdocArray = batchSchema.path('events');// The `events` array can contain 2 different types of events, a// 'clicked' event that requires an element id that was clicked...constclickedSchema =newSchema({element: {type:String,required:true}
}, {_id:false});// Make sure to attach any hooks to `eventSchema` and `clickedSchema`// **before** calling `discriminator()`.constClicked= docArray.discriminator('Clicked', clickedSchema);// ... and a 'purchased' event that requires the product that was purchased.constPurchased= docArray.discriminator('Purchased',newSchema({product: {type:String,required:true}
}, {_id:false}));constBatch= db.model('EventBatch', batchSchema);// Create a new batch of events with different kindsconstdoc =awaitBatch.create({events: [
    {kind:'Clicked',element:'#hero',message:'hello'},
    {kind:'Purchased',product:'action-figure-1',message:'world'}
  ]
});

assert.equal(doc.events.length,2);

assert.equal(doc.events[0].element,'#hero');
assert.equal(doc.events[0].message,'hello');
assert.ok(doc.events[0]instanceofClicked);

assert.equal(doc.events[1].product,'action-figure-1');
assert.equal(doc.events[1].message,'world');
assert.ok(doc.events[1]instanceofPurchased);

doc.events.push({kind:'Purchased',product:'action-figure-2'});awaitdoc.save();

assert.equal(doc.events.length,3);

assert.equal(doc.events[2].product,'action-figure-2');
assert.ok(doc.events[2]instanceofPurchased);
```


## Single nested discriminators

[Single nested discriminators](#single-nested-discriminators)


You can also define discriminators on single nested subdocuments, similar to how you can define discriminators on arrays of subdocuments.


As a general best practice, make sure you declare any hooks on your schemasbeforeyou use them.
You shouldnotcallpre()orpost()after callingdiscriminator().

`pre()`
`post()`
`discriminator()`

```javascript
constshapeSchema =Schema({name:String}, {discriminatorKey:'kind'});constschema =Schema({shape: shapeSchema });// For TypeScript, use `schema.path<Schema.Types.Subdocument>('shape').discriminator(...)`schema.path('shape').discriminator('Circle',Schema({radius:String}));
schema.path('shape').discriminator('Square',Schema({side:Number}));constMyModel= mongoose.model('ShapeTest', schema);// If `kind` is set to 'Circle', then `shape` will have a `radius` propertyletdoc =newMyModel({shape: {kind:'Circle',radius:5} });
doc.shape.radius;// 5// If `kind` is set to 'Square', then `shape` will have a `side` propertydoc =newMyModel({shape: {kind:'Square',side:10} });
doc.shape.side;// 10
```


[Source](https://mongoosejs.com/docs/discriminators.html)