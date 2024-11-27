# Faster Mongoose Queries With Lean


# Faster Mongoose Queries With Lean

[Faster Mongoose Queries With Lean](#faster-mongoose-queries-with-lean)


Thelean optiontells Mongoose to skiphydratingthe result documents. This
makes queries faster and less memory intensive, but the result documents are
plain old JavaScript objects (POJOs),notMongoose documents.
In this tutorial, you'll learn more about the tradeoffs of usinglean().

[lean option](../api/query.html#query_Query-lean)

[hydrating](../api/model.html#model_Model-hydrate)

[Mongoose documents](../documents.html)

`lean()`

Using LeanLean and PopulateWhen to Use LeanPluginsBigInts

- Using Lean

- Lean and Populate

- When to Use Lean

- Plugins

- BigInts


## Using Lean

[Using Lean](#using-lean)


By default, Mongoose queries return an instance of theMongooseDocumentclass. Documents are much
heavier than vanilla JavaScript objects, because they have a lot of internal
state for change tracking. Enabling theleanoption tells Mongoose to skip
instantiating a full Mongoose document and just give you the POJO.

[MongooseDocumentclass](../api/document.html#Document)

`Document`
`lean`

```javascript
constleanDoc =awaitMyModel.findOne().lean();
```


How much smaller are lean documents? Here's a comparison.


```javascript
constschema =newmongoose.Schema({name:String});constMyModel= mongoose.model('Test', schema);awaitMyModel.create({name:'test'});constnormalDoc =awaitMyModel.findOne();// To enable the `lean` option for a query, use the `lean()` function.constleanDoc =awaitMyModel.findOne().lean();v8Serialize(normalDoc).length;// approximately 180v8Serialize(leanDoc).length;// approximately 55, about 3x smaller!// In case you were wondering, the JSON form of a Mongoose doc is the same// as the POJO. This additional memory only affects how much memory your// Node.js process uses, not how much data is sent over the network.JSON.stringify(normalDoc).length===JSON.stringify(leanDoc).length;// true
```


Under the hood, after executing a query, Mongoose converts the query results
from POJOs to Mongoose documents. If you turn on theleanoption, Mongoose
skips this step.

`lean`

```javascript
constnormalDoc =awaitMyModel.findOne();constleanDoc =awaitMyModel.findOne().lean();

normalDocinstanceofmongoose.Document;// truenormalDoc.constructor.name;// 'model'leanDocinstanceofmongoose.Document;// falseleanDoc.constructor.name;// 'Object'
```


The downside of enablingleanis that lean docs don't have:

`lean`

Change trackingCasting and validationGetters and settersVirtualssave()

- Change tracking

- Casting and validation

- Getters and setters

- Virtuals

- save()

`save()`

For example, the following code sample shows that thePersonmodel's getters
and virtuals don't run if you enablelean.

`Person`
`lean`

```javascript
// Define a `Person` model. Schema has 2 custom getters and a `fullName`// virtual. Neither the getters nor the virtuals will run if lean is enabled.constpersonSchema =newmongoose.Schema({firstName: {type:String,get: capitalizeFirstLetter
  },lastName: {type:String,get: capitalizeFirstLetter
  }
});
personSchema.virtual('fullName').get(function() {return`${this.firstName}${this.lastName}`;
});functioncapitalizeFirstLetter(v) {// Convert 'bob' -> 'Bob'returnv.charAt(0).toUpperCase() + v.substring(1);
}constPerson= mongoose.model('Person', personSchema);// Create a doc and load it as a lean docawaitPerson.create({firstName:'benjamin',lastName:'sisko'});constnormalDoc =awaitPerson.findOne();constleanDoc =awaitPerson.findOne().lean();

normalDoc.fullName;// 'Benjamin Sisko'normalDoc.firstName;// 'Benjamin', because of `capitalizeFirstLetter()`normalDoc.lastName;// 'Sisko', because of `capitalizeFirstLetter()`leanDoc.fullName;// undefinedleanDoc.firstName;// 'benjamin', custom getter doesn't runleanDoc.lastName;// 'sisko', custom getter doesn't run
```


## Lean and Populate

[Lean and Populate](#lean-and-populate)


Populateworks withlean(). If you
use bothpopulate()andlean(), theleanoption propagates to the
populated documents as well. In the below example, both the top-level
'Group' documents and the populated 'Person' documents will be lean.

[Populate](../populate.html)

`lean()`
`populate()`
`lean()`
`lean`

```javascript
// Create modelsconstGroup= mongoose.model('Group',newmongoose.Schema({name:String,members: [{type: mongoose.ObjectId,ref:'Person'}]
}));constPerson= mongoose.model('Person',newmongoose.Schema({name:String}));// Initialize dataconstpeople =awaitPerson.create([
  {name:'Benjamin Sisko'},
  {name:'Kira Nerys'}
]);awaitGroup.create({name:'Star Trek: Deep Space Nine Characters',members: people.map(p=>p._id)
});// Execute a lean queryconstgroup =awaitGroup.findOne().lean().populate('members');
group.members[0].name;// 'Benjamin Sisko'group.members[1].name;// 'Kira Nerys'// Both the `group` and the populated `members` are lean.groupinstanceofmongoose.Document;// falsegroup.members[0]instanceofmongoose.Document;// falsegroup.members[1]instanceofmongoose.Document;// false
```


Virtual populatealso works with lean.

[Virtual populate](../populate.html#populate-virtuals)


```javascript
// Create modelsconstgroupSchema =newmongoose.Schema({name:String});
groupSchema.virtual('members', {ref:'Person',localField:'_id',foreignField:'groupId'});constGroup= mongoose.model('Group', groupSchema);constPerson= mongoose.model('Person',newmongoose.Schema({name:String,groupId: mongoose.ObjectId}));// Initialize dataconstg =awaitGroup.create({name:'DS9 Characters'});awaitPerson.create([
  {name:'Benjamin Sisko',groupId: g._id},
  {name:'Kira Nerys',groupId: g._id}
]);// Execute a lean queryconstgroup =awaitGroup.findOne().lean().populate({path:'members',options: {sort: {name:1} }
});
group.members[0].name;// 'Benjamin Sisko'group.members[1].name;// 'Kira Nerys'// Both the `group` and the populated `members` are lean.groupinstanceofmongoose.Document;// falsegroup.members[0]instanceofmongoose.Document;// falsegroup.members[1]instanceofmongoose.Document;// false
```


## When to Use Lean

[When to Use Lean](#when-to-use-lean)


If you're executing a query and sending the results without modification to,
say, anExpress response, you should
use lean. In general, if you do not modify the query results and do not usecustom getters, you should uselean(). If you modify the query results or rely on features like getters
ortransforms, you should not
uselean().

[Express response](http://expressjs.com/en/4x/api.html#res)

[custom getters](../api/schematype.html#schematype_SchemaType-get)

`lean()`
[transforms](../api/document.html#document_Document-toObject)

`lean()`

Below is an example of anExpress routethat is a good candidate forlean(). This route does not modify thepersondoc and doesn't rely on any Mongoose-specific functionality.

[Express route](http://expressjs.com/en/guide/routing.html)

`lean()`
`person`

```javascript
// As long as you don't need any of the Person model's virtuals or getters,// you can use `lean()`.app.get('/person/:id',function(req, res) {Person.findOne({_id: req.params.id}).lean().then(person=>res.json({ person })).catch(error=>res.json({error: error.message}));
});
```


Below is an example of an Express route that shouldnotuselean(). As
a general rule of thumb,GETroutes are good candidates forlean()in aRESTful API.
On the other hand,PUT,POST, etc. routes generally should not uselean().

`lean()`
`GET`
`lean()`
[RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer)

`PUT`
`POST`
`lean()`

```javascript
// This route should **not** use `lean()`, because lean means no `save()`.app.put('/person/:id',function(req, res) {Person.findOne({_id: req.params.id}).then(person=>{
      assert.ok(person);Object.assign(person, req.body);returnperson.save();
    }).then(person=>res.json({ person })).catch(error=>res.json({error: error.message}));
});
```


Remember that virtuals donotend up inlean()query results. Use themongoose-lean-virtuals pluginto add virtuals to your lean query results.

`lean()`
[mongoose-lean-virtuals plugin](http://plugins.mongoosejs.io/plugins/lean-virtuals)


## Plugins

[Plugins](#plugins)


Usinglean()bypasses all Mongoose features, includingvirtuals,getters/setters,
anddefaults. If you want to
use these features withlean(), you need to use the corresponding plugin:

`lean()`
[virtuals](virtuals.html)

[getters/setters](getters-setters.html)

[defaults](../api/schematype.html#schematype_SchemaType-default)

`lean()`

mongoose-lean-virtualsmongoose-lean-gettersmongoose-lean-defaults

- mongoose-lean-virtuals

- mongoose-lean-getters

- mongoose-lean-defaults


However, you need to keep in mind that Mongoose does not hydrate lean documents,
sothiswill be a POJO in virtuals, getters, and default functions.

`this`

```javascript
constschema =newSchema({name:String});
schema.plugin(require('mongoose-lean-virtuals'));

schema.virtual('lowercase',function() {thisinstanceofmongoose.Document;// falsethis.name;// Worksthis.get('name');// Crashes because `this` is not a Mongoose document.});
```


## BigInts

[BigInts](#bigints)


By default, the MongoDB Node driver converts longs stored in MongoDB into JavaScript numbers,notBigInts.
Set theuseBigInt64option on yourlean()queries to inflate longs into BigInts.

[BigInts](https://thecodebarbarian.com/an-overview-of-bigint-in-node-js.html)

`useBigInt64`
`lean()`

```javascript
constPerson= mongoose.model('Person',newmongoose.Schema({name:String,age:BigInt}));// Mongoose will convert `age` to a BigIntconst{ age } =awaitPerson.create({name:'Benjamin Sisko',age:37});typeofage;// 'bigint'// By default, if you store a document with a BigInt property in MongoDB and you// load the document with `lean()`, the BigInt property will be a numberletperson =awaitPerson.findOne({name:'Benjamin Sisko'}).lean();typeofperson.age;// 'number'// Set the `useBigInt64` option to opt in to converting MongoDB longs to BigInts.person =awaitPerson.findOne({name:'Benjamin Sisko'}).setOptions({useBigInt64:true}).lean();typeofperson.age;// 'bigint'
```


[Source](https://mongoosejs.com/docs/tutorials/lean.html)