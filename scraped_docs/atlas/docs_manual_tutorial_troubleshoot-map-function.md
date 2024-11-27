# Troubleshoot the Map Function - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Map-Reduce Troubleshoot the Map Function On this page Verify Key and Value Pairs Note Aggregation Pipeline as Alternative to Map-Reduce Starting in MongoDB 5.0, map-reduce is
deprecated: Instead of map-reduce , you should use an aggregation pipeline . Aggregation
pipelines provide better performance and usability than map-reduce. You can rewrite map-reduce operations using aggregation pipeline
stages , such as $group , $merge , and others. For map-reduce operations that require custom functionality, you can
use the $accumulator and $function aggregation
operators. You can use those
operators to define custom aggregation expressions in JavaScript. For examples of aggregation pipeline alternatives to map-reduce, see: Map-Reduce to Aggregation Pipeline Map-Reduce Examples An aggregation pipeline is also
easier to troubleshoot than a map-reduce operation. The map function is a JavaScript function that associates or "maps"
a value with a key and emits the key and value pair during a map-reduce operation. Verify Key and Value Pairs To verify the key and value pairs emitted by the map function, write your own emit function. Consider a collection orders that contains documents of the
following prototype: { _id : ObjectId ( "50a8240b927d5d8b5891743c" ) , cust_id : "abc123" , ord_date : new Date ( "Oct 04, 2012" ) , status : 'A' , price : 250 , items : [ { sku : "mmm" , qty : 5 , price : 2.5 } , { sku : "nnn" , qty : 5 , price : 2.5 } ] } Define the map function that maps the price to the cust_id for each document and emits the cust_id and price pair: var map = function ( ) { emit ( this . cust_id , this . price ) ; } ; Define the emit function to print the key and value: var emit = function ( key, value ) { print ( "emit" ) ; print ( "key: " + key + "  value: " + tojson ( value)) ; } Invoke the map function with a single document from the orders collection: var myDoc = db. orders . findOne ( { _id : ObjectId ( "50a8240b927d5d8b5891743c" ) } ) ; map. apply ( myDoc) ; Verify the key and value pair is as you expected. emit key : abc123 value : 250 Invoke the map function with multiple documents from the orders collection: var myCursor = db. orders . find ( { cust_id : "abc123" } ) ; while ( myCursor. hasNext ( )) { var doc = myCursor. next ( ) ; print ( "document _id= " + tojson ( doc. _id )) ; map. apply ( doc) ; print ( ) ; } Verify the key and value pairs are as you expected. Tip See also: The map function must meet various requirements. For a list of all
the requirements for the map function, see mapReduce ,
or mongosh helper method db.collection.mapReduce() . Back Perform with Increments Next Troubleshoot Reduce
