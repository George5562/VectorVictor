# $derivative (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $derivative (aggregation) On this page Definition Behavior Example Definition New in version 5.0 . $derivative Returns the average rate of change within the specified window , which is calculated using the: First and last documents in the $setWindowFields stage window . Numerator, which is set to the result of subtracting the numeric expression value for the first
document from the expression value
for the last document. Denominator, which is set to the result of subtracting the sortBy field value for the first
document from the sortBy field value
for the last document. $derivative is only available in the $setWindowFields stage. You must specify a window in the $setWindowFields stage when
using $derivative . $derivative syntax: { $derivative: { input: <expression>, unit: <time unit> } } $derivative takes a document with these fields: Field Description input Specifies the expression to
evaluate. The expression must evaluate to a number. unit A string that specifies the time unit. Use one of these
strings: "week" "day" "hour" "minute" "second" "millisecond" If the sortBy field is not a date, you
must omit a unit . If you specify a unit , you must specify a date
in the sortBy field. Behavior You must specify a window in the $setWindowFields stage when using $derivative . Example Create a deliveryFleet collection that contains odometer
readings for delivery trucks recorded at 30 second intervals: db. deliveryFleet . insertMany ( [ { truckID : "1" , timeStamp : new Date ( "2020-05-18T14:10:30Z" ) , miles : 1295.1 } , { truckID : "1" , timeStamp : new Date ( "2020-05-18T14:11:00Z" ) , miles : 1295.63 } , { truckID : "1" , timeStamp : new Date ( "2020-05-18T14:11:30Z" ) , miles : 1296.25 } , { truckID : "1" , timeStamp : new Date ( "2020-05-18T14:12:00Z" ) , miles : 1296.76 } , { truckID : "2" , timeStamp : new Date ( "2020-05-18T14:10:30Z" ) , miles : 10234.1 } , { truckID : "2" , timeStamp : new Date ( "2020-05-18T14:11:00Z" ) , miles : 10234.33 } , { truckID : "2" , timeStamp : new Date ( "2020-05-18T14:11:30Z" ) , miles : 10234.73 } , { truckID : "2" , timeStamp : new Date ( "2020-05-18T14:12:00Z" ) , miles : 10235.13 } ] ) This example uses $derivative in the $setWindowFields stage to obtain the average speed in miles
per hour for each truck, and the $match stage to filter the
results to trucks whose speed exceeded 50 miles per hour: db. deliveryFleet . aggregate ( [ { $setWindowFields : { partitionBy : "$truckID" , sortBy : { timeStamp : 1 } , output : { truckAverageSpeed : { $derivative : { input : "$miles" , unit : "hour" } , window : { range : [ - 30 , 0 ] , unit : "second" } } } } } , { $match : { truckAverageSpeed : { $gt : 50 } } } ] ) In the example: The $setWindowFields stage obtains the average speed in
miles per hour for each truck: partitionBy: "$truckID" partitions the documents in the collection by truckID . sortBy: { timeStamp: 1 } sorts the documents in each partition by timeStamp in ascending order ( 1 ), so the earliest
odometer reading is first. output sets the miles derivative value in a new
field called truckAverageSpeed using $derivative that
is run in a range window. The input expression is set to "$miles" , which is used in the numerator for the derivative
calculation. The $derivative unit is set to "hour" for the timeStamp field, which is used in the
denominator for the derivative calculation. The window contains the range between a lower limit of -30 seconds (the previous 30 seconds from the current
document in the output) and 0 seconds (matches the current
document's timeStamp value in the output). This means $derivative returns the average speed for each truck in
miles per hour in the 30 second window. The $match stage uses the greater than operator $gt to filter the results to trucks whose speed exceeded
50 miles per hour. In the following example output, the speed for truck 1 is shown in the truckAverageSpeed field. The speed for truck 2 is not shown because
truck 2 did not exceed 50 miles per hour. { "_id" : ObjectId ( "60cb8a7e833dfeadc8e6285c" ) , "truckID" : "1" , "timeStamp" : ISODate ( "2020-05-18T14:11:00Z" ) , "miles" : 1295.63 , "truckAverageSpeed" : 63.60000000002401 } { "_id" : ObjectId ( "60cb8a7e833dfeadc8e6285d" ) , "truckID" : "1" , "timeStamp" : ISODate ( "2020-05-18T14:11:30Z" ) , "miles" : 1296.25 , "truckAverageSpeed" : 74.3999999999869 } { "_id" : ObjectId ( "60cb8a7e833dfeadc8e6285e" ) , "truckID" : "1" , "timeStamp" : ISODate ( "2020-05-18T14:12:00Z" ) , "miles" : 1296.76 , "truckAverageSpeed" : 61.199999999998916 } Back $denseRank Next $divide
