# Run Commands - MongoDB Shell


Docs Home / MongoDB Shell Run Commands On this page Format Input and Output Switch Databases Terminate a Running Command Command Exceptions Clear the mongosh Console To run commands in mongosh , you must first connect to a MongoDB deployment . Format Input and Output mongosh uses the Node.js BSON parser parser to parse BSON data. You can use the parser's EJSON interface to transform your
data when you work with mongosh . For examples that use EJSON, see: EJSON . Switch Databases To display the database you are using, type db : db The operation should return test , which is the default database. To switch databases, issue the use <db> helper, as in the
following example: use < database > To access a different database from the current database without
switching your current database context, see the db.getSiblingDB() method. To list the databases available to the user, use the helper show
dbs . Create a New Database and Collection To create a new database, issue the use <db> command with the
database that you would like to create. For example, the following
commands create both the database myNewDatabase and the collection myCollection using the insertOne() operation: use myNewDatabase db. myCollection . insertOne ( { x : 1 } ) ; If a collection does not exist, MongoDB creates the collection when you
first store data for that collection. Terminate a Running Command To terminate a running command or query in mongosh ,
press Ctrl + C . When you enter Ctrl + C , mongosh : interrupts the active command, tries to terminate the ongoing, server-side operation, and returns a command prompt. If mongosh cannot cleanly terminate the running process,
it issues a warning. Note Pressing Ctrl + C in mongosh does not terminate
asynchronous code. Asynchronous operations such as setTimeout or
operations like fs.readFile continue to run. There is no way to terminate asynchronous code in mongosh . This is the same behavior as in the Node.js REPL . Pressing Ctrl + C once will not exit mongosh , press Ctrl + C twice to  exit mongosh . You can also terminate a script from within the script code by calling the exit(<code>) command. For more information, refer to Terminate a Script on Error . Command Exceptions For commands whose output includes { ok: 0 } , mongosh returns a
consistent exception and omits the server raw output. The legacy mongo shell returns output that varies for each command. Clear the mongosh Console The cls command clears the console. You can also clear the console
with Ctrl + L and console.clear() . Back Configure Telemetry Options Next Perform CRUD Operations
