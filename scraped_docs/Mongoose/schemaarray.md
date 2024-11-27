# SchemaArray


# SchemaArray

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


SchemaArray()SchemaArray.checkRequired()SchemaArray.get()SchemaArray.optionsSchemaArray.prototype.checkRequired()SchemaArray.prototype.enum()SchemaArray.schemaNameSchemaArray.set()

- SchemaArray()

`SchemaArray()`
- SchemaArray.checkRequired()

`SchemaArray.checkRequired()`
- SchemaArray.get()

`SchemaArray.get()`
- SchemaArray.options

`SchemaArray.options`
- SchemaArray.prototype.checkRequired()

`SchemaArray.prototype.checkRequired()`
- SchemaArray.prototype.enum()

`SchemaArray.prototype.enum()`
- SchemaArray.schemaName

`SchemaArray.schemaName`
- SchemaArray.set()

`SchemaArray.set()`
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


SchemaArray()SchemaArray.checkRequired()SchemaArray.get()SchemaArray.optionsSchemaArray.prototype.checkRequired()SchemaArray.prototype.enum()SchemaArray.schemaNameSchemaArray.set()

- SchemaArray()

`SchemaArray()`
- SchemaArray.checkRequired()

`SchemaArray.checkRequired()`
- SchemaArray.get()

`SchemaArray.get()`
- SchemaArray.options

`SchemaArray.options`
- SchemaArray.prototype.checkRequired()

`SchemaArray.prototype.checkRequired()`
- SchemaArray.prototype.enum()

`SchemaArray.prototype.enum()`
- SchemaArray.schemaName

`SchemaArray.schemaName`
- SchemaArray.set()

`SchemaArray.set()`

### SchemaArray()

[SchemaArray()](#SchemaArray())

`SchemaArray()`

key«String»cast«SchemaType»options«Object»schemaOptions«Object»

- key«String»

`key`
- cast«SchemaType»

`cast`
- options«Object»

`options`
- schemaOptions«Object»

`schemaOptions`

«SchemaType»

- «SchemaType»

[«SchemaType»](schematype.html)


Array SchemaType constructor


### SchemaArray.checkRequired()

[SchemaArray.checkRequired()](#SchemaArray.checkRequired())

`SchemaArray.checkRequired()`

fn«Function»

- fn«Function»

`fn`

«Function»

- «Function»


Override the function the required validator uses to check whether an array
passes therequiredcheck.

`required`

#### Example:

[Example:](#example)


```javascript
// Require non-empty array to pass `required` checkmongoose.Schema.Types.Array.checkRequired(v=>Array.isArray(v) && v.length);constM = mongoose.model({arr: {type:Array,required:true} });newM({arr: [] }).validateSync();// `null`, validation fails!
```


### SchemaArray.get()

[SchemaArray.get()](#SchemaArray.get())

`SchemaArray.get()`

getter«Function»

- getter«Function»

`getter`

«this»

- «this»


«property»

- «property»


Attaches a getter for all Array instances


### SchemaArray.options

[SchemaArray.options](#SchemaArray.options)

`SchemaArray.options`

«property»

- «property»


Options for all arrays.


castNonArrays:trueby default. Iffalse, Mongoose will throw a CastError when a value isn't an array. Iftrue, Mongoose will wrap the provided value in an array before casting.

- castNonArrays:trueby default. Iffalse, Mongoose will throw a CastError when a value isn't an array. Iftrue, Mongoose will wrap the provided value in an array before casting.

`castNonArrays`
`true`
`false`
`true`

### SchemaArray.prototype.checkRequired()

[SchemaArray.prototype.checkRequired()](#SchemaArray.prototype.checkRequired())

`SchemaArray.prototype.checkRequired()`

value«Any»doc«Document»

- value«Any»

`value`
- doc«Document»

`doc`

«Boolean»

- «Boolean»


Check if the given value satisfies therequiredvalidator.

`required`

### SchemaArray.prototype.enum()

[SchemaArray.prototype.enum()](#SchemaArray.prototype.enum())

`SchemaArray.prototype.enum()`

[...args]«String|Object»enumeration values

- [...args]«String|Object»enumeration values

`[...args]`

«SchemaArray»this

- «SchemaArray»this


Adds an enum validator if this is an array of strings or numbers. Equivalent toSchemaString.prototype.enum()orSchemaNumber.prototype.enum()

`SchemaString.prototype.enum()`
`SchemaNumber.prototype.enum()`

### SchemaArray.schemaName

[SchemaArray.schemaName](#SchemaArray.schemaName)

`SchemaArray.schemaName`

«property»

- «property»


This schema type's name, to defend against minifiers that mangle
function names.


### SchemaArray.set()

[SchemaArray.set()](#SchemaArray.set())

`SchemaArray.set()`

option«String»The option you'd like to set the value forvalue«Any»value for option

- option«String»The option you'd like to set the value for

`option`
- value«Any»value for option

`value`

«undefined,void»

- «undefined,void»


Sets a default option for all Array instances.


#### Example:

[Example:](#example)


```javascript
// Make all Array instances have `required` of true by default.mongoose.Schema.Array.set('required',true);constUser= mongoose.model('User',newSchema({test:Array}));newUser({ }).validateSync().errors.test.message;// Path `test` is required.
```


[Source](https://mongoosejs.com/docs/api/schemaarray.html#SchemaArray.prototype.checkRequired())