# $isoWeek (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $isoWeek (aggregation) On this page Definition Behavior Example Definition $isoWeek Returns the week number in ISO 8601 format, ranging from 1 to 53 . Week numbers start at 1 with the week (Monday through
Sunday) that contains the year's first Thursday. The $isoWeek expression has the following operator expression syntax : { $isoWeek : < dateExpression > } The argument can be: An expression that resolves to a Date , a Timestamp , or an ObjectID . A document with this format: { date : < dateExpression > , timezone : < tzExpression > } Field Description date The date to which the operator is applied. <dateExpression> must be a valid expression that resolves to a Date , a Timestamp ,
or an ObjectID . timezone Optional. The timezone of the operation result. <tzExpression> must be a valid expression that resolves to a string formatted as either
an Olson Timezone Identifier or a UTC Offset .
If no timezone is provided, the result is in UTC. Format Examples Olson Timezone Identifier "America/New_York" "Europe/London" "GMT" UTC Offset +/-[hh]:[mm], e.g. "+04:45" +/-[hh][mm], e.g. "-0530" +/-[hh], e.g. "+03" Behavior Example Result { $isoWeek : { date : new Date ( "Jan 4, 2016" ) } } 1 { $isoWeek : new Date ( "2016-01-01" ) } 53 { $isoWeek : { date : new Date ( "August 14, 2011" ) , timezone : "America/Chicago" } } 32 { $isoWeek : ISODate ( "1998-11-02T00:00:00Z" ) } 45 { $isoWeek : { date : ISODate ( "1998-11-02T00:00:00Z" ) , timezone : "-0500" } } 44 { $isoWeek : "March 28, 1976" } error { $isoWeek : Date ( "2016-01-01" ) } error { $isoWeek : "2009-04-09" } error Note $isoWeek cannot take a string as an argument. Example A collection called deliveries contains the following documents: db. deliveries . insertMany ( [ { _id : 1 , date : ISODate ( "2006-10-24T00:00:00Z" ) , city : "Boston" } , { _id : 2 , date : ISODate ( "2011-08-18T00:00:00Z" ) , city : "Detroit" } ] ) The following operation returns the week number for each date field. db. deliveries . aggregate ( [ { $project : { _id : 0 , city : "$city" , weekNumber : { $isoWeek : "$date" } } } ] ) The operation returns the following results: [ { city : "Boston" , weekNumber : 43 } , { city : "Detroit" , weekNumber : 33 } ] Tip See also: $isoDayOfWeek (aggregation) $isoWeekYear (aggregation) Back $isoDayOfWeek Next $isoWeekYear