# Get Started with Atlas Stream Processing - MongoDB Atlas


Docs Home / MongoDB Atlas / Atlas Stream Processing Get Started with Atlas Stream Processing On this page Prerequisites Procedure In Atlas , go to the Stream Processing page for your project. Create a Stream Processing Instance. Get the stream processing instance connection string. Add a MongoDB Atlas connection to the connection registry. Verify that your streaming data source emits messages. Create a persistent stream processor. Start the stream processor. Verify the output of the stream processor. Drop the stream processor. Next Steps This tutorial takes you through the steps of setting up Atlas Stream Processing
and running your first stream processor. Prerequisites To complete this tutorial you need: An Atlas project mongosh version 2.0 or higher An Atlas user with the Project Owner or
the Project Stream Processing Owner role to manage a
Stream Processing Instance and Connection Registry Note The Project Owner role allows you to create database
deployments, manage project access and project settings, manage
IP Access List entries, and more. The Project Stream Processing Owner role enables
Atlas Stream Processing actions such as viewing, creating, deleting, and
editing stream processing instances, and viewing, adding, modifying,
and deleting connections in the connection registry. See Project Roles to learn more about the
differences between the two roles. A database user with the atlasAdmin role to create
and run stream processors An Atlas cluster Procedure 1 In Atlas , go to the Stream Processing page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Stream Processing under
the Services heading. The Stream Processing page displays. 2 Create a Stream Processing Instance. Click Get Started in the lower-right corner. Atlas provides a brief explanation of core Atlas Stream Processing
components. Click the Create instance button. On the Create a stream processing instance page, configure your instance as follows: Tier : SP30 Provider : AWS Region : us-east-1 Instance Name : tutorialInstance Click Create . 3 Get the stream processing instance connection string. Locate the overview panel of your
stream processing instance and click Connect . Select I have the MongoDB shell installed . From the Select your mongo shell version dropdown
menu, select the latest version of mongosh . Copy the connection string provided under Run your connection string in your command line .
You will need this in a later step. Click Close . 4 Add a MongoDB Atlas connection to the connection registry. This connection serves as our streaming data sink. In the pane for your stream processing instance, click Configure . In the Connection Registry tab, click + Add Connection in the upper right. Click Atlas Database . In the Connection Name field, enter mongodb1 .
From the Atlas Cluster drop down, select an Atlas cluster without any data stored on it. Click Add connection . 5 Verify that your streaming data source emits messages. Your stream processing instance comes preconfigured with a connection to a sample
data source called sample_stream_solar . This source
generates a stream of reports from various solar power
devices. Each report describes the observed wattage and
temperature of a single solar device at a specific point in
time, as well as that device's maximum wattage. The following document is a representative example. { device_id : 'device_8' , group_id : 7 , timestamp : ' 2024 -08 -12 T21 : 41 : 01.788 + 00 : 00 ' , max_watts : 450 , event_type : 0 , obs : { watts : 252 , temp : 17 } , _ts : ISODate(' 2024 -08 -12 T21 : 41 : 01.788 Z') , _stream_meta : { source : { type : 'generated' } } } To verify that this source emits messages, create a stream
processor interactively. Open a terminal application of your choice. Connect to your stream processing instance with mongosh . Paste the mongosh connection string that you copied
in a previous step into your terminal, where <atlas-stream-processing-url> is the URL of your stream processing instance
and <username> is a user with the atlasAdmin role. mongosh "mongodb://<atlas-stream-processing-url>/" --tls --authenticationDatabase admin --username <username> Enter your password when prompted. Create the stream processor. Copy the following code into your mongosh prompt: sp.process([{"$source": { "connectionName": "sample_stream_solar" }}]) Verify that data from the sample_stream_solar connection displays to the console, and terminate
the process. Stream processors you create with sp.process() don't
persist after you terminate them. 6 Create a persistent stream processor. Using an aggregation pipeline , you can transform each document
as it is ingested. The following aggregation pipeline derives
the maximum temperature and the average, median, maximum, and
minimum wattages of each solar device at one-second intervals. Configure a $source stage. The following $source stage ingests data from the sample_stream_solar source. let s = { $ source : { connectionName: "sample_stream_solar" } } Configure a $group stage. The following $group stage organizes all incoming data
according to their group_id , accumulates the values of
the obs.temp and obs.watts fields of all documents
for each group_id , then derives the desired data. let g = { $ group: { _id: "$group_id", max_temp: { $avg: "$obs.temp" }, avg_watts: { $min: "$obs.watts" }, median_watts: { $min: "$obs.watts" }, max_watts: { $max: "$obs.watts" }, min_watts: { $min: "$obs.watts" } } } Configure a $tumblingWindow stage. In order to perform accumulations such as $group on
streaming data, Atlas Stream Processing uses windows to bound the data set. The following $tumblingWindow stage separates the stream into
consecutive 10-second intervals. This means, for example, that when the $group stage
computes a value for median_watts , it takes the obs.watts values for all documents with a given group_id ingested in the previous 10 seconds. let t = { $tumblingWindow: { interval: { size: NumberInt(10), unit: "second" }, pipeline: [g] } } Configure a $merge stage. $merge allows you to write your processed streaming data
to an Atlas database. let m = { $ merge: { into: { connectionName: "mongodb1", db: "solarDb", coll: "solarColl" } } } Create the stream processor. Assign a name to your new stream processor, and declare its
aggregation pipeline by listing each stage in order. The $group stage belongs to the nested pipeline of the $tumblingWindow , and you must not include it in the
processor pipeline definition. sp.createStreamProcessor("solarDemo", [s, t, m]) This creates a stream processor named solarDemo that
applies the previously defined query and writes the
processed data to the solarColl collection of the solarDb database on the cluster you connected to.
It returns various measurements derived from 10-second intervals
of observations from your solar devices. To learn more about how Atlas Stream Processing writes to at-rest
databases, see $merge . 7 Start the stream processor. Run the following command in mongosh : sp.solarDemo.start() 8 Verify the output of the stream processor. To verify that the processor is active, run the following
command in mongosh : sp.solarDemo.stats() This command reports operational statistics of the solarDemo stream processor. To verify that the stream processor is writing data to your Atlas cluster: In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. Click the Browse Collections button for your cluster. The Data Explorer displays. View the MySolar collection. Alternatively, you can display a sampling of processed documents
in the terminal using mongosh : sp.solarDemo.sample() HIDE OUTPUT { _id : 10 , max_watts : 136 , min_watts : 130 , avg_watts : 133 , median_watts : 130 , max_temp : 7 , _stream_meta : { source : { type : 'generated' } , window : { start : ISODate(' 2024 -08 -12 T22 : 49 : 05.000 Z') , end : ISODate(' 2024 -08 -12 T22 : 49 : 10.000 Z') } } } Note The preceding is a representative example. Streaming data are
not static, and each user sees distinct documents. 9 Drop the stream processor. Run the following command in mongosh : sp.solarDemo.drop() To confirm that you have dropped avgWatts , list
all your available stream processors: sp.listStreamProcessors() Next Steps Learn how to: Manage Stream Processors Manage Stream Processing Instances Back Overview Next Stream Processor Windows
