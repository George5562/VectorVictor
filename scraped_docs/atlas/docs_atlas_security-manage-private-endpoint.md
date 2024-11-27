# Manage and Connect from Private Endpoints - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Private Endpoints Manage and Connect from Private Endpoints On this page Required Access Connect from a Private Endpoint View Private Endpoints Remove a Private Endpoint from Atlas Note This feature is not available for M0 Free clusters, M2 , and M5 clusters. To learn more about which features are unavailable,
see Atlas M0 (Free Cluster), M2, and M5 Limits . After you set up a private endpoint for a cluster , follow these steps to manage and
connect from your Atlas private endpoint. To learn more about using private endpoints with Atlas , see Learn About Private Endpoints in Atlas . Required Access To view private endpoints, you must have Project Read Only access to the project. To delete private endpoints, you must have Project Owner access
or higher to the project. Users with Organization Owner access must add themselves to the
project as a Project Owner . Connect from a Private Endpoint Important For considerations about private endpoint-aware connection
strings, see Private Endpoint-Aware Connection Strings . Use a private endpoint-aware connection string to connect to an Atlas cluster with the following procedure: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Click Connect Click Connect for the cluster to
which you want to connect. 3 Select the Private Endpoint connection type. 4 Select the private endpoint to which you want to connect. 5 Create a Database User. Important Skip this step if Atlas indicates in the Setup connection security step that you have at least
one database user configured in your project. To manage existing
database users, see Configure Database Users . To access the cluster, you need a MongoDB user with
access to the desired database or databases on the
cluster in your project. If your
project has no MongoDB users, Atlas prompts you to create a new
user with the Atlas Admin role. Enter the new user's Username . Enter a Password for this new user or click Autogenerate Secure Password . Click Create Database User to save the user. Use this user to connect to your cluster in the
following step. Once you have added a database user, click Choose Your Connection Method . 6 Click Choose a connection method . View Private Endpoints AWS PrivateLink Azure Private Link GCP Private Service Connect Atlas CLI Atlas UI Endpoints To return the details of the AWS private endpoint you specify using the Atlas CLI, run the following command: atlas privateEndpoints aws describe <privateEndpointId> [options] To list all AWS private endpoints in a project using the Atlas CLI, run the following command: atlas privateEndpoints aws list [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas privateEndpoints aws describe and atlas privateEndpoints aws list . Interface Endpoints To return the AWS private endpoint interface that you specify. using the
Atlas CLI, run the following command: atlas privateEndpoints aws interfaces describe <interfaceEndpointId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints aws interfaces describe . 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the Private Endpoint tab and then the following tab. Click Dedicated Cluster for a private endpoint
for your dedicated Atlas cluster. (default) Atlas CLI Atlas UI Endpoints To return the details of the Azure private endpoint you specify using the Atlas CLI, run the following command: atlas privateEndpoints azure describe <privateEndpointId> [options] To list all Azure private endpoints in a project using the Atlas CLI, run the following command: atlas privateEndpoints azure list [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas privateEndpoints azure describe and atlas privateEndpoints azure list . Interface Endpoints To return the Azure private endpoint interface that you specify. using the
Atlas CLI, run the following command: atlas privateEndpoints azure interfaces describe <privateEndpointResourceId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints azure interfaces describe . 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the Private Endpoint tab and then the following tab. Click Dedicated Cluster for a private endpoint
for your dedicated Atlas cluster. (default) Atlas CLI Atlas UI Endpoints To return the details of the Google Cloud private endpoint you specify using the Atlas CLI, run the following command: atlas privateEndpoints gcp describe <privateEndpointId> [options] To list all Google Cloud private endpoints in a project using the Atlas CLI, run the following command: atlas privateEndpoints gcp list [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas privateEndpoints gcp describe and atlas privateEndpoints gcp list . Interface Endpoints To return the Google Cloud private endpoint interface that you specify. using the
Atlas CLI, run the following command: atlas privateEndpoints gcp interfaces describe <id> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints gcp interfaces describe . 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the Private Endpoint tab and then the following tab. Click Dedicated Cluster for a private endpoint
for your dedicated Atlas cluster. (default) Remove a Private Endpoint from Atlas AWS PrivateLink Azure Private Link GCP Private Service Connect Atlas CLI Atlas UI Endpoints To delete the AWS private endpoint you specify using the
Atlas CLI, run the following command: atlas privateEndpoints aws delete <privateEndpointId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints aws delete . Interface Endpoints To delete the AWS private endpoint interface you specify using the
Atlas CLI, run the following command: atlas privateEndpoints aws interfaces delete <interfaceEndpointId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints aws interfaces delete . 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Remove the private endpoint from Atlas . Click the Private Endpoint tab. Next to the private endpoint you want to remove, click Terminate . To confirm, click Confirm in the dialog box. Atlas CLI Atlas UI Endpoints To delete the Azure private endpoint you specify using the
Atlas CLI, run the following command: atlas privateEndpoints azure delete <privateEndpointId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints azure delete . Interface Endpoints To delete the Azure private endpoint interface you specify using the
Atlas CLI, run the following command: atlas privateEndpoints azure interfaces delete <privateEndpointResourceId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints azure interfaces delete . 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Remove the private endpoint from Atlas . Click the Private Endpoint tab. Next to the private endpoint you want to remove, click Terminate . To confirm, click Confirm in the dialog box. Atlas CLI Atlas UI Endpoints To delete the Google Cloud private endpoint you specify using the
Atlas CLI, run the following command: atlas privateEndpoints gcp delete <privateEndpointId> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints gcp delete . Interface Endpoints To delete the Google Cloud private endpoint interface you specify using the
Atlas CLI, run the following command: atlas privateEndpoints gcp interfaces delete <id> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas privateEndpoints gcp interfaces delete . 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Remove the private endpoint from Atlas . Click the Private Endpoint tab. Next to the private endpoint you want to remove, click Terminate . To confirm, click Confirm in the dialog box. Back Dedicated Clusters Next Troubleshoot
