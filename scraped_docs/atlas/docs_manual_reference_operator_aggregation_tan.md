# $tan (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $tan (aggregation) On this page Behavior Example $tan Returns the tangent of a value that is measured in radians. $tan has the following syntax: { $tan : < expression > } $tan takes any valid expression that resolves to a number. If the
expression returns a value in degrees, use the $degreesToRadians operator to convert the
result to radians. By default $tan returns values as a double . $tan can also return values as a 128-bit decimal as long as the <expression> resolves to a 128-bit decimal value. For more information on expressions, see Expression Operators . Behavior null , NaN , and +/- Infinity If the argument resolves to a value of null or refers to a field
that is missing, $tan returns null . If the
argument resolves to NaN , $tan returns NaN .
If the argument resolves to negative or positive infinity, $tan throws an error. Example Results { $tan: NaN } NaN { $tan: null } null { $tan : Infinity} or { $tan : -Infinity } Throws an error message resembling the following formatted
output: "errmsg" : "Failed to optimize pipeline :: caused by :: cannot apply $tan to -inf, value must in (-inf,inf)" Example Tangent of Value in Degrees Tangent of Value in Radians The trigonometry collection contains a document that
stores one side and one angle in a right-angle triangle: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "angle_a" : NumberDecimal( "53.13010235415597870314438744090659" ), "side_a" : NumberDecimal( "3" ) } The following aggregation operation uses the $tan expression to calculate the side opposite
to angle_a and add it to the input document using the $addFields pipeline stage. db.trigonometry.aggregate([ { $addFields : { "side_b" : { $multiply : [ { $tan : { $degreesToRadians : " $angle_a " } }, " $side_a " ] } } } ]) The $degreesToRadians expression converts the
degree value of angle_a to the equivalent value in radians. The command returns the following output: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "angle_a" : NumberDecimal( "53.13010235415597870314438744090659" ), "side_a" : NumberDecimal( "3" ) "side_b" : NumberDecimal(4.000000000000000000000000000000000 ") } Since angle_a and side_a are stored as 128-bit decimals , the output of $tan is a 128-bit decimal. The trigonometry collection contains a document that
stores the hypotenuse and one angle in a right-angle triangle: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "angle_a" : NumberDecimal( "0.9272952180016122324285124629224288" ), "side_a" : NumberDecimal( "3" ) } The following aggregation operation uses the $tan expression to calculate the side adjacent
to angle_a and add it to the input document using the $addFields pipeline stage. db.trigonometry.aggregate([ { $addFields : { "side_b" : { $multiply : [ { $tan : " $angle_a " }, " $side_a " ] } } } ]) The command returns the following output: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "angle_a" : NumberDecimal( "0.9272952180016122324285124629224288" ), "side_a" : NumberDecimal( "3" ) "side_b" : NumberDecimal( "3.999999999999999999999999999999999" ) } Since angle_a and side_a are stored as 128-bit decimals , the output of $tan is a 128-bit decimal. Back $switch Next $tanh