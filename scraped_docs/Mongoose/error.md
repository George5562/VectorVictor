# Error


# Error

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


Error()Error.CastErrorError.DivergentArrayErrorError.DocumentNotFoundErrorError.MissingSchemaErrorError.MongooseServerSelectionErrorError.OverwriteModelErrorError.ParallelSaveErrorError.StrictModeErrorError.StrictPopulateErrorError.ValidationErrorError.ValidatorErrorError.VersionErrorError.messagesError.prototype.name

- Error()

`Error()`
- Error.CastError

`Error.CastError`
- Error.DivergentArrayError

`Error.DivergentArrayError`
- Error.DocumentNotFoundError

`Error.DocumentNotFoundError`
- Error.MissingSchemaError

`Error.MissingSchemaError`
- Error.MongooseServerSelectionError

`Error.MongooseServerSelectionError`
- Error.OverwriteModelError

`Error.OverwriteModelError`
- Error.ParallelSaveError

`Error.ParallelSaveError`
- Error.StrictModeError

`Error.StrictModeError`
- Error.StrictPopulateError

`Error.StrictPopulateError`
- Error.ValidationError

`Error.ValidationError`
- Error.ValidatorError

`Error.ValidatorError`
- Error.VersionError

`Error.VersionError`
- Error.messages

`Error.messages`
- Error.prototype.name

`Error.prototype.name`
[SchemaArray](schemaarray.html)

[SchemaDocumentArray](schemadocumentarray.html)

[SchemaSubdocument](schemasubdocument.html)

[SchemaBoolean](schemaboolean.html)

[SchemaBuffer](schemabuffer.html)

[SchemaNumber](schemanumber.html)

[SchemaObjectId](schemaobjectid.html)

[SchemaString](schemastring.html)

[DocumentArray](documentarray.html)

[Subdocument](subdocument.html)

[ArraySubdocument](arraysubdocument.html)

[Buffer](buffer.html)

[Decimal128](decimal128.html)

[Map](map.html)

[Array](array.html)


Error()Error.CastErrorError.DivergentArrayErrorError.DocumentNotFoundErrorError.MissingSchemaErrorError.MongooseServerSelectionErrorError.OverwriteModelErrorError.ParallelSaveErrorError.StrictModeErrorError.StrictPopulateErrorError.ValidationErrorError.ValidatorErrorError.VersionErrorError.messagesError.prototype.name

- Error()

`Error()`
- Error.CastError

`Error.CastError`
- Error.DivergentArrayError

`Error.DivergentArrayError`
- Error.DocumentNotFoundError

`Error.DocumentNotFoundError`
- Error.MissingSchemaError

`Error.MissingSchemaError`
- Error.MongooseServerSelectionError

`Error.MongooseServerSelectionError`
- Error.OverwriteModelError

`Error.OverwriteModelError`
- Error.ParallelSaveError

`Error.ParallelSaveError`
- Error.StrictModeError

`Error.StrictModeError`
- Error.StrictPopulateError

`Error.StrictPopulateError`
- Error.ValidationError

`Error.ValidationError`
- Error.ValidatorError

`Error.ValidatorError`
- Error.VersionError

`Error.VersionError`
- Error.messages

`Error.messages`
- Error.prototype.name

`Error.prototype.name`

### Error()

[Error()](#Error())

`Error()`

msg«String»Error message

- msg«String»Error message

`msg`

«constructor»

- «constructor»


«Error»

- «Error»

[«Error»](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Error)


MongooseError constructor. MongooseError is the base class for all
Mongoose-specific errors.


#### Example:

[Example:](#example)


```javascript
constModel= mongoose.model('Test',newmongoose.Schema({answer:Number}));constdoc =newModel({answer:'not a number'});consterr = doc.validateSync();

errinstanceofmongoose.Error.ValidationError;// true
```


### Error.CastError

[Error.CastError](#Error.CastError)

`Error.CastError`

«property»

- «property»


An instance of this error class will be returned when mongoose failed to
cast a value.


### Error.DivergentArrayError

[Error.DivergentArrayError](#Error.DivergentArrayError)

`Error.DivergentArrayError`

«property»

- «property»


An instance of this error will be returned if you used an array projection
and then modified the array in an unsafe way.


### Error.DocumentNotFoundError

[Error.DocumentNotFoundError](#Error.DocumentNotFoundError)

`Error.DocumentNotFoundError`

«property»

- «property»


An instance of this error class will be returned whensave()fails
because the underlying
document was not found. The constructor takes one parameter, the
conditions that mongoose passed toupdateOne()when trying to update
the document.

`save()`
`updateOne()`

### Error.MissingSchemaError

[Error.MissingSchemaError](#Error.MissingSchemaError)

`Error.MissingSchemaError`

«property»

- «property»


Thrown when you try to access a model that has not been registered yet


### Error.MongooseServerSelectionError

[Error.MongooseServerSelectionError](#Error.MongooseServerSelectionError)

`Error.MongooseServerSelectionError`

«property»

- «property»


Thrown when the MongoDB Node driver can't connect to a valid server
to send an operation to.


### Error.OverwriteModelError

[Error.OverwriteModelError](#Error.OverwriteModelError)

`Error.OverwriteModelError`

«property»

- «property»


Thrown when a model with the given name was already registered on the connection.
Seethe FAQ aboutOverwriteModelError.

[the FAQ aboutOverwriteModelError](/docs/faq.html#overwrite-model-error)

`OverwriteModelError`

### Error.ParallelSaveError

[Error.ParallelSaveError](#Error.ParallelSaveError)

`Error.ParallelSaveError`

«property»

- «property»


An instance of this error class will be returned when you callsave()multiple
times on the same document in parallel. See theFAQfor more
information.

`save()`
[FAQ](/docs/faq.html)


### Error.StrictModeError

[Error.StrictModeError](#Error.StrictModeError)

`Error.StrictModeError`

«property»

- «property»


Thrown when your try to pass values to model constructor that
were not specified in schema or change immutable properties whenstrictmode is"throw"

`strict`
`"throw"`

### Error.StrictPopulateError

[Error.StrictPopulateError](#Error.StrictPopulateError)

`Error.StrictPopulateError`

«property»

- «property»


An instance of this error class will be returned when mongoose failed to
populate with a path that is not existing.


### Error.ValidationError

[Error.ValidationError](#Error.ValidationError)

`Error.ValidationError`

«property»

- «property»


An instance of this error class will be returned whenvalidationfailed.
Theerrorsproperty contains an object whose keys are the paths that failed and whose values are
instances of CastError or ValidationError.

[validation](/docs/validation.html)

`errors`

### Error.ValidatorError

[Error.ValidatorError](#Error.ValidatorError)

`Error.ValidatorError`

«property»

- «property»


AValidationErrorhas a hash oferrorsthat contain individualValidatorErrorinstances.

`ValidationError`
`errors`
`ValidatorError`

#### Example:

[Example:](#example)


```javascript
constschema =Schema({name: {type:String,required:true} });constModel= mongoose.model('Test', schema);constdoc =newModel({});// Top-level error is a ValidationError, **not** a ValidatorErrorconsterr = doc.validateSync();
errinstanceofmongoose.Error.ValidationError;// true// A ValidationError `err` has 0 or more ValidatorErrors keyed by the// path in the `err.errors` property.err.errors['name']instanceofmongoose.Error.ValidatorError;

err.errors['name'].kind;// 'required'err.errors['name'].path;// 'name'err.errors['name'].value;// undefined
```


Instances ofValidatorErrorhave the following properties:

`ValidatorError`

kind: The validator'stype, like'required'or'regexp'path: The path that failed validationvalue: The value that failed validation

- kind: The validator'stype, like'required'or'regexp'

`kind`
`type`
`'required'`
`'regexp'`
- path: The path that failed validation

`path`
- value: The value that failed validation

`value`

### Error.VersionError

[Error.VersionError](#Error.VersionError)

`Error.VersionError`

«property»

- «property»


An instance of this error class will be returned when you callsave()after
the document in the database was changed in a potentially unsafe way. See
theversionKeyoptionfor more information.

`save()`
[versionKeyoption](/docs/guide.html#versionKey)

`versionKey`

### Error.messages

[Error.messages](#Error.messages)

`Error.messages`

«property»

- «property»


Error.messages

- Error.messages

[Error.messages](#Error.messages)


The default built-in validator error messages.


### Error.prototype.name

[Error.prototype.name](#Error.prototype.name)

`Error.prototype.name`

«String»

- «String»


The name of the error. The name uniquely identifies this Mongoose error. The
possible values are:


MongooseError: general Mongoose errorCastError: Mongoose could not convert a value to the type defined in the schema path. May be in aValidationErrorclass'errorsproperty.DivergentArrayError: You attempted tosave()an array that was modified after you loaded it with a$elemMatchor similar projectionMissingSchemaError: You tried to access a model withmongoose.model()that was not definedDocumentNotFoundError: The document you tried tosave()was not foundValidatorError: error from an individual schema path's validatorValidationError: error returned fromvalidate()orvalidateSync(). Contains zero or moreValidatorErrorinstances in.errorsproperty.MissingSchemaError: You calledmongoose.Document()without a schemaObjectExpectedError: Thrown when you set a nested path to a non-object value withstrict mode set.ObjectParameterError: Thrown when you pass a non-object value to a function which expects an object as a paramterOverwriteModelError: Thrown when you callmongoose.model()to re-define a model that was already defined.ParallelSaveError: Thrown when you callsave()on a document when the same document instance is already saving.StrictModeError: Thrown when you set a path that isn't the schema andstrict modeis set tothrow.VersionError: Thrown when thedocument is out of sync

- MongooseError: general Mongoose error

`MongooseError`
- CastError: Mongoose could not convert a value to the type defined in the schema path. May be in aValidationErrorclass'errorsproperty.

`CastError`
`ValidationError`
`errors`
- DivergentArrayError: You attempted tosave()an array that was modified after you loaded it with a$elemMatchor similar projection

`DivergentArrayError`
`save()`
`$elemMatch`
- MissingSchemaError: You tried to access a model withmongoose.model()that was not defined

`MissingSchemaError`
`mongoose.model()`
- DocumentNotFoundError: The document you tried tosave()was not found

`DocumentNotFoundError`
`save()`
- ValidatorError: error from an individual schema path's validator

`ValidatorError`
- ValidationError: error returned fromvalidate()orvalidateSync(). Contains zero or moreValidatorErrorinstances in.errorsproperty.

`ValidationError`
`validate()`
`validateSync()`
`ValidatorError`
`.errors`
- MissingSchemaError: You calledmongoose.Document()without a schema

`MissingSchemaError`
`mongoose.Document()`
- ObjectExpectedError: Thrown when you set a nested path to a non-object value withstrict mode set.

`ObjectExpectedError`
- ObjectParameterError: Thrown when you pass a non-object value to a function which expects an object as a paramter

`ObjectParameterError`
- OverwriteModelError: Thrown when you callmongoose.model()to re-define a model that was already defined.

`OverwriteModelError`
`mongoose.model()`
- ParallelSaveError: Thrown when you callsave()on a document when the same document instance is already saving.

`ParallelSaveError`
`save()`
- StrictModeError: Thrown when you set a path that isn't the schema andstrict modeis set tothrow.

`StrictModeError`
`throw`
- VersionError: Thrown when thedocument is out of sync

`VersionError`

[Source](https://mongoosejs.com/docs/api/error.html#Error.messages)