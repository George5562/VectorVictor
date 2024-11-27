# SQL to Aggregation Mapping Chart - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference SQL to Aggregation Mapping Chart On this page Examples The aggregation pipeline allows
MongoDB to provide native aggregation capabilities that corresponds to
many common data aggregation operations in SQL. The following table provides an overview of common SQL aggregation
terms, functions, and concepts and the corresponding MongoDB aggregation operators : SQL Terms, Functions, and Concepts MongoDB Aggregation Operators WHERE $match GROUP BY $group HAVING $match SELECT $project ORDER BY $sort LIMIT $limit SUM() $sum COUNT() $sum $sortByCount join $lookup SELECT INTO NEW_TABLE $out MERGE INTO TABLE $merge UNION ALL $unionWith For a list of all aggregation pipeline and expression operators, see: Aggregation Stages Aggregation Operators Tip See also: SQL to MongoDB Mapping Chart Examples The following table presents a quick reference of SQL aggregation
statements and the corresponding MongoDB statements. The examples in
the table assume the following conditions: The SQL examples assume two tables, orders and order_lineitem that join by the order_lineitem.order_id and
the orders.id columns. The MongoDB examples assume one collection orders that contain
documents of the following prototype: { cust_id : "abc123" , ord_date : ISODate ( "2012-11-02T17:04:11.102Z" ) , status : 'A' , price : 50 , items : [ { sku : "xxx" , qty : 25 , price : 1 } , { sku : "yyy" , qty : 25 , price : 1 } ] } SQL Example MongoDB Example Description SELECT COUNT ( * ) AS count FROM orders db. orders . aggregate ( [ { $group : { _id : null , count : { $sum : 1 } } } ] ) Count all records
from orders SELECT SUM ( price) AS total FROM orders db. orders . aggregate ( [ { $group : { _id : null , total : { $sum : "$price" } } } ] ) Sum the price field
from orders SELECT cust_id, SUM ( price) AS total FROM orders GROUP BY cust_id db. orders . aggregate ( [ { $group : { _id : "$cust_id" , total : { $sum : "$price" } } } ] ) For each unique cust_id ,
sum the price field. SELECT cust_id, SUM ( price) AS total FROM orders GROUP BY cust_id ORDER BY total db. orders . aggregate ( [ { $group : { _id : "$cust_id" , total : { $sum : "$price" } } } , { $sort : { total : 1 } } ] ) For each unique cust_id ,
sum the price field,
results sorted by sum. SELECT cust_id, ord_date, SUM ( price) AS total FROM orders GROUP BY cust_id, ord_date db. orders . aggregate ( [ { $group : { _id : { cust_id : "$cust_id" , ord_date : { $dateToString : { format : "%Y-%m-%d" , date : "$ord_date" }} } , total : { $sum : "$price" } } } ] ) For each unique cust_id , ord_date grouping,
sum the price field.
Excludes the time portion of the date. SELECT cust_id, count ( * ) FROM orders GROUP BY cust_id HAVING count ( * ) > 1 db. orders . aggregate ( [ { $group : { _id : "$cust_id" , count : { $sum : 1 } } } , { $match : { count : { $gt : 1 } } } ] ) For cust_id with multiple records,
return the cust_id and
the corresponding record count. SELECT cust_id, ord_date, SUM ( price) AS total FROM orders GROUP BY cust_id, ord_date HAVING total > 250 db. orders . aggregate ( [ { $group : { _id : { cust_id : "$cust_id" , ord_date : { $dateToString : { format : "%Y-%m-%d" , date : "$ord_date" }} } , total : { $sum : "$price" } } } , { $match : { total : { $gt : 250 } } } ] ) For each unique cust_id , ord_date grouping, sum the price field
and return only where the
sum is greater than 250.
Excludes the time portion of the date. SELECT cust_id, SUM ( price) as total FROM orders WHERE status = 'A' GROUP BY cust_id db. orders . aggregate ( [ { $match : { status : 'A' } } , { $group : { _id : "$cust_id" , total : { $sum : "$price" } } } ] ) For each unique cust_id with status A ,
sum the price field. SELECT cust_id, SUM ( price) as total FROM orders WHERE status = 'A' GROUP BY cust_id HAVING total > 250 db. orders . aggregate ( [ { $match : { status : 'A' } } , { $group : { _id : "$cust_id" , total : { $sum : "$price" } } } , { $match : { total : { $gt : 250 } } } ] ) For each unique cust_id with status A ,
sum the price field and return
only where the
sum is greater than 250. SELECT cust_id, SUM ( li.qty) as qty FROM orders o, order_lineitem li WHERE li.order_id = o.id GROUP BY cust_id db. orders . aggregate ( [ { $unwind : "$items" } , { $group : { _id : "$cust_id" , qty : { $sum : "$items.qty" } } } ] ) For each unique cust_id ,
sum the corresponding
line item qty fields
associated with the
orders. SELECT COUNT ( * ) FROM ( SELECT cust_id, ord_date FROM orders GROUP BY cust_id, ord_date) as DerivedTable db. orders . aggregate ( [ { $group : { _id : { cust_id : "$cust_id" , ord_date : { $dateToString : { format : "%Y-%m-%d" , date : "$ord_date" }} } } } , { $group : { _id : null , count : { $sum : 1 } } } ] ) Count the number of distinct cust_id , ord_date groupings.
Excludes the time portion of the date. Tip See also: SQL to MongoDB Mapping Chart db.collection.aggregate() Aggregation Stages Back Variables Next Map-Reduce
