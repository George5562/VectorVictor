# $literal (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $literal (aggregation) On this page Definition Behavior Examples Definition $literal Returns a value without parsing. Use for values that the aggregation
pipeline may interpret as an expression. The $literal expression has the following syntax: { $literal: <value> } Behavior If the <value> is an expression , $literal does not evaluate the expression but instead
returns the unparsed expression. Example Result { $literal: { $add: [ 2, 3 ] } } { "$add" : [ 2, 3 ] } { $literal:  { $literal: 1 } } { "$literal" : 1 } Examples Treat $ as a Literal In expression ,
the dollar sign $ evaluates to a field path; i.e. provides access
to the field. For example, the $eq expression $eq: [
"$price", "$1" ] performs an equality check between the value in the
field named price and the value in the field named 1 in the
document. The following example uses a $literal expression to treat
a string that contains a dollar sign "$1" as a constant value. A storeInventory collection has the following documents: db. storeInventory . insertMany ( [ { "_id" : 1 , "item" : "napkins" , price : "$2.50" } , { "_id" : 2 , "item" : "coffee" , price : "1" } , { "_id" : 3 , "item" : "soap" , price : "$1" } ] ) db. storeInventory . aggregate ( [ { $project : { costsOneDollar : { $eq : [ "$price" , { $literal : "$1" } ] } } } ] ) This operation projects a field named costsOneDollar that holds a
boolean value, indicating whether the value of the price field is
equal to the string "$1" : { "_id" : 1 , "costsOneDollar" : false } { "_id" : 2 , "costsOneDollar" : false } { "_id" : 3 , "costsOneDollar" : true } Project a New Field with Value 1 The $project stage uses the expression <field>: 1 to
include the <field> in the output. The following example uses the $literal to return a new field set to the value of 1 . A books collection has the following documents: db. books . insertMany ( [ { "_id" : 1 , "title" : "Dracula" , "condition" : "new" } , { "_id" : 2 , "title" : "The Little Prince" , "condition" : "new" } ]) The { $literal: 1 } expression returns a new editionNumber field set to the value 1 : db. books . aggregate ( [ { $project : { "title" : 1 , "editionNumber" : { $literal : 1 } } } ] ) The operation results in the following documents: { "_id" : 1 , "title" : "Dracula" , "editionNumber" : 1 } { "_id" : 2 , "title" : "The Little Prince" , "editionNumber" : 1 } Back $linearFill Next $ln
