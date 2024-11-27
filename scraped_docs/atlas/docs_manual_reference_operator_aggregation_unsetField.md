# $unsetField (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $unsetField (aggregation) On this page Definition Syntax Behavior Examples Definition $unsetField New in version 5.0 . Removes a specified field in a document. You can use $unsetField to remove fields with names
that contain periods ( . ) or that start with dollar signs
( $ ). $unsetField is an alias for $setField using $$REMOVE to remove fields. Syntax $unsetField has the following syntax: { $unsetField : { field : < String > , input : < Object > , } } You must provide the following fields: Field Type Description field String Field in the input object that you want to add, update, or
remove. field can be any valid expression that resolves to a string
constant. input Object Document that contains the field that you want to add or
update. input must resolve to an object, missing , null , or undefined . Behavior If input evaluates to missing , undefined , or null , $unsetField returns null and does not update input . If input evaluates to anything other than an object, missing , undefined , or null , $unsetField returns an
error. If field resolves to anything other than a string constant, $unsetField returns an error. If field doesn't exist in input , $unsetField adds it. $unsetField doesn't implicitly traverse objects or
arrays. For example, $unsetField evaluates a field value of "a.b.c" as a top-level field "a.b.c" instead of as a
nested field, { "a": { "b": { "c": } } } . Examples Remove Fields that Contain Periods ( . ) Consider the inventory collection: db. inventory . insertMany ( [ { _id : 1 , item : "sweatshirt" , qty : 300 , "price.usd" : 45.99 } , { _id : 2 , item : "winter coat" , qty : 200 , "price.usd" : 499.99 } , { _id : 3 , item : "sun dress" , qty : 250 , "price.usd" : 199.99 } , { _id : 4 , item : "leather boots" , qty : 300 , "price.usd" : 249.99 } , { _id : 5 , item : "bow tie" , qty : 180 , "price.usd" : 9.99 } ] ) Use the $replaceWith pipeline stage and the $unsetField operator to remove the "price.usd" field
from each document: db. inventory . aggregate ( [ { $replaceWith : { $unsetField : { field : "price.usd" , input : "$$ROOT" } } } ] ) The operation returns the following results: [ { _id : 1 , item : 'sweatshirt' , qty : 300 } , { _id : 2 , item : 'winter coat' , qty : 200 } , { _id : 3 , item : 'sun dress' , qty : 250 } , { _id : 4 , item : 'leather boots' , qty : 300 } , { _id : 5 , item : 'bow tie' , qty : 180 } ] Remove Fields that Start with a Dollar Sign ( $ ) Consider the inventory collection: db. inventory . insertMany ( [ { _id : 1 , item : "sweatshirt" , qty : 300 , "$price" : 45.99 } , { _id : 2 , item : "winter coat" , qty : 200 , "$price" : 499.99 } , { _id : 3 , item : "sun dress" , qty : 250 , "$price" : 199.99 } , { _id : 4 , item : "leather boots" , qty : 300 , "$price" : 249.99 } , { _id : 5 , item : "bow tie" , qty : 180 , "$price" : 9.99 } ] ) Use the $replaceWith pipeline stage with the $unsetField and $literal operators to
remove the "$price" field from each document: db. inventory . aggregate ( [ { $replaceWith : { $unsetField : { field : { $literal : "$price" } , input : "$$ROOT" } } } ] ) The operation returns the following results: [ { _id : 1 , item : 'sweatshirt' , qty : 300 } , { _id : 2 , item : 'winter coat' , qty : 200 } , { _id : 3 , item : 'sun dress' , qty : 250 } , { _id : 4 , item : 'leather boots' , qty : 300 } , { _id : 5 , item : 'bow tie' , qty : 180 } ] Remove A Subfield Consider the inventory collection: db. inventory . insertMany ( [ { _id : 1 , item : "sweatshirt" , qty : 300 , "price" : { "usd" : 45.99 , "euro" : 38.77 } } , { _id : 2 , item : "winter coat" , qty : 200 , "price" : { "usd" : 499.99 , "euro" : 420.51 } } , { _id : 3 , item : "sun dress" , qty : 250 , "price" : { "usd" : 199.99 , "euro" : 167.70 } } , { _id : 4 , item : "leather boots" , qty : 300 , "price" : { "usd" : 249.99 , "euro" : 210.68 } } , { _id : 5 , item : "bow tie" , qty : 180 , "price" : { "usd" : 9.99 , "euro" : 8.42 } } ] ) The "price" field contains a document with two subfields, "usd" and "euro" . You cannot use "price.euro" to identify and remove "euro" because MongoDB parses "price.euro" as a top level field
name that happens to contain a period ( . ). Use the $replaceWith pipeline stage with $setField and a nested $unsetField operation to remove the "euro" field: db. inventory . aggregate ( [ { $replaceWith : { $setField : { field : "price" , input : "$$ROOT" , value : { $unsetField : { field : "euro" , input : { $getField : "price" } } } } } } ] ) The operation returns the following results: [ { _id : 1 , item : "sweatshirt" , qty : 300 , price : { usd : 45.99 } } , { _id : 2 , item : "winter coat" , qty : 200 , price : { usd : 499.99 } } , { _id : 3 , item : "sun dress" , qty : 250 , price : { usd : 199.99 } } , { _id : 4 , item : "leather boots" , qty : 300 , price : { usd : 249.99 } } , { _id : 5 , item : "bow tie" , qty : 180 , price : { usd : 9.99 } } ] Tip See also: $setField Back $type Next $week