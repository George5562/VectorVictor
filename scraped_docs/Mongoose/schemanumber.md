# SchemaNumber


# SchemaNumber

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


SchemaNumber()SchemaNumber.checkRequired()SchemaNumber.get()SchemaNumber.get()SchemaNumber.prototype.checkRequired()SchemaNumber.prototype.enum()SchemaNumber.prototype.max()SchemaNumber.prototype.min()SchemaNumber.schemaNameSchemaNumber.set()

- SchemaNumber()

`SchemaNumber()`
- SchemaNumber.checkRequired()

`SchemaNumber.checkRequired()`
- SchemaNumber.get()

`SchemaNumber.get()`
- SchemaNumber.get()

`SchemaNumber.get()`
- SchemaNumber.prototype.checkRequired()

`SchemaNumber.prototype.checkRequired()`
- SchemaNumber.prototype.enum()

`SchemaNumber.prototype.enum()`
- SchemaNumber.prototype.max()

`SchemaNumber.prototype.max()`
- SchemaNumber.prototype.min()

`SchemaNumber.prototype.min()`
- SchemaNumber.schemaName

`SchemaNumber.schemaName`
- SchemaNumber.set()

`SchemaNumber.set()`
[SchemaObjectId](schemaobjectid.html)

[SchemaString](schemastring.html)

[DocumentArray](documentarray.html)

[Subdocument](subdocument.html)

[ArraySubdocument](arraysubdocument.html)

[Buffer](buffer.html)

[Decimal128](decimal128.html)

[Map](map.html)

[Array](array.html)


SchemaNumber()SchemaNumber.checkRequired()SchemaNumber.get()SchemaNumber.get()SchemaNumber.prototype.checkRequired()SchemaNumber.prototype.enum()SchemaNumber.prototype.max()SchemaNumber.prototype.min()SchemaNumber.schemaNameSchemaNumber.set()

- SchemaNumber()

`SchemaNumber()`
- SchemaNumber.checkRequired()

`SchemaNumber.checkRequired()`
- SchemaNumber.get()

`SchemaNumber.get()`
- SchemaNumber.get()

`SchemaNumber.get()`
- SchemaNumber.prototype.checkRequired()

`SchemaNumber.prototype.checkRequired()`
- SchemaNumber.prototype.enum()

`SchemaNumber.prototype.enum()`
- SchemaNumber.prototype.max()

`SchemaNumber.prototype.max()`
- SchemaNumber.prototype.min()

`SchemaNumber.prototype.min()`
- SchemaNumber.schemaName

`SchemaNumber.schemaName`
- SchemaNumber.set()

`SchemaNumber.set()`

### SchemaNumber()

[SchemaNumber()](#SchemaNumber())

`SchemaNumber()`

key«String»options«Object»

- key«String»

`key`
- options«Object»

`options`

«SchemaType»

- «SchemaType»

[«SchemaType»](schematype.html)


Number SchemaType constructor.


### SchemaNumber.checkRequired()

[SchemaNumber.checkRequired()](#SchemaNumber.checkRequired())

`SchemaNumber.checkRequired()`

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

### SchemaNumber.get()

[SchemaNumber.get()](#SchemaNumber.get())

`SchemaNumber.get()`

getter«Function»

- getter«Function»

`getter`

«this»

- «this»


«property»

- «property»


Attaches a getter for all Number instances.


#### Example:

[Example:](#example)


```javascript
// Make all numbers round downmongoose.Number.get(function(v) {returnMath.floor(v); });constModel= mongoose.model('Test',newSchema({test:Number}));newModel({test:3.14}).test;// 3
```


### SchemaNumber.get()

[SchemaNumber.get()](#SchemaNumber.get())

`SchemaNumber.get()`

caster«Function»

- caster«Function»

`caster`

«Function»

- «Function»


«property»

- «property»


Get/set the function used to cast arbitrary values to numbers.


#### Example:

[Example:](#example)


```javascript
// Make Mongoose cast empty strings '' to 0 for paths declared as numbersconstoriginal = mongoose.Number.cast();
mongoose.Number.cast(v=>{if(v ==='') {return0; }returnoriginal(v);
});// Or disable casting entirelymongoose.Number.cast(false);
```


### SchemaNumber.prototype.checkRequired()

[SchemaNumber.prototype.checkRequired()](#SchemaNumber.prototype.checkRequired())

`SchemaNumber.prototype.checkRequired()`

value«Any»doc«Document»

- value«Any»

`value`
- doc«Document»

`doc`

«Boolean»

- «Boolean»


Check if the given value satisfies a required validator.


### SchemaNumber.prototype.enum()

[SchemaNumber.prototype.enum()](#SchemaNumber.prototype.enum())

`SchemaNumber.prototype.enum()`

values«Array»allowed values[message]«String»optional custom error message

- values«Array»allowed values

`values`
- [message]«String»optional custom error message

`[message]`

«SchemaType»this

- «SchemaType»this


Customized Error Messages

- Customized Error Messages

[Customized Error Messages](/docs/api/error.html#Error.messages)


Sets a enum validator


#### Example:

[Example:](#example)


```javascript
consts =newSchema({n: {type:Number,enum: [1,2,3] });constM = db.model('M', s);constm =newM({n:4});awaitm.save();// throws validation errorm.n=3;awaitm.save();// succeeds
```


### SchemaNumber.prototype.max()

[SchemaNumber.prototype.max()](#SchemaNumber.prototype.max())

`SchemaNumber.prototype.max()`

maximum«Number»number[message]«String»optional custom error message

- maximum«Number»number

`maximum`
- [message]«String»optional custom error message

`[message]`

«SchemaType»this

- «SchemaType»this


Customized Error Messages

- Customized Error Messages

[Customized Error Messages](/docs/api/error.html#Error.messages)


Sets a maximum number validator.


#### Example:

[Example:](#example)


```javascript
consts =newSchema({n: {type:Number,max:10})constM = db.model('M', s)constm =newM({n:11})
m.save(function(err) {console.error(err)// validator errorm.n=10;
  m.save()// success})// custom error messages// We can also use the special {MAX} token which will be replaced with the invalid valueconstmax = [10,'The value of path `{PATH}` ({VALUE}) exceeds the limit ({MAX}).'];constschema =newSchema({n: {type:Number,max: max })constM = mongoose.model('Measurement', schema);consts=newM({n:4});
s.validate(function(err) {console.log(String(err))// ValidationError: The value of path `n` (4) exceeds the limit (10).})
```


### SchemaNumber.prototype.min()

[SchemaNumber.prototype.min()](#SchemaNumber.prototype.min())

`SchemaNumber.prototype.min()`

value«Number»minimum number[message]«String»optional custom error message

- value«Number»minimum number

`value`
- [message]«String»optional custom error message

`[message]`

«SchemaType»this

- «SchemaType»this


Customized Error Messages

- Customized Error Messages

[Customized Error Messages](/docs/api/error.html#Error.messages)


Sets a minimum number validator.


#### Example:

[Example:](#example)


```javascript
consts =newSchema({n: {type:Number,min:10})constM = db.model('M', s)constm =newM({n:9})
m.save(function(err) {console.error(err)// validator errorm.n=10;
  m.save()// success})// custom error messages// We can also use the special {MIN} token which will be replaced with the invalid valueconstmin = [10,'The value of path `{PATH}` ({VALUE}) is beneath the limit ({MIN}).'];constschema =newSchema({n: {type:Number,min: min })constM = mongoose.model('Measurement', schema);consts=newM({n:4});
s.validate(function(err) {console.log(String(err))// ValidationError: The value of path `n` (4) is beneath the limit (10).})
```


### SchemaNumber.schemaName

[SchemaNumber.schemaName](#SchemaNumber.schemaName)

`SchemaNumber.schemaName`

«property»

- «property»


This schema type's name, to defend against minifiers that mangle
function names.


### SchemaNumber.set()

[SchemaNumber.set()](#SchemaNumber.set())

`SchemaNumber.set()`

option«String»The option you'd like to set the value forvalue«Any»value for option

- option«String»The option you'd like to set the value for

`option`
- value«Any»value for option

`value`

«undefined,void»

- «undefined,void»


«property»

- «property»


Sets a default option for all Number instances.


#### Example:

[Example:](#example)


```javascript
// Make all numbers have option `min` equal to 0.mongoose.Schema.Number.set('min',0);constOrder= mongoose.model('Order',newSchema({amount:Number}));newOrder({amount: -10}).validateSync().errors.amount.message;// Path `amount` must be larger than 0.
```


[Source](https://mongoosejs.com/docs/api/schemanumber.html#SchemaNumber.prototype.checkRequired())