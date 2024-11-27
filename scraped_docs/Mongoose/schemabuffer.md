# SchemaBuffer


# SchemaBuffer

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


SchemaBuffer()SchemaBuffer.checkRequired()SchemaBuffer.get()SchemaBuffer.prototype.checkRequired()SchemaBuffer.prototype.subtype()SchemaBuffer.schemaNameSchemaBuffer.set()

- SchemaBuffer()

`SchemaBuffer()`
- SchemaBuffer.checkRequired()

`SchemaBuffer.checkRequired()`
- SchemaBuffer.get()

`SchemaBuffer.get()`
- SchemaBuffer.prototype.checkRequired()

`SchemaBuffer.prototype.checkRequired()`
- SchemaBuffer.prototype.subtype()

`SchemaBuffer.prototype.subtype()`
- SchemaBuffer.schemaName

`SchemaBuffer.schemaName`
- SchemaBuffer.set()

`SchemaBuffer.set()`
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


SchemaBuffer()SchemaBuffer.checkRequired()SchemaBuffer.get()SchemaBuffer.prototype.checkRequired()SchemaBuffer.prototype.subtype()SchemaBuffer.schemaNameSchemaBuffer.set()

- SchemaBuffer()

`SchemaBuffer()`
- SchemaBuffer.checkRequired()

`SchemaBuffer.checkRequired()`
- SchemaBuffer.get()

`SchemaBuffer.get()`
- SchemaBuffer.prototype.checkRequired()

`SchemaBuffer.prototype.checkRequired()`
- SchemaBuffer.prototype.subtype()

`SchemaBuffer.prototype.subtype()`
- SchemaBuffer.schemaName

`SchemaBuffer.schemaName`
- SchemaBuffer.set()

`SchemaBuffer.set()`

### SchemaBuffer()

[SchemaBuffer()](#SchemaBuffer())

`SchemaBuffer()`

key«String»options«Object»

- key«String»

`key`
- options«Object»

`options`

«SchemaType»

- «SchemaType»

[«SchemaType»](schematype.html)


Buffer SchemaType constructor


### SchemaBuffer.checkRequired()

[SchemaBuffer.checkRequired()](#SchemaBuffer.checkRequired())

`SchemaBuffer.checkRequired()`

fn«Function»

- fn«Function»

`fn`

«Function»

- «Function»


«property»

- «property»


Override the function the required validator uses to check whether a string
passes therequiredcheck.

`required`

#### Example:

[Example:](#example)


```javascript
// Allow empty strings to pass `required` checkmongoose.Schema.Types.String.checkRequired(v=>v !=null);constM = mongoose.model({buf: {type:Buffer,required:true} });newM({buf:Buffer.from('') }).validateSync();// validation passes!
```


### SchemaBuffer.get()

[SchemaBuffer.get()](#SchemaBuffer.get())

`SchemaBuffer.get()`

getter«Function»

- getter«Function»

`getter`

«this»

- «this»


«property»

- «property»


Attaches a getter for all Buffer instances


#### Example:

[Example:](#example)


```javascript
// Always convert to string when getting an ObjectIdmongoose.Schema.Types.Buffer.get(v=>v.toString('hex'));constModel= mongoose.model('Test',newSchema({buf:Buffer} }));typeof(newModel({buf:Buffer.fromString('hello') }).buf);// 'string'
```


### SchemaBuffer.prototype.checkRequired()

[SchemaBuffer.prototype.checkRequired()](#SchemaBuffer.prototype.checkRequired())

`SchemaBuffer.prototype.checkRequired()`

value«Any»doc«Document»

- value«Any»

`value`
- doc«Document»

`doc`

«Boolean»

- «Boolean»


Check if the given value satisfies a required validator. To satisfy a
required validator, a buffer must not be null or undefined and have
non-zero length.


### SchemaBuffer.prototype.subtype()

[SchemaBuffer.prototype.subtype()](#SchemaBuffer.prototype.subtype())

`SchemaBuffer.prototype.subtype()`

subtype«Number»the default subtype

- subtype«Number»the default subtype

`subtype`

«SchemaType»this

- «SchemaType»this


Sets the defaultsubtypefor this buffer. You can find alist of allowed subtypes here.

[subtype](https://studio3t.com/whats-new/best-practices-uuid-mongodb/)

[list of allowed subtypes here](https://api.mongodb.com/python/current/api/bson/binary.html)


#### Example:

[Example:](#example)


```javascript
consts =newSchema({uuid: {type:Buffer,subtype:4});constM = db.model('M', s);constm =newM({uuid:'test string'});
m.uuid._subtype;// 4
```


### SchemaBuffer.schemaName

[SchemaBuffer.schemaName](#SchemaBuffer.schemaName)

`SchemaBuffer.schemaName`

«property»

- «property»


This schema type's name, to defend against minifiers that mangle
function names.


### SchemaBuffer.set()

[SchemaBuffer.set()](#SchemaBuffer.set())

`SchemaBuffer.set()`

option«String»The option you'd like to set the value forvalue«Any»value for option

- option«String»The option you'd like to set the value for

`option`
- value«Any»value for option

`value`

«undefined,void»

- «undefined,void»


«property»

- «property»


Sets a default option for all Buffer instances.


#### Example:

[Example:](#example)


```javascript
// Make all buffers have `required` of true by default.mongoose.Schema.Buffer.set('required',true);constUser= mongoose.model('User',newSchema({test:Buffer}));newUser({ }).validateSync().errors.test.message;// Path `test` is required.
```


[Source](https://mongoosejs.com/docs/api/schemabuffer.html#SchemaBuffer.prototype.checkRequired())