# Insert Documents - MongoDB Shell


Docs Home / MongoDB Shell / Perform CRUD Operations Insert Documents On this page Insert a Single Document Insert Multiple Documents Insert Behavior Learn More The MongoDB shell provides the following methods to insert documents
into a collection: To insert a single document, use db.collection.insertOne() . To insert multiple documents, use db.collection.insertMany() . The examples on this page reference the Atlas sample dataset . You can create a free Atlas cluster and populate that cluster with sample data to follow along with
these examples. To learn more, see Get Started with Atlas . Insert a Single Document db.collection.insertOne() inserts a single document into a collection. If the document
does not specify an _id field, MongoDB adds the _id field with
an ObjectId value to the new document. See Insert Behavior . Example To insert a new document into the sample_mflix.movies collection: use sample_mflix db. movies . insertOne ( { title : "The Favourite" , genres : [ "Drama" , "History" ] , runtime : 121 , rated : "R" , year : 2018 , directors : [ "Yorgos Lanthimos" ] , cast : [ "Olivia Colman" , "Emma Stone" , "Rachel Weisz" ] , type : "movie" } ) insertOne() returns a document that
includes the newly inserted document's _id field value. To retrieve the inserted document, read the collection : db. movies . find ( { title : "The Favourite" } ) To ensure you return the document you inserted, you can instead
query by _id . Insert Multiple Documents db.collection.insertMany() can insert multiple documents into a collection. Pass an array
of documents to the method. If the documents do not specify an _id field, MongoDB adds the _id field with an ObjectId value to each
document. See Insert Behavior . Example To insert two new documents into the sample_mflix.movies collection: use sample_mflix db. movies . insertMany ( [ { title : "Jurassic World: Fallen Kingdom" , genres : [ "Action" , "Sci-Fi" ] , runtime : 130 , rated : "PG-13" , year : 2018 , directors : [ "J. A. Bayona" ] , cast : [ "Chris Pratt" , "Bryce Dallas Howard" , "Rafe Spall" ] , type : "movie" } , { title : "Tag" , genres : [ "Comedy" , "Action" ] , runtime : 105 , rated : "R" , year : 2018 , directors : [ "Jeff Tomsic" ] , cast : [ "Annabelle Wallis" , "Jeremy Renner" , "Jon Hamm" ] , type : "movie" } ]) insertMany() returns a document that
includes the newly inserted documents' _id field values. To read documents in the collection : db. movies . find ( { } ) Insert Behavior To learn more about the specific behavior of inserting documents,
see Insert Behavior . Learn More To see more examples of inserting documents into a collection, see
the insertOne() and db.collection.insertMany() method pages. To see all available methods to insert documents into a collection,
see Additional Methods for Inserts Back Perform CRUD Operations Next Read
