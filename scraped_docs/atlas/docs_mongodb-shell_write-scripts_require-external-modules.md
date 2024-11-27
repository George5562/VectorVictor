# Include External Files and Modules in Scripts - MongoDB Shell


Docs Home / MongoDB Shell / Write Scripts Include External Files and Modules in Scripts On this page Require a Local File Require a Built-In Module Require an npm Module Important A complete description of Node.js, modules, and the require() function is out of scope for this tutorial. To learn more, see
the Node.js Documentation . To use files and modules in your mongosh interactions, use the require() function. In your mongosh scripts, you can require: Local files Built-in Node.js modules External (npm) Node.js modules Require a Local File You can use JavaScript files in mongosh scripts without any
additional setup or configuration. Note mongosh does not execute files imported with require() .
Instead, mongosh adds everything from an imported file to the
current execution scope. Example To include a file named test.js that is located in the current
working directory, use one of the following commands: require ( './tests.js' ) var tests = require ( './tests.js' ) Require a Built-In Module You can require built-in Node.js modules (such as fs ) in mongosh without any additional setup or configuration. Example The following example creates and executes a script that: Connects to a local deployment running on the default port. Populates the myDatabase.employees collection with sample data. Uses the fs module to write a document from the myDatabase.employees collection to a file named employee.json . Create a file named employee-to-text-file.js with the
following contents: const fs = require ( 'fs' ) ; db = connect ( 'mongodb://localhost/myDatabase' ) ; db. employees . insertMany ( [ { "name" : "Alice" , "department" : "engineering" } , { "name" : "Bob" , "department" : "sales" } , { "name" : "Carol" , "department" : "finance" } ] ) const document = db. employees . findOne ( ) ; fs. writeFileSync ( 'employee.json' , JSON . stringify ( document )) ; To load and execute the employee-to-text-file.js file, run the
following command from mongosh : load ( "employee-to-text-file.js" ) To confirm that the data was written to the file, open the employee.json file. Require an npm Module You can require Node.js modules (such as those downloaded from npm ). To use external modules, you must
install the modules either: Globally In the node_modules directory in your current working directory. There are two packaging standards for Node.js modules. Packaging Standard Works with require() CommonJS (CJS) Yes ECMAScript Module (ES Module) No You cannot require() an ES module in mongosh . If you want to use
functionality from an ES module, check to see if there is a CommonJS
version that you can use instead. For more information, see: Node.js module documentation Installing older versions of npm packages Tip You can require remote npm modules using this construction: const localRequire = require ( 'module' ). createRequire ( __filename) ; For an example, see index.js in the resumetoken snippet. Example Important To run this example, you must install the date-fns module either
globally or in the node_modules directory in your
current working directory. The following example creates and executes a script that: Connects to a local deployment running on the default port. Populates the myDatabase.cakeSales collection with sample data. Uses the date-fns module to format dates. Create a file named date-fns-formatting.js with the following
contents: const formatDistance = require ( 'date-fns/formatDistance' ) db = connect ( 'mongodb://localhost/myDatabase' ) ; db. cakeSales . insertMany ( [ { _id : 0 , type : "chocolate" , orderDate : new Date ( "2020-05-18T14:10:30Z" ) , state : "CA" , price : 13 , quantity : 120 } , { _id : 1 , type : "chocolate" , orderDate : new Date ( "2021-03-20T11:30:05Z" ) , state : "WA" , price : 14 , quantity : 140 } , { _id : 2 , type : "vanilla" , orderDate : new Date ( "2021-01-11T06:31:15Z" ) , state : "CA" , price : 12 , quantity : 145 } , { _id : 3 , type : "vanilla" , orderDate : new Date ( "2020-02-08T13:13:23Z" ) , state : "WA" , price : 13 , quantity : 104 } , { _id : 4 , type : "strawberry" , orderDate : new Date ( "2019-05-18T16:09:01Z" ) , state : "CA" , price : 41 , quantity : 162 } , { _id : 5 , type : "strawberry" , orderDate : new Date ( "2019-01-08T06:12:03Z" ) , state : "WA" , price : 43 , quantity : 134 } ] ) const saleDate0 = db. cakeSales . findOne ( { _id : 0 } ). orderDate const saleDate1 = db. cakeSales . findOne ( { _id : 1 } ). orderDate const saleDateDistance0 = formatDistance ( saleDate0 , new Date ( ) , { addSuffix : true }) const saleDateDistance1 = formatDistance ( saleDate1 , new Date ( ) , { addSuffix : true }) print ( "{ _id: 0 } orderDate was " + saleDateDistance0) print ( "{ _id: 1 } orderDate was " + saleDateDistance1) To load and execute the date-fns-formatting.js file, run the
following command from mongosh : load ( "date-fns-formatting.js" ) mongosh outputs something like the following: { _id: 0 } orderDate was over 1 year ago { _id: 1 } orderDate was 7 months ago Your output may vary depending on the date that you run the example. Back Write Scripts Next require() versus load()