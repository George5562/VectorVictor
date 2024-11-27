# $dateAdd (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $dateAdd (aggregation) On this page Definition Behavior Examples Definition $dateAdd New in version 5.0 . Increments a Date() object by a
specified number of time units. The $dateAdd expression has the following syntax: { $dateAdd : { startDate : < Expression > , unit : < Expression > , amount : < Expression > , timezone : < tzExpression > } } Returns a Date() . The startDate can be any expression that
resolves to type Date, Timestamp or ObjectId. No matter which data
type is used as input, the value returned will be a Date() object. Field Required/Optional Description startDate Required The beginning date, in UTC, for the addition operation. The startDate can be any expression that resolves to
a Date , a Timestamp ,
or an ObjectID . unit Required The unit used to measure the amount of time added to
the startDate . The unit is an expression that resolves to
one of the following strings: year quarter week month day hour minute second millisecond amount Required The number of units added to the startDate . The amount is an expression that resolves to an integer or long. The amount can also
resolve to an integral decimal or a double if that value can
be converted to a long without loss of precision. timezone Optional The timezone to carry out the operation. <tzExpression> must be a
valid expression that resolves to a
string formatted as either an Olson Timezone Identifier or a UTC Offset .
If no timezone is provided, the result is displayed in UTC . Format Examples Olson Timezone Identifier "America/New_York" "Europe/London" "GMT" UTC Offset + /- [hh]:[mm], e.g. "+04:45" + /- [hh][mm], e.g. "-0530" + /- [hh], e.g. "+03" For more information on expressions and types see Expression Operators and BSON Types . Behavior Time Measurement MongoDB follows prevaling database usage and works with time in UTC. The dateAdd expression always takes a startDate in UTC and returns
a result in UTC. If the timezone is specified, the calculation will
be done using the specified timezone . The timezone is especially
important when a calculation involves Daylight Savings Time (DST). If the unit is a month , or larger the operation adjusts to
account for the last day of the month. Adding one month on the last
day of October, for example, demonstrates the "last-day-of-the-month"
adjustment. { $dateAdd : { startDate : ISODate ( "2020-10-31T12:10:05Z" ) , unit : "month" , amount : 1 } } Notice that the date returned, ISODate("2020-11-30T12:10:05Z") , is
the 30th and not the 31st since November has fewer days than October. Time Zone When using an Olson Timezone Identifier in the <timezone> field, MongoDB applies the DST offset
if applicable for the specified timezone. For example, consider a sales collection with the following document: { "_id" : 1 , "item" : "abc" , "price" : 20 , "quantity" : 5 , "date" : ISODate ( "2017-05-20T10:24:51.303Z" ) } The following aggregation illustrates how MongoDB handles the DST
offset for the Olson Timezone Identifier. The example uses the $hour and $minute operators to return the
corresponding portions of the date field: db. sales . aggregate ( [ { $project : { "nycHour" : { $hour : { date : "$date" , timezone : "-05:00" } } , "nycMinute" : { $minute : { date : "$date" , timezone : "-05:00" } } , "gmtHour" : { $hour : { date : "$date" , timezone : "GMT" } } , "gmtMinute" : { $minute : { date : "$date" , timezone : "GMT" } } , "nycOlsonHour" : { $hour : { date : "$date" , timezone : "America/New_York" } } , "nycOlsonMinute" : { $minute : { date : "$date" , timezone : "America/New_York" } } } }]) The operation returns the following result: { "_id" : 1 , "nycHour" : 5 , "nycMinute" : 24 , "gmtHour" : 10 , "gmtMinute" : 24 , "nycOlsonHour" : 6 , "nycOlsonMinute" : 24 } Examples Add a Future Date Consider a collection of customer orders with these documents: db. shipping . insertMany ( [ { custId : 456 , purchaseDate : ISODate ( "2020-12-31" ) } , { custId : 457 , purchaseDate : ISODate ( "2021-02-28" ) } , { custId : 458 , purchaseDate : ISODate ( "2021-02-26" ) } ] ) The normal shipping time is 3 days. You can use $dateAdd in an
aggregation pipeline to set an expectedDeliveryDate 3 days in the
future. db. shipping . aggregate ( [ { $project : { expectedDeliveryDate : { $dateAdd : { startDate : "$purchaseDate" , unit : "day" , amount : 3 } } } } , { $merge : "shipping" } ] ) After adding 3 days to the purchaseDate with $dateAdd in the $project stage, the $merge stage updates the
original documents with the expectedDeliveryDate . The resulting documents look like this: { "_id" : ObjectId ( "603dd4b2044b995ad331c0b2" ) , "custId" : 456 , "purchaseDate" : ISODate ( "2020-12-31T00:00:00Z" ) , "expectedDeliveryDate" : ISODate ( "2021-01-03T00:00:00Z" ) } { "_id" : ObjectId ( "603dd4b2044b995ad331c0b3" ) , "custId" : 457 , "purchaseDate" : ISODate ( "2021-02-28T00:00:00Z" ) , "expectedDeliveryDate" : ISODate ( "2021-03-03T00:00:00Z" ) } { "_id" : ObjectId ( "603dd4b2044b995ad331c0b4" ) , "custId" : 458 , "purchaseDate" : ISODate ( "2021-02-26T00:00:00Z" ) , "expectedDeliveryDate" : ISODate ( "2021-03-01T00:00:00Z" ) } Filter on a Date Range Update the shipping collection from the last example with this code
to add delivery dates to the documents: db. shipping . updateOne ( { custId : 456 } , { $set : { deliveryDate : ISODate ( "2021-01-10" ) } } ) db. shipping . updateOne ( { custId : 457 } , { $set : { deliveryDate : ISODate ( "2021-03-01" ) } } ) db. shipping . updateOne ( { custId : 458 } , { $set : { deliveryDate : ISODate ( "2021-03-02" ) } } ) You want to find late shipments. Use $dateAdd in a $match stage to create a filter that matches documents in a
range of dates defined by a starting point ( $purchaseDate ) and a
time period given by $dateAdd . db. shipping . aggregate ( [ { $match : { $expr : { $gt : [ "$deliveryDate" , { $dateAdd : { startDate : "$purchaseDate" , unit : "day" , amount : 5 } } ] } } } , { $project : { _id : 0 , custId : 1 , purchased : { $dateToString : { format : "%Y-%m-%d" , date : "$purchaseDate" } } , delivery : { $dateToString : { format : "%Y-%m-%d" , date : "$deliveryDate" } } } } ] ) The $match stage uses $gt and $dateAdd in
an expression ( $expr ) to compare the actual deliveryDate with an expected date. Documents with delivery dates more than 5 days
after the purchaseDate are passed on to the $project stage. The $project stage uses the $dateToString expression to convert the dates to a more readable format. Without the
conversion, MongoDB returns the date in ISODate format and
assumes a UTC timezone. In this example only one record is returned: { "custId" : 456 , "purchased" : "2020-12-31" , "delivery" : "2021-01-10" } Adjust for Daylight Savings Time All dates are stored internally in UTC time. When a timezone is
specified, $dateAdd uses local time to carry out the calculations.
The results are displayed in UTC. You have customers in several timezones and you want to see what effect
daylight savings time might have on your billing periods if you bill by day or by hour . Create this collection of connection times: db. billing . insertMany ( [ { location : "America/New_York" , login : ISODate ( "2021-03-13T10:00:00-0500" ) , logout : ISODate ( "2021-03-14T18:00:00-0500" ) } , { location : "America/Mexico_City" , login : ISODate ( "2021-03-13T10:00:00-00:00" ) , logout : ISODate ( "2021-03-14T08:00:00-0500" ) } ] ) First add 1 day, then add 24 hours to the login dates in each
document. db. billing . aggregate ( [ { $project : { _id : 0 , location : 1 , start : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : "$login" } } , days : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : { $dateAdd : { startDate : "$login" , unit : "day" , amount : 1 , timezone : "$location" } } } } , hours : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : { $dateAdd : { startDate : "$login" , unit : "hour" , amount : 24 , timezone : "$location" } } } } , startTZInfo : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : "$login" , timezone : "$location" } } , daysTZInfo : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : { $dateAdd : { startDate : "$login" , unit : "day" , amount : 1 , timezone : "$location" } } , timezone : "$location" } } , hoursTZInfo : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : { $dateAdd : { startDate : "$login" , unit : "hour" , amount : 24 , timezone : "$location" } } , timezone : "$location" } } , } } ] ). pretty ( ) The $dateToString expression reformats the output for
readability. Results are summarized here: Field New York Mexico City Start 2021-03-13 15:00 2021-03-13 10:00 Start, TZ Info 2021-03-13 10:00 2021-03-13 04:00 1 Day 2021-03-14 14:00 2021-03-14 10:00 1 Day, TZ Info 2021-03-14 10:00 2021-03-14 04:00 24 Hours 2021-03-14 15:00 2021-03-14 10:00 24 Hours, TZ Info 2021-03-14 11:00 2021-03-14 04:00 The chart highlights several points: Unformatted dates are returned in UTC. The $login for New York is
UTC -5, however the start , days , and hours rows display
the time in UTC. March 14th is the start of DST in New York, but not in Mexico. The
calculated time is adjusted when a location switches to DST and
crosses from one day to the next. DST modifies the length of the day , not the hour . There is no
DST change for hours . There is an only an adjustment for DST when
the measurement unit is day or larger and the computation
crosses a clock change in the specified timezone . Tip See also: $dateSubtract , $dateDiff Back $covarianceSamp Next $dateDiff