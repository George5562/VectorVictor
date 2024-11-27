# Modify a View - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / Databases & Collections / Views Modify a View On this page Example Drop and Recreate the View Use the collMod Command To modify a view, you can either: Drop and recreate the view. Use the collMod command. Example Consider the following view named lowStock : db. createView ( "lowStock" , "products" , [ { $match : { quantity : { $lte : 20 } } } ] ) Drop and Recreate the View The following commands modify lowStock by dropping and
recreating the view: db. lowStock . drop ( ) db. createView ( "lowStock" , "products" , [ { $match : { quantity : { $lte : 10 } } } ] ) Use the collMod Command Alternatively, you can use the collMod command to modify the view: db. runCommand ( { collMod : "lowStock" , viewOn : "products" , "pipeline" : [ { $match : { quantity : { $lte : 10 } } } ] } ) Back Use Default Collation Next Remove
