# Write Scripts - MongoDB Shell


Docs Home / MongoDB Shell Write Scripts On this page Compatibility Execute a JavaScript File Execute a Script from Within mongosh Execute a Script From the Command Line Execute a Script From the Command Line with Authentication Terminate a Script on Error Execute Code From a Configuration File Execute JavaScript Code Execute MongoDB Code Execute JavaScript and MongoDB Code Open a New Connection Connect to a Local MongoDB Instance Connect to an Atlas Deployment Connect to a MongoDB Instance that Enforces Access Control Use connect() to Connect to a MongoDB Instance Connection Considerations You can write scripts for the MongoDB Shell that modify data in MongoDB or
perform administrative operations. You may also want to package your
scripts as snippets for easier distribution and
management. This tutorial introduces using the MongoDB Shell with JavaScript to
access MongoDB. Compatibility You can write scripts for the MongoDB Shell for deployments hosted
in the following environments: MongoDB Atlas : The fully
managed service for MongoDB deployments in the cloud MongoDB Enterprise : The
subscription-based, self-managed version of MongoDB MongoDB Community : The
source-available, free-to-use, and self-managed version of MongoDB To learn more about using the MongoDB Shell for deployments
hosted in MongoDB Atlas, see Connect via mongosh . Execute a JavaScript File Execute a Script from Within mongosh You can execute a .js file from within the MongoDB Shell using the load() method. File Paths The load() method accepts relative
and absolute paths. If the current working directory of the MongoDB Shell is /data/db , and connect-and-insert.js is in the /data/db/scripts directory, then the following calls within the MongoDB Shell are equivalent: load ( "scripts/connect-and-insert.js" ) load ( "/data/db/scripts/connect-and-insert.js" ) Example The following example creates and executes a script that: Connects to a local instance running on the default port. Connects to the myDatabase database. Populates the movies collection with sample documents. Create a file named connect-and-insert.js with the following
contents: db = connect ( 'mongodb://localhost/myDatabase' ) ; db. movies . insertMany ( [ { title : 'Titanic' , year : 1997 , genres : [ 'Drama' , 'Romance' ] } , { title : 'Spirited Away' , year : 2001 , genres : [ 'Animation' , 'Adventure' , 'Family' ] } , { title : 'Casablanca' , genres : [ 'Drama' , 'Romance' , 'War' ] } ] ) To load and execute the connect-and-insert.js file, use mongosh to connect to your deployment and run the following
command: load ( "connect-and-insert.js" ) To confirm that the documents loaded correctly, use the myDatabase collection and query the movies collection. use myDatabase db. movies . find ( ) Note There is no search path for the load() method. If the target
script is not in the current working directory or the full specified
path, the MongoDB Shell cannot access the file. Execute a Script From the Command Line You can use mongosh to execute a script from the command
line without entering the mongosh console. To specify the filename, use the --file or -f parameter to
specify the filename. You may also need to specify connection
information in addition to the --file or -f parameters. Tip If you pass a filename to mongosh without using the
parameter flags the connection may fail if there are other command
line arguments. To pass filenames always use --file or -f . Example The following example creates scripts and runs them from the command
line. loadMovies.js , uses insertMany() to a
update a local MongodDB instance. queryMovies.js uses db.collection.find() to verify
the update. Copy this script and save it as loadMovies.js . db = connect ( 'mongodb://localhost/films' ) ; db. movies . insertMany ( [ { title : 'Titanic' , year : 1997 , genres : [ 'Drama' , 'Romance' ] } , { title : 'Spirited Away' , year : 2001 , genres : [ 'Animation' , 'Adventure' , 'Family' ] } , { title : 'Casablanca' , genres : [ 'Drama' , 'Romance' , 'War' ] } ] ) Tip Verify the connection string in the highlighted line. If your
MongoDB instance is not running on localhost:27017 , you
must edit the connection string. For example, the following connection string connects to localhost port 27500 : db = connect ( 'mongodb://localhost:27500/films' ) ; Copy this script and save it as queryMovies.js . db = connect ( 'mongodb://localhost/films' ) ; printjson ( db. movies . find ( { } ) ) ; Run the scripts from the command line. mongosh - - file loadMovies. js - - file queryMovies. js Verify the output. Loading file : loadMovies. js Loading file : queryMovies. js [ { _id : ObjectId ( "616f1b8092dbee425b661117" ) , title : 'Titanic' , year : 1997 , genres : [ 'Drama' , 'Romance' ] } , { _id : ObjectId ( "616f1b8092dbee425b661118" ) , title : 'Spirited Away' , year : 2001 , genres : [ 'Animation' , 'Adventure' , 'Family' ] } , { _id : ObjectId ( "616f1b8092dbee425b661119" ) , title : 'Casablanca' , genres : [ 'Drama' , 'Romance' , 'War' ] } ] The output of the db.collection.find() command shows
that the movies collection was updated. Tip To make the output visible, use printjson() to call db.collection.find() . printjson ( db. movies . find ( { } ) ) ; Execute a Script From the Command Line with Authentication To execute a script against a remote mongod instance that
requires authentication, specify the connection and authentication
details in addition to the filename. For example: mongosh - - host 172.17 .0 .3 - - port 27500 - - username filmFan - - password superSecret - - file loadMovies. js You can also specify the shortened form of the options: mongosh - - host 172.17 .0 .3 - - port 27500 - u filmFan - p superSecret - f loadMovies. js Tip In shells like bash and zsh , if you begin a command with a
space it will not be saved in your command history. This minimizes
exposure if you enter passwords on the command line. Terminate a Script on Error It is often useful to terminate a running script if an exception is thrown, or
in the case of unexpected results. Exiting at a specific point in the script
prevents the execution of unnecessary code and potentially unexpected results. To terminate a script, you can call the exit(<code>) method, where the <code> is any user-specified value. As a best practice, wrap code in a try - catch , calling the exit method in the catch block. Likewise, to check the results of a query or any command,
you can add an if - else statement and call the exit method if the
results are not what is expected. Execute Code From a Configuration File On startup, mongosh checks your HOME directory for a
JavaScript file named .mongoshrc.js . If this file is found, mongosh reads the content of .mongoshrc.js before
displaying the prompt for the first time. Tip See also: Customize the mongosh Prompt .mongoshrc Configuration File Execute JavaScript Code To update the mongosh prompt to display line numbers, add
the following code to <your-home-directory>/.mongoshrc.js let cmdCount = 1 ; prompt = function ( ) { return ( cmdCount + + ) + "> " ; } The prompt will look like this: 1 > show collections 2 > use test 3 > Execute MongoDB Code To create a log of when your mongosh client connects to a
database, add the following code to <your-home-directory>/.mongoshrc.js : db. clientConnections . insertOne ( { connectTime : ISODate ( ) } ) Each time you connect to a database, the MongoDB server adds a
document like the following to the clientConnections collection. { _id : ObjectId ( "61d4bbf0fa4c85f53418070f" ) , connectTime : ISODate ( "2022-01-04T21:28:16.367Z" ) } Execute JavaScript and MongoDB Code The current database name is part of the default mongosh prompt. To
reformat the prompt to show the database and hostname, use a function
like this one: { const hostnameSymbol = Symbol ( 'hostname' ) ; prompt = () => { if ( ! db [ hostnameSymbol]) db [ hostnameSymbol] = db. serverStatus ( ). host ; return ` ${db.getName()} @ ${db[hostnameSymbol]} > ` ; } ; } The prompt will look like this: admin@ centos0722 : 27502 > Open a New Connection From the MongoDB Shell or from a JavaScript file, you can instantiate
database connections using the Mongo() method: new Mongo ( ) new Mongo (< host > ) new Mongo (< host : port > ) Note The MongoDB Shell does not support the ClientSideFieldLevelEncryptionOptions document with the Mongo() method. Connect to a Local MongoDB Instance Consider a MongoDB instance running on localhost on the default port. The following example: Instantiates a new connection to the instance, and Sets the global db variable to myDatabase using the Mongo.getDB() method. conn = Mongo ( ) ; db = conn. getDB ( "myDatabase" ) ; Connect to an Atlas Deployment To connect to a deployment hosted in MongoDB Atlas, run the mongosh command with your
Atlas connection string. For example: mongosh "mongodb+srv://YOUR_CLUSTER_NAME.YOUR_HASH.mongodb.net/" --apiVersion YOUR_API_VERSION --username YOUR_USERNAME Once you've established a connection to your deployment, you can
instantiate database connections directly from the MongoDB Shell .
The following example: Instantiates a connection to the current deployment by using the db.getMongo() method. Sets the global db variable to myDatabase by using the Mongo.getDB() method. conn = db. getMongo ( ) db = conn. getDB ( "myDatabase" ) ; Connect to a MongoDB Instance that Enforces Access Control To connect to a MongoDB instance that enforces access control, you
must include the credentials in the connection string . The following command connects to a MongoDB instance that is: Running on localhost on the default port, and Secured using SCRAM . conn = Mongo ( "mongodb://<username>:<password>@localhost:27017/<authDB>" ) ; Note The MongoDB Shell redacts credentials from the command history and the logs . Use connect() to Connect to a MongoDB Instance You can also use the connect() method to connect to the MongoDB instance. The following command: Connects to the MongoDB instance that is running on localhost with
the non-default port 27020 , and Sets the global db variable. db = connect ( "localhost:27020/myDatabase" ) ; Connection Considerations Consider portability and the operating environment when you write
scripts. Script Includes Connection Detail If the connection details are included in the script: You do not need to specify connection information on the command
line. You should use the --nodb parameter. Consider a mongod instance running on localhost:27500 . The following script prints the number of users. Copy the code and save
it as getUserCount.js . db = connect ( "localhost:27500/admin" ) ; Ë printjson ( db. system . users . countDocuments ( ) ) ; Run getUserCount.js : mongosh - - nodb - - file getUserCount. js mongosh defaults to port 27170. mongod is running on port 27500. The --nodb parameter instructs mongosh to run a
script without first connecting to a mongod instance. The highlighted line is correct, but getUserCount.js will not run
without --nodb because mongosh cannot connect to the
local instance. With --nodb , mongosh runs getUserCount.js and uses the highlighted information to connect. Script Does Not Include Connection Details It is convenient to specify connection information in your script, but
that also makes it less portable. The getUserCount.js script would
have to be updated to run on a remote instance or one running on a
different port. To increase portability, use db.getSiblingDB() and specify
the connection information on the command line. The following script is more portable than getUserCount.js because
it does not have specific connection details. Copy the code and save it
as portableGetUserCount.js . db = db. getSiblingDB ( "admin" ) ; printjson ( db. system . users . countDocuments ( ) ) ; To run portableGetUserCount.js , specify the host and port on the
command line: mongosh - - host 172.17 .0 .3 - - port 27500 - - file portableGetUserCount. js To run portableGetUserCount.js on a different host or port, change
the connection details on the command line. Unlike getUserCount.js ,
you do not have to edit the script to run portableGetUserCount.js . Back Client-Side Field Level Encryption Next Include Files & Modules
