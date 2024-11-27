# $tanh (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $tanh (aggregation) On this page Behavior Example $tanh Returns the hyperbolic tangent of a value that is measured in
radians. $tanh has the following syntax: { $tanh : < expression > } $tanh takes any valid expression that resolves to a number, measured in
radians. If the expression returns a value in degrees, use the $degreesToRadians operator to convert the value to
radians. By default $tanh returns values as a double . $tanh can also return values as a 128-bit decimal if the <expression> resolves to a 128-bit
decimal value. For more information on expressions, see Expression Operators . Behavior null , NaN , and +/- Infinity If the input argument resolves to a value of null or refers to a
field that is missing, $tanh returns null . If the
argument resolves to NaN , $tanh returns NaN . If
the argument resolves to negative or positive Infinity , $tanh returns -1 or 1 respectively. Example Results { $tanh: NaN } NaN { $tanh: null } null { $tanh: -Infinity } -1 { $tanh: Infinity } 1 Example Hyperbolic Tangent in Degrees Hyperbolic Tangent in Radians The following trigonometry collection contains a document
that stores an angle value measured in degrees: db. trigonometry . insertOne ( { "_id" : ObjectId ( "5c50782193f833234ba90d45" ) , "angle" : NumberDecimal ( "53.1301023541559787031443874490659" ) } ) The following aggregation operation uses the $tanh expression to calculate the hyperbolic
tangent of angle and adds it to the input document using
the $addFields pipeline stage: db. trigonometry . aggregate ( [ { $addFields : { "tanh_output" : { $tanh : { $degreesToRadians : "$angle" } } } } ] ) The $degreesToRadians expression converts the angle in degrees to radians. Example output: { "_id" : ObjectId ( "5c50782193f833234ba90d45" ) , "angle" : NumberDecimal ( "53.1301023541559787031443874490659" ) , "tanh_output" : NumberDecimal ( "0.7293303448445332820512777329448416" ) } Because angle is stored as a 128-bit decimal , the $tanh output is also a
128-bit decimal. The following trigonometry collection contains a document
that stores an angle value measured in radians: db. trigonometry . insertOne ( { "_id" : ObjectId ( "5c50782193f833234ba90d55" ) , "angle" : NumberDecimal ( "1.6301023541559787031443874490659" ) } ) The following aggregation operation uses the $tanh expression to calculate the hyperbolic
tangent of angle and adds it to the input document using
the $addFields pipeline stage: db. trigonometry . aggregate ( [ { $addFields : { "tanh_output" : { $tanh : "$angle" } } } ] ) Example output: { "_id" : ObjectId ( "5c50782193f833234ba90d55" ) , "angle" : NumberDecimal ( "1.6301023541559787031443874490659" ) , "tanh_output" : NumberDecimal ( "0.9260761562750713360156803177935379" ) } Because angle is stored as a 128-bit decimal , the $tanh output is also
a 128-bit decimal. Back $tan Next $toBool
