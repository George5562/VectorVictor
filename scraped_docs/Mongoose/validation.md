# Validation


# Validation

[Validation](#validation)


Before we get into the specifics of validation syntax, please keep the following rules in mind:


Validation is defined in theSchemaTypeValidation ismiddleware. Mongoose registers validation as apre('save')hook on every schema by default.Validation always runs as thefirstpre('save')hook. This means that validation doesn't run on any changes you make inpre('save')hooks.You can disable automatic validation before save by setting thevalidateBeforeSaveoptionYou can manually run validation usingdoc.validate()ordoc.validateSync()You can manually mark a field as invalid (causing validation to fail) by usingdoc.invalidate(...)Validators are not run on undefined values. The only exception is therequiredvalidator.When you callModel#save, Mongoose also runs subdocument validation. If an error occurs, yourModel#savepromise rejectsValidation is customizable

- Validation is defined in theSchemaType

- Validation ismiddleware. Mongoose registers validation as apre('save')hook on every schema by default.

`pre('save')`
- Validation always runs as thefirstpre('save')hook. This means that validation doesn't run on any changes you make inpre('save')hooks.

`pre('save')`
`pre('save')`
- You can disable automatic validation before save by setting thevalidateBeforeSaveoption

- You can manually run validation usingdoc.validate()ordoc.validateSync()

`doc.validate()`
`doc.validateSync()`
- You can manually mark a field as invalid (causing validation to fail) by usingdoc.invalidate(...)

`doc.invalidate(...)`
- Validators are not run on undefined values. The only exception is therequiredvalidator.

`required`
- When you callModel#save, Mongoose also runs subdocument validation. If an error occurs, yourModel#savepromise rejects

- Validation is customizable


```javascript
constschema =newSchema({name: {type:String,required:true}
});constCat= db.model('Cat', schema);// This cat has no name :(constcat =newCat();leterror;try{awaitcat.save();
}catch(err) {
  error = err;
}

assert.equal(error.errors['name'].message,'Path `name` is required.');

error = cat.validateSync();
assert.equal(error.errors['name'].message,'Path `name` is required.');
```


Built-in ValidatorsCustom Error MessagesTheuniqueOption is Not a ValidatorCustom ValidatorsAsync Custom ValidatorsValidation ErrorsCast ErrorsGlobal SchemaType ValidationRequired Validators On Nested ObjectsUpdate ValidatorsUpdate Validators andthisUpdate Validators Only Run On Updated PathsUpdate Validators Only Run For Some Operations

- Built-in Validators

- Custom Error Messages

- TheuniqueOption is Not a Validator

`unique`
- Custom Validators

- Async Custom Validators

- Validation Errors

- Cast Errors

- Global SchemaType Validation

- Required Validators On Nested Objects

- Update Validators

- Update Validators andthis

`this`
- Update Validators Only Run On Updated Paths

- Update Validators Only Run For Some Operations


## Built-in Validators

[Built-in Validators](#built-in-validators)


Mongoose has several built-in validators.


AllSchemaTypeshave the built-inrequiredvalidator. The required validator uses theSchemaType'scheckRequired()functionto determine if the value satisfies the required validator.Numbershaveminandmaxvalidators.Stringshaveenum,match,minLength, andmaxLengthvalidators.

- AllSchemaTypeshave the built-inrequiredvalidator. The required validator uses theSchemaType'scheckRequired()functionto determine if the value satisfies the required validator.

`checkRequired()`
- Numbershaveminandmaxvalidators.

`min`
`max`
- Stringshaveenum,match,minLength, andmaxLengthvalidators.

`enum`
`match`
`minLength`
`maxLength`

Each of the validator links above provide more information about how to enable them and customize their error messages.


```javascript
constbreakfastSchema =newSchema({eggs: {type:Number,min: [6,'Too few eggs'],max:12},bacon: {type:Number,required: [true,'Why no bacon?']
  },drink: {type:String,enum: ['Coffee','Tea'],required:function() {returnthis.bacon>3;
    }
  }
});constBreakfast= db.model('Breakfast', breakfastSchema);constbadBreakfast =newBreakfast({eggs:2,bacon:0,drink:'Milk'});leterror = badBreakfast.validateSync();
assert.equal(error.errors['eggs'].message,'Too few eggs');
assert.ok(!error.errors['bacon']);
assert.equal(error.errors['drink'].message,'`Milk` is not a valid enum value for path `drink`.');

badBreakfast.bacon=5;
badBreakfast.drink=null;

error = badBreakfast.validateSync();
assert.equal(error.errors['drink'].message,'Path `drink` is required.');

badBreakfast.bacon=null;
error = badBreakfast.validateSync();
assert.equal(error.errors['bacon'].message,'Why no bacon?');
```


## Custom Error Messages

[Custom Error Messages](#custom-error-messages)


You can configure the error message for individual validators in your schema. There are two equivalent
ways to set the validator error message:


Array syntax:min: [6, 'Must be at least 6, got {VALUE}']Object syntax:enum: { values: ['Coffee', 'Tea'], message: '{VALUE} is not supported' }

- Array syntax:min: [6, 'Must be at least 6, got {VALUE}']

`min: [6, 'Must be at least 6, got {VALUE}']`
- Object syntax:enum: { values: ['Coffee', 'Tea'], message: '{VALUE} is not supported' }

`enum: { values: ['Coffee', 'Tea'], message: '{VALUE} is not supported' }`

Mongoose also supports rudimentary templating for error messages.
Mongoose replaces{VALUE}with the value being validated.

`{VALUE}`

```javascript
constbreakfastSchema =newSchema({eggs: {type:Number,min: [6,'Must be at least 6, got {VALUE}'],max:12},drink: {type:String,enum: {values: ['Coffee','Tea'],message:'{VALUE} is not supported'}
  }
});constBreakfast= db.model('Breakfast', breakfastSchema);constbadBreakfast =newBreakfast({eggs:2,drink:'Milk'});consterror = badBreakfast.validateSync();
assert.equal(error.errors['eggs'].message,'Must be at least 6, got 2');
assert.equal(error.errors['drink'].message,'Milk is not supported');
```


## TheuniqueOption is Not a Validator

[TheuniqueOption is Not a Validator](#the-code>unique</code>-option-is-not-a-validator)

`unique`

A common gotcha for beginners is that theuniqueoption for schemas
isnota validator. It's a convenient helper for buildingMongoDB unique indexes.
See theFAQfor more information.

`unique`
[MongoDB unique indexes](https://www.mongodb.com/docs/manual/core/index-unique/)

[FAQ](faq.html)


```javascript
constuniqueUsernameSchema =newSchema({username: {type:String,unique:true}
});constU1= db.model('U1', uniqueUsernameSchema);constU2= db.model('U2', uniqueUsernameSchema);constdup = [{username:'Val'}, {username:'Val'}];// Race condition! This may save successfully, depending on whether// MongoDB built the index before writing the 2 docs.U1.create(dup).then(() =>{
  }).catch(err=>{
  });// You need to wait for Mongoose to finish building the `unique`// index before writing. You only need to build indexes once for// a given collection, so you normally don't need to do this// in production. But, if you drop the database between tests,// you will need to use `init()` to wait for the index build to finish.U2.init().then(() =>U2.create(dup)).catch(error=>{// `U2.create()` will error, but will *not* be a mongoose validation error, it will be// a duplicate key error.// See: https://masteringjs.io/tutorials/mongoose/e11000-duplicate-keyassert.ok(error);
    assert.ok(!error.errors);
    assert.ok(error.message.indexOf('duplicate key error') !== -1);
  });
```


## Custom Validators

[Custom Validators](#custom-validators)


If the built-in validators aren't enough, you can define custom validators
to suit your needs.


Custom validation is declared by passing a validation function.
You can find detailed instructions on how to do this in theSchemaType#validate()API docs.

[SchemaType#validate()API docs](api/schematype.html#schematype_SchemaType-validate)

`SchemaType#validate()`

```javascript
constuserSchema =newSchema({phone: {type:String,validate: {validator:function(v) {return/\d{3}-\d{3}-\d{4}/.test(v);
      },message:props=>`${props.value}is not a valid phone number!`},required: [true,'User phone number required']
  }
});constUser= db.model('user', userSchema);constuser =newUser();leterror;

user.phone='555.0123';
error = user.validateSync();
assert.equal(error.errors['phone'].message,'555.0123 is not a valid phone number!');

user.phone='';
error = user.validateSync();
assert.equal(error.errors['phone'].message,'User phone number required');

user.phone='201-555-0123';// Validation succeeds! Phone number is defined// and fits `DDD-DDD-DDDD`error = user.validateSync();
assert.equal(error,null);
```


## Async Custom Validators

[Async Custom Validators](#async-custom-validators)


Custom validators can also be asynchronous. If your validator function
returns a promise (like anasyncfunction), mongoose will wait for that
promise to settle. If the returned promise rejects, or fulfills with
the valuefalse, Mongoose will consider that a validation error.

`async`
`false`

```javascript
constuserSchema =newSchema({name: {type:String,// You can also make a validator async by returning a promise.validate:() =>Promise.reject(newError('Oops!'))
  },email: {type:String,// There are two ways for an promise-based async validator to fail:// 1) If the promise rejects, Mongoose assumes the validator failed with the given error.// 2) If the promise resolves to `false`, Mongoose assumes the validator failed and creates an error with the given `message`.validate: {validator:() =>Promise.resolve(false),message:'Email validation failed'}
  }
});constUser= db.model('User', userSchema);constuser =newUser();

user.email='test@test.co';
user.name='test';leterror;try{awaituser.validate();
}catch(err) {
  error = err;
}
assert.ok(error);
assert.equal(error.errors['name'].message,'Oops!');
assert.equal(error.errors['email'].message,'Email validation failed');
```


## Validation Errors

[Validation Errors](#validation-errors)


Errors returned after failed validation contain anerrorsobject
whose values areValidatorErrorobjects. EachValidatorErrorhaskind,path,value, andmessageproperties.
A ValidatorError also may have areasonproperty. If an error was
thrown in the validator, this property will contain the error that was
thrown.

`errors`
`ValidatorError`
[ValidatorError](api/error.html#error_Error-ValidatorError)

`kind`
`path`
`value`
`message`
`reason`

```javascript
consttoySchema =newSchema({color:String,name:String});constvalidator =function(value) {return/red|white|gold/i.test(value);
};
toySchema.path('color').validate(validator,'Color `{VALUE}` not valid','Invalid color');
toySchema.path('name').validate(function(v) {if(v !=='Turbo Man') {thrownewError('Need to get a Turbo Man for Christmas');
  }returntrue;
},'Name `{VALUE}` is not valid');constToy= db.model('Toy', toySchema);consttoy =newToy({color:'Green',name:'Power Ranger'});leterror;try{awaittoy.save();
}catch(err) {
  error = err;
}// `error` is a ValidationError object// `error.errors.color` is a ValidatorError objectassert.equal(error.errors.color.message,'Color `Green` not valid');
assert.equal(error.errors.color.kind,'Invalid color');
assert.equal(error.errors.color.path,'color');
assert.equal(error.errors.color.value,'Green');// If your validator throws an exception, mongoose will use the error// message. If your validator returns `false`,// mongoose will use the 'Name `Power Ranger` is not valid' message.assert.equal(error.errors.name.message,'Need to get a Turbo Man for Christmas');
assert.equal(error.errors.name.value,'Power Ranger');// If your validator threw an error, the `reason` property will contain// the original error thrown, including the original stack trace.assert.equal(error.errors.name.reason.message,'Need to get a Turbo Man for Christmas');

assert.equal(error.name,'ValidationError');
```


## Cast Errors

[Cast Errors](#cast-errors)


Before running validators, Mongoose attempts to coerce values to the correct type. This process is calledcastingthe document.
If casting fails for a given path, theerror.errorsobject will contain aCastErrorobject.

`error.errors`
`CastError`

Casting runs before validation, and validation does not run if casting fails.
That means your custom validators may assumevisnull,undefined, or an instance of the type specified in your schema.

`v`
`null`
`undefined`

```javascript
constvehicleSchema =newmongoose.Schema({numWheels: {type:Number,max:18}
});constVehicle= db.model('Vehicle', vehicleSchema);constdoc =newVehicle({numWheels:'not a number'});consterr = doc.validateSync();

err.errors['numWheels'].name;// 'CastError'// 'Cast to Number failed for value "not a number" at path "numWheels"'err.errors['numWheels'].message;
```


By default, Mongoose cast error messages look likeCast to Number failed for value "pie" at path "numWheels".
You can overwrite Mongoose's default cast error message by thecastoption on your SchemaType to a string as follows.

`Cast to Number failed for value "pie" at path "numWheels"`
`cast`

```javascript
constvehicleSchema =newmongoose.Schema({numWheels: {type:Number,cast:'{VALUE} is not a number'}
});constVehicle= db.model('Vehicle', vehicleSchema);constdoc =newVehicle({numWheels:'pie'});consterr = doc.validateSync();

err.errors['numWheels'].name;// 'CastError'// "pie" is not a numbererr.errors['numWheels'].message;
```


Mongoose's cast error message templating supports the following parameters:


{PATH}: the path that failed to cast{VALUE}: a string representation of the value that failed to cast{KIND}: the type that Mongoose attempted to cast to, like'String'or'Number'

- {PATH}: the path that failed to cast

`{PATH}`
- {VALUE}: a string representation of the value that failed to cast

`{VALUE}`
- {KIND}: the type that Mongoose attempted to cast to, like'String'or'Number'

`{KIND}`
`'String'`
`'Number'`

You can also define a function that Mongoose will call to get the cast error message as follows.


```javascript
constvehicleSchema =newmongoose.Schema({numWheels: {type:Number,cast: [null,(value, path, model, kind) =>`"${value}" is not a number`]
  }
});constVehicle= db.model('Vehicle', vehicleSchema);constdoc =newVehicle({numWheels:'pie'});consterr = doc.validateSync();

err.errors['numWheels'].name;// 'CastError'// "pie" is not a numbererr.errors['numWheels'].message;
```


## Global SchemaType Validation

[Global SchemaType Validation](#global-schematype-validation)


In addition to defining custom validators on individual schema paths, you can also configure a custom validator to run on every instance of a givenSchemaType.
For example, the following code demonstrates how to make empty string''an invalid value forallstring paths.

`SchemaType`
`''`

```javascript
// Add a custom validator to all stringsmongoose.Schema.Types.String.set('validate',v=>v ==null|| v >0);constuserSchema =newSchema({name:String,email:String});constUser= db.model('User', userSchema);constuser =newUser({name:'',email:''});consterr =awaituser.validate().then(() =>null,err=>err);
err.errors['name'];// ValidatorErrorerr.errors['email'];// ValidatorError
```


## Required Validators On Nested Objects

[Required Validators On Nested Objects](#required-validators-on-nested-objects)


Defining validators on nested objects in mongoose is tricky, because
nested objects are not fully fledged paths.


```javascript
letpersonSchema =newSchema({name: {first:String,last:String}
});

assert.throws(function() {// This throws an error, because 'name' isn't a full fledged pathpersonSchema.path('name').required(true);
},/Cannot.*'required'/);// To make a nested object required, use a single nested schemaconstnameSchema =newSchema({first:String,last:String});

personSchema =newSchema({name: {type: nameSchema,required:true}
});constPerson= db.model('Person', personSchema);constperson =newPerson();consterror = person.validateSync();
assert.ok(error.errors['name']);
```


## Update Validators

[Update Validators](#update-validators)


In the above examples, you learned about document validation. Mongoose also
supports validation forupdate(),updateOne(),updateMany(),
andfindOneAndUpdate()operations.
Update validators are off by default - you need to specify
therunValidatorsoption.

[update()](api/query.html#query_Query-update)

`update()`
[updateOne()](api/query.html#query_Query-updateOne)

`updateOne()`
[updateMany()](api/query.html#query_Query-updateMany)

`updateMany()`
[findOneAndUpdate()](api/query.html#query_Query-findOneAndUpdate)

`findOneAndUpdate()`
`runValidators`

To turn on update validators, set therunValidatorsoption forupdate(),updateOne(),updateMany(), orfindOneAndUpdate().
Be careful: update validators are off by default because they have several
caveats.

`runValidators`
`update()`
`updateOne()`
`updateMany()`
`findOneAndUpdate()`

```javascript
consttoySchema =newSchema({color:String,name:String});constToy= db.model('Toys', toySchema);Toy.schema.path('color').validate(function(value) {return/red|green|blue/i.test(value);
},'Invalid color');constopts = {runValidators:true};leterror;try{awaitToy.updateOne({}, {color:'not a color'}, opts);
}catch(err) {
  error = err;
}

assert.equal(error.errors.color.message,'Invalid color');
```


## Update Validators andthis

[Update Validators andthis](#update-validators-and-code>this</code>)

`this`

There are a couple of key differences between update validators and
document validators. In the color validation function below,thisrefers
to the document being validated when using document validation.
However, when running update validators,thisrefers to the query object instead of the document.
Because queries have a neat.get()function, you can get the updated value of the property you want.

`this`
`this`
`.get()`

```javascript
consttoySchema =newSchema({color:String,name:String});

toySchema.path('color').validate(function(value) {// When running in `validate()` or `validateSync()`, the// validator can access the document using `this`.// When running with update validators, `this` is the Query,// **not** the document being updated!// Queries have a `get()` method that lets you get the// updated value.if(this.get('name') &&this.get('name').toLowerCase().indexOf('red') !== -1) {returnvalue ==='red';
  }returntrue;
});constToy= db.model('ActionFigure', toySchema);consttoy =newToy({color:'green',name:'Red Power Ranger'});// Validation failed: color: Validator failed for path `color` with value `green`leterror = toy.validateSync();
assert.ok(error.errors['color']);constupdate = {color:'green',name:'Red Power Ranger'};constopts = {runValidators:true};

error =null;try{awaitToy.updateOne({}, update, opts);
}catch(err) {
  error = err;
}// Validation failed: color: Validator failed for path `color` with value `green`assert.ok(error);
```


## Update Validators Only Run On Updated Paths

[Update Validators Only Run On Updated Paths](#update-validators-only-run-on-updated-paths)


The other key difference is that update validators only run on the paths
specified in the update. For instance, in the below example, because
'name' is not specified in the update operation, update validation will
succeed.


When using update validators,requiredvalidatorsonlyfail when
you try to explicitly$unsetthe key.

`required`
`$unset`

```javascript
constkittenSchema =newSchema({name: {type:String,required:true},age:Number});constKitten= db.model('Kitten', kittenSchema);constupdate = {color:'blue'};constopts = {runValidators:true};// Operation succeeds despite the fact that 'name' is not specifiedawaitKitten.updateOne({}, update, opts);constunset = {$unset: {name:1} };// Operation fails because 'name' is requiredconsterr =awaitKitten.updateOne({}, unset, opts).then(() =>null,err=>err);
assert.ok(err);
assert.ok(err.errors['name']);
```


## Update Validators Only Run For Some Operations

[Update Validators Only Run For Some Operations](#update-validators-only-run-for-some-operations)


One final detail worth noting: update validatorsonlyrun on the
following update operators:


$set$unset$push$addToSet$pull$pullAll

- $set

`$set`
- $unset

`$unset`
- $push

`$push`
- $addToSet

`$addToSet`
- $pull

`$pull`
- $pullAll

`$pullAll`

For instance, the below update will succeed, regardless of the value ofnumber, because update validators ignore$inc.

`number`
`$inc`

Also,$push,$addToSet,$pull, and$pullAllvalidation doesnotrun any validation on the array itself, only individual elements
of the array.

`$push`
`$addToSet`
`$pull`
`$pullAll`

```javascript
consttestSchema =newSchema({number: {type:Number,max:0},arr: [{message: {type:String,maxlength:10} }]
});// Update validators won't check this, so you can still `$push` 2 elements// onto the array, so long as they don't have a `message` that's too long.testSchema.path('arr').validate(function(v) {returnv.length<2;
});constTest= db.model('Test', testSchema);letupdate = {$inc: {number:1} };constopts = {runValidators:true};// There will never be a validation error hereawaitTest.updateOne({}, update, opts);// This will never error either even though the array will have at// least 2 elements.update = {$push: [{message:'hello'}, {message:'world'}] };awaitTest.updateOne({}, update, opts);
```


## Next Up

[Next Up](#next-up)


Now that we've coveredValidation, let's take a look atMiddleware.

`Validation`
[Middleware](middleware.html)


[Source](https://mongoosejs.com/docs/validation.html#the-unique-option-is-not-a-validator)