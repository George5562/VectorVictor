# Change Streams


# Change Streams

[Change Streams](#change-streams)


Change streamslet you listen for updates to documents in a given model's collection, or even documents in an entire database.
Unlikemiddleware, change streams are a MongoDB server construct, which means they pick up changes from anywhere.
Even if you update a document from a MongoDB GUI, your Mongoose change stream will be notified.

[Change streams](https://www.mongodb.com/developer/languages/javascript/nodejs-change-streams-triggers/)

[middleware](middleware.html)


Thewatch()function creates a change stream.
Change streams emit a'data'event when a document is updated.

`watch()`
`'data'`

```javascript
constPerson= mongoose.model('Person',newmongoose.Schema({name:String}));// Create a change stream. The 'change' event gets emitted when there's a// change in the database. Print what the change stream emits.Person.watch().on('change',data=>console.log(data));// Insert a doc, will trigger the change stream handler aboveawaitPerson.create({name:'Axl Rose'});
```


The above script will print output that looks like:


```javascript
{_id: {_data:'8262408DAC000000012B022C0100296E5A10042890851837DB4792BE6B235E8B85489F46645F6964006462408DAC6F5C42FF5EE087A20004'},operationType:'insert',clusterTime:newTimestamp({t:1648397740,i:1}),fullDocument: {_id:newObjectId("62408dac6f5c42ff5ee087a2"),name:'Axl Rose',__v:0},ns: {db:'test',coll:'people'},documentKey: {_id:newObjectId("62408dac6f5c42ff5ee087a2") }
}
```


Note that youmustbe connected to a MongoDB replica set or sharded cluster to use change streams.
If you try to callwatch()when connected to a standalone MongoDB server, you'll get the below error.

`watch()`

If you're usingwatch()in production, we recommend usingMongoDB Atlas.
For local development, we recommendmongodb-memory-serverorrun-rsto start a replica set locally.

`watch()`
[MongoDB Atlas](https://www.mongodb.com/atlas/database)

[mongodb-memory-server](https://www.npmjs.com/package/mongodb-memory-server)

[run-rs](https://www.npmjs.com/package/run-rs)


## Iterating usingnext()

[Iterating usingnext()](#iterating-using-code>next()</code>)

`next()`

If you want to iterate through a change stream in aAWS Lambda function, donotuse event emitters to listen to the change stream.
You need to make sure you close your change stream when your Lambda function is done executing, because your change stream may end up in an inconsistent state if Lambda stops your container while the change stream is pulling data from MongoDB.

[AWS Lambda function](lambda.html)


Change streams also have anext()function that lets you explicitly wait for the next change to come in.
UseresumeAfterto track where the last change stream left off, and add a timeout to make sure your handler doesn't wait forever if no changes come in.

`next()`
`resumeAfter`

```javascript
letresumeAfter =undefined;exports.handler=async(event, context) => {// add this so that we can re-use any static/global variables between function calls if Lambda// happens to re-use existing containers for the invocation.context.callbackWaitsForEmptyEventLoop=false;awaitconnectToDatabase();constchangeStream =awaitCountry.watch([], { resumeAfter });// Change stream `next()` will wait forever if there are no changes. So make sure to// stop listening to the change stream after a fixed period of time.consttimeoutPromise =newPromise(resolve=>setTimeout(() =>resolve(false),1000));letdoc =null;while(doc =awaitPromise.race([changeStream.next(), timeoutPromise])) {console.log('Got', doc);
  }// `resumeToken` tells you where the change stream left off, so next function instance// can pick up any changes that happened in the meantime.resumeAfter = changeStream.resumeToken;awaitchangeStream.close();
};
```


[Source](https://mongoosejs.com/docs/change-streams.html)