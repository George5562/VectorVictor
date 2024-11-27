# Run Aggregation Pipelines - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data Run Aggregation Pipelines On this page Required Roles Access the Aggregation Pipeline Builder Create an Aggregation Pipeline Export an Aggregation Pipeline to Driver Language Configure Aggregation Pipeline Settings You can use the Atlas UI to process your data by building aggregation pipelines .
Aggregation pipelines transform your documents into aggregated results
based on selected pipeline stages . The Atlas aggregation pipeline builder is primarily designed for
building pipelines, rather than executing them. The pipeline builder
provides an easy way to export your pipeline to execute in a driver . Required Roles To create and execute aggregation pipelines in the
Atlas UI, you must have the Project Data Access Read Only role or higher. To utilize the $out stage in your pipeline, you must
have the Project Data Access Read/Write role. Access the Aggregation Pipeline Builder 1 Select the database for the collection. The main panel and Namespaces on the left side list the
collections in the database. click to enlarge 2 Select the collection on the left-hand side or in the main panel. The main panel displays the Find , Indexes ,
and Aggregation views. 3 Select the Aggregation view. When you first open the Aggregation view, Atlas displays an empty aggregation pipeline. click to enlarge Create an Aggregation Pipeline 1 Select an aggregation stage. Select an aggregation stage from the Select dropdown in
the bottom-left panel. click to enlarge The toggle to the right of the dropdown dictates whether the
stage is enabled. 2 Fill in your aggregation stage. Fill in your stage with the appropriate values.
If Comment Mode is enabled, the pipeline
builder provides syntactic guidelines for your selected stage. As you modify your stage, Atlas updates the preview documents on
the right based on the results of the current stage. Aggregation pipelines that do not contain a write stage (such as $out or $merge )
are automatically postfixed with a $limit stage that restricts output to 10 documents by default.
You can change the number of documents allowed through the $limit stage by updating the value
field for Number of Preview Documents in the Aggregation Pipeline Settings . click to enlarge 3 Add additional stages to your pipeline as desired. There are two ways to add additional stages to your pipeline: Click the Add Stage button at the bottom of the pipeline
to add a new stage at the end of your pipeline: Click the button on a stage to add a new stage
directly after the stage where the button was clicked. To delete a pipeline stage, click Delete on the desired stage. 4 Repeat steps 1 and 2 for each additional stage. Collation Use collation to specify
language-specific rules for string comparison, such as rules for lettercase and accent marks. To specify a collation document, click Collation at
the top of the pipeline builder. A collation document has the following fields: { locale : < string > , caseLevel : < boolean > , caseFirst : < string > , strength : < int > , numericOrdering : < boolean > , alternate : < string > , maxVariable : < string > , backwards : < boolean > } The locale field is mandatory; all other collation fields are
optional. For descriptions of the fields, see Collation Document . Import an Aggregation Pipeline from Text You can import aggregation pipelines from plain text into the
pipeline builder to easily modify and verify your pipelines. To import a pipeline from plain text: 1 Open the New Pipeline from Text dialog box. Click the arrow next to the plus icon at the top of the
pipeline builder. Click New Pipeline from Text . click to enlarge 2 Type or paste your pipeline in the dialog box. Your pipeline must match the syntax of the pipeline parameter of
the db.collection.aggregate() method. 3 Click Create New . 4 Click Confirm in the ensuing dialog box. Reset Your Pipeline To return your pipeline to the initial blank state, click the plus icon
at the top of the pipeline builder. Export an Aggregation Pipeline to Driver Language You can use the aggregation pipeline builder to export your finished
pipeline to one of the supported driver languages ; Java,
Node, C#, and Python 3. Use this feature to format and export pipelines
for use in your applications. To export your aggregation pipeline: 1 Construct an aggregation pipeline. For instructions on creating an aggregation pipeline, see Create an Aggregation Pipeline . 2 Click Export to Language at the top of the pipeline builder. 3 Select your desired export language. In the Export Pipeline To dropdown, select your desired
language. The My Pipeline pane on the left displays your
pipeline in mongosh syntax. The pane on the right displays your pipeline in the selected
language. 4 Include import statements, if desired. (Optional) : Check the Include Import Statements option
to include the required import statements for the language selected. 5 Click the Copy button. Click the Copy button at the top-right of the pipeline
to copy the pipeline for the selected language to your clipboard.
You can now integrate your pipeline into your application. 6 Click Close to return to the aggregation pipeline builder. Configure Aggregation Pipeline Settings You can configure aggregation pipeline settings in the Atlas UI. Limitations Atlas limits the number of input documents for previews of the
following stages to 100,000: $group $bucket $bucketAuto This limit allows the preview to run faster. Atlas doesn't
apply a limit when the pipeline runs. You can't change the limit for preview input documents in the
Atlas UI. To change the limit for input documents with Compass , see Aggregation Pipeline Builder Settings . Modify Aggregation Pipeline Settings To modify the aggregation pipeline builder settings: 1 Click the icon at the top-right of the pipeline builder. 2 Modify pipeline settings as desired. You can modify the following settings in the Atlas UI: Setting Description Default Comment Mode When enabled, Atlas adds helper comments to each stage. Changing this setting only affects new stages and doesn't
modify stages which have already been added to your pipeline. On Number of Preview Documents Number of documents to show in the preview for each stage. You can only preview a maximum of 20 documents for each
stage. 10 3 Click Apply to save your changes. Back Indexes Next Triggers
