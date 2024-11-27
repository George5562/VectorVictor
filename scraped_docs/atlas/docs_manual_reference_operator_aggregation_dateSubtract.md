# $dateSubtract (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $dateSubtract (aggregation) On this page Definition Behavior Examples Definition $dateSubtract New in version 5.0 . Decrements a Date() object by a
specified number of time units. The $dateSubtract expression has the following syntax: { $dateSubtract : { startDate : < Expression > , unit : < Expression > , amount : < Expression > , timezone : < tzExpression > } } Returns a Date() . The startDate can be any expression that
resolves to type Date, Timestamp or ObjectId. No matter which data
type is used as input, the value returned will be a Date() object. Field Required/Optional Description startDate Required The beginning date, in UTC, for the subtraction operation.
The startDate can be any expression that resolves to
a Date , a Timestamp ,
or an ObjectID . unit Required The unit used to measure the amount of time
subtracted from the startDate . The unit is an expression that resolves to
one of the following strings: year quarter week month day hour minute second millisecond amount Required The number of units subtracted from the startDate .
The amount is an expression that resolves to
an integer or long. The amount can also resolve to an
integral decimal and or a double if that value can be
converted to a long without loss of precision. timezone Optional The timezone to carry out the operation. <tzExpression> must be a
valid expression that resolves to a
string formatted as either an Olson Timezone Identifier or a UTC Offset .
If no timezone is provided, the result is displayed in UTC . Format Examples Olson Timezone Identifier "America/New_York" "Europe/London" "GMT" UTC Offset + /- [hh]:[mm], e.g. "+04:45" + /- [hh][mm], e.g. "-0530" + /- [hh], e.g. "+03" For more information on expressions and types see Expression Operators and BSON Types . Behavior Time Measurement MongoDB follows prevaling database usage and works with time in UTC. The dateSubtract expression always takes a startDate in UTC and
returns a result in UTC. If the timezone is specified, the
calculation will be done using the specified timezone . The timezone
is especially important when a calculation involves Daylight Savings
Time (DST). If the unit is a month , or larger the operation adjusts to
account for the last day of the month. Subtracting one month on the
last day of March, for example, demonstrates the
"last-day-of-the-month" adjustment. { $dateSubtract : { startDate : ISODate ( "2021-03-31T12:10:05Z" ) , unit : "month" , amount : 1 } } Notice that the date returned, ISODate("2021-02-28T12:10:05Z") , is
the 28th and not the 31st since February has fewer days than March. Time Zone When using an Olson Timezone Identifier in the <timezone> field, MongoDB applies the DST offset
if applicable for the specified timezone. For example, consider a sales collection with the following document: { "_id" : 1 , "item" : "abc" , "price" : 20 , "quantity" : 5 , "date" : ISODate ( "2017-05-20T10:24:51.303Z" ) } The following aggregation illustrates how MongoDB handles the DST
offset for the Olson Timezone Identifier. The example uses the $hour and $minute operators to return the
corresponding portions of the date field: db. sales . aggregate ( [ { $project : { "nycHour" : { $hour : { date : "$date" , timezone : "-05:00" } } , "nycMinute" : { $minute : { date : "$date" , timezone : "-05:00" } } , "gmtHour" : { $hour : { date : "$date" , timezone : "GMT" } } , "gmtMinute" : { $minute : { date : "$date" , timezone : "GMT" } } , "nycOlsonHour" : { $hour : { date : "$date" , timezone : "America/New_York" } } , "nycOlsonMinute" : { $minute : { date : "$date" , timezone : "America/New_York" } } } }]) The operation returns the following result: { "_id" : 1 , "nycHour" : 5 , "nycMinute" : 24 , "gmtHour" : 10 , "gmtMinute" : 24 , "nycOlsonHour" : 6 , "nycOlsonMinute" : 24 } Examples Subtract A Fixed Amount Consider a collection of system connection times like these: db. connectionTime . insertMany ( [ { custId : 457 , login : ISODate ( "2020-12-25T19:04:00" ) , logout : ISODate ( "2020-12-28T09:04:00" ) } , { custId : 457 , login : ISODate ( "2021-01-27T05:12:00" ) , logout : ISODate ( "2021-01-28T13:05:00" ) } , { custId : 458 , login : ISODate ( "2021-01-22T06:27:00" ) , logout : ISODate ( "2021-01-31T11:00:00" ) } , { custId : 459 , login : ISODate ( "2021-02-14T20:14:00" ) , logout : ISODate ( "2021-02-17T16:05:00" ) } , { custId : 460 , login : ISODate ( "2021-02-26T02:44:00" ) , logout : ISODate ( "2021-02-18T14:13:00" ) } ] ) Due to a service issue you need to subtract 3 hours from each of the
January 2021 logout times. You can use $dateSubtract in an
aggregation pipeline to decrement the logoutTime . db. connectionTime . aggregate ( [ { $match : { $expr : { $eq : [ { $year : "$logout" } , 2021 ] } , $expr : { $eq : [ { $month : "$logout" } , 1 ] } } } , { $project : { logoutTime : { $dateSubtract : { startDate : "$logout" , unit : "hour" , amount : 3 } } } } , { $merge : "connectionTime" } ] ) Two similar comparisons are made in the $match stage. First
the $year and $month operators extract the
year and month, respectively, from the logoutTime Date object. Then
the month and year are checked to see if they match the selection
targets. Since "January" is encoded as "1", $expr is true when
the year and month are equal ( $eq ) to "2021" and "1". The $project stage uses $dateSubtract to subtract 3
hours from the logoutTime of each selected dcoument. Finaly, the $merge stage updates the collection, writing
the new logoutTime for the modified documents. Note Unlike $out , the $merge stage only updates the
matched documents and preserves the rest of the collection. For more
details see: $out compared with $merge . The resulting documents look like this: { "_id" : ObjectId ( "603dd94b044b995ad331c0b5" ) , "custId" : 457 , "login" : ISODate ( "2020-12-25T19:04:00Z" ) , "logout" : ISODate ( "2020-12-28T09:04:00Z" ) } { "_id" : ObjectId ( "603dd94b044b995ad331c0b6" ) , "custId" : 457 , "login" : ISODate ( "2021-01-27T05:12:00Z" ) , "logout" : ISODate ( "2021-01-28T13:05:00Z" ) , "logoutTime" : ISODate ( "2021-01-28T10:05:00Z" ) } { "_id" : ObjectId ( "603dd94b044b995ad331c0b7" ) , "custId" : 458 , "login" : ISODate ( "2021-01-22T06:27:00Z" ) , "logout" : ISODate ( "2021-01-31T11:00:00Z" ) , "logoutTime" : ISODate ( "2021-01-31T08:00:00Z" ) } { "_id" : ObjectId ( "603dd94b044b995ad331c0b8" ) , "custId" : 459 , "login" : ISODate ( "2021-02-14T20:14:00Z" ) , "logout" : ISODate ( "2021-02-17T16:05:00Z" ) } { "_id" : ObjectId ( "603dd94b044b995ad331c0b9" ) , "custId" : 460 , "login" : ISODate ( "2021-02-26T02:44:00Z" ) , "logout" : ISODate ( "2021-02-18T14:13:00Z" ) } Filter by Relative Dates You want to send a survey to clients who have used your service in the
past week. The $dateSubtract expression can create a range filter
relative to the time the query is executed. db. connectionTime . aggregate ( [ { $match : { $expr : { $gt : [ "$logoutTime" , { $dateSubtract : { startDate : "$$NOW" , unit : "week" , amount : 1 } } ] } } } , { $project : { _id : 0 , custId : 1 , loggedOut : { $dateToString : { format : "%Y-%m-%d" , date : "$logoutTime" } } } } ] ) The built in aggregation variable $$NOW returns the
current datetime in ISODate format. The $match stage uses the value in $$NOW to get today's date.
Then the comparison expression ( $expr ) filters the collection
using greater than ( $gt ) and $dateSubtract to match
documents that have a logoutTime in the past week. The $project stage uses the $dateToString expression to convert the dates to a more readable format. Without the
conversion, MongoDB returns the date in ISODate format and
assumes a UTC timezone. The output shows two customers have logged out in the last week. { "custId" : 459 , "loggedOut" : "2021-02-17" } { "custId" : 460 , "loggedOut" : "2021-02-18" } Adjust for Daylight Savings Time All dates are stored internally in UTC time. When a timezone is
specified, $dateSubtract uses local time to carry out the
calculations. The results are displayed in UTC. You have customers in several timezones and you want to see what effect
daylight savings time might have on your billing periods if you bill by day or by hour . Create this collection of connection times: db. billing . insertMany ( [ { location : "America/New_York" , login : ISODate ( "2021-03-14T10:00:00-0500" ) , logout : ISODate ( "2021-03-14T18:00:00-0500" ) } , { location : "America/Mexico_City" , login : ISODate ( "2021-03-14T10:00:00-00:00" ) , logout : ISODate ( "2021-03-15T08:00:00-0500" ) } ] ) First subtract 1 day, then subtract 24 hours from the login dates
in each document. db. billing . aggregate ( [ { $project : { _id : 0 , location : 1 , start : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : "$login" } } , days : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : { $dateSubtract : { startDate : "$login" , unit : "day" , amount : 1 , timezone : "$location" } } } } , hours : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : { $dateSubtract : { startDate : "$login" , unit : "hour" , amount : 24 , timezone : "$location" } } } } , startTZInfo : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : "$login" , timezone : "$location" } } , daysTZInfo : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : { $dateSubtract : { startDate : "$login" , unit : "day" , amount : 1 , timezone : "$location" } } , timezone : "$location" } } , hoursTZInfo : { $dateToString : { format : "%Y-%m-%d %H:%M" , date : { $dateSubtract : { startDate : "$login" , unit : "hour" , amount : 24 , timezone : "$location" } } , timezone : "$location" } } , } } ] ). pretty ( ) The $dateToString expression reformats the output for
readability. Results are summarized here: Field New York Mexico City Start 2021-03-14 15:00 2021-03-14 15:00 Start, TZ Info 2021-03-14 11:00 2021-03-14 04:00 1 Day 2021-03-13 16:00 2021-03-13 15:00 1 Day, TZInfo 2021-03-13 11:00 2021-03-13 09:00 24 Hours 2021-03-13 15:00 2021-03-13 15:00 24 Hours, TZInfo 2021-03-13 10:00 2021-03-13 09:00 The chart highlights several points: Unformatted dates are returned in UTC. The $login for New York is
UTC -5, however the start , days , and hours rows display
the time in UTC. March 14th is the start of DST in New York, but not in Mexico. The
calculated time is adjusted when a location switches to DST and
crosses from one day to the next. DST modifies the length of the day , not the hour . There is no
DST change for hours . There is an only an adjustment for DST when
the measurement unit is day or larger and the computation
crosses a clock change in the specified timezone . Tip See also: $dateAdd , $dateDiff Back $dateFromString Next $dateToParts
