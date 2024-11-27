# Create an Index on an Embedded Field in an Array - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Multikey Create an Index on an Embedded Field in an Array On this page About this Task Procedure Results Sort Results Learn More You can create indexes on embedded document fields within arrays. These
indexes improve performance for queries on specific embedded fields that
appear in arrays. When you create an index on a field inside an array,
MongoDB stores that index as a multikey index. To create an index, use the db.collection.createIndex() method. Your operation should resemble this prototype: db. < collection > . createIndex ( { < field > : < sortOrder > } ) About this Task The example on this page uses an inventory collection that contains
these documents: db. inventory . insertMany ( [ { "item" : "t-shirt" , "stock" : [ { "size" : "small" , "quantity" : 8 } , { "size" : "large" , "quantity" : 10 } , ] } , { "item" : "sweater" , "stock" : [ { "size" : "small" , "quantity" : 4 } , { "size" : "large" , "quantity" : 7 } , ] } , { "item" : "vest" , "stock" : [ { "size" : "small" , "quantity" : 6 } , { "size" : "large" , "quantity" : 1 } ] } ] ) You need to order more inventory any time you have less than five of an
item in stock. To find which items to reorder, you query for documents
where an element in the stock array has a quantity less than 5 . To improve performance for this query, you can create an index on
the stock.quantity field. Procedure The following operation creates an ascending multikey index on the stock.quantity field of the inventory collection: db. inventory . createIndex ( { "stock.quantity" : 1 } ) Because stock contains an array value, MongoDB stores this
index as a multikey index. Results The index contains a key for each individual value that appears in the stock.quantity field. The index is ascending, meaning the keys are
stored in this order: [ 1, 4, 6, 7, 8, 10 ] . The index supports queries that select on the stock.quantity field. For
example, the following query returns documents where at least one
element in the stock array has a quantity less than 5 : db. inventory . find ( { "stock.quantity" : { $lt : 5 } } ) Output: [ { _id : ObjectId ( "63449793b1fac2ee2e957ef3" ) , item : 'vest' , stock : [ { size : 'small' , quantity : 6 } , { size : 'large' , quantity : 1 } ] } , { _id : ObjectId ( "63449793b1fac2ee2e957ef2" ) , item : 'sweater' , stock : [ { size : 'small' , quantity : 4 } , { size : 'large' , quantity : 7 } ] } ] Sort Results The index also supports sort operations on the stock.quantity field,
such as this query: db. inventory . find ( ). sort ( { "stock.quantity" : - 1 } ) Output: [ { _id : ObjectId ( "63449793b1fac2ee2e957ef1" ) , item : 't-shirt' , stock : [ { size : 'small' , quantity : 8 } , { size : 'large' , quantity : 10 } ] } , { _id : ObjectId ( "63449793b1fac2ee2e957ef2" ) , item : 'sweater' , stock : [ { size : 'small' , quantity : 4 } , { size : 'large' , quantity : 7 } ] } , { _id : ObjectId ( "63449793b1fac2ee2e957ef3" ) , item : 'vest' , stock : [ { size : 'small' , quantity : 6 } , { size : 'large' , quantity : 1 } ] } ] When sorting an array of objects, in a descending sort, MongoDB sorts
based on the field with the highest-valued element first. Note Index Sort Order Using a descending single-field index may negatively impact index
performance. For best performance, only use ascending single-field
indexes. Learn More Create a multikey index on an array of scalar values . Learn about multikey index bounds . Back Create on Array Field Next Bounds
