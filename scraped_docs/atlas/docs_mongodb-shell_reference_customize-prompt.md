# Customize the mongosh Prompt - MongoDB Shell


Docs Home / MongoDB Shell / Configure Customize the mongosh Prompt On this page Display Line Numbers Display Database and Hostname Display System Up Time and Document Count By default the mongosh prompt includes the current
database name. You can modify the prompt variable to display custom
strings or to return dynamic information about your mongosh session. Custom prompts are not stored when you exit mongosh . To
have a custom prompt persist through restarts, add the code for your
custom prompt to .mongoshrc.js . Display Line Numbers To display line numbers in the mongosh prompt, run the
following code inside mongosh : let cmdCount = 1 ; prompt = function ( ) { return ( cmdCount + + ) + "> " ; } The prompt will look like this: 1 > show collections 2 > use test 3 > Display Database and Hostname The current database name is part of the default mongosh prompt. To
reformat the prompt to show the database and hostname, use a function
like this one: { const hostnameSymbol = Symbol ( 'hostname' ) ; prompt = () => { if ( ! db [ hostnameSymbol]) db [ hostnameSymbol] = db. serverStatus ( ). host ; return ` ${db.getName()} @ ${db[hostnameSymbol]} > ` ; } ; } The prompt will look like this: admin@ centos0722 : 27502 > Display System Up Time and Document Count To create a prompt that shows the system uptime and a count of
documents across all collections in the current database, use a
function like this one: prompt = function ( ) { return "Uptime:" + db. serverStatus ( ). uptime + " Documents:" + db. stats ( ). objects + " > " ; } Back Use a Configuration File Next Configure Telemetry Options
