# Getting Started


# Getting Started

[Getting Started](#getting-started)


First be sure you haveMongoDBandNode.jsinstalled.

[MongoDB](https://www.mongodb.com/try/download/community)

[Node.js](http://nodejs.org/en/download)


Next install Mongoose from the command line usingnpm:

`npm`

```javascript
npm install mongoose --save
```


Now say we like fuzzy kittens and want to record every kitten we ever meet
in MongoDB.
The first thing we need to do is include mongoose in our project and open a
connection to thetestdatabase on our locally running instance of MongoDB.

`test`

```javascript
// getting-started.jsconstmongoose =require('mongoose');main().catch(err=>console.log(err));asyncfunctionmain() {awaitmongoose.connect('mongodb://127.0.0.1:27017/test');// use `await mongoose.connect('mongodb://user:password@127.0.0.1:27017/test');` if your database has auth enabled}
```


For brevity, let's assume that all following code is within themain()function.

`main()`

With Mongoose, everything is derived from aSchema.
Let's get a reference to it and define our kittens.

[Schema](guide.html)


```javascript
constkittySchema =newmongoose.Schema({name:String});
```


So far so good. We've got a schema with one property,name, which will be aString. The next step is compiling our schema into aModel.

`name`
`String`
[Model](models.html)


```javascript
constKitten= mongoose.model('Kitten', kittySchema);
```


A model is a class with which we construct documents.
In this case, each document will be a kitten with properties and behaviors as declared in our schema.
Let's create a kitten document representing the little guy we just met on the sidewalk outside:


```javascript
constsilence =newKitten({name:'Silence'});console.log(silence.name);// 'Silence'
```


Kittens can meow, so let's take a look at how to add "speak" functionality
to our documents:


```javascript
//NOTE:methods must be added to the schema before compiling it with mongoose.model()kittySchema.methods.speak=functionspeak() {constgreeting =this.name?'Meow name is '+this.name:'I don\'t have a name';console.log(greeting);
};constKitten= mongoose.model('Kitten', kittySchema);
```


Functions added to themethodsproperty of a schema get compiled into
theModelprototype and exposed on each document instance:

`methods`
`Model`

```javascript
constfluffy =newKitten({name:'fluffy'});
fluffy.speak();// "Meow name is fluffy"
```


We have talking kittens! But we still haven't saved anything to MongoDB.
Each document can be saved to the database by calling itssavemethod. The first argument to the callback will be an error if any occurred.

[save](api/model.html#model_Model-save)


```javascript
awaitfluffy.save();
fluffy.speak();
```


Say time goes by and we want to display all the kittens we've seen.
We can access all of the kitten documents through our Kittenmodel.

[model](models.html)


```javascript
constkittens =awaitKitten.find();console.log(kittens);
```


We just logged all of the kittens in our db to the console.
If we want to filter our kittens by name, Mongoose supports MongoDBs richqueryingsyntax.

[querying](queries.html)


```javascript
awaitKitten.find({name:/^fluff/});
```


This performs a search for all documents with a name property that begins
with "fluff" and returns the result as an array of kittens to the callback.


## Congratulations

[Congratulations](#congratulations)


That's the end of our quick start. We created a schema, added a custom document method, saved and queried kittens in MongoDB using Mongoose. Head over to theguide, orAPI docsfor more.

[guide](guide.html)

[API docs](api/mongoose.html)


[Source](https://mongoosejs.com/docs/index.html)