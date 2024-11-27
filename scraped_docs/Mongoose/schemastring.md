# SchemaString


# SchemaString

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


SchemaString()SchemaString.checkRequired()SchemaString.get()SchemaString.get()SchemaString.prototype.checkRequired()SchemaString.prototype.enum()SchemaString.prototype.lowercase()SchemaString.prototype.match()SchemaString.prototype.maxlength()SchemaString.prototype.minlength()SchemaString.prototype.trim()SchemaString.prototype.uppercase()SchemaString.schemaNameSchemaString.set()

- SchemaString()

`SchemaString()`
- SchemaString.checkRequired()

`SchemaString.checkRequired()`
- SchemaString.get()

`SchemaString.get()`
- SchemaString.get()

`SchemaString.get()`
- SchemaString.prototype.checkRequired()

`SchemaString.prototype.checkRequired()`
- SchemaString.prototype.enum()

`SchemaString.prototype.enum()`
- SchemaString.prototype.lowercase()

`SchemaString.prototype.lowercase()`
- SchemaString.prototype.match()

`SchemaString.prototype.match()`
- SchemaString.prototype.maxlength()

`SchemaString.prototype.maxlength()`
- SchemaString.prototype.minlength()

`SchemaString.prototype.minlength()`
- SchemaString.prototype.trim()

`SchemaString.prototype.trim()`
- SchemaString.prototype.uppercase()

`SchemaString.prototype.uppercase()`
- SchemaString.schemaName

`SchemaString.schemaName`
- SchemaString.set()

`SchemaString.set()`
[DocumentArray](documentarray.html)

[Subdocument](subdocument.html)

[ArraySubdocument](arraysubdocument.html)

[Buffer](buffer.html)

[Decimal128](decimal128.html)

[Map](map.html)

[Array](array.html)


SchemaString()SchemaString.checkRequired()SchemaString.get()SchemaString.get()SchemaString.prototype.checkRequired()SchemaString.prototype.enum()SchemaString.prototype.lowercase()SchemaString.prototype.match()SchemaString.prototype.maxlength()SchemaString.prototype.minlength()SchemaString.prototype.trim()SchemaString.prototype.uppercase()SchemaString.schemaNameSchemaString.set()

- SchemaString()

`SchemaString()`
- SchemaString.checkRequired()

`SchemaString.checkRequired()`
- SchemaString.get()

`SchemaString.get()`
- SchemaString.get()

`SchemaString.get()`
- SchemaString.prototype.checkRequired()

`SchemaString.prototype.checkRequired()`
- SchemaString.prototype.enum()

`SchemaString.prototype.enum()`
- SchemaString.prototype.lowercase()

`SchemaString.prototype.lowercase()`
- SchemaString.prototype.match()

`SchemaString.prototype.match()`
- SchemaString.prototype.maxlength()

`SchemaString.prototype.maxlength()`
- SchemaString.prototype.minlength()

`SchemaString.prototype.minlength()`
- SchemaString.prototype.trim()

`SchemaString.prototype.trim()`
- SchemaString.prototype.uppercase()

`SchemaString.prototype.uppercase()`
- SchemaString.schemaName

`SchemaString.schemaName`
- SchemaString.set()

`SchemaString.set()`

### SchemaString()

[SchemaString()](#SchemaString())

`SchemaString()`

key«String»options«Object»

- key«String»

`key`
- options«Object»

`options`

«SchemaType»

- «SchemaType»

[«SchemaType»](schematype.html)


String SchemaType constructor.


### SchemaString.checkRequired()

[SchemaString.checkRequired()](#SchemaString.checkRequired())

`SchemaString.checkRequired()`

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


### SchemaString.get()

[SchemaString.get()](#SchemaString.get())

`SchemaString.get()`

caster«Function»

- caster«Function»

`caster`

«Function»

- «Function»


«property»

- «property»


Get/set the function used to cast arbitrary values to strings.


#### Example:

[Example:](#example)


```javascript
// Throw an error if you pass in an object. Normally, Mongoose allows// objects with custom `toString()` functions.constoriginal = mongoose.Schema.Types.String.cast();
mongoose.Schema.Types.String.cast(v=>{
  assert.ok(v ==null||typeofv !=='object');returnoriginal(v);
});// Or disable casting entirelymongoose.Schema.Types.String.cast(false);
```


### SchemaString.get()

[SchemaString.get()](#SchemaString.get())

`SchemaString.get()`

getter«Function»

- getter«Function»

`getter`

«this»

- «this»


«property»

- «property»


Attaches a getter for all String instances.


#### Example:

[Example:](#example)


```javascript
// Make all numbers round downmongoose.Schema.String.get(v=>v.toLowerCase());constModel= mongoose.model('Test',newSchema({test:String}));newModel({test:'FOO'}).test;// 'foo'
```


### SchemaString.prototype.checkRequired()

[SchemaString.prototype.checkRequired()](#SchemaString.prototype.checkRequired())

`SchemaString.prototype.checkRequired()`

value«Any»doc«Document»

- value«Any»

`value`
- doc«Document»

`doc`

«Boolean»

- «Boolean»


Check if the given value satisfies therequiredvalidator. The value is
considered valid if it is a string (that is, notnullorundefined) and
has positive length. Therequiredvalidatorwillfail for empty
strings.

`required`
`null`
`undefined`
`required`

### SchemaString.prototype.enum()

[SchemaString.prototype.enum()](#SchemaString.prototype.enum())

`SchemaString.prototype.enum()`

[...args]«String|Object»enumeration values

- [...args]«String|Object»enumeration values

`[...args]`

«SchemaType»this

- «SchemaType»this


Customized Error MessagesEnums in JavaScript

- Customized Error Messages

[Customized Error Messages](/docs/api/error.html#Error.messages)

- Enums in JavaScript

[Enums in JavaScript](https://masteringjs.io/tutorials/fundamentals/enum)


Adds an enum validator


#### Example:

[Example:](#example)


```javascript
conststates = ['opening','open','closing','closed']consts =newSchema({state: {type:String,enum: states }})constM = db.model('M', s)constm =newM({state:'invalid'})
m.save(function(err) {console.error(String(err))// ValidationError: `invalid` is not a valid enum value for path `state`.m.state='open'm.save(callback)// success})// or with custom error messagesconstenum = {values: ['opening','open','closing','closed'],message:'enum validator failed for path `{PATH}` with value `{VALUE}`'}consts =newSchema({state: {type:String,enum: enum })constM = db.model('M', s)constm =newM({state:'invalid'})
m.save(function(err) {console.error(String(err))// ValidationError: enum validator failed for path `state` with value `invalid`m.state='open'm.save(callback)// success})
```


### SchemaString.prototype.lowercase()

[SchemaString.prototype.lowercase()](#SchemaString.prototype.lowercase())

`SchemaString.prototype.lowercase()`

«SchemaType»this

- «SchemaType»this


Adds a lowercasesetter.

[setter](/docs/api/schematype.html#SchemaType.prototype.set())


#### Example:

[Example:](#example)


```javascript
consts =newSchema({email: {type:String,lowercase:true}})constM = db.model('M', s);constm =newM({email:'SomeEmail@example.COM'});console.log(m.email)// someemail@example.comM.find({email:'SomeEmail@example.com'});// Queries by 'someemail@example.com'
```


Note thatlowercasedoesnotaffect regular expression queries:

`lowercase`

#### Example:

[Example:](#example)


```javascript
// Still queries for documents whose `email` matches the regular// expression /SomeEmail/. Mongoose does **not** convert the RegExp// to lowercase.M.find({email:/SomeEmail/});
```


### SchemaString.prototype.match()

[SchemaString.prototype.match()](#SchemaString.prototype.match())

`SchemaString.prototype.match()`

regExp«RegExp»regular expression to test against[message]«String»optional custom error message

- regExp«RegExp»regular expression to test against

`regExp`
- [message]«String»optional custom error message

`[message]`

«SchemaType»this

- «SchemaType»this


Customized Error Messages

- Customized Error Messages

[Customized Error Messages](/docs/api/error.html#Error.messages)


Sets a regexp validator.


Any value that does not passregExp.test(val) will fail validation.

`regExp`

#### Example:

[Example:](#example)


```javascript
consts =newSchema({name: {type:String,match:/^a/}})constM = db.model('M', s)constm =newM({name:'I am invalid'})
m.validate(function(err) {console.error(String(err))// "ValidationError: Path `name` is invalid (I am invalid)."m.name='apples'm.validate(function(err) {
    assert.ok(err)// success})
})// using a custom error messageconstmatch = [/\.html$/,"That file doesn't end in .html ({VALUE})"];consts =newSchema({file: {type:String,match: match }})constM = db.model('M', s);constm =newM({file:'invalid'});
m.validate(function(err) {console.log(String(err))// "ValidationError: That file doesn't end in .html (invalid)"})
```


Empty strings,undefined, andnullvalues always pass the match validator. If you require these values, enable therequiredvalidator also.

`undefined`
`null`
`required`

```javascript
consts =newSchema({name: {type:String,match:/^a/,required:true}})
```


### SchemaString.prototype.maxlength()

[SchemaString.prototype.maxlength()](#SchemaString.prototype.maxlength())

`SchemaString.prototype.maxlength()`

value«Number»maximum string length[message]«String»optional custom error message

- value«Number»maximum string length

`value`
- [message]«String»optional custom error message

`[message]`

«SchemaType»this

- «SchemaType»this


Customized Error Messages

- Customized Error Messages

[Customized Error Messages](/docs/api/error.html#Error.messages)


Sets a maximum length validator.


#### Example:

[Example:](#example)


```javascript
constschema =newSchema({postalCode: {type:String,maxlength:9})constAddress= db.model('Address', schema)constaddress =newAddress({postalCode:'9512512345'})
address.save(function(err) {console.error(err)// validator erroraddress.postalCode='95125';
  address.save()// success})// custom error messages// We can also use the special {MAXLENGTH} token which will be replaced with the maximum allowed lengthconstmaxlength = [9,'The value of path `{PATH}` (`{VALUE}`) exceeds the maximum allowed length ({MAXLENGTH}).'];constschema =newSchema({postalCode: {type:String,maxlength: maxlength })constAddress= mongoose.model('Address', schema);constaddress =newAddress({postalCode:'9512512345'});
address.validate(function(err) {console.log(String(err))// ValidationError: The value of path `postalCode` (`9512512345`) exceeds the maximum allowed length (9).})
```


### SchemaString.prototype.minlength()

[SchemaString.prototype.minlength()](#SchemaString.prototype.minlength())

`SchemaString.prototype.minlength()`

value«Number»minimum string length[message]«String»optional custom error message

- value«Number»minimum string length

`value`
- [message]«String»optional custom error message

`[message]`

«SchemaType»this

- «SchemaType»this


Customized Error Messages

- Customized Error Messages

[Customized Error Messages](/docs/api/error.html#Error.messages)


Sets a minimum length validator.


#### Example:

[Example:](#example)


```javascript
constschema =newSchema({postalCode: {type:String,minlength:5})constAddress= db.model('Address', schema)constaddress =newAddress({postalCode:'9512'})
address.save(function(err) {console.error(err)// validator erroraddress.postalCode='95125';
  address.save()// success})// custom error messages// We can also use the special {MINLENGTH} token which will be replaced with the minimum allowed lengthconstminlength = [5,'The value of path `{PATH}` (`{VALUE}`) is shorter than the minimum allowed length ({MINLENGTH}).'];constschema =newSchema({postalCode: {type:String,minlength: minlength })constAddress= mongoose.model('Address', schema);constaddress =newAddress({postalCode:'9512'});
address.validate(function(err) {console.log(String(err))// ValidationError: The value of path `postalCode` (`9512`) is shorter than the minimum length (5).})
```


### SchemaString.prototype.trim()

[SchemaString.prototype.trim()](#SchemaString.prototype.trim())

`SchemaString.prototype.trim()`

«SchemaType»this

- «SchemaType»this


Adds a trimsetter.

[setter](/docs/api/schematype.html#SchemaType.prototype.set())


The string value will betrimmedwhen set.

[trimmed](https://masteringjs.io/tutorials/fundamentals/trim-string)


#### Example:

[Example:](#example)


```javascript
consts =newSchema({name: {type:String,trim:true}});constM = db.model('M', s);conststring =' some name ';console.log(string.length);// 11constm =newM({name: string });console.log(m.name.length);// 9// Equivalent to `findOne({ name: string.trim() })`M.findOne({name: string });
```


Note thattrimdoesnotaffect regular expression queries:

`trim`

#### Example:

[Example:](#example)


```javascript
// Mongoose does **not** trim whitespace from the RegExp.M.find({name:/ some name /});
```


### SchemaString.prototype.uppercase()

[SchemaString.prototype.uppercase()](#SchemaString.prototype.uppercase())

`SchemaString.prototype.uppercase()`

«SchemaType»this

- «SchemaType»this


Adds an uppercasesetter.

[setter](/docs/api/schematype.html#SchemaType.prototype.set())


#### Example:

[Example:](#example)


```javascript
consts =newSchema({caps: {type:String,uppercase:true}})constM = db.model('M', s);constm =newM({caps:'an example'});console.log(m.caps)// AN EXAMPLEM.find({caps:'an example'})// Matches documents where caps = 'AN EXAMPLE'
```


Note thatuppercasedoesnotaffect regular expression queries:

`uppercase`

#### Example:

[Example:](#example)


```javascript
// Mongoose does **not** convert the RegExp to uppercase.M.find({email:/an example/});
```


### SchemaString.schemaName

[SchemaString.schemaName](#SchemaString.schemaName)

`SchemaString.schemaName`

«property»

- «property»


This schema type's name, to defend against minifiers that mangle
function names.


### SchemaString.set()

[SchemaString.set()](#SchemaString.set())

`SchemaString.set()`

option«String»The option you'd like to set the value forvalue«Any»value for option

- option«String»The option you'd like to set the value for

`option`
- value«Any»value for option

`value`

«undefined,void»

- «undefined,void»


«property»

- «property»


Sets a default option for all String instances.


#### Example:

[Example:](#example)


```javascript
// Make all strings have option `trim` equal to true.mongoose.Schema.String.set('trim',true);constUser= mongoose.model('User',newSchema({name:String}));newUser({name:'   John Doe   '}).name;// 'John Doe'
```


[Source](https://mongoosejs.com/docs/api/schemastring.html#SchemaString.prototype.checkRequired())