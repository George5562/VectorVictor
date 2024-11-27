# $sinh (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $sinh (aggregation) On this page Behavior Example $sinh Returns the hyperbolic sine of a value that is measured in radians. $sinh has the following syntax: { $sinh : < expression > } $sinh takes any valid expression that resolves to a number, measured in
radians. If the expression returns a value in degrees, use the $degreesToRadians operator to convert the value to
radians. By default $sinh returns values as a double . $sinh can also return values as a 128-bit decimal if the <expression> resolves to a 128-bit
decimal value. For more information on expressions, see Expression Operators . Behavior null , NaN , and +/- Infinity If the input argument resolves to a value of null or refers to a
field that is missing, $sinh returns null . If the
argument resolves to NaN , $sinh returns NaN . If
the argument resolves to negative or positive Infinity , $sinh returns negative or positive Infinity respectively. Example Results { $sinh: NaN } NaN { $sinh: null } null { $sinh: -Infinity } -Infinity { $sinh: Infinity } Infinity Example Hyperbolic Sine of Value in Degrees Hyperbolic Sine of Value in Radians The following trigonometry collection contains a document
that stores an angle value measured in degrees: db. trigonometry . insertOne ( { "_id" : ObjectId ( "5c50782193f833234ba90d25" ) , "angle" : NumberDecimal ( "53.1301023541559787031443874490659" ) } ) The following aggregation operation uses the $sinh expression to calculate the hyperbolic sine
of angle and adds it to the input document using the $addFields pipeline stage: db. trigonometry . aggregate ( [ { $addFields : { "sinh_output" : { $sinh : { $degreesToRadians : "$angle" } } } } ] ) The $degreesToRadians expression converts the angle in degrees to radians. Example output: { "_id" : ObjectId ( "5c50782193f833234ba90d25" ) , "angle" : NumberDecimal ( "53.1301023541559787031443874490659" ) , "sinh_output" : NumberDecimal ( "1.066020404405732132503284522731829" ) } Because angle is stored as a 128-bit decimal , the $sinh output is also a
128-bit decimal. The following trigonometry collection contains a document
that stores an angle value measured in radians: db. trigonometry . insertOne ( { "_id" : ObjectId ( "5c50782193f833234ba90d35" ) , "angle" : NumberDecimal ( "1.6301023541559787031443874490659" ) } ) The following aggregation operation uses the $sinh expression to calculate the hyperbolic sine
of angle and adds it to the input document using the $addFields pipeline stage: db. trigonometry . aggregate ( [ { $addFields : { "sinh_output" : { $sinh : "$angle" } } } ] ) Example output: { "_id" : ObjectId ( "5c50782193f833234ba90d35" ) , "angle" : NumberDecimal ( "1.6301023541559787031443874490659" ) , "sinh_output" : NumberDecimal ( "2.454243813557362033961729701069671" ) } Because angle is stored as a 128-bit decimal , the $sinh output is also
a 128-bit decimal. Back $sin Next $slice
