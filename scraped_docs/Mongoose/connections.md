# Connections


# Connections

[Connections](#connections)


You can connect to MongoDB with themongoose.connect()method.

`mongoose.connect()`

```javascript
mongoose.connect('mongodb://127.0.0.1:27017/myapp');
```


This is the minimum needed to connect themyappdatabase running locally on the default port (27017).
For local MongoDB databases, we recommend using127.0.0.1instead oflocalhost.
That is because Node.js 18 and up prefer IPv6 addresses, which means, on many machines, Node.js will resolvelocalhostto the IPv6 address::1and Mongoose will be unable to connect, unless the mongodb instance is running with ipv6 enabled.

`myapp`
`127.0.0.1`
`localhost`
`localhost`
`::1`

You can also specify several more parameters in theuri:

`uri`

```javascript
mongoose.connect('mongodb://username:password@host:port/database?options...');
```


See themongodb connection string specfor more details.

[mongodb connection string spec](http://www.mongodb.com/docs/manual/reference/connection-string/)


BufferingError HandlingOptionsserverSelectionTimeoutMSConnection String OptionsConnection EventsA note about keepAliveServer SelectionReplica Set ConnectionsReplica Set Host NamesMulti-mongos supportMultiple connectionsConnection PoolsMulti Tenant Connections

- Buffering

- Error Handling

- Options

- serverSelectionTimeoutMS

- Connection String Options

- Connection Events

- A note about keepAlive

- Server Selection

- Replica Set Connections

- Replica Set Host Names

- Multi-mongos support

- Multiple connections

- Connection Pools

- Multi Tenant Connections


## Operation Buffering

[Operation Buffering](#buffering)


Mongoose lets you start using your models immediately, without waiting for
mongoose to establish a connection to MongoDB.


```javascript
mongoose.connect('mongodb://127.0.0.1:27017/myapp');constMyModel= mongoose.model('Test',newSchema({name:String}));// WorksawaitMyModel.findOne();
```


That's because mongoose buffers model function calls internally. This
buffering is convenient, but also a common source of confusion. Mongoose
willnotthrow any errors by default if you use a model without
connecting.


```javascript
constMyModel= mongoose.model('Test',newSchema({name:String}));constpromise =MyModel.findOne();setTimeout(function() {
  mongoose.connect('mongodb://127.0.0.1:27017/myapp');
},60000);// Will just hang until mongoose successfully connectsawaitpromise;
```


To disable buffering, turn off thebufferCommandsoption on your schema.
If you havebufferCommandson and your connection is hanging, try turningbufferCommandsoff to see if you haven't opened a connection properly.
You can also disablebufferCommandsglobally:

[bufferCommandsoption on your schema](guide.html#bufferCommands)

`bufferCommands`
`bufferCommands`
`bufferCommands`
`bufferCommands`

```javascript
mongoose.set('bufferCommands',false);
```


Note that buffering is also responsible for waiting until Mongoose
creates collections if you use theautoCreateoption.
If you disable buffering, you should also disable theautoCreateoption and usecreateCollection()to createcapped collectionsorcollections with collations.

[autoCreateoption](guide.html#autoCreate)

`autoCreate`
`autoCreate`
[createCollection()](api/model.html#model_Model-createCollection)

`createCollection()`
[capped collections](guide.html#capped)

[collections with collations](guide.html#collation)


```javascript
constschema =newSchema({name:String}, {capped: {size:1024},bufferCommands:false,autoCreate:false// disable `autoCreate` since `bufferCommands` is false});constModel= mongoose.model('Test', schema);// Explicitly create the collection before using it// so the collection is capped.awaitModel.createCollection();
```


## Error Handling

[Error Handling](#error-handling)


There are two classes of errors that can occur with a Mongoose connection.


Error on initial connection: If initial connection fails, Mongoose will emit an 'error' event and the promisemongoose.connect()returns will reject. However, Mongoose willnotautomatically try to reconnect.Error after initial connection was established: Mongoose will attempt to reconnect, and it will emit an 'error' event.

- Error on initial connection: If initial connection fails, Mongoose will emit an 'error' event and the promisemongoose.connect()returns will reject. However, Mongoose willnotautomatically try to reconnect.

`mongoose.connect()`
- Error after initial connection was established: Mongoose will attempt to reconnect, and it will emit an 'error' event.


To handle initial connection errors, you should use.catch()ortry/catchwith async/await.

`.catch()`
`try/catch`

```javascript
mongoose.connect('mongodb://127.0.0.1:27017/test').catch(error=>handleError(error));// Or:try{awaitmongoose.connect('mongodb://127.0.0.1:27017/test');
}catch(error) {handleError(error);
}
```


To handle errors after initial connection was established, you should
listen for error events on the connection. However, you still need to
handle initial connection errors as shown above.


```javascript
mongoose.connection.on('error',err=>{logError(err);
});
```


Note that Mongoose does not necessarily emit an 'error' event if it loses connectivity to MongoDB. You should
listen to thedisconnectedevent to report when Mongoose is disconnected from MongoDB.

`disconnected`

## Options

[Options](#options)


Theconnectmethod also accepts anoptionsobject which will be passed
on to the underlying MongoDB driver.

`connect`
`options`

```javascript
mongoose.connect(uri, options);
```


A full list of options can be found on theMongoDB Node.js driver docs forMongoClientOptions.
Mongoose passes options to the driver without modification, modulo a few
exceptions that are explained below.

[MongoDB Node.js driver docs forMongoClientOptions](https://mongodb.github.io/node-mongodb-native/4.2/interfaces/MongoClientOptions.html)

`MongoClientOptions`

bufferCommands- This is a mongoose-specific option (not passed to the MongoDB driver) that disablesMongoose's buffering mechanismuser/pass- The username and password for authentication. These options are Mongoose-specific, they are equivalent to the MongoDB driver'sauth.usernameandauth.passwordoptions.autoIndex- By default, mongoose will automatically build indexes defined in your schema when it connects. This is great for development, but not ideal for large production deployments, because index builds can cause performance degradation. If you setautoIndexto false, mongoose will not automatically build indexes foranymodel associated with this connection.dbName- Specifies which database to connect to and overrides any database specified in the connection string. This is useful if you are unable to specify a default database in the connection string like withsomemongodb+srvsyntax connections.

- bufferCommands- This is a mongoose-specific option (not passed to the MongoDB driver) that disablesMongoose's buffering mechanism

`bufferCommands`
- user/pass- The username and password for authentication. These options are Mongoose-specific, they are equivalent to the MongoDB driver'sauth.usernameandauth.passwordoptions.

`user`
`pass`
`auth.username`
`auth.password`
- autoIndex- By default, mongoose will automatically build indexes defined in your schema when it connects. This is great for development, but not ideal for large production deployments, because index builds can cause performance degradation. If you setautoIndexto false, mongoose will not automatically build indexes foranymodel associated with this connection.

`autoIndex`
`autoIndex`
- dbName- Specifies which database to connect to and overrides any database specified in the connection string. This is useful if you are unable to specify a default database in the connection string like withsomemongodb+srvsyntax connections.

`dbName`
`mongodb+srv`

Below are some of the options that are important for tuning Mongoose.


promiseLibrary- Sets theunderlying driver's promise library.maxPoolSize- The maximum number of sockets the MongoDB driver will keep open for this connection. By default,maxPoolSizeis 100. Keep in mind that MongoDB only allows one operation per socket at a time, so you may want to increase this if you find you have a few slow queries that are blocking faster queries from proceeding. SeeSlow Trains in MongoDB and Node.js. You may want to decreasemaxPoolSizeif you are running intoconnection limits.minPoolSize- The minimum number of sockets the MongoDB driver will keep open for this connection. The MongoDB driver may close sockets that have been inactive for some time. You may want to increaseminPoolSizeif you expect your app to go through long idle times and want to make sure your sockets stay open to avoid slow trains when activity picks up.socketTimeoutMS- How long the MongoDB driver will wait before killing a socket due to inactivityafter initial connection. A socket may be inactive because of either no activity or a long-running operation.socketTimeoutMSdefaults to 0, which means Node.js will not time out the socket due to inactivity. This option is passed toNode.jssocket#setTimeout()functionafter the MongoDB driver successfully completes.family- Whether to connect using IPv4 or IPv6. This option passed toNode.js'dns.lookup()function. If you don't specify this option, the MongoDB driver will try IPv6 first and then IPv4 if IPv6 fails. If yourmongoose.connect(uri)call takes a long time, trymongoose.connect(uri, { family: 4 })authSource- The database to use when authenticating withuserandpass. In MongoDB,users are scoped to a database. If you are getting an unexpected login failure, you may need to set this option.serverSelectionTimeoutMS- The MongoDB driver will try to find a server to send any given operation to, and keep retrying forserverSelectionTimeoutMSmilliseconds. If not set, the MongoDB driver defaults to using30000(30 seconds).heartbeatFrequencyMS- The MongoDB driver sends a heartbeat everyheartbeatFrequencyMSto check on the status of the connection. A heartbeat is subject toserverSelectionTimeoutMS, so the MongoDB driver will retry failed heartbeats for up to 30 seconds by default. Mongoose only emits a'disconnected'event after a heartbeat has failed, so you may want to decrease this setting to reduce the time between when your server goes down and when Mongoose emits'disconnected'. We recommend you donotset this setting below 1000, too many heartbeats can lead to performance degradation.

- promiseLibrary- Sets theunderlying driver's promise library.

`promiseLibrary`
- maxPoolSize- The maximum number of sockets the MongoDB driver will keep open for this connection. By default,maxPoolSizeis 100. Keep in mind that MongoDB only allows one operation per socket at a time, so you may want to increase this if you find you have a few slow queries that are blocking faster queries from proceeding. SeeSlow Trains in MongoDB and Node.js. You may want to decreasemaxPoolSizeif you are running intoconnection limits.

`maxPoolSize`
`maxPoolSize`
`maxPoolSize`
- minPoolSize- The minimum number of sockets the MongoDB driver will keep open for this connection. The MongoDB driver may close sockets that have been inactive for some time. You may want to increaseminPoolSizeif you expect your app to go through long idle times and want to make sure your sockets stay open to avoid slow trains when activity picks up.

`minPoolSize`
`minPoolSize`
- socketTimeoutMS- How long the MongoDB driver will wait before killing a socket due to inactivityafter initial connection. A socket may be inactive because of either no activity or a long-running operation.socketTimeoutMSdefaults to 0, which means Node.js will not time out the socket due to inactivity. This option is passed toNode.jssocket#setTimeout()functionafter the MongoDB driver successfully completes.

`socketTimeoutMS`
`socketTimeoutMS`
`socket#setTimeout()`
- family- Whether to connect using IPv4 or IPv6. This option passed toNode.js'dns.lookup()function. If you don't specify this option, the MongoDB driver will try IPv6 first and then IPv4 if IPv6 fails. If yourmongoose.connect(uri)call takes a long time, trymongoose.connect(uri, { family: 4 })

`family`
`dns.lookup()`
`mongoose.connect(uri)`
`mongoose.connect(uri, { family: 4 })`
- authSource- The database to use when authenticating withuserandpass. In MongoDB,users are scoped to a database. If you are getting an unexpected login failure, you may need to set this option.

`authSource`
`user`
`pass`
- serverSelectionTimeoutMS- The MongoDB driver will try to find a server to send any given operation to, and keep retrying forserverSelectionTimeoutMSmilliseconds. If not set, the MongoDB driver defaults to using30000(30 seconds).

`serverSelectionTimeoutMS`
`serverSelectionTimeoutMS`
`30000`
- heartbeatFrequencyMS- The MongoDB driver sends a heartbeat everyheartbeatFrequencyMSto check on the status of the connection. A heartbeat is subject toserverSelectionTimeoutMS, so the MongoDB driver will retry failed heartbeats for up to 30 seconds by default. Mongoose only emits a'disconnected'event after a heartbeat has failed, so you may want to decrease this setting to reduce the time between when your server goes down and when Mongoose emits'disconnected'. We recommend you donotset this setting below 1000, too many heartbeats can lead to performance degradation.

`heartbeatFrequencyMS`
`heartbeatFrequencyMS`
`serverSelectionTimeoutMS`
`'disconnected'`
`'disconnected'`

## serverSelectionTimeoutMS

[serverSelectionTimeoutMS](#serverselectiontimeoutms)


TheserverSelectionTimeoutMSoption is extremely important: it controls how long the MongoDB Node.js driver will attempt to retry any operation before erroring out.
This includes initial connection, likeawait mongoose.connect(), as well as any operations that make requests to MongoDB, likesave()orfind().

`serverSelectionTimeoutMS`
`await mongoose.connect()`
`save()`
`find()`

By default,serverSelectionTimeoutMSis 30000 (30 seconds).
This means that, for example, if you callmongoose.connect()when your standalone MongoDB server is down, yourmongoose.connect()call will only throw an error after 30 seconds.

`serverSelectionTimeoutMS`
`mongoose.connect()`
`mongoose.connect()`

```javascript
// Throws an error "getaddrinfo ENOTFOUND doesnt.exist" after 30 secondsawaitmongoose.connect('mongodb://doesnt.exist:27017/test');
```


Similarly, if your standalone MongoDB server goes down after initial connection, anyfind()orsave()calls will error out after 30 seconds, unless your MongoDB server is restarted.

`find()`
`save()`

While 30 seconds seems like a long time,serverSelectionTimeoutMSmeans you're unlikely to see any interruptions during areplica set failover.
If you lose your replica set primary, the MongoDB Node driver will ensure that any operations you send during the replica set election will eventually execute, assuming that the replica set election takes less thanserverSelectionTimeoutMS.

`serverSelectionTimeoutMS`
[replica set failover](https://www.mongodb.com/docs/manual/replication/#automatic-failover)

`serverSelectionTimeoutMS`

To get faster feedback on failed connections, you can reduceserverSelectionTimeoutMSto 5000 as follows.
We don't recommend reducingserverSelectionTimeoutMSunless you are running a standalone MongoDB server rather than a replica set, or unless you are using a serverless runtime likeAWS Lambda.

`serverSelectionTimeoutMS`
`serverSelectionTimeoutMS`
[AWS Lambda](lambda.html)


```javascript
mongoose.connect(uri, {serverSelectionTimeoutMS:5000});
```


There is no way to tuneserverSelectionTimeoutMSindependently formongoose.connect()vs for queries.
If you want to reduceserverSelectionTimeoutMSfor queries and other operations, but still retrymongoose.connect()for longer, you are responsible for retrying theconnect()calls yourself using aforloop ora tool like p-retry.

`serverSelectionTimeoutMS`
`mongoose.connect()`
`serverSelectionTimeoutMS`
`mongoose.connect()`
`connect()`
`for`
[a tool like p-retry](https://github.com/Automattic/mongoose/issues/12967#issuecomment-1411227968)


```javascript
constserverSelectionTimeoutMS =5000;// Prints "Failed 0", "Failed 1", "Failed 2" and then throws an// error. Exits after approximately 15 seconds.for(leti =0; i <3; ++i) {try{awaitmongoose.connect('mongodb://doesnt.exist:27017/test', {
      serverSelectionTimeoutMS
    });break;
  }catch(err) {console.log('Failed', i);if(i >=2) {throwerr;
    }
  }
}
```


## Callback

[Callback](#callback)


Theconnect()function also accepts a callback parameter and returns apromise.

`connect()`
[promise](promises.html)


```javascript
mongoose.connect(uri, options,function(error) {// Check error in initial connection. There is no 2nd param to the callback.});// Or using promisesmongoose.connect(uri, options).then(() =>{/** ready to use. The `mongoose.connect()` promise resolves to mongoose instance. */},err=>{/** handle initial connection error */}
);
```


## Connection String Options

[Connection String Options](#connection-string-options)


You can also specify driver options in your connection string asparameters in the query stringportion of the URI. This only applies to options passed to the MongoDB
driver. Youcan'tset Mongoose-specific options likebufferCommandsin the query string.

[parameters in the query string](https://en.wikipedia.org/wiki/Query_string)

`bufferCommands`

```javascript
mongoose.connect('mongodb://127.0.0.1:27017/test?socketTimeoutMS=1000&bufferCommands=false&authSource=otherdb');// The above is equivalent to:mongoose.connect('mongodb://127.0.0.1:27017/test', {socketTimeoutMS:1000// Note that mongoose will **not** pull `bufferCommands` from the query string});
```


The disadvantage of putting options in the query string is that query
string options are harder to read. The advantage is that you only need a
single configuration option, the URI, rather than separate options forsocketTimeoutMS, etc. Best practice is to put options
that likely differ between development and production, likereplicaSetorssl, in the connection string, and options that should remain constant,
likesocketTimeoutMSormaxPoolSize, in the options object.

`socketTimeoutMS`
`replicaSet`
`ssl`
`socketTimeoutMS`
`maxPoolSize`

The MongoDB docs have a full list ofsupported connection string options.
Below are some options that are often useful to set in the connection string because they
are closely associated with the hostname and authentication information.

[supported connection string options](https://www.mongodb.com/docs/manual/reference/connection-string/)


authSource- The database to use when authenticating withuserandpass. In MongoDB,users are scoped to a database. If you are getting an unexpected login failure, you may need to set this option.family- Whether to connect using IPv4 or IPv6. This option passed toNode.js'dns.lookup()function. If you don't specify this option, the MongoDB driver will try IPv6 first and then IPv4 if IPv6 fails. If yourmongoose.connect(uri)call takes a long time, trymongoose.connect(uri, { family: 4 })

- authSource- The database to use when authenticating withuserandpass. In MongoDB,users are scoped to a database. If you are getting an unexpected login failure, you may need to set this option.

`authSource`
`user`
`pass`
- family- Whether to connect using IPv4 or IPv6. This option passed toNode.js'dns.lookup()function. If you don't specify this option, the MongoDB driver will try IPv6 first and then IPv4 if IPv6 fails. If yourmongoose.connect(uri)call takes a long time, trymongoose.connect(uri, { family: 4 })

`family`
`dns.lookup()`
`mongoose.connect(uri)`
`mongoose.connect(uri, { family: 4 })`

## Connection Events

[Connection Events](#connection-events)


Connections inherit fromNode.js'EventEmitterclass,
and emit events when something happens to the connection, like losing
connectivity to the MongoDB server. Below is a list of events that a
connection may emit.

[Node.js'EventEmitterclass](https://nodejs.org/api/events.html#events_class_eventemitter)

`EventEmitter`

connecting: Emitted when Mongoose starts making its initial connection to the MongoDB serverconnected: Emitted when Mongoose successfully makes its initial connection to the MongoDB server, or when Mongoose reconnects after losing connectivity. May be emitted multiple times if Mongoose loses connectivity.open: Emitted after'connected'andonOpenis executed on all of this connection's models. May be emitted multiple times if Mongoose loses connectivity.disconnecting: Your app calledConnection#close()to disconnect from MongoDB. This includes callingmongoose.disconnect(), which callsclose()on all connections.disconnected: Emitted when Mongoose lost connection to the MongoDB server. This event may be due to your code explicitly closing the connection, the database server crashing, or network connectivity issues.close: Emitted afterConnection#close()successfully closes the connection. If you callconn.close(), you'll get both a 'disconnected' event and a 'close' event.reconnected: Emitted if Mongoose lost connectivity to MongoDB and successfully reconnected. Mongoose attempts toautomatically reconnectwhen it loses connection to the database.error: Emitted if an error occurs on a connection, like aparseErrordue to malformed data or a payload larger than16MB.

- connecting: Emitted when Mongoose starts making its initial connection to the MongoDB server

`connecting`
- connected: Emitted when Mongoose successfully makes its initial connection to the MongoDB server, or when Mongoose reconnects after losing connectivity. May be emitted multiple times if Mongoose loses connectivity.

`connected`
- open: Emitted after'connected'andonOpenis executed on all of this connection's models. May be emitted multiple times if Mongoose loses connectivity.

`open`
`'connected'`
`onOpen`
- disconnecting: Your app calledConnection#close()to disconnect from MongoDB. This includes callingmongoose.disconnect(), which callsclose()on all connections.

`disconnecting`
`Connection#close()`
`mongoose.disconnect()`
`close()`
- disconnected: Emitted when Mongoose lost connection to the MongoDB server. This event may be due to your code explicitly closing the connection, the database server crashing, or network connectivity issues.

`disconnected`
- close: Emitted afterConnection#close()successfully closes the connection. If you callconn.close(), you'll get both a 'disconnected' event and a 'close' event.

`close`
`Connection#close()`
`conn.close()`
- reconnected: Emitted if Mongoose lost connectivity to MongoDB and successfully reconnected. Mongoose attempts toautomatically reconnectwhen it loses connection to the database.

`reconnected`
- error: Emitted if an error occurs on a connection, like aparseErrordue to malformed data or a payload larger than16MB.

`error`
`parseError`

When you're connecting to a single MongoDB server (a"standalone"), Mongoose will emitdisconnectedif it gets
disconnected from the standalone server, andconnectedif it successfully connects to the standalone. In areplica set, Mongoose will emitdisconnectedif it loses connectivity to the replica set primary, andconnectedif it manages to reconnect to the replica set primary.

["standalone"](https://www.mongodb.com/docs/cloud-manager/tutorial/deploy-standalone/)

`disconnected`
`connected`
[replica set](https://www.mongodb.com/docs/manual/replication/)

`disconnected`
`connected`

If you are usingmongoose.connect(), you can use the following to listen to the above events:

`mongoose.connect()`

```javascript
mongoose.connection.on('connected',() =>console.log('connected'));
mongoose.connection.on('open',() =>console.log('open'));
mongoose.connection.on('disconnected',() =>console.log('disconnected'));
mongoose.connection.on('reconnected',() =>console.log('reconnected'));
mongoose.connection.on('disconnecting',() =>console.log('disconnecting'));
mongoose.connection.on('close',() =>console.log('close'));

mongoose.connect('mongodb://127.0.0.1:27017/mongoose_test');
```


Withmongoose.createConnection(), use the following instead:

`mongoose.createConnection()`

```javascript
constconn = mongoose.createConnection('mongodb://127.0.0.1:27017/mongoose_test');

conn.on('connected',() =>console.log('connected'));
conn.on('open',() =>console.log('open'));
conn.on('disconnected',() =>console.log('disconnected'));
conn.on('reconnected',() =>console.log('reconnected'));
conn.on('disconnecting',() =>console.log('disconnecting'));
conn.on('close',() =>console.log('close'));
```


## A note about keepAlive

[A note about keepAlive](#keepAlive)


Before Mongoose 5.2.0, you needed to enable thekeepAliveoption to initiateTCP keepaliveto prevent"connection closed"errors.
However,keepAlivehas beentrueby default since Mongoose 5.2.0, and thekeepAliveis deprecated as of Mongoose 7.2.0.
Please removekeepAliveandkeepAliveInitialDelayoptions from your Mongoose connections.

`keepAlive`
[TCP keepalive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/overview.html)

`"connection closed"`
`keepAlive`
`true`
`keepAlive`
`keepAlive`
`keepAliveInitialDelay`

## Replica Set Connections

[Replica Set Connections](#replicaset_connections)


To connect to a replica set you pass a comma delimited list of hosts to
connect to rather than a single host.


```javascript
mongoose.connect('mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]'[, options]);
```


For example:


```javascript
mongoose.connect('mongodb://user:pw@host1.com:27017,host2.com:27017,host3.com:27017/testdb');
```


To connect to a single node replica set, specify thereplicaSetoption.

`replicaSet`

```javascript
mongoose.connect('mongodb://host1:port1/?replicaSet=rsName');
```


## Server Selection

[Server Selection](#server-selection)


The underlying MongoDB driver uses a process known asserver selectionto connect to MongoDB and send operations to MongoDB.
If the MongoDB driver can't find a server to send an operation to afterserverSelectionTimeoutMS,
you'll get the below error:

[server selection](https://github.com/mongodb/specifications/blob/master/source/server-selection/server-selection.rst)

`serverSelectionTimeoutMS`

You can configure the timeout using theserverSelectionTimeoutMSoption
tomongoose.connect():

`serverSelectionTimeoutMS`
`mongoose.connect()`

```javascript
mongoose.connect(uri, {serverSelectionTimeoutMS:5000// Timeout after 5s instead of 30s});
```


AMongoTimeoutErrorhas areasonproperty that explains why
server selection timed out. For example, if you're connecting to
a standalone server with an incorrect password,reasonwill contain an "Authentication failed" error.

`MongoTimeoutError`
`reason`
`reason`

```javascript
constmongoose =require('mongoose');consturi ='mongodb+srv://username:badpw@cluster0-OMITTED.mongodb.net/'+'test?retryWrites=true&w=majority';// Prints "MongoServerError: bad auth Authentication failed."mongoose.connect(uri, {serverSelectionTimeoutMS:5000}).catch(err=>console.log(err.reason));
```


## Replica Set Host Names

[Replica Set Host Names](#replicaset-hostnames)


MongoDB replica sets rely on being able to reliably figure out the domain name for each member.On Linux and OSX, the MongoDB server uses the output of thehostnamecommandto figure out the domain name to report to the replica set.
This can cause confusing errors if you're connecting to a remote MongoDB replica set running on a machine that reports itshostnameaslocalhost:

[hostnamecommand](https://linux.die.net/man/1/hostname)

`hostname`
`hostname`
`localhost`

```javascript
// Can get this error even if your connection string doesn't include
// `localhost` if `rs.conf()` reports that one replica set member has
// `localhost` as its host name.
MongooseServerSelectionError: connect ECONNREFUSED localhost:27017
```


If you're experiencing a similar error, connect to the replica set using themongoshell and run thers.conf()command to check the host names of each replica set member.
Followthis page's instructions to change a replica set member's host name.

`mongo`
[rs.conf()](https://www.mongodb.com/docs/manual/reference/method/rs.conf/)

`rs.conf()`
[this page's instructions to change a replica set member's host name](https://www.mongodb.com/docs/manual/tutorial/change-hostnames-in-a-replica-set/#change-hostnames-while-maintaining-replica-set-availability)


You can also check thereason.serversproperty ofMongooseServerSelectionErrorto see what the MongoDB Node driver thinks the state of your replica set is.
Thereason.serversproperty contains amapof server descriptions.

`reason.servers`
`MongooseServerSelectionError`
`reason.servers`
[map](https://masteringjs.io/tutorials/fundamentals/map)


```javascript
if(err.name==='MongooseServerSelectionError') {// Contains a Map describing the state of your replica set. For example:// Map(1) {//   'localhost:27017' => ServerDescription {//     address: 'localhost:27017',//     type: 'Unknown',//     ...//   }// }console.log(err.reason.servers);
}
```


## Multi-mongos support

[Multi-mongos support](#mongos_connections)


You can also connect to multiplemongosinstances
for high availability in a sharded cluster. You donot need to pass any special options to connect to multiple mongosin mongoose 5.x.

[mongos](https://www.mongodb.com/docs/manual/reference/program/mongos/)

[not need to pass any special options to connect to multiple mongos](http://mongodb.github.io/node-mongodb-native/3.0/tutorials/connect/#connect-to-sharded-cluster)


```javascript
// Connect to 2 mongos serversmongoose.connect('mongodb://mongosA:27501,mongosB:27501', cb);
```


## Multiple connections

[Multiple connections](#multiple_connections)


So far we've seen how to connect to MongoDB using Mongoose's default
connection. Mongoose creates adefault connectionwhen you callmongoose.connect().
You can access the default connection usingmongoose.connection.

`mongoose.connect()`
`mongoose.connection`

You may need multiple connections to MongoDB for several reasons.
One reason is if you have multiple databases or multiple MongoDB clusters.
Another reason is to work aroundslow trains.
Themongoose.createConnection()function takes the same arguments asmongoose.connect()and returns a new connection.

[slow trains](https://thecodebarbarian.com/slow-trains-in-mongodb-and-nodejs)

`mongoose.createConnection()`
`mongoose.connect()`

```javascript
constconn = mongoose.createConnection('mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]', options);
```


Thisconnectionobject is then used to create and retrievemodels.
Models arealwaysscoped to a single connection.

[connection](api/connection.html#connection_Connection)

[models](api/model.html#model_Model)


```javascript
constUserModel= conn.model('User', userSchema);
```


ThecreateConnection()function returns a connection instance, not a promise.
If you want to useawaitto make sure Mongoose successfully connects to MongoDB, use theasPromise()function:

`createConnection()`
`await`
[asPromise()function](api/connection.html#Connection.prototype.asPromise())

`asPromise()`

```javascript
// `asPromise()` returns a promise that resolves to the connection// once the connection succeeds, or rejects if connection failed.constconn =awaitmongoose.createConnection(connectionString).asPromise();
```


If you use multiple connections, you should make sure you export schemas,notmodels.
Exporting a model from a file is called theexport model pattern.
The export model pattern is limited because you can only use one connection.


```javascript
constuserSchema =newSchema({name:String,email:String});// The alternative to the export model pattern is the export schema pattern.module.exports= userSchema;// Because if you export a model as shown below, the model will be scoped// to Mongoose's default connection.// module.exports = mongoose.model('User', userSchema);
```


If you use the export schema pattern, you still need to create models somewhere.
There are two common patterns.
The first is to create a function that instantiates a new connection and registers all models on that connection.
With this pattern, you may also register connections with a dependency injector
or anotherinversion of control (IOC) pattern.

[inversion of control (IOC) pattern](https://thecodebarbarian.com/using-ramda-as-a-dependency-injector)


```javascript
constmongoose =require('mongoose');module.exports=functionconnectionFactory() {constconn = mongoose.createConnection(process.env.MONGODB_URI);

  conn.model('User',require('../schemas/user'));
  conn.model('PageView',require('../schemas/pageView'));returnconn;
};
```


Exporting a function that creates a new connection is the most flexible pattern.
However, that pattern can make it tricky to get access to your connection from your route handlers or wherever your business logic is.
An alternative pattern is to export a connection and register the models on the connection in the file's top-level scope as follows.


```javascript
// connections/index.jsconstmongoose =require('mongoose');constconn = mongoose.createConnection(process.env.MONGODB_URI);
conn.model('User',require('../schemas/user'));module.exports= conn;
```


You can create separate files for each connection, likeconnections/web.jsandconnections/mobile.jsif you want to create separate connections for your web API backend and your mobile API backend.
Your business logic can thenrequire()orimportthe connection it needs.

`connections/web.js`
`connections/mobile.js`
`require()`
`import`

## Connection Pools

[Connection Pools](#connection_pools)


Eachconnection, whether created withmongoose.connectormongoose.createConnectionare all backed by an internal configurable
connection pool defaulting to a maximum size of 100. Adjust the pool size
using your connection options:

`connection`
`mongoose.connect`
`mongoose.createConnection`

```javascript
// With object optionsmongoose.createConnection(uri, {maxPoolSize:10});// With connection string optionsconsturi ='mongodb://127.0.0.1:27017/test?maxPoolSize=10';
mongoose.createConnection(uri);
```


The connection pool size is important becauseMongoDB currently can only process one operation per socket.
SomaxPoolSizefunctions as a cap on the number of concurrent operations.

[MongoDB currently can only process one operation per socket](https://thecodebarbarian.com/slow-trains-in-mongodb-and-nodejs)

`maxPoolSize`

## Multi Tenant Connections

[Multi Tenant Connections](#multi-tenant-connections)


In the context of Mongoose, a multi-tenant architecture typically means a case where multiple different clients talk to MongoDB through a single Mongoose application.
This typically means each client makes queries and executes updates through a single Mongoose application, but has a distinct MongoDB database within the same MongoDB cluster.


We recommend readingthis article about multi-tenancy with Mongoose; it has a good description of how we define multi-tenancy and a more detailed overview of our recommended patterns.

[this article about multi-tenancy with Mongoose](https://medium.com/brightlab-techblog/multitenant-node-js-application-with-mongoose-mongodb-f8841a285b4f)


There are two patterns we recommend for multi-tenancy in Mongoose:


Maintain one connection pool, switch between tenants using theConnection.prototype.useDb()method.Maintain a separate connection pool per tenant, store connections in a map orPOJO.

- Maintain one connection pool, switch between tenants using theConnection.prototype.useDb()method.

`Connection.prototype.useDb()`
- Maintain a separate connection pool per tenant, store connections in a map orPOJO.


The following is an example of pattern (1).
We recommend pattern (1) for cases where you have a small number of tenants, or if each individual tenant's workload is light (approximately < 1 request per second, all requests take < 10ms of database processing time).
Pattern (1) is simpler to implement and simpler to manage in production, because there is only 1 connection pool.
But, under high load, you will likely run into issues where some tenants' operations slow down other tenants' operations due toslow trains.

[slow trains](https://thecodebarbarian.com/slow-trains-in-mongodb-and-nodejs)


```javascript
constexpress =require('express');constmongoose =require('mongoose');

mongoose.connect('mongodb://127.0.0.1:27017/main');
mongoose.set('debug',true);

mongoose.model('User', mongoose.Schema({name:String}));constapp =express();

app.get('/users/:tenantId',function(req, res) {constdb = mongoose.connection.useDb(`tenant_${req.params.tenantId}`, {// `useCache` tells Mongoose to cache connections by database name, so// `mongoose.connection.useDb('foo', { useCache: true })` returns the// same reference each time.useCache:true});// Need to register models every time a new connection is createdif(!db.models['User']) {
    db.model('User', mongoose.Schema({name:String}));
  }console.log('Find users from', db.name);
  db.model('User').find().then(users=>res.json({ users })).catch(err=>res.status(500).json({message: err.message}));
});

app.listen(3000);
```


The following is an example of pattern (2).
Pattern (2) is more flexible and better for use cases with > 10k tenants and > 1 requests/second.
Because each tenant has a separate connection pool, one tenants' slow operations will have minimal impact on other tenants.
However, this pattern is harder to implement and manage in production.
In particular,MongoDB does have a limit on the number of open connections, andMongoDB Atlas has separate limits on the number of open connections, so you need to make sure the total number of sockets in your connection pools doesn't go over MongoDB's limits.

[MongoDB does have a limit on the number of open connections](https://www.mongodb.com/blog/post/tuning-mongodb--linux-to-allow-for-tens-of-thousands-connections)

[MongoDB Atlas has separate limits on the number of open connections](https://www.mongodb.com/docs/atlas/reference/atlas-limits)


```javascript
constexpress =require('express');constmongoose =require('mongoose');consttenantIdToConnection = {};constapp =express();

app.get('/users/:tenantId',function(req, res) {letinitialConnection =Promise.resolve();const{ tenantId } = req.params;if(!tenantIdToConnection[tenantId]) {
    tenantIdToConnection[tenantId] = mongoose.createConnection(`mongodb://127.0.0.1:27017/tenant_${tenantId}`);
    tenantIdToConnection[tenantId].model('User', mongoose.Schema({name:String}));
    initialConnection = tenantIdToConnection[tenantId].asPromise();
  }constdb = tenantIdToConnection[tenantId];
  initialConnection.then(() =>db.model('User').find()).then(users=>res.json({ users })).catch(err=>res.status(500).json({message: err.message}));
});

app.listen(3000);
```


## Next Up

[Next Up](#next)


Now that we've covered connections, let's take a look atmodels.

[models](models.html)


[Source](https://mongoosejs.com/docs/connections.html#multiple_connections)