# Mongoose Virtuals


# Mongoose Virtuals

[Mongoose Virtuals](#mongoose-virtuals)


In Mongoose, a virtual is a property that isnotstored in MongoDB.
Virtuals are typically used for computed properties on documents.


Your First VirtualVirtual SettersVirtuals in JSONVirtuals with LeanLimitationsPopulateVirtuals via schema optionsFurther Reading

- Your First Virtual

- Virtual Setters

- Virtuals in JSON

- Virtuals with Lean

- Limitations

- Populate

- Virtuals via schema options

- Further Reading


## Your First Virtual

[Your First Virtual](#your-first-virtual)


Suppose you have aUsermodel. Every user has anemail, but you also
want the email's domain. For example, the domain portion of
'test@gmail.com' is 'gmail.com'.

`User`
`email`
[test@gmail.com](mailto:test@gmail.com)


Below is one way to implement thedomainproperty using a virtual.
You define virtuals on a schema using theSchema#virtual()function.

`domain`
[Schema#virtual()function](../api/schema.html#schema_Schema-virtual)

`Schema#virtual()`

```javascript
constuserSchema = mongoose.Schema({email:String});// Create a virtual property `domain` that's computed from `email`.userSchema.virtual('domain').get(function() {returnthis.email.slice(this.email.indexOf('@') +1);
});constUser= mongoose.model('User', userSchema);constdoc =awaitUser.create({email:'test@gmail.com'});// `domain` is now a property on User documents.doc.domain;// 'gmail.com'
```


TheSchema#virtual()function returns aVirtualTypeobject. Unlike normal document properties,
virtuals do not have any underlying value and Mongoose does not do
any type coercion on virtuals. However, virtuals do havegetters and setters, which make
them ideal for computed properties, like thedomainexample above.

`Schema#virtual()`
[VirtualTypeobject](../api/virtualtype.html)

`VirtualType`
[getters and setters](getters-setters.html)

`domain`

## Virtual Setters

[Virtual Setters](#virtual-setters)


You can also use virtuals to set multiple properties at once as an
alternative tocustom setters on normal properties. For example, suppose
you have two string properties:firstNameandlastName. You can
create a virtual propertyfullNamethat lets you set both of
these properties at once. The key detail is that, in virtual getters and
setters,thisrefers to the document the virtual is attached to.

[custom setters on normal properties](getters-setters.html#setters)

`firstName`
`lastName`
`fullName`
`this`

```javascript
constuserSchema = mongoose.Schema({firstName:String,lastName:String});// Create a virtual property `fullName` with a getter and setter.userSchema.virtual('fullName').get(function() {return`${this.firstName}${this.lastName}`; }).set(function(v) {// `v` is the value being set, so use the value to set// `firstName` and `lastName`.constfirstName = v.substring(0, v.indexOf(' '));constlastName = v.substring(v.indexOf(' ') +1);this.set({ firstName, lastName });
  });constUser= mongoose.model('User', userSchema);constdoc =newUser();// Vanilla JavaScript assignment triggers the setterdoc.fullName='Jean-Luc Picard';

doc.fullName;// 'Jean-Luc Picard'doc.firstName;// 'Jean-Luc'doc.lastName;// 'Picard'
```


## Virtuals in JSON

[Virtuals in JSON](#virtuals-in-json)


By default, Mongoose does not include virtuals when you convert a document to JSON.
For example, if you pass a document toExpress'res.json()function, virtuals willnotbe included by default.

[Express'res.json()function](http://expressjs.com/en/4x/api.html#res.json)

`res.json()`

To include virtuals inres.json(), you need to set thetoJSONschema optionto{ virtuals: true }.

`res.json()`
[toJSONschema option](../guide.html#toJSON)

`toJSON`
`{ virtuals: true }`

```javascript
constopts = {toJSON: {virtuals:true} };constuserSchema = mongoose.Schema({_id:Number,email:String}, opts);// Create a virtual property `domain` that's computed from `email`.userSchema.virtual('domain').get(function() {returnthis.email.slice(this.email.indexOf('@') +1);
});constUser= mongoose.model('User', userSchema);constdoc =newUser({_id:1,email:'test@gmail.com'});

doc.toJSON().domain;// 'gmail.com'// {"_id":1,"email":"test@gmail.com","domain":"gmail.com","id":"1"}JSON.stringify(doc);// To skip applying virtuals, pass `virtuals: false` to `toJSON()`doc.toJSON({virtuals:false}).domain;// undefined
```


## Virtuals inconsole.log()

[Virtuals inconsole.log()](#virtuals-in-code>console.log()</code>)

`console.log()`

By default, Mongoose doesnotinclude virtuals inconsole.log()output.
To include virtuals inconsole.log(), you need to set thetoObjectschema optionto{ virtuals: true }, or usetoObject()before printing the object.

`console.log()`
`console.log()`
[toObjectschema option](../guide.html#toObject)

`toObject`
`{ virtuals: true }`
`toObject()`

```javascript
console.log(doc.toObject({virtuals:true}));
```


## Virtuals with Lean

[Virtuals with Lean](#virtuals-with-lean)


Virtuals are properties on Mongoose documents. If you use thelean option, that means your queries return POJOs
rather than full Mongoose documents. That means no virtuals if you uselean().

[lean option](lean.html)

[lean()](../api/query.html#query_Query-lean)

`lean()`

```javascript
constfullDoc =awaitUser.findOne();
fullDoc.domain;// 'gmail.com'constleanDoc =awaitUser.findOne().lean();
leanDoc.domain;// undefined
```


If you uselean()for performance, but still need virtuals, Mongoose
has anofficially supportedmongoose-lean-virtualspluginthat decorates lean documents with virtuals.

`lean()`
[officially supportedmongoose-lean-virtualsplugin](https://plugins.mongoosejs.io/plugins/lean-virtuals)

`mongoose-lean-virtuals`

## Limitations

[Limitations](#limitations)


Mongoose virtuals arenotstored in MongoDB, which means you can't query
based on Mongoose virtuals.


```javascript
// Will **not** find any results, because `domain` is not stored in// MongoDB.constdoc =awaitUser.findOne({domain:'gmail.com'},null, {strictQuery:false});
doc;// undefined
```


If you want to query by a computed property, you should set the property using
acustom setterorpre save middleware.

[custom setter](getters-setters.html)

[pre save middleware](../middleware.html)


## Populate

[Populate](#populate)


Mongoose also supportspopulating virtuals. A populated
virtual contains documents from another collection. To define a populated
virtual, you need to specify:

[populating virtuals](../populate.html)


Therefoption, which tells Mongoose which model to populate documents from.ThelocalFieldandforeignFieldoptions. Mongoose will populate documents from the model inrefwhoseforeignFieldmatches this document'slocalField.

- Therefoption, which tells Mongoose which model to populate documents from.

`ref`
- ThelocalFieldandforeignFieldoptions. Mongoose will populate documents from the model inrefwhoseforeignFieldmatches this document'slocalField.

`localField`
`foreignField`
`ref`
`foreignField`
`localField`

```javascript
constuserSchema = mongoose.Schema({_id:Number,email:String});constblogPostSchema = mongoose.Schema({title:String,authorId:Number});// When you `populate()` the `author` virtual, Mongoose will find the// first document in the User model whose `_id` matches this document's// `authorId` property.blogPostSchema.virtual('author', {ref:'User',localField:'authorId',foreignField:'_id',justOne:true});constUser= mongoose.model('User', userSchema);constBlogPost= mongoose.model('BlogPost', blogPostSchema);awaitBlogPost.create({title:'Introduction to Mongoose',authorId:1});awaitUser.create({_id:1,email:'test@gmail.com'});constdoc =awaitBlogPost.findOne().populate('author');
doc.author.email;// 'test@gmail.com'
```


## Virtuals via schema options

[Virtuals via schema options](#virtuals-via-schema-options)


Virtuals can also be defined in the schema-options directly without having to use.virtual:

[.virtual](../api/schema.html#Schema.prototype.virtual)

`.virtual`

```javascript
constuserSchema = mongoose.Schema({firstName:String,lastName:String}, {virtuals: {// Create a virtual property `fullName` with a getter and setterfullName: {get() {return`${this.firstName}${this.lastName}`; },set(v) {// `v` is the value being set, so use the value to set// `firstName` and `lastName`.constfirstName = v.substring(0, v.indexOf(' '));constlastName = v.substring(v.indexOf(' ') +1);this.set({ firstName, lastName });
      }
    }
  }
});constUser= mongoose.model('User', userSchema);constdoc =newUser();// Vanilla JavaScript assignment triggers the setterdoc.fullName='Jean-Luc Picard';

doc.fullName;// 'Jean-Luc Picard'doc.firstName;// 'Jean-Luc'doc.lastName;// 'Picard'
```


The same also goes for virtual options, like virtual populate:


```javascript
constuserSchema = mongoose.Schema({_id:Number,email:String});constblogPostSchema = mongoose.Schema({title:String,authorId:Number}, {virtuals: {// When you `populate()` the `author` virtual, Mongoose will find the// first document in the User model whose `_id` matches this document's// `authorId` property.author: {options: {ref:'User',localField:'authorId',foreignField:'_id',justOne:true}
    }
  }
});constUser= mongoose.model('User', userSchema);constBlogPost= mongoose.model('BlogPost', blogPostSchema);awaitBlogPost.create({title:'Introduction to Mongoose',authorId:1});awaitUser.create({_id:1,email:'test@gmail.com'});constdoc =awaitBlogPost.findOne().populate('author');
doc.author.email;// 'test@gmail.com'
```


## Further Reading

[Further Reading](#further-reading)


Virtuals in Mongoose SchemasPopulate VirtualsMongoose Lean Virtuals pluginGetting Started With Mongoose VirtualsUnderstanding Virtuals in Mongoose

- Virtuals in Mongoose Schemas

- Populate Virtuals

- Mongoose Lean Virtuals plugin

- Getting Started With Mongoose Virtuals

- Understanding Virtuals in Mongoose


[Source](https://mongoosejs.com/docs/tutorials/virtuals.html#virtuals-via-schema-options)