# Get Started with Atlas - MongoDB Atlas


Docs Home / MongoDB Atlas Get Started with Atlas On this page Overview Go Further with Atlas Overview MongoDB Atlas provides an easy way to host and manage your data in
the cloud. This tutorial guides you through creating an Atlas cluster, connecting to it, and loading sample
data. You can get started with Atlas through the Atlas CLI or the Atlas User Interface. Select a tab based on how you
would like to get started: Atlas CLI Atlas UI To create and authenticate with your Atlas account, create one free database, load sample data, add your IP address to your project IP access list, create a MongoDB user, and view your connection string using the
Atlas CLI, run the following command: atlas setup [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas setup . For step-by-step instructions on using this command, see Get Started with Atlas from the Atlas CLI . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI You can also run atlas setup if you have an Atlas account
and an organization/project, but you haven't set up a cluster. To get started using the Atlas UI: 1 Create an Atlas account. Register for an Atlas account using your Google Account
or an email address. 2 Deploy a Free cluster. Create and deploy a Free cluster . You can use Atlas Free clusters as a small-scale development
environment to host your data. Free clusters never expire, and
provide access to a subset of Atlas features. 3 Manage database users for your cluster. Manage database users for your cluster . For
security purposes, Atlas requires clients to authenticate as
MongoDB database users to access clusters. 4 Manage the IP access list. Manage the list of trusted IP addresses . An IP uniquely
identifies a device connecting to a network. In Atlas , you
can connect to a cluster only from a trusted IP address.
Within Atlas , you can create a list of trusted IP addresses,
referred to as an IP access list. An IP accesss list defines
the IP addresses that can connect to your cluster and access
your data. 5 Connect to your cluster. Connect to your cluster using the mongosh , the Node.js driver , the PyMongo driver , or Compass . 6 Insert and view a document. Insert a document into your cluster using one of the
supported MongoDB Drivers . MongoDB drivers let you
interact with your databases programmatically with a supported
programming language. 7 Load sample data. Load sample data into your Atlas clusters . Atlas provides sample data that you can
load into your Atlas clusters. You can use this
data to quickly get started experimenting with data in
MongoDB and using tools such as the Atlas UI and MongoDB Charts . You can also generate synthetic data that aligns to your
real data's schema. To learn more, see Generate Synthetic Data . Go Further with Atlas Build full-text search on top of your data. To learn more, see What is MongoDB Atlas Search ? . Back What is MongoDB Atlas? Next Create an Account
