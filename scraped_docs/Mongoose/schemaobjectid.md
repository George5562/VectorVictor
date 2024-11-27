# SchemaObjectId


# SchemaObjectId

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


SchemaObjectId()SchemaObjectId.checkRequired()SchemaObjectId.get()SchemaObjectId.get()SchemaObjectId.prototype.auto()SchemaObjectId.prototype.checkRequired()SchemaObjectId.schemaNameSchemaObjectId.set()

- SchemaObjectId()

`SchemaObjectId()`
- SchemaObjectId.checkRequired()

`SchemaObjectId.checkRequired()`
- SchemaObjectId.get()

`SchemaObjectId.get()`
- SchemaObjectId.get()

`SchemaObjectId.get()`
- SchemaObjectId.prototype.auto()

`SchemaObjectId.prototype.auto()`
- SchemaObjectId.prototype.checkRequired()

`SchemaObjectId.prototype.checkRequired()`
- SchemaObjectId.schemaName

`SchemaObjectId.schemaName`
- SchemaObjectId.set()

`SchemaObjectId.set()`
[SchemaString](schemastring.html)

[DocumentArray](documentarray.html)

[Subdocument](subdocument.html)

[ArraySubdocument](arraysubdocument.html)

[Buffer](buffer.html)

[Decimal128](decimal128.html)

[Map](map.html)

[Array](array.html)


SchemaObjectId()SchemaObjectId.checkRequired()SchemaObjectId.get()SchemaObjectId.get()SchemaObjectId.prototype.auto()SchemaObjectId.prototype.checkRequired()SchemaObjectId.schemaNameSchemaObjectId.set()

- SchemaObjectId()

`SchemaObjectId()`
- SchemaObjectId.checkRequired()

`SchemaObjectId.checkRequired()`
- SchemaObjectId.get()

`SchemaObjectId.get()`
- SchemaObjectId.get()

`SchemaObjectId.get()`
- SchemaObjectId.prototype.auto()

`SchemaObjectId.prototype.auto()`
- SchemaObjectId.prototype.checkRequired()

`SchemaObjectId.prototype.checkRequired()`
- SchemaObjectId.schemaName

`SchemaObjectId.schemaName`
- SchemaObjectId.set()

`SchemaObjectId.set()`

### SchemaObjectId()

[SchemaObjectId()](#SchemaObjectId())

`SchemaObjectId()`

key«String»options«Object»

- key«String»

`key`
- options«Object»

`options`

«SchemaType»

- «SchemaType»

[«SchemaType»](schematype.html)


ObjectId SchemaType constructor.


### SchemaObjectId.checkRequired()

[SchemaObjectId.checkRequired()](#SchemaObjectId.checkRequired())

`SchemaObjectId.checkRequired()`

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
// Allow empty strings to pass `required` checkmongoose.Schema.Types.String.checkRequired(v=>v !=null);constM = mongoose.model({str: {type:String,required:true} });newM({str:''}).validateSync();// `null`, validation passes!
```


### SchemaObjectId.get()

[SchemaObjectId.get()](#SchemaObjectId.get())

`SchemaObjectId.get()`

getter«Function»

- getter«Function»

`getter`

«this»

- «this»


«property»

- «property»


Attaches a getter for all ObjectId instances


#### Example:

[Example:](#example)


```javascript
// Always convert to string when getting an ObjectIdmongoose.ObjectId.get(v=>v.toString());constModel= mongoose.model('Test',newSchema({}));typeof(newModel({})._id);// 'string'
```


### SchemaObjectId.get()

[SchemaObjectId.get()](#SchemaObjectId.get())

`SchemaObjectId.get()`

caster«Function»

- caster«Function»

`caster`

«Function»

- «Function»


«property»

- «property»


Get/set the function used to cast arbitrary values to objectids.


#### Example:

[Example:](#example)


```javascript
// Make Mongoose only try to cast length 24 strings. By default, any 12// char string is a valid ObjectId.constoriginal = mongoose.ObjectId.cast();
mongoose.ObjectId.cast(v=>{
  assert.ok(typeofv !=='string'|| v.length===24);returnoriginal(v);
});// Or disable casting entirelymongoose.ObjectId.cast(false);
```


### SchemaObjectId.prototype.auto()

[SchemaObjectId.prototype.auto()](#SchemaObjectId.prototype.auto())

`SchemaObjectId.prototype.auto()`

turnOn«Boolean»auto generated ObjectId defaults

- turnOn«Boolean»auto generated ObjectId defaults

`turnOn`

«SchemaType»this

- «SchemaType»this


Adds an auto-generated ObjectId default if turnOn is true.


### SchemaObjectId.prototype.checkRequired()

[SchemaObjectId.prototype.checkRequired()](#SchemaObjectId.prototype.checkRequired())

`SchemaObjectId.prototype.checkRequired()`

value«Any»doc«Document»

- value«Any»

`value`
- doc«Document»

`doc`

«Boolean»

- «Boolean»


Check if the given value satisfies a required validator.


### SchemaObjectId.schemaName

[SchemaObjectId.schemaName](#SchemaObjectId.schemaName)

`SchemaObjectId.schemaName`

«property»

- «property»


This schema type's name, to defend against minifiers that mangle
function names.


### SchemaObjectId.set()

[SchemaObjectId.set()](#SchemaObjectId.set())

`SchemaObjectId.set()`

option«String»The option you'd like to set the value forvalue«Any»value for option

- option«String»The option you'd like to set the value for

`option`
- value«Any»value for option

`value`

«undefined,void»

- «undefined,void»


«property»

- «property»


Sets a default option for all ObjectId instances.


#### Example:

[Example:](#example)


```javascript
// Make all object ids have option `required` equal to true.mongoose.Schema.ObjectId.set('required',true);constOrder= mongoose.model('Order',newSchema({userId:ObjectId}));newOrder({ }).validateSync().errors.userId.message;// Path `userId` is required.
```


[Source](https://mongoosejs.com/docs/api/schemaobjectid.html#ObjectId.prototype.checkRequired())