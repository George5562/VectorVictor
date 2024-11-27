# Connect via mongosh - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters / Connection Methods Connect via mongosh On this page Prerequisites Connect to Your Cluster Troubleshooting The Connect dialog box for a cluster provides
the details to connect to a cluster via the MongoDB
shell, mongosh . Prerequisites TLS Clients must support TLS to connect to an Atlas cluster. Clients must support the SNI TLS extension to
connect to an Atlas M0 Free cluster or an M2/M5 Shared cluster. MongoDB 4.0 and later shell supports the SNI TLS extension. IP Access List To access a cluster, you must connect from an IP address on the Atlas project's IP access list. If you need to add an IP address to
the IP access list, you can do so in the Connect dialog box.
You can also add the IP address from the Network Access tab . Database User To access a cluster, you must create a database user with access to the
desired databases on your Atlas cluster. Database users are
separate from Atlas users. Database users have access to MongoDB
databases, while Atlas users have access to the Atlas application itself. You can create a database user to access your Atlas cluster in
the Connect dialog box. You can also add the database user from
the Cluster view . Connect to Your Cluster 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Click Connect . Click Connect for the cluster to
which you want to connect. 3 Choose your Connection Security. Choose Connection Type from the set of available buttons. Note Options Display if Feature Enabled Atlas displays the connection type options after you enable Private IP for Peering , Private Endpoint , or
both. If you haven't enabled either feature, no buttons display
and Connection Type defaults to Standard . Standard Connection Private IP for Peering Private Endpoint Connection Use this connection type for allowed public IP addresses. Use this connection type if you enabled peering: For Google Cloud or Azure and are connecting with {{connChoice}}
from a peered network, or For AWS and are connecting with {{connChoice}} from a
peered network which uses a custom DNS service. If neither of these apply, add your IP address to your IP
access list and use the Standard Connection string. If you are
connecting directly to Atlas from an office or home
network, this might be the preferred option. Note Peer must be available You can't select this option unless one of your peers
is marked as AVAILABLE . To check the status of your peers : In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. Note Multi-Cloud Clusters If your application isn't hosted on the same cloud service
provider as your cluster's primary , the application
can only perform secondary reads. With multi-cloud clusters, consider adding the readPreference connection option to your connection string .
Use one of the following values: primaryPreferred secondary secondaryPreferred Use the connection string for the appropriate interface
endpoint if you are connecting with {{connChoice}} over a
Private Endpoint connection either because {{connChoice}}: Runs inside your cloud provider network, or Has transitive network access to your cloud provider network. You want to use an optimized connection string . If none of these apply, add your IP address to your IP
access list and use the Standard Connection string. If you are
connecting directly to Atlas from an office or home
network, this might be the preferred option. Note You can't select this option unless your configured
PrivateLink connection is ready to use. To check the status of your AWS PrivateLink : In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 4 Choose how you want to limit connections to your cluster. Standard Connection Private IP for Peering Private Endpoint Connection Add a Connection IP Address Important Skip this step if Atlas indicates in the Setup connection security step that you have
already configured an IP access list entry in your cluster.
To manage the IP access list, see Add Entries to the Access List . Atlas allows standard client connections to the cluster
from entries in the project's IP access list . The project IP access list differs from the API access list , which
restricts API access to specific IP or CIDR addresses. If the IP access list is empty, Atlas prompts you to add an
IP address to the project's IP access list. You can either: Click Add Your Current IP Address to allow
access from your current IP address. Click Add an IP Address to add a single IP
address or a CIDR -notated range of addresses. Provide an optional description for the newly added IP address
or CIDR range. Click Add IP Address to add the
address to the IP access list. Add a Connection IP Address Important Skip this step if Atlas indicates in the Setup connection security step that you have
already configured an IP access list entry in your cluster.
To manage the IP access list, see Add Entries to the
IP access list . Atlas allows standard client connections to the cluster
from entries in the project's IP access list . The project IP access list differs from the API access list , which
restricts API access to specific IP or CIDR addresses. If the IP access list is empty, Atlas prompts you to add an
IP address to the project's IP access list. Click Add a Different IP Address to add a single IP
address or a CIDR -notated range of addresses. Provide an optional description for the newly added IP address
or CIDR range. Click Add IP Address to add the
address to the IP access list. Under Choose Connection Type , select Private Endpoint . If you see the Private Link Type options,
select one of the following options: Optimized SRV Connection for
load-balanced connections. Legacy SRV Connection for
non-load-balanced connections. To learn more, see Improve Connection Performance for Sharded Clusters Behind a Private Endpoint . Under Choose Private Endpoint , select the
endpoint you want to use. 5 Create a Database User. Important Skip this step if Atlas indicates in the Setup connection security step that you have at least
one database user configured in your project. To manage existing
database users, see Configure Database Users . To access the cluster, you need a MongoDB user with access to the
desired database or databases on the cluster in your project. If your
project has no MongoDB users, Atlas prompts you to create a new
user with the Atlas Admin role. Enter the new user's Username . Enter a Password for this new user or click Autogenerate Secure Password . Click Create Database User to save the user. Use this user to connect to your cluster in the following step. Once you have added an IP address to your IP access list and added a
database user, click Choose Your Connection Method . 6 Connect to your Atlas cluster with mongosh . Select Shell . The next screen offers you options to proceed based on whether or
not you already have mongosh installed on your system. I do not have the MongoDB Shell installed I have the MongoDB Shell installed Select your OS from the dropdown menu. Windows macOS Linux Download using one of the following options: Click Download mongosh to
begin the download. Click Copy download URL to copy a
download URL to your clipboard, then either: Use curl to fetch the installer file
from the URL , or Paste the URL in a browser window. Download the installer from the MongoDB Shell page. Extract the files from the downloaded archive. Add the mongosh binary to your PATH environment variable. Ensure that the extracted MongoDB Shell binary
is in the desired location in your filesystem,
then add that location to your PATH environment variable. Open the Control Panel . In the System and Security category, click System . Click Advanced system settings .
The System Properties modal
displays. Click Environment Variables . Select Path and click Edit . Click New and add the filepath to
your mongosh binary. Step 3 of the Atlas modal displays a
copyable connection string. This string
includes the name of the MongoDB user that can
authenticate with the cluster. Copy this
string. To connect as a different MongoDB user,
change the --username option. Paste the mongosh command and connection string
into a terminal. Run the command. The shell
prompts you for the password . Note If the input device is not a terminal, mongosh doesn't prompt for a password.
Instead, mongosh interprets any input on stdin after the connection string as a password. Use the Homebrew command provided. Copy the Homebrew command from the Atlas UI
window and run it in a terminal. Step 3 of the Atlas modal displays a
copyable connection string. This string
includes the name of the MongoDB user that can
authenticate with the cluster. Copy this
string. To connect as a different MongoDB user,
change the --username option. Paste the mongosh command and connection string
into a terminal. Run the command. The shell
prompts you for the password . Note If the input device is not a terminal, mongosh doesn't prompt for a password.
Instead, mongosh interprets any input on stdin after the connection string as a password. Download the installer using one of the
following options: Click Download mongosh to
begin the download. Click Copy download URL to copy a
download URL to your clipboard, then either: Use curl to fetch the installer file
from the URL , or Paste the URL in a browser window. Download the installer from the MongoDB Shell page. Note The type of file you download depends on the
operating system you selected. If you select
a version of: Ubuntu or Debian you receive a .deb package. RHEL, Amazon Linux, or SUSE you receive
an .rpm package. If your operating system isn't listed, see
the .tgz installation instructions in the mongosh documentation. Install the mongosh package. .deb Package .rpm Package Use dpkg to install mongosh : sudo dpkg -i mongodb-mongosh_<mongosh-version-and-platform>.deb Use rpm to install mongosh : sudo rpm -i mongodb-mongosh_<mongosh-version-and-platform>.rpm Step 3 of the Atlas modal displays a
copyable connection string. This string
includes the name of the MongoDB user that can
authenticate with the cluster. Copy this
string. To connect as a different MongoDB user,
change the --username option. Paste the mongosh command and connection string
into a terminal. Run the command. The shell
prompts you for the password. Note If the input device is not a terminal, mongosh doesn't prompt for a password.
Instead, mongosh interprets any input on stdin after the connection string as a password. Select mongosh from the dropdown menu.
We recommend that you upgrade to the latest version
of the shell. To check the installed version of the mongosh , run: mongosh --version Step 2 of the Atlas modal displays a copyable
connection string that includes the name of the
MongoDB user that can authenticate with the cluster. Copy
this string. To connect as a different MongoDB user,
change the --username option. Paste the mongosh command and connection string into a
terminal. Run the command. The shell prompts you for the password . Note If the input device is not a terminal, mongosh doesn't prompt for a password.
Instead, mongosh interprets any input on stdin after the connection string as a password. Troubleshooting If you are experiencing issues connecting to your cluster, see Troubleshoot Connection Issues . Back Compass Next BI Connector
