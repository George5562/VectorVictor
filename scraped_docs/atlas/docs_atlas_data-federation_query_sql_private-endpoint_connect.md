# Connect to Atlas SQL with a Federated Database Instance Private Endpoint - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / SQL / Connect Connect to Atlas SQL with a Federated Database Instance Private Endpoint On this page Prerequisites Procedure This page describes how to connect to a cluster using Atlas SQL with a
Federated Database Instance private endpoint. Prerequisites An Atlas cluster running MongoDB version 5.0 or later. A private endpoint configured in your
Federated Database Instance instance. Procedure Follow these steps to connect your Atlas cluster with Atlas SQL
using a Federated Database Instance private endpoint . 1 Under Atlas SQL , click Connect . 2 Select Private Endpoint . 3 Select your Federated Database Instance private endpoint. Select your Federated Database Instance private endpoint from the Choose private endpoint dropdown. This endpoint includes "Data Federation" in the name and is
distinct from a "Dedicated" endpoint associated with your Atlas cluster. 4 Click Choose a connection method . 5 Select Atlas SQL . 6 Validate the provided connection string Confirm that the provided connection string in the URL field
contains the characters pl , which indicates a private link. Back Power BI Next Query
