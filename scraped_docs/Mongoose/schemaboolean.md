# SchemaBoolean


# SchemaBoolean

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


SchemaBoolean()SchemaBoolean.checkRequired()SchemaBoolean.convertToFalseSchemaBoolean.convertToTrueSchemaBoolean.get()SchemaBoolean.get()SchemaBoolean.prototype.checkRequired()SchemaBoolean.schemaNameSchemaBoolean.set()

- SchemaBoolean()

`SchemaBoolean()`
- SchemaBoolean.checkRequired()

`SchemaBoolean.checkRequired()`
- SchemaBoolean.convertToFalse

`SchemaBoolean.convertToFalse`
- SchemaBoolean.convertToTrue

`SchemaBoolean.convertToTrue`
- SchemaBoolean.get()

`SchemaBoolean.get()`
- SchemaBoolean.get()

`SchemaBoolean.get()`
- SchemaBoolean.prototype.checkRequired()

`SchemaBoolean.prototype.checkRequired()`
- SchemaBoolean.schemaName

`SchemaBoolean.schemaName`
- SchemaBoolean.set()

`SchemaBoolean.set()`
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


SchemaBoolean()SchemaBoolean.checkRequired()SchemaBoolean.convertToFalseSchemaBoolean.convertToTrueSchemaBoolean.get()SchemaBoolean.get()SchemaBoolean.prototype.checkRequired()SchemaBoolean.schemaNameSchemaBoolean.set()

- SchemaBoolean()

`SchemaBoolean()`
- SchemaBoolean.checkRequired()

`SchemaBoolean.checkRequired()`
- SchemaBoolean.convertToFalse

`SchemaBoolean.convertToFalse`
- SchemaBoolean.convertToTrue

`SchemaBoolean.convertToTrue`
- SchemaBoolean.get()

`SchemaBoolean.get()`
- SchemaBoolean.get()

`SchemaBoolean.get()`
- SchemaBoolean.prototype.checkRequired()

`SchemaBoolean.prototype.checkRequired()`
- SchemaBoolean.schemaName

`SchemaBoolean.schemaName`
- SchemaBoolean.set()

`SchemaBoolean.set()`

### SchemaBoolean()

[SchemaBoolean()](#SchemaBoolean())

`SchemaBoolean()`

path«String»options«Object»

- path«String»

`path`
- options«Object»

`options`

«SchemaType»

- «SchemaType»

[«SchemaType»](schematype.html)


Boolean SchemaType constructor.


### SchemaBoolean.checkRequired()

[SchemaBoolean.checkRequired()](#SchemaBoolean.checkRequired())

`SchemaBoolean.checkRequired()`

fn«Function»

- fn«Function»

`fn`

«Function»

- «Function»


«property»

- «property»


Override the function the required validator uses to check whether a boolean
passes therequiredcheck.

`required`

### SchemaBoolean.convertToFalse

[SchemaBoolean.convertToFalse](#SchemaBoolean.convertToFalse)

`SchemaBoolean.convertToFalse`

«Set»

- «Set»


Configure which values get casted tofalse.

`false`

#### Example:

[Example:](#example)


```javascript
constM = mongoose.model('Test',newSchema({b:Boolean}));newM({b:'nay'}).b;// undefinedmongoose.Schema.Types.Boolean.convertToFalse.add('nay');newM({b:'nay'}).b;// false
```


### SchemaBoolean.convertToTrue

[SchemaBoolean.convertToTrue](#SchemaBoolean.convertToTrue)

`SchemaBoolean.convertToTrue`

«Set»

- «Set»


Configure which values get casted totrue.

`true`

#### Example:

[Example:](#example)


```javascript
constM = mongoose.model('Test',newSchema({b:Boolean}));newM({b:'affirmative'}).b;// undefinedmongoose.Schema.Boolean.convertToTrue.add('affirmative');newM({b:'affirmative'}).b;// true
```


### SchemaBoolean.get()

[SchemaBoolean.get()](#SchemaBoolean.get())

`SchemaBoolean.get()`

getter«Function»

- getter«Function»

`getter`

«this»

- «this»


«property»

- «property»


Attaches a getter for all Boolean instances


#### Example:

[Example:](#example)


```javascript
mongoose.Schema.Boolean.get(v=>v ===true?'yes':'no');constOrder= mongoose.model('Order',newSchema({isPaid:Boolean}));newOrder({isPaid:false}).isPaid;// 'no'
```


### SchemaBoolean.get()

[SchemaBoolean.get()](#SchemaBoolean.get())

`SchemaBoolean.get()`

caster«Function»

- caster«Function»

`caster`

«Function»

- «Function»


«property»

- «property»


Get/set the function used to cast arbitrary values to booleans.


#### Example:

[Example:](#example)


```javascript
// Make Mongoose cast empty string '' to false.constoriginal = mongoose.Schema.Boolean.cast();
mongoose.Schema.Boolean.cast(v=>{if(v ==='') {returnfalse;
  }returnoriginal(v);
});// Or disable casting entirelymongoose.Schema.Boolean.cast(false);
```


### SchemaBoolean.prototype.checkRequired()

[SchemaBoolean.prototype.checkRequired()](#SchemaBoolean.prototype.checkRequired())

`SchemaBoolean.prototype.checkRequired()`

value«Any»

- value«Any»

`value`

«Boolean»

- «Boolean»


Check if the given value satisfies a required validator. For a boolean
to satisfy a required validator, it must be strictly equal to true or to
false.


### SchemaBoolean.schemaName

[SchemaBoolean.schemaName](#SchemaBoolean.schemaName)

`SchemaBoolean.schemaName`

«property»

- «property»


This schema type's name, to defend against minifiers that mangle
function names.


### SchemaBoolean.set()

[SchemaBoolean.set()](#SchemaBoolean.set())

`SchemaBoolean.set()`

option«String»The option you'd like to set the value forvalue«Any»value for option

- option«String»The option you'd like to set the value for

`option`
- value«Any»value for option

`value`

«undefined,void»

- «undefined,void»


«property»

- «property»


Sets a default option for all Boolean instances.


#### Example:

[Example:](#example)


```javascript
// Make all booleans have `default` of false.mongoose.Schema.Boolean.set('default',false);constOrder= mongoose.model('Order',newSchema({isPaid:Boolean}));newOrder({ }).isPaid;// false
```


[Source](https://mongoosejs.com/docs/api/schemaboolean.html#SchemaBoolean.prototype.checkRequired())