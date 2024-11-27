# Documents


# Documents

[Documents](#documents)


Mongoosedocumentsrepresent a one-to-one mapping
to documents as stored in MongoDB. Each document is an instance of itsModel.

[documents](api/document.html)

[Model](models.html)


Documents vs ModelsRetrievingUpdating Usingsave()Setting Nested PropertiesUpdating Using QueriesValidatingOverwriting

- Documents vs Models

- Retrieving

- Updating Usingsave()

`save()`
- Setting Nested Properties

- Updating Using Queries

- Validating

- Overwriting


## Documents vs Models

[Documents vs Models](#documents-vs-models)


DocumentandModelare distinct
classes in Mongoose. The Model class is a subclass of the Document class.
When you use theModel constructor, you create a
new document.

[Document](api/document.html#Document)

[Model](api/model.html#Model)

[Model constructor](api/model.html#Model)


```javascript
constMyModel= mongoose.model('Test',newSchema({name:String}));constdoc =newMyModel();

docinstanceofMyModel;// truedocinstanceofmongoose.Model;// truedocinstanceofmongoose.Document;// true
```


In Mongoose, a "document" generally means an instance of a model.
You should not have to create an instance of the Document class without
going through a model.


## Retrieving

[Retrieving](#retrieving)


When you load documents from MongoDB using model functions likefindOne(),
you get a Mongoose document back.

[findOne()](api/model.html#model_Model-findOne)

`findOne()`

```javascript
constdoc =awaitMyModel.findOne();

docinstanceofMyModel;// truedocinstanceofmongoose.Model;// truedocinstanceofmongoose.Document;// true
```


## Updating Usingsave()

[Updating Usingsave()](#updating-using-save)

`save()`

Mongoose documents track changes. You can modify a document using vanilla
JavaScript assignments and Mongoose will convert it intoMongoDB update operators.

[MongoDB update operators](https://www.mongodb.com/docs/manual/reference/operator/update/)


```javascript
doc.name='foo';// Mongoose sends an `updateOne({ _id: doc._id }, { $set: { name: 'foo' } })`// to MongoDB.awaitdoc.save();
```


Thesave()method returns a promise. Ifsave()succeeds, the promise
resolves to the document that was saved.

`save()`
`save()`

```javascript
doc.save().then(savedDoc=>{
  savedDoc === doc;// true});
```


If the document with the corresponding_idis not found, Mongoose will
report aDocumentNotFoundError:

`_id`
`DocumentNotFoundError`

```javascript
constdoc =awaitMyModel.findOne();// Delete the document so Mongoose won't be able to save changesawaitMyModel.deleteOne({_id: doc._id});

doc.name='foo';awaitdoc.save();// Throws DocumentNotFoundError
```


## Setting Nested Properties

[Setting Nested Properties](#setting-nested-properties)


Mongoose documents have aset()function that you can use to safely set deeply nested properties.

`set()`

```javascript
constschema =newSchema({nested: {subdoc:newSchema({name:String})
  }
});constTestModel= mongoose.model('Test', schema);constdoc =newTestModel();
doc.set('nested.subdoc.name','John Smith');
doc.nested.subdoc.name;// 'John Smith'
```


Mongoose documents also have aget()function that lets you safely read deeply nested properties.get()lets you avoid having to explicitly check for nullish values, similar to JavaScript'soptional chaining operator?..

`get()`
`get()`
[optional chaining operator?.](https://masteringjs.io/tutorials/fundamentals/optional-chaining-array)

`?.`

```javascript
constdoc2 =newTestModel();

doc2.get('nested.subdoc.name');// undefineddoc2.nested?.subdoc?.name;// undefineddoc2.set('nested.subdoc.name','Will Smith');
doc2.get('nested.subdoc.name');// 'Will Smith'
```


You can use optional chaining?.and nullish coalescing??with Mongoose documents.
However, be careful when usingnullish coalescing assignments??=to create nested paths with Mongoose documents.

`?.`
`??`
[nullish coalescing assignments??=](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment)

`??=`

```javascript
// The following works fineconstdoc3 =newTestModel();
doc3.nested.subdoc??= {};
doc3.nested.subdoc.name='John Smythe';// The following does **NOT** work.// Do not use the following pattern with Mongoose documents.constdoc4 =newTestModel();
(doc4.nested.subdoc??= {}).name='Charlie Smith';
doc.nested.subdoc;// Empty objectdoc.nested.subdoc.name;// undefined.
```


## Updating Using Queries

[Updating Using Queries](#updating-using-queries)


Thesave()function is generally the right
way to update a document with Mongoose. Withsave(), you get fullvalidationandmiddleware.

[save()](api/model.html#model_Model-save)

`save()`
`save()`
[validation](validation.html)

[middleware](middleware.html)


For cases whensave()isn't flexible enough, Mongoose lets you create
your ownMongoDB updateswith casting,middleware, andlimited validation.

`save()`
[MongoDB updates](https://www.mongodb.com/docs/manual/reference/operator/update/)

[middleware](middleware.html#notes)

[limited validation](validation.html#update-validators)


```javascript
// Update all documents in the `mymodels` collectionawaitMyModel.updateMany({}, {$set: {name:'foo'} });
```


Note thatupdate(),updateMany(),findOneAndUpdate(), etc. donotexecutesave()middleware. If you need save middleware and full validation,
first query for the document and thensave()it.

`update()`
`updateMany()`
`findOneAndUpdate()`
`save()`
`save()`

## Validating

[Validating](#validating)


Documents are casted and validated before they are saved. Mongoose first casts
values to the specified type and then validates them. Internally, Mongoose
calls the document'svalidate()methodbefore saving.

[validate()method](api/document.html#document_Document-validate)

`validate()`

```javascript
constschema =newSchema({name:String,age: {type:Number,min:0} });constPerson= mongoose.model('Person', schema);constp =newPerson({name:'foo',age:'bar'});// Cast to Number failed for value "bar" at path "age"awaitp.validate();constp2 =newPerson({name:'foo',age: -1});// Path `age` (-1) is less than minimum allowed value (0).awaitp2.validate();
```


Mongoose also supports limited validation on updates using therunValidatorsoption.
Mongoose casts parameters to query functions likefindOne(),updateOne()by default. However, Mongoose doesnotrun validation on query function
parameters by default. You need to setrunValidators: truefor Mongoose
to validate.

[runValidatorsoption](validation.html#update-validators)

`runValidators`
`findOne()`
`updateOne()`
`runValidators: true`

```javascript
// Cast to number failed for value "bar" at path "age"awaitPerson.updateOne({}, {age:'bar'});// Path `age` (-1) is less than minimum allowed value (0).awaitPerson.updateOne({}, {age: -1}, {runValidators:true});
```


Read thevalidationguide for more details.

[validation](validation.html)


## Overwriting

[Overwriting](#overwriting)


There are 2 different ways to overwrite a document (replacing all keys in the
document). One way is to use theDocument#overwrite()functionfollowed bysave().

[Document#overwrite()function](api/document.html#document_Document-overwrite)

`Document#overwrite()`
`save()`

```javascript
constdoc =awaitPerson.findOne({ _id });// Sets `name` and unsets all other propertiesdoc.overwrite({name:'Jean-Luc Picard'});awaitdoc.save();
```


The other way is to useModel.replaceOne().

[Model.replaceOne()](api/model.html#model_Model-replaceOne)

`Model.replaceOne()`

```javascript
// Sets `name` and unsets all other propertiesawaitPerson.replaceOne({ _id }, {name:'Jean-Luc Picard'});
```


## Next Up

[Next Up](#next-up)


Now that we've covered Documents, let's take a look atSubdocuments.

[Subdocuments](subdocs.html)


[Source](https://mongoosejs.com/docs/documents.html)