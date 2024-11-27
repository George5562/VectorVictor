# SchemaTypeOptions


# SchemaTypeOptions

[Mongoose](mongoose.html)

[Schema](schema.html)

[Connection](connection.html)

[Document](document.html)

[Model](model.html)

[Query](query.html)

[QueryCursor](querycursor.html)

[Aggregate](aggregate.html)

[AggregationCursor](aggregationcursor.html)

[SchemaType](schematype.html)

[VirtualType](virtualtype.html)

[Error](error.html)

[SchemaArray](schemaarray.html)

[SchemaDocumentArray](schemadocumentarray.html)

[SchemaSubdocument](schemasubdocument.html)

[SchemaBoolean](schemaboolean.html)

[SchemaBuffer](schemabuffer.html)

[SchemaNumber](schemanumber.html)

[SchemaObjectId](schemaobjectid.html)

[SchemaString](schemastring.html)

[SchemaTypeOptions](schematypeoptions.html)


SchemaTypeOptions()SchemaTypeOptions.prototype.castSchemaTypeOptions.prototype.defaultSchemaTypeOptions.prototype.immutableSchemaTypeOptions.prototype.indexSchemaTypeOptions.prototype.refSchemaTypeOptions.prototype.refSchemaTypeOptions.prototype.requiredSchemaTypeOptions.prototype.selectSchemaTypeOptions.prototype.sparseSchemaTypeOptions.prototype.textSchemaTypeOptions.prototype.transformSchemaTypeOptions.prototype.typeSchemaTypeOptions.prototype.uniqueSchemaTypeOptions.prototype.validate

- SchemaTypeOptions()

`SchemaTypeOptions()`
- SchemaTypeOptions.prototype.cast

`SchemaTypeOptions.prototype.cast`
- SchemaTypeOptions.prototype.default

`SchemaTypeOptions.prototype.default`
- SchemaTypeOptions.prototype.immutable

`SchemaTypeOptions.prototype.immutable`
- SchemaTypeOptions.prototype.index

`SchemaTypeOptions.prototype.index`
- SchemaTypeOptions.prototype.ref

`SchemaTypeOptions.prototype.ref`
- SchemaTypeOptions.prototype.ref

`SchemaTypeOptions.prototype.ref`
- SchemaTypeOptions.prototype.required

`SchemaTypeOptions.prototype.required`
- SchemaTypeOptions.prototype.select

`SchemaTypeOptions.prototype.select`
- SchemaTypeOptions.prototype.sparse

`SchemaTypeOptions.prototype.sparse`
- SchemaTypeOptions.prototype.text

`SchemaTypeOptions.prototype.text`
- SchemaTypeOptions.prototype.transform

`SchemaTypeOptions.prototype.transform`
- SchemaTypeOptions.prototype.type

`SchemaTypeOptions.prototype.type`
- SchemaTypeOptions.prototype.unique

`SchemaTypeOptions.prototype.unique`
- SchemaTypeOptions.prototype.validate

`SchemaTypeOptions.prototype.validate`
[DocumentArray](documentarray.html)

[Subdocument](subdocument.html)

[ArraySubdocument](arraysubdocument.html)

[Buffer](buffer.html)

[Decimal128](decimal128.html)

[Map](map.html)

[Array](array.html)


SchemaTypeOptions()SchemaTypeOptions.prototype.castSchemaTypeOptions.prototype.defaultSchemaTypeOptions.prototype.immutableSchemaTypeOptions.prototype.indexSchemaTypeOptions.prototype.refSchemaTypeOptions.prototype.refSchemaTypeOptions.prototype.requiredSchemaTypeOptions.prototype.selectSchemaTypeOptions.prototype.sparseSchemaTypeOptions.prototype.textSchemaTypeOptions.prototype.transformSchemaTypeOptions.prototype.typeSchemaTypeOptions.prototype.uniqueSchemaTypeOptions.prototype.validate

- SchemaTypeOptions()

`SchemaTypeOptions()`
- SchemaTypeOptions.prototype.cast

`SchemaTypeOptions.prototype.cast`
- SchemaTypeOptions.prototype.default

`SchemaTypeOptions.prototype.default`
- SchemaTypeOptions.prototype.immutable

`SchemaTypeOptions.prototype.immutable`
- SchemaTypeOptions.prototype.index

`SchemaTypeOptions.prototype.index`
- SchemaTypeOptions.prototype.ref

`SchemaTypeOptions.prototype.ref`
- SchemaTypeOptions.prototype.ref

`SchemaTypeOptions.prototype.ref`
- SchemaTypeOptions.prototype.required

`SchemaTypeOptions.prototype.required`
- SchemaTypeOptions.prototype.select

`SchemaTypeOptions.prototype.select`
- SchemaTypeOptions.prototype.sparse

`SchemaTypeOptions.prototype.sparse`
- SchemaTypeOptions.prototype.text

`SchemaTypeOptions.prototype.text`
- SchemaTypeOptions.prototype.transform

`SchemaTypeOptions.prototype.transform`
- SchemaTypeOptions.prototype.type

`SchemaTypeOptions.prototype.type`
- SchemaTypeOptions.prototype.unique

`SchemaTypeOptions.prototype.unique`
- SchemaTypeOptions.prototype.validate

`SchemaTypeOptions.prototype.validate`

### SchemaTypeOptions()

[SchemaTypeOptions()](#SchemaTypeOptions())

`SchemaTypeOptions()`

«constructor»

- «constructor»


The options defined on a schematype.


#### Example:

[Example:](#example)


```javascript
constschema =newSchema({name:String});
schema.path('name').optionsinstanceofmongoose.SchemaTypeOptions;// true
```


### SchemaTypeOptions.prototype.cast

[SchemaTypeOptions.prototype.cast](#SchemaTypeOptions.prototype.cast)

`SchemaTypeOptions.prototype.cast`

«String»

- «String»


Allows overriding casting logic for this individual path. If a string, the
given string overwrites Mongoose's default cast error message.


#### Example:

[Example:](#example)


```javascript
constschema =newSchema({num: {type:Number,cast:'{VALUE} is not a valid number'}
});// Throws 'CastError: "bad" is not a valid number'schema.path('num').cast('bad');constModel= mongoose.model('Test', schema);constdoc =newModel({num:'fail'});consterr = doc.validateSync();

err.errors['num'];// 'CastError: "fail" is not a valid number'
```


### SchemaTypeOptions.prototype.default

[SchemaTypeOptions.prototype.default](#SchemaTypeOptions.prototype.default)

`SchemaTypeOptions.prototype.default`

«Function|Any»

- «Function|Any»


The default value for this path. If a function, Mongoose executes the function
and uses the return value as the default.


### SchemaTypeOptions.prototype.immutable

[SchemaTypeOptions.prototype.immutable](#SchemaTypeOptions.prototype.immutable)

`SchemaTypeOptions.prototype.immutable`

«Function|Boolean»

- «Function|Boolean»


Iftruthy, Mongoose will
disallow changes to this path once the document
is saved to the database for the first time. Read more aboutimmutability in Mongoose here.

[truthy](https://masteringjs.io/tutorials/fundamentals/truthy)

[immutability in Mongoose here](https://thecodebarbarian.com/whats-new-in-mongoose-5-6-immutable-properties.html)


### SchemaTypeOptions.prototype.index

[SchemaTypeOptions.prototype.index](#SchemaTypeOptions.prototype.index)

`SchemaTypeOptions.prototype.index`

«Boolean|Number|Object»

- «Boolean|Number|Object»


Iftruthy, Mongoose will
build an index on this path when the model is compiled.

[truthy](https://masteringjs.io/tutorials/fundamentals/truthy)


### SchemaTypeOptions.prototype.ref

[SchemaTypeOptions.prototype.ref](#SchemaTypeOptions.prototype.ref)

`SchemaTypeOptions.prototype.ref`

«Function|String»

- «Function|String»


The model thatpopulate()should use if populating this path.

`populate()`

### SchemaTypeOptions.prototype.ref

[SchemaTypeOptions.prototype.ref](#SchemaTypeOptions.prototype.ref)

`SchemaTypeOptions.prototype.ref`

«Function|String»

- «Function|String»


The path in the document thatpopulate()should use to find the model
to use.

`populate()`

### SchemaTypeOptions.prototype.required

[SchemaTypeOptions.prototype.required](#SchemaTypeOptions.prototype.required)

`SchemaTypeOptions.prototype.required`

«Function|Boolean»

- «Function|Boolean»


If true, attach a required validator to this path, which ensures this path
cannot be set to a nullish value. If a function, Mongoose calls the
function and only checks for nullish values if the function returns a truthy value.


### SchemaTypeOptions.prototype.select

[SchemaTypeOptions.prototype.select](#SchemaTypeOptions.prototype.select)

`SchemaTypeOptions.prototype.select`

«Boolean|Number»

- «Boolean|Number»


Whether to include or exclude this path by default when loading documents
usingfind(),findOne(), etc.

`find()`
`findOne()`

### SchemaTypeOptions.prototype.sparse

[SchemaTypeOptions.prototype.sparse](#SchemaTypeOptions.prototype.sparse)

`SchemaTypeOptions.prototype.sparse`

«Boolean|Number»

- «Boolean|Number»


Iftruthy, Mongoose will
build a sparse index on this path.

[truthy](https://masteringjs.io/tutorials/fundamentals/truthy)


### SchemaTypeOptions.prototype.text

[SchemaTypeOptions.prototype.text](#SchemaTypeOptions.prototype.text)

`SchemaTypeOptions.prototype.text`

«Boolean|Number|Object»

- «Boolean|Number|Object»


Iftruthy, Mongoose
will build a text index on this path.

[truthy](https://masteringjs.io/tutorials/fundamentals/truthy)


### SchemaTypeOptions.prototype.transform

[SchemaTypeOptions.prototype.transform](#SchemaTypeOptions.prototype.transform)

`SchemaTypeOptions.prototype.transform`

«Function»

- «Function»


Define a transform function for this individual schema type.
Only called when callingtoJSON()ortoObject().

`toJSON()`
`toObject()`

#### Example:

[Example:](#example)


```javascript
constschema =Schema({myDate: {type:Date,transform:v=>v.getFullYear()
  }
});constModel= mongoose.model('Test', schema);constdoc =newModel({myDate:newDate('2019/06/01') });
doc.myDateinstanceofDate;// trueconstres = doc.toObject({transform:true});
res.myDate;// 2019
```


### SchemaTypeOptions.prototype.type

[SchemaTypeOptions.prototype.type](#SchemaTypeOptions.prototype.type)

`SchemaTypeOptions.prototype.type`

«Function|String|Object»

- «Function|String|Object»


The type to cast this path to.


### SchemaTypeOptions.prototype.unique

[SchemaTypeOptions.prototype.unique](#SchemaTypeOptions.prototype.unique)

`SchemaTypeOptions.prototype.unique`

«Boolean|Number»

- «Boolean|Number»


Iftruthy, Mongoose
will build a unique index on this path when the
model is compiled.Theuniqueoption isnota validator.

[truthy](https://masteringjs.io/tutorials/fundamentals/truthy)

[Theuniqueoption isnota validator](/docs/validation.html#the-unique-option-is-not-a-validator)

`unique`

### SchemaTypeOptions.prototype.validate

[SchemaTypeOptions.prototype.validate](#SchemaTypeOptions.prototype.validate)

`SchemaTypeOptions.prototype.validate`

«Function|Object»

- «Function|Object»


Function or object describing how to validate this schematype.


[Source](https://mongoosejs.com/docs/api/schematypeoptions.html)