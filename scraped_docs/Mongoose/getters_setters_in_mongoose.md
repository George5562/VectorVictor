# Getters/Setters in Mongoose


# Getters/Setters in Mongoose

[Getters/Setters in Mongoose](#getterssetters-in-mongoose)


Mongoose getters and setters allow you to execute custom logic when getting or setting a property on aMongoose document. Getters let you transform data in MongoDB into a more user friendly form, and setters let you transform user data before it gets to MongoDB.

[Mongoose document](../documents.html)


## Getters

[Getters](#getters)


Suppose you have aUsercollection and you want to obfuscate user emails to protect your users' privacy. Below is a basicuserSchemathat obfuscates the user's email address.

`User`
`userSchema`

```javascript
constuserSchema =newSchema({email: {type:String,get: obfuscate
  }
});// Mongoose passes the raw value in MongoDB `email` to the getterfunctionobfuscate(email) {constseparatorIndex = email.indexOf('@');if(separatorIndex <3) {// 'ab@gmail.com' -> '**@gmail.com'returnemail.slice(0, separatorIndex).replace(/./g,'*') +
      email.slice(separatorIndex);
  }// 'test42@gmail.com' -> 'te****@gmail.com'returnemail.slice(0,2) +
    email.slice(2, separatorIndex).replace(/./g,'*') +
    email.slice(separatorIndex);
}constUser= mongoose.model('User', userSchema);constuser =newUser({email:'ab@gmail.com'});
user.email;// **@gmail.com
```


Keep in mind that getters donotimpact the underlying data stored in
MongoDB. If you saveuser, theemailproperty will be 'ab@gmail.com' in
the database.

`user`
`email`
[ab@gmail.com](mailto:ab@gmail.com)


By default, Mongoose doesnotexecute getters when converting a document to JSON, includingExpress'res.json()function.

[Express'res.json()function](http://expressjs.com/en/4x/api.html#res.json)

`res.json()`

```javascript
app.get(function(req, res) {returnUser.findOne().// The `email` getter will NOT run herethen(doc=>res.json(doc)).catch(err=>res.status(500).json({message: err.message}));
});
```


To run getters when converting a document to JSON, set thetoJSON.gettersoption totruein your schemaas shown below.

[toJSON.gettersoption totruein your schema](../guide.html#toJSON)

`toJSON.getters`
`true`

```javascript
constuserSchema =newSchema({email: {type:String,get: obfuscate
  }
}, {toJSON: {getters:true} });// Or, globallymongoose.set('toJSON', {getters:true});// Or, on a one-off basisapp.get(function(req, res) {returnUser.findOne().// The `email` getter will run herethen(doc=>res.json(doc.toJSON({getters:true}))).catch(err=>res.status(500).json({message: err.message}));
});
```


To skip getters on a one-off basis, useuser.get()with thegettersoption set tofalseas shown below.

[user.get()with thegettersoption set tofalse](../api/document.html#document_Document-get)

`user.get()`
`getters`
`false`

```javascript
user.get('email',null, {getters:false});// 'ab@gmail.com'
```


## Setters

[Setters](#setters)


Suppose you want to make sure all user emails in your database are lowercased to
make it easy to search without worrying about case. Below is an exampleuserSchemathat ensures emails are lowercased.

`userSchema`

```javascript
constuserSchema =newSchema({email: {type:String,set:v=>v.toLowerCase()
  }
});constUser= mongoose.model('User', userSchema);constuser =newUser({email:'TEST@gmail.com'});
user.email;// 'test@gmail.com'// The raw value of `email` is lowercaseduser.get('email',null, {getters:false});// 'test@gmail.com'user.set({email:'NEW@gmail.com'});
user.email;// 'new@gmail.com'
```


Mongoose also runs setters on update operations, likeupdateOne(). Mongoose willupsert a documentwith a
lowercasedemailin the below example.

[updateOne()](../api/query.html#query_Query-updateOne)

`updateOne()`
[upsert a document](https://masteringjs.io/tutorials/mongoose/upsert)

`email`

```javascript
awaitUser.updateOne({}, {email:'TEST@gmail.com'}, {upsert:true});constdoc =awaitUser.findOne();
doc.email;// 'test@gmail.com'
```


In a setter function,thiscan be either the document being set or the query
being run. If you don't want your setter to run when you callupdateOne(),
you add an if statement that checks ifthisis a Mongoose document as shown
below.

`this`
`updateOne()`
`this`

```javascript
constuserSchema =newSchema({email: {type:String,set: toLower
  }
});functiontoLower(email) {// Don't transform `email` if using `updateOne()` or `updateMany()`if(!(thisinstanceofmongoose.Document)) {returnemail;
  }returnemail.toLowerCase();
}constUser= mongoose.model('User', userSchema);awaitUser.updateOne({}, {email:'TEST@gmail.com'}, {upsert:true});constdoc =awaitUser.findOne();
doc.email;// 'TEST@gmail.com'
```


## Passing Parameters using$locals

[Passing Parameters using$locals](#passing-parameters-using-code>$locals</code>)

`$locals`

You can't pass parameters to your getter and setter functions like you do to normal function calls.
To configure or pass additional properties to your getters and setters, you can use the document's$localsproperty.

`$locals`

The$localsproperty is the preferred place to store any program-defined data on your document without conflicting with schema-defined properties.
In your getter and setter functions,thisis the document being accessed, so you set properties on$localsand then access those properties in your getters examples.
For example, the following shows how you can use$localsto configure the language for a custom getter that returns a string in different languages.

`$locals`
`this`
`$locals`
`$locals`

```javascript
constinternationalizedStringSchema =newSchema({en:String,es:String});constingredientSchema =newSchema({// Instead of setting `name` to just a string, set `name` to a map// of language codes to strings.name: {type: internationalizedStringSchema,// When you access `name`, pull the document's localeget:function(value) {returnvalue[this.$locals.language||'en'];
    }
  }
});constrecipeSchema =newSchema({ingredients: [{type: mongoose.ObjectId,ref:'Ingredient'}]
});constIngredient= mongoose.model('Ingredient', ingredientSchema);constRecipe= mongoose.model('Recipe', recipeSchema);// Create some sample dataconst{ _id } =awaitIngredient.create({name: {en:'Eggs',es:'Huevos'}
});awaitRecipe.create({ingredients: [_id] });// Populate with setting `$locals.language` for internationalizationconstlanguage ='es';constrecipes =awaitRecipe.find().populate({path:'ingredients',transform:function(doc) {
    doc.$locals.language= language;returndoc;
  }
});// Gets the ingredient's name in Spanish `name.es`assert.equal(recipes[0].ingredients[0].name,'Huevos');// 'Huevos'
```


## Differences vs ES6 Getters/Setters

[Differences vs ES6 Getters/Setters](#differences-vs-es6-getterssetters)


Mongoose setters are different fromES6 settersbecause they allow you to transform the value being set. With ES6 setters, you
would need to store an internal_emailproperty to use a setter. With Mongoose,
you donotneed to define an internal_emailproperty or define a
corresponding getter foremail.

[ES6 setters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)

`_email`
`_email`
`email`

```javascript
classUser{// This won't convert the email to lowercase! That's because `email`// is just a setter, the actual `email` property doesn't store any data.// also eslint will warn about using "return" on a settersetemail(v) {// eslint-disable-next-line no-setter-returnreturnv.toLowerCase();
  }
}constuser =newUser();
user.email='TEST@gmail.com';

user.email;// undefined
```


[Source](https://mongoosejs.com/docs/tutorials/getters-setters.html)