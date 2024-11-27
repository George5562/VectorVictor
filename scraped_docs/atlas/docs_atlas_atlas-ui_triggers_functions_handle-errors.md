# Handle Errors in Functions - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data / Triggers / Functions Handle Errors in Functions On this page View Logs Retry Functions Recursively Call Function in Error Handling Blocks Use Database Triggers to Retry This page explains how to work with errors in Atlas Functions. Note Custom Error Handling for Database Triggers Using AWS EventBridge You can create a custom error handler specifically for database
Triggers using AWS EventBridge. For more information, refer to Custom Error Handling . You can handle Function errors using standard JavaScript error handling techniques
like try...catch statements . function willThrowAndHandleError ( ) { try { throw new Error ( "This will always happen" ) ; } catch ( err) { console . error ( "An error occurred. Error message:" + err. message ) ; } } exports = willThrowAndHandleError ; View Logs You can view records of all Function executions invoked by an Atlas Trigger
on the Logs page. This includes Functions that failed to
successfully execute due to an error. For more information, see Trigger Logs . Retry Functions Atlas Functions do not have built-in retry behavior. You can add custom retry behavior. For example, you might want to add
retry behavior if the third-party service that your Function calls has
intermittent connectivity, and you want the Function to re-execute
even if the third-party service is temporarily down. The following sections describe the available strategies to add retry
behavior to your Functions: Recursively Call Functions in Error Handling Blocks Use Database Triggers to Retry Functions Recursively Call Function in Error Handling Blocks You can handle operations that might fail by calling a Function recursively. On a high level, this process includes the following components: Execute operations that you want to retry in a try statement
and have the Function call itself in a catch statement. To prevent indefinite execution, set a maximum number of retries.
Every time the Function fails and enters the catch statement,
increment a count of the current number of retries.
Stop the recursive execution when the Function's current number of retries
reaches the max number of retries. You may also want to throttle retries to reduce the total number of executions
in a time frame. The following table describes some advantages and disadvantages
of handling Function retries with the recursive call strategy. Advantages Disadvantages All retry logic occurs within one function. Function can return a value after a retry. Minimal additional code. All retries must occur within a single Function's max execution time. The following code example demonstrates an implementation of retrying a Function
by using recursion in error-handling blocks: Recursive Call Strategy Example // Utility function to suspend execution of current process async function sleep ( milliseconds ) { await new Promise ( ( resolve ) => setTimeout ( resolve , milliseconds)) ; } // Set variables to be used by all calls to `mightFail` // Tip: You could also store `MAX_RETRIES` and `THROTTLE_TIME_MS` // in App Services Values const MAX_RETRIES = 5 ; const THROTTLE_TIME_MS = 5000 ; let currentRetries = 0 ; let errorMessage = "" ; async function mightFail ( ...inputVars ) { if ( currentRetries === MAX_RETRIES ) { console . error ( `Reached maximum number of retries ( ${MAX_RETRIES} ) without successful execution.` ) ; console . error ( "Error Message:" , errorMessage) ; return ; } let res ; try { // operation that might fail res = await callFlakyExternalService ( ... inputVars) ; } catch ( err) { errorMessage = err. message ; // throttle retries await sleep ( THROTTLE_TIME_MS ) ; currentRetries + + ; res = await mightFail ( ... inputVars) ; } return res ; } exports = mightFail ; Use Database Triggers to Retry You can also retry Functions by using a Database Trigger to execute retries and a MongoDB collection to track previously-failed executions. On a high level, this process includes the following components: Main Function that executes the logic you want to retry,
wrapped in the handler function. Failed execution tracker MongoDB collection that tracks failed executions of the main Function. Handler Function that invokes the main Function and logs when the function fails
to the failed execution tracker collection. Database Trigger Function that reruns the handler function whenever
the handler function adds an error to the failed execution tracker collection. You can support multiple main functions with one set of a handler Function,
execution tracker collection, and Database Trigger Function. Advantages Disadvantages Each retry is its own Function execution, with own max execution time
and resources. If the Function is retried, it cannot return a value. Each Function call requires two Function invocations, one for the Function
itself and one for the retry handler. More complex logic, which can be more difficult to write, debug, and monitor. You can create a retry mechanism for Functions in the Atlas UI or using the
App Services CLI. The following procedure walks you through creating a handler,
a retry Database Trigger Function, and a main Function. 1 Create the Handler Function First, create the handler Function handleRetry that invokes the main Function. handleRetry accepts the following parameters: Parameter Type Description functionToRetry JavaScript Function Function to retry. functionName String Name of the function you want to retry. operationId ObjectId Unique identifier for the main function's execution, including retries. previousRetries Number How many times the main function has previously been tried. ...args Rest parameters Indefinite number of arguments passed to the main function. handleRetry performs the following operations: Attempts to execute functionToRetry in a try statement.
If the execution is successful, handleRetry returns the value
returned by functionToRetry . If the execution of functionToRetry in the previous step throws an error,
the catch statement handles the error as follows: Checks if the number of previous retries equals the
maximum permitted number of retries.
If the two numbers are the same, then the function throws an error
because the max retries has been reached. The function no longer attempts
to retry. Build a function execution log entry object to insert into the database. Get a reference to the failed execution tracker collection. Insert the function log execution log entry into
the failed execution tracker collection. This insertion operation
causes the Database Trigger Function, which you will make in the next step,
to fire. The main function is passed as the argument functionToRetry . handleRetry attempts to execute the main Function.
If the execution fails, this function attempts to retry the main function. Atlas UI App Services CLI Navigate to Functions . Click the button Create New Function . In the field Name , add handleRetry . In the Function Editor add the following code, then
save the Function: handleRetry.js // Tip: You could also put this in an App Services Value const MAX_FUNC_RETRIES = 5 ; async function handleRetry ( functionToRetry, functionName, operationId, previousRetries, ...args ) { try { // Try to execute the main function const response = await functionToRetry ( ... args) ; return response ; } catch ( err) { // Evaluates if should retry function again. // If no retry, throws error and stops retrying. if ( previousRetries === MAX_FUNC_RETRIES ) { throw new Error ( `Maximum number of attempts reached ( ${MAX_FUNC_RETRIES} ) for function ' ${functionName} ': ${err.message} ` ) ; } // Build function execution log entry for insertion into database. const logEntry = { operationId , errorMessage : err. message , timestamp : new Date ( ) , retries : previousRetries + 1 , args , functionName , } ; // Get reference to database collection const executionLog = context. services . get ( "mongodb-atlas" ) . db ( "logs" ) . collection ( "failed_execution_logs" ) ; // Add execution log entry to database await executionLog. insertOne ( logEntry) ; return ; } } exports = handleRetry ; Add the following to functions/config.json : functions/config.json [ { "name" : "handleRetry" , "private" : true , "run_as_system" : true } // ...other configuration ] Create the file for the Function functions/handleRetry.js : functions/handleRetry.js // Tip: You could also put this in an App Services Value const MAX_FUNC_RETRIES = 5 ; async function handleRetry ( functionToRetry, functionName, operationId, previousRetries, ...args ) { try { // Try to execute the main function const response = await functionToRetry ( ... args) ; return response ; } catch ( err) { // Evaluates if should retry function again. // If no retry, throws error and stops retrying. if ( previousRetries === MAX_FUNC_RETRIES ) { throw new Error ( `Maximum number of attempts reached ( ${MAX_FUNC_RETRIES} ) for function ' ${functionName} ': ${err.message} ` ) ; } // Build function execution log entry for insertion into database. const logEntry = { operationId , errorMessage : err. message , timestamp : new Date ( ) , retries : previousRetries + 1 , args , functionName , } ; // Get reference to database collection const executionLog = context. services . get ( "mongodb-atlas" ) . db ( "logs" ) . collection ( "failed_execution_logs" ) ; // Add execution log entry to database await executionLog. insertOne ( logEntry) ; return ; } } exports = handleRetry ; Deploy your changes: Run the following command to deploy your changes: appservices push 2 Create the Retry Database Trigger Atlas UI App Services CLI Navigate to the Triggers page: If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Triggers under
the Services heading. The Triggers page displays. Click Add a Trigger . Create the Trigger with the following configuration: Field Value Name Name of your choosing (ex: retryOperation ) Enabled Yes Skip Events on Re-Enable Yes Event Ordering Yes Cluster Name Name of your choosing (ex: mongodb-atlas ) Database Name Name of your choosing (ex: logs ) Collection Name Name of your choosing (ex: failed_execution_logs ) Operation Type Insert Full Document Yes Document Preimage No Select An Event Type Function Function Click + New Function . Refer to the following information
about the contents of the function. Advanced Configuration N/A - No advanced configuration necessary. Now add the code to the Function that the Trigger invokes. The function retryOperation takes as a parameter logEntry , the document that the
retry handler posted to the failed execution tracker collection.
Then, retryOperation uses context.functions.execute() to invoke the main function with information from logEntry . In the field Function Name , add retryOperationDbTrigger . For the field Function , add the following code,
then save the Trigger: functions/retryOperationDbTrigger.js async function retryOperation ( { fullDocument: logEntry } ) { // parse values from log entry posted to database const { args , retries , functionName , operationId } = logEntry ; // Re-execute the main function await context. functions . execute ( functionName , ... args , operationId , retries) ; } exports = retryOperation ; Authenticate a MongoDB Atlas user: Use your MongoDB Atlas Administration API Key to
log in to the App Services CLI: appservices login --api-key="<API KEY>" --private-api-key="<PRIVATE KEY>" Pull your App's latest configuration files: Run the following command to get a local copy of your configuration files: appservices pull --remote=<App ID> By default, the command pulls files into the current working directory. You can
specify a directory path with the optional --local flag. Add configuration for the Database Trigger. For more information,
refer to the Trigger configuration reference . triggers/retryOperation.json { "name" : "retry" , "type" : "DATABASE" , "config" : { "operation_types" : [ "INSERT" ] , "database" : "logs" , "collection" : "failed_execution_logs" , "service_name" : "mongodb-atlas" , "project" : { } , "full_document" : true , "full_document_before_change" : false , "unordered" : false , "skip_catchup_events" : false } , "disabled" : false , "event_processors" : { "FUNCTION" : { "config" : { "function_name" : "retryOperationDbTrigger" } } } } Now add the code to the functions/config.json Function
that the Trigger invokes. The function retryOperation takes as a parameter logEntry , the document that the
retry handler posted to the failed execution tracker collection.
Then, retryOperation uses context.functions.execute() to invoke the main function with information from logEntry . functions/config.json [ // ...other configuration { "name" : "retryOperationDbTrigger" , "private" : true } ] Add the following code to the file functions/retryOperationDbTrigger.js : retryOperationDbTrigger.js async function retryOperation ( { fullDocument: logEntry } ) { // parse values from log entry posted to database const { args , retries , functionName , operationId } = logEntry ; // Re-execute the main function await context. functions . execute ( functionName , ... args , operationId , retries) ; } exports = retryOperation ; Deploy your changes: Run the following command to deploy your changes: appservices push 3 Create the Main Function Now that you have the function handler and the retry Database Trigger Function,
you can write the main function. In the following example, the Function randomly throws an error when performing addition.
The JavaScript functions that execute this logic are the following: getRandomOneTwoThree() : Helper function for generating errors
for the example. additionOrFailure() : Function with the main logic. The invocation of additionOrFailure() wrapped by the retry handler
occurs in the exported function additionWithRetryHandler() . All functions that use the retry handler function should resemble this function. You must include the correct parameters to make this function work
with the rest of the retry logic. These parameters are: Parameter Type Description ...args Rest parameters Zero or more parameters to pass to the function with main logic.
In the case of this example, the two numbers added
in additionOrFailure() , num1 and num2 . operationId BSON.Object.Id Unique identifier for the Function
call and retries. Set default value to a new BSON.ObjectId() . retries Number Set default value to 0. The body of additionWithRetryHandler is the retry handler handleRetry invoked by context.functions.execute() ,
which in turn invokes additionOrFailure . The arguments you pass to context.functions.execute() are the following: Argument Type Description "handleRetry" String Name of the Function you defined to invoke the main function
and post to the retry logs if the main function doesn't properly execute. additionOrFailure JavaScript function The main function that handleRetry() invokes. operationId BSON.ObjectId Passed in as argument from the parameter operationId of additionWithRetryHandler() . retries Number Passed in as argument from the parameter retries of additionWithRetryHandler() . ...args Spread arguments Zero or more arguments to pass to the function with main logic.
Passed in as argument from the parameter ...args of additionWithRetryHandler() Atlas UI App Services CLI In the field Function Name , add additionWithRetryHandler . For the field Function , add the following code: additionWithRetryHandler.js // randomly generates 1, 2, or 3 function getRandomOneTwoThree ( ) { return Math . floor ( Math . random ( ) * 3 ) + 1 ; } function additionOrFailure ( num1, num2 ) { // Throw error if getRandomOneTwoThree returns 1 const rand = getRandomOneTwoThree ( ) ; if ( rand === 1 ) throw new Error ( "Uh oh!!" ) ; const sum = num1 + num2 ; console . log ( `Successful addition of ${num1} + ${num2} . Result: ${sum} ` ) ; // Otherwise return the sum return sum ; } async function additionWithRetryHandler ( inputVar1, inputVar2, // create a new `operation_id` if one not provided operationId = new BSON.ObjectId () , // count number of attempts retries = 0 ) { const res = await context. functions . execute ( "handleRetry" , additionOrFailure , "additionWithRetryHandler" , // MUST BE NAME OF FUNCTION operationId , retries , inputVar1 , inputVar2 ) ; return res ; } exports = additionWithRetryHandler ; Click Save . Add the Function metadata to functions/config.json : functions/config.json [ // ...other configuration { "name" : "additionWithRetryHandler" , "private" : false } ] Add the following code to the file functions/additionWithRetryHandler.js : functions/additionWithRetryHandler.js // randomly generates 1, 2, or 3 function getRandomOneTwoThree ( ) { return Math . floor ( Math . random ( ) * 3 ) + 1 ; } function additionOrFailure ( num1, num2 ) { // Throw error if getRandomOneTwoThree returns 1 const rand = getRandomOneTwoThree ( ) ; if ( rand === 1 ) throw new Error ( "Uh oh!!" ) ; const sum = num1 + num2 ; console . log ( `Successful addition of ${num1} + ${num2} . Result: ${sum} ` ) ; // Otherwise return the sum return sum ; } async function additionWithRetryHandler ( inputVar1, inputVar2, // create a new `operation_id` if one not provided operationId = new BSON.ObjectId () , // count number of attempts retries = 0 ) { const res = await context. functions . execute ( "handleRetry" , additionOrFailure , "additionWithRetryHandler" , // MUST BE NAME OF FUNCTION operationId , retries , inputVar1 , inputVar2 ) ; return res ; } exports = additionWithRetryHandler ; Deploy your changes: Run the following command to deploy your changes: appservices push Now when you invoke additionWithRetryHandler , the Function will retry if it fails. Back External Dependencies Next JavaScript Support