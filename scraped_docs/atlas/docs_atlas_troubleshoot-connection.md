# Troubleshoot Connection Issues - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters Troubleshoot Connection Issues On this page Cluster Connect button is disabled Connecting IP address not in IP Access List Authentication to the cluster failed Too many open connections to your cluster Degraded performance in sharded clusters during spikes in connection counts Attempting to connect from behind a firewall Cluster Availability MongoDB Compass Troubleshooting Connection String Issues This page outlines common connection issues and possible resolutions. To learn more about connecting to an Atlas cluster, see the Get Started with Atlas tutorial. Note If you are an enterprise customer looking for support, file a ticket .
For community support, visit MongoDB Community
Resources . Note Serverless instances don't support connecting via certain drivers
or driver versions at this time. To learn more, see Serverless Instance Limitations . Cluster Connect button is disabled Your cluster's Connect button may be disabled if your
cluster is in the provisioning state. Your
cluster needs to provision when it is first deployed.
Clusters also must provision when you scaled them up or down . The provisoning process can
take up to 10 minutes, after which the Connect button will
become enabled. Connecting IP address not in IP Access List Before connecting to your Atlas cluster, check that you added your
host's IP address to the IP access list for your
cluster's project. Atlas allows client connections only from IP
addresses and CIDR address ranges in the IP access list. Authentication to the cluster failed To connect to Atlas , you must authenticate with a MongoDB database
user. To create a database user for your cluster, see Configure Database Users . Possible solutions If you have created a user and are having trouble authenticating,
try the following: Check that you are using the correct username and password for
your database user, and that you are connecting to the correct
cluster. Check that you are specifying the correct authSource database in
your connection string. If you have a special character in your password, see Special characters in connection string password . Too many open connections to your cluster Atlas sets limits for concurrent incoming connections to a
cluster. For clusters, this is based on the cluster tier. If
you try to connect when you are at this limit, MongoDB displays an error stating connection refused because too many open connections . For a detailed comparision of cluster tiers and their maximum
concurrent connections, see Connection Limits and Cluster Tier . Possible solutions Close any open connections to your cluster not currently in use. Scale your cluster to a higher tier to
support more concurrent connections. Restart your application. To prevent this issue in the future, consider using the maxPoolSize connection string option to limit the
number of connections in the connection pool. To learn how to fix this issue, see Fix Connection Issues . Degraded performance in sharded clusters during spikes in connection counts Atlas can generate an optimized SRV connection string for sharded
clusters using the load balancers from your private endpoint
service. When you use an optimized connection string, Atlas limits
the number of connections per mongos between your application and
your sharded cluster. The limited connections per mongos improve performance during spikes in connection counts. Note Atlas doesn't support optimized connection strings for
clusters that run on Google Cloud or Azure . To learn more about optimized connection strings for sharded
clusters behind a private endpoint, see Improve Connection Performance for Sharded Clusters Behind a Private Endpoint . Attempting to connect from behind a firewall Connecting to the Atlas UI Atlas uses a CDN to serve content quickly. If your organization
uses a firewall, add the following Atlas CDN host to the
firewall's allow list to prevent issues accessing the
Atlas UI: https://assets.mongodb-cdn.com/ . Connecting to a Cluster Atlas clusters operate on port 27017 . You must be able to reach
this port to connect to your clusters. Additionally, ensure that the
appropriate ports are open for the following: For sharded clusters, grant access to port 27016. For BI Connector , grant access to port 27015. You can check your ability to reach a port using the third-party Outgoing port tester . Example To check your ability to reach port 27017, visit http://portquiz.net:27017 . If you can't access these ports, check your system firewall settings
and ensure that they are not blocking access to these ports. Cluster Availability If you are using a mongodb+srv:// connection string and your driver or shell can't find the
DNS host of the Atlas cluster, the cluster
might be paused or deleted. Check that the cluster exists. If
this is a paused cluster, you can resume the cluster if necessary. Note Atlas automatically pauses idle M0 clusters after 60 days
with no connections. MongoDB Compass Troubleshooting If you use MongoDB Compass to connect to your cluster and experience issues,
see: Connection Refused using SRV Connection String in this section. Compass Connection Errors in the MongoDB Compass documentation. If you use a self-managed X.509 certificate or an auto-generated X.509 certificate managed by Atlas to authenticate to the MongoDB database, when you
connect to MongoDB Compass , you must: In MongoDB Compass , choose Fill in connection fields individually . In the Authentication dropdown,  select X.509 . Select More Options . In the SSL dropdown, select Server and Client Validation . Add the same path to the downloaded Atlas -managed certificate, or
the self-managed certificate (depending on which you use) to each of
these fields: Certificate Authority , Client Certificate ,
and Client Private Key . To learn more, see Connect to MongoDB in the MongoDB Compass documentation. Connection String Issues Incorrect Connection String Format The connection string format you use to connect to Atlas depends on several factors, including: Your mongosh version. To learn more, see Connect via mongosh . Your driver version. To learn more, see Connect via Drivers . Verify your connection string in a test environment before putting
it into production. Special Characters in Connection String Password If your password includes special characters, and you are using your
password in a connection string URI, encode the special characters. If you try to update a password with a special character that requires percent encoding , the following error message
appears: This password contains special characters which will be URL-encoded. Note The following characters and the space character must be converted
using percent encoding if included in a
username or password: : / ? # [ ] @ ! $ & ' ( ) * , ; = % For example, if your password in plain-text is p@ssw0rd'9'! , you
need to encode your password as: p%40ssw0rd%279%27%21 â¤ Use the Select your language drop-down menu to set the
language of the encoding example in this section. Go Java (Sync) Node.js Python 1 package main 2 3 import ( 4 "context" 5 "fmt" 6 "net/url" 7 8 "go.mongodb.org/mongo-driver/bson" 9 "go.mongodb.org/mongo-driver/mongo" 10 "go.mongodb.org/mongo-driver/mongo/options" 11 ) 12 13 func main () { 14 username := "<username>" 15 password := "<password>" 16 cluster := "<clusterName>" 17 authSource := "<authSource>" 18 authMechanism := "<authMechanism>" 19 20 uri := "mongodb+srv://" + url.QueryEscape(username) + ":" + 21 url.QueryEscape(password) + "@" + cluster + 22 "/?authSource=" + authSource + 23 "&authMechanism=" + authMechanism 24 25 client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri)) 26 if err != nil { 27 panic (err) 28 } 29 defer client.Disconnect(context.TODO()) 30 31 collection := client.Database( "<dbName>" ).Collection( "<collName>" ) 32 33 cursor, err := collection.Find(context.TODO(), bson.D{}) 34 if err != nil { 35 panic (err) 36 } 37 38 var results []bson.D 39 if err = cursor.All(context.TODO(), &results); err != nil { 40 panic (err) 41 } 42 for _, result := range results { 43 fmt.Println(result) 44 } 45 } 1 import com.mongodb.client.MongoClient; 2 import com.mongodb.client.MongoClients; 3 import com.mongodb.client.MongoCollection; 4 import com.mongodb.client.MongoDatabase; 5 6 import org.bson.Document; 7 import java.net. URLEncoder; 8 9 public class Encoding { 10 11 public static void main (String [] args) { 12 13 try { 14 String username = URLEncoder.encode( "<username>" , "UTF-8" ); 15 String password = URLEncoder.encode( "<password>" , "UTF-8" ); 16 String cluster = "<clusterName>" ; 17 String authSource = "<authSource>" ; 18 String authMechanism = "<authMechanism>" ; 19 20 String uri = "mongodb+srv://" + username + ":" + password + "@" + cluster + 21 "/?authSource=" + authSource + "&authMechanism=" + authMechanism; 22 23 MongoClient mongoClient = MongoClients.create(uri); 24 25 MongoDatabase database = mongoClient.getDatabase( "<dbName>" ); 26 MongoCollection<Document> collection = database.getCollection( "<collName>" ); 27 28 collection.find().forEach(doc -> System.out.println(doc.toJson())); 29 30 } catch (Exception e){ 31 System.err.println(e.getCause()); 32 33 } 34 } 35 } 1 const { MongoClient } = require ( "mongodb" ) ; 2 3 const username = encodeURIComponent ( "<username>" ) ; 4 const password = encodeURIComponent ( "<password>" ) ; 5 const cluster = "<clusterName>" ; 6 const authSource = "<authSource>" ; 7 const authMechanism = "<authMechanism>" ; 8 9 let uri = 10 `mongodb+srv:// ${username} : ${password} @ ${cluster} /?authSource= ${authSource} &authMechanism= ${authMechanism} ` ; 11 12 const client = new MongoClient ( uri) ; 13 14 async function run ( ) { 15 try { 16 await client. connect ( ) ; 17 18 const database = client. db ( "<dbName>" ) ; 19 const ratings = database. collection ( "<collName>" ) ; 20 21 const cursor = ratings. find ( ) ; 22 23 await cursor. forEach ( doc => console . dir ( doc)) ; 24 } finally { 25 await client. close ( ) ; 26 } 27 } 28 run ( ). catch ( console . dir ) ; 1 import pymongo 2 from urllib.parse import quote_plus 3 4 username = quote_plus( '<username>' ) 5 password = quote_plus( '<password>' ) 6 cluster = '<clusterName>' 7 authSource = '<authSource>' 8 authMechanism = '<authMechanism>' 9 10 uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism 11 12 client = pymongo.MongoClient(uri) 13 14 result = client[ "<dbName" ][ "<collName>" ].find() 15 16 # print results 17 for i in result: 18 print (i) Important Do not encode special characters in your password if you are using
your password outside of a connection string URI (for example,
pasting it into mongosh ). Connection String Incompatible with Driver Version If you see this error message, your driver is likely out of date. For
instructions on updating your driver, refer to your specific Driver Documentation . Internet Service Provider DNS Blocks Connection String When you use the DNS seed list connection string format to connect to Atlas , you might see the following error: DNSHostNotFound: Failed to look up service "<MongoDB service name>" This error may occur when using the default DNS server that your ISP provides. That DNS server might not support SRV lookups that
the DNS seed list connection string format uses. To resolve the issue, you can try changing your DNS configuration to
use a public DNS server . Example You can configure your network settings to use Google Public DNS instead of your ISP 's DNS servers. After you update your network settings to use a public DNS server, connect to the cluster . Connection String Error with DB Tools on Ubuntu 18.04 If running Ubuntu 18.04 and using the DNS seed list connection string format ( mongodb+srv:// ) to connect to Atlas from one of
the MongoDB Database Tools ( mongodump , mongorestore , etc), you might see the following
error: lookup nta8e.mongodb.net on 123.45.67.8:27017: cannot unmarshal DNS message If so, use one of the following connection options instead: use the --uri option with a non-SRV connection string ( mongodb:// ). use the --host option to specify the host to connect. Connection Refused using SRV Connection String When using the DNS seed list connection string format ( mongodb+srv:// ) with a driver or Compass, you may
receive in the following error: Error: querySrv ECONNREFUSED _mongodb._tcp.<SRV Record> To begin troubleshooting you will need both the DNS SRV name and the nodes'
individual hostnames and port numbers from the seed list connection string for
the cluster. To find the DNS SRV name: Follow the Steps 1-6 in Connect Your Application . In Step 7 select the latest version of the driver you chose. The DNS SRV name begins after the @ symbol following the password and ends
with .mongodb.net .
- For example, cluster0.dfget.mongodb.net . To find the nodes' hostnames and port numbers: Follow the Steps 1-6 in Connect Your Application . In Step 7 select the latest version of the driver you chose. In Step 7 select the oldest driver version under Non-Stable API Each of the hostnames is in a comma-separated list beginning after the @ symbol following the password and ending with .mongodb.net . Note the port numbers after each of the hostnames. The cluster's connection string may have a variety of hostnames and ports,
depending on its topology and the connection method. For more information on how Private Endpoints work, see Configure Private Endpoints . Test Basic Network Connectivity: Run the following commands in a terminal or command prompt on the application
server experiencing the issue: DNS SRV resolution test: Linux/MacOS: dig SRV _mongodb._tcp.<DNS SRV name> Windows: nslookup -debug -q=SRV  _mongodb._tcp.<DNS SRV name> Under the ANSWER SECTION in the response, you should see one result for each
of the nodes in the cluster.
- For example: ;; ANSWER SECTION: _mongodb._tcp.gcluster0.dfget.mongodb.net. 60 IN SRV 0 0 27017 cluster0-shard-00-00.dfget.mongodb.net. _mongodb._tcp.gcluster0.dfget.mongodb.net. 60 IN SRV 0 0 27017 cluster0-shard-00-01.dfget.mongodb.net. _mongodb._tcp.gcluster0.dfget.mongodb.net. 60 IN SRV 0 0 27017 cluster0-shard-00-02.dfget.mongodb.net. DNS node hostname resolution tests: For each hostname in the cluster run this command: Linux/MacOS: dig <Node Hostname> Windows: nslookup -debug -q=A <Node Hostname> Under the ANSWER SECTION in the response, you should see the IP address that
the DNS hostname resolved to. For example: ;; ANSWER SECTION: cluster0-shard-00-00.ag9in.mongodb.net. 60 IN A 10.10.10.10 Ping test: Note ICMP requests may be blocked by the cloud provider across Private Endpoint
connections. For each hostname in the cluster run this command: Linux/Mac OS: ping -c 10 <Node Hostname> Windows: ping /n 10 <Node Hostname> End-to-End network connection test: Linux/Mac/OS: nc -zv <Node Hostname> <Node Port Number> Windows: Test-NetConnection -Port <Node Port Number> -InformationLevel "Detailed" -ComputerName "<Node Hostname>" Back Google Cloud Next Configure Security Features