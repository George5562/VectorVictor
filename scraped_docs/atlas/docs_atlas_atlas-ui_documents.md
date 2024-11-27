# Create, View, Update, and Delete Documents - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data Create, View, Update, and Delete Documents On this page Required Roles Insert Documents View, Filter, and Sort Documents Edit One Document Delete One Document You can use the Atlas UI to manage documents inside
your collections. Documents are individual records in a MongoDB
collection and are the basic unit of data in MongoDB. Viewing documents and collections in the Atlas UI can provide a
high-level overview of your database schema. You can use the Atlas UI to ensure you are following MongoDB's core data modeling concepts,
such as utilizing embedded documents and arrays. Tip See also: Data Modeling Required Roles To insert , edit ,
or delete documents , you must have been
granted access through one of the following roles: Project Owner or Organization Owner Project Data Access Admin Project Data Access Read/Write Insert Documents To add one or more documents to a collection through the
Atlas UI, you can specify the documents to insert
from scratch or you can clone an existing document and modify its
fields and values as needed. Insert One Document 1 Go to the Find tab in the Atlas UI. Select the collection and go to the Find tab. 2 Click Insert Document . The document editor appears with the _id field with an ObjectId value that reflects the time of its generation and
not the insertion time of the document. As such, the ObjectId does not represent a strict insertion order. 3 Modify the document. To add a new field after an existing field, hover over the field
and click on the plus sign that appears over the field's line
number. To delete a field, hover over the field and click on the x sign
that appears to the left of the field's line number. You cannot
delete the _id field. To edit a field name, value, or type, click on the field name,
value, or type. 4 Click Insert . Insert Multiple Documents 1 Go to the Find tab in the Atlas UI. Select the collection and go to the Find tab. 2 Click Insert Document . Atlas UI opens the Insert to Collection dialog box. 3 Select the JSON View. 4 Type or paste an array of documents to insert. Example The following array of documents inserts three documents into
the collection: [ { "name" : "Alice" , "age" : 26 , "email" : "alice@abc.com" } , { "name" : "Bob" , "age" : 43 , "email" : "bob@def.com" } , { "name" : "Carol" , "age" : 19 , "email" : "carol@xyz.com" } ] 5 Click Insert . Clone One Document 1 Go to Find tab in the Atlas UI. Select the collection and go to the Find tab. Up to 20 documents displays in the tab. 2 Optional. Specify a filter. To specify filter condition, type in a query filter document in the filter bar. For
example, to specify equality condition, use a filter document of the
form: { < field1 > : < value1 > , ... } To use query operators to specify a filter condition, use a filter
document of the form: { < field1 > : { < queryoperator > : < value1 > } , ... } 3 Clone the document. To clone a document displayed in the query results, hover over the
document and click on its clone document icon. The document editor appears with the _id field with an ObjectId value that reflects the time of its generation and
not the insertion time of the document. As such, the ObjectId does not represent a strict insertion order. 4 Modify the document. To add a new field after an existing field, hover over the field
and click on the plus sign that appears over the field's line
number. To delete a field, hover over the field and click on the x sign
that appears to the left of the field's line number. You cannot
delete the _id field. To edit a field name, value, or type, click on the field name,
value, or type. 5 Click Insert . View, Filter, and Sort Documents To view documents for a collection: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Go to the Collections page. Click the Browse Collections button for your cluster. The Data Explorer displays. To filter and sort documents for a collection: 1 Select the database for the collection. The main panel and Namespaces on the left side list the
collections in the database. click to enlarge 2 Select the collection on the left-hand side or in the main panel. The main panel displays the Find view and the Indexes view. 3 Select the Find view. The panel displays the documents in the collection. Collections of
smaller documents display up to 20 documents per page. Collections
of larger documents display a single document per page. 4 Optional: Specify a query to find specific documents. You can use the query bar to search for specific documents in your
collection. You perform the following actions with the query bar: Filter a query Project fields to include or exclude specific fields in the query
results Sort the documents in the results Apply collation to specify language-specific rules Note You can't skip documents and omit them from query results from the Atlas query bar. To skip documents, use the $skip pipeline stage in the aggregation pipeline builder. Filter Query Results To specify a filter condition, type a query filter into the Filter field. For example, to specify an equality
condition, use a filter with the form: { < field1 > : < value1 > , ... } To use query operators to specify a
filter condition, use a filter with the following form: { < field1 > : { < queryoperator > : < value1 > } , ... } Note The Atlas UI does not support date queries
that use the IsoDate() function. Instead, use the MongoDB Extended JSON (v2) $date data type
for date queries. For example, the following query returns all documents where
the date added to a created_at field is equal to or more
recent than midnight on January 1, 2019, UTC time: { created_at : { $gte : { $date : "2019-01-01T00:00-00:00" } } } For more information on specifying query filters, including
compound conditions, see Query Documents . Project Fields in Query Results To specify the document fields to include or exclude in the
results, click More Options in the query bar and
specify the document fields in the Project field. To include fields, specify the field name and set to 1 in
the project document. For example, to include the year and name fields in the documents: { year : 1 , name : 1 } Atlas returns the fields specified in the Project field and the _id field, which is
returned unless it is explicitly excluded. To exclude fields, specify the field name and set to 0 in
the project document. For example, to exclude the year and name fields in the documents: { year : 0 , name : 0 } Atlas returns all fields except the fields specified in Project . To learn more about project documents, see $project . Sort Query Results To sort the order of the documents in the results, click More Options in the query bar and enter the sort document in the Sort field. To specify ascending order for a field, set the field to 1 in the sort document. To specify descending order for a field, set the field to -1 in the sort documents. For example, the following sort document sorts results
first by year in descending order, and within each year,
sorts by name in ascending order: { year : - 1 , name : 1 } To learn more about sort documents, see $sort . Specify Collation Important Feature unavailable in Serverless Instances Serverless instances don't support this
feature at this time. To learn more, see Serverless Instance Limitations . To specify language-specific rules for string comparison, such
as rules for lettercase and accent marks, click More Options in the query bar and enter the collation
document in the Collation field. Use the locale field in the collation document to specify the ICU
Locale code for
the desired language. For example, to use the pinyin variant of the Chinese collation, use the following collation
document: { "locale" : "zh@collation=pinyin" } To learn more about collation documents, see Collation . Note As you type, the Apply button is disabled and the
field name in the User Interface turns red until a valid query is
entered. 5 Click Apply to run your query. Number of Documents Displayed per Page The Atlas UI limits the total byte size of documents shown per
page. As a result, you may see varying numbers of documents per page,
especially if your documents vary significantly in size. Edit One Document To edit a document from a collection through the Atlas UI: 1 Go to Find tab in the Atlas UI. Select the collection and go to the Find tab. Up to 20 documents displays in the tab. 2 Optional. Specify a filter. To specify filter condition, type in a query filter document in the filter bar. For
example, to specify equality condition, use a filter document of the
form: { < field1 > : < value1 > , ... } To use query operators to specify a filter condition, use a filter
document of the form: { < field1 > : { < queryoperator > : < value1 > } , ... } 3 Edit the document. To edit a document displayed in the query results, hover over the
document to edit and click on the pencil icon. The document appears in the document editor: To add a new field, hover over the field and click on the plus
sign that appears over the field's line number. To delete a field, hover over the field and click on the x sign
that appears to the left of the field's line number. You cannot
delete the _id field. To edit a field name, value, or type, click on the field name,
value, or type. To revert a specific change, hover over the edited field and click the
revert icon that appears to the left of the field's line number. 4 Save or cancel changes. To confirm and save changes, click the Update button. To cancel all modifications to the document, click the Cancel button. Delete One Document To delete a document from a collection through the Atlas UI: 1 Go to Find tab in the Atlas UI. Select the collection and go to the Find tab. Up to 20 documents displays in the tab. 2 Optional. Specify a filter. To specify filter condition, type in a query filter document in the filter bar. For
example, to specify equality condition, use a filter document of the
form: { < field1 > : < value1 > , ... } To use query operators to specify a filter condition, use a filter
document of the form: { < field1 > : { < queryoperator > : < value1 > } , ... } 3 Delete the document. To delete a document displayed in the query results, hover over the
document to delete and click on the trash can icon. The document is flagged for deletion. 4 To confirm, click the Delete button. Back Collections Next Indexes
