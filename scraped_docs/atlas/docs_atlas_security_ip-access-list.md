# Configure IP Access List Entries - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features Configure IP Access List Entries On this page In Atlas , go to the Project Settings page. In Atlas , go to the Project Activity Feed page. Required Access View IP Access List Entries Add IP Access List Entries Modify IP Access List Entries Delete IP Access List Entries Atlas only allows client connections to the cluster
from entries in the project's IP access list. Each entry is either a
single IP address or a CIDR -notated range of addresses. For AWS clusters with one or more VPC Peering connections to the same AWS region, you can specify a Security Group
associated with a peered VPC . For Atlas clusters deployed on Google Cloud Platform (GCP) or Microsoft Azure , add the IP addresses of your Google Cloud or Azure services to Atlas project IP access list to grant those services
access to the cluster. The IP access list applies to all clusters in the
project and can have up to 200 IP access list entries, with the
following exception: projects with an existing sharded cluster
created before August 25, 2017 can have up to 100 IP access list
entries. Atlas supports creating temporary IP access list entries that
expire within a user-configurable 7-day period. When you create, delete, or change temporary and non-temporary IP access
list entries, Atlas notifies you of these events in the project's Activity Feed . For example, if you modify the address of an
IP access list entry, the Activity Feed reports the deletion of the old
entry and the creation of the new entry. To view the project's Activity Feed: 1 In Atlas , go to the Project Settings page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Settings . The Project Settings page
displays. 2 In Atlas , go to the Project Activity Feed page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Do one of the following steps: Click the Project Activity Feed icon in the right
side of the navigation bar. Next to the Projects menu, expand the Options menu, click Project Settings , and click Activity Feed in the sidebar. The Project Activity Feed page displays. Tip See also: View All Activity . Note Activity Feed Considerations Atlas does not report updates to an IP access list entry's
comment in the Activity Feed. When you modify the address of an IP access list entry, the
Activity Feed reports two new activities: one for the deletion of
the old entry and one for the creation of the new entry. Required Access To manage IP Access List entries, you must have Project Owner access
to the project. Users with Organization Owner access must add themselves to the
project as a Project Owner . View IP Access List Entries Atlas CLI Atlas UI To list IP access list entries for your project using the Atlas CLI, run the following command: atlas accessLists list [options] To return the details for the IP access list entry you specify using the Atlas CLI, run the following command: atlas accessLists describe <entry> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas accessLists list and atlas accessLists describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Click the IP Access List tab. IP Address IP address or CIDR block. If this
cluster is hosted on AWS ,
you can provide an AWS Security Group ID as well. Comment Description or other information about the access list
entry. Status Status of the IP access list entry: Status Description Inactive Atlas is not using the IP access list entry. No cloud
provider containers are provisioned for the project. Pending Atlas is configuring the IP access list entry for the
project. Active Atlas has configured the IP access list entry for every
container provisioned in the project. Active in regions: <regions> Atlas has configured the IP access list entry for every
container provisioned in the project for the regions listed, but
not any other containers that exist for the project. This
applies to AWS security groups only. Failed Atlas could not configure the IP access list entry for every
container provisioned for the project. Actions Options to Edit or Delete . Add IP Access List Entries Atlas CLI Atlas Administration API Atlas UI To create an IP access list for your project using the
Atlas CLI, run the following command: atlas accessLists create [entry] [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas accessLists create . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI You can use the Atlas Administration API to add
existing IP access list entries . 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Go to IP Access List view. If it isn't already displayed, click the IP Access List tab. Click Add IP Address . 3 Enter an IP address, CIDR block, or Security Group ID. Important Ensure that you add the IP address you will use to
access MongoDB as the admin user. Enter the desired IP address or CIDR -notated range of addresses: Entry Grants An IP address Access from that address. A CIDR -notated range of IP addresses Access from the designated range of addresses. For peer VPC connections, you can specify the CIDR block
(or a subset) or the associated Security Group. The Internet provides online tools for converting a range of
IP addresses to CIDR , such as http://www.ipaddressguide.com/cidr . IMPORTANT: Adding the CIDR 0.0.0.0/0 allows access from anywhere.
Ensure that strong credentials (username and password) are
used for all database users when allowing access from
anywhere. Security Group ID (AWS Only) Access via Security Group membership from a peered VPC. IMPORTANT: Atlas does not support adding AWS security groups to
IP access lists in projects with VPC peering connections
in multiple regions. 4 (Optional) Set the IP access list as temporary. Check the Save as temporary access list option to specify
a length of time that the IP address will be added. After this time, Atlas removes the address from the IP access list. You can select
one of the following time periods for the address to be added: 6 hours 1 day 1 week In the IP Access List view, temporary access list entries
display the time remaining until the address will expire. Once the IP
address expires and is deleted, any client or application attempting
to connect to the cluster from the address can't access the cluster. Note You cannot set AWS security groups as temporary access list
entries. 5 Click Save and Close . Modify IP Access List Entries Atlas CLI Atlas Administration API Atlas UI You can't modify IP access list entries with the Atlas CLI.
Select a different interface to learn how to modify IP access
list entries. You can use the Atlas Administration API to modify
existing IP access list entries . 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Go to IP Access List view. If it isn't already displayed, click the IP Access List tab. 3 Edit the target IP access list entry Click Edit for the entry you want to modify. You can modify the IP address or CIDR block of the entry and the
comment associated with the entry. If the entry is temporarily
added, Atlas displays the remaining time until it will
remove the entry and a dropdown to modify the duration of the
IP access list entry or convert it to a permanent entry. Note You can't change a permanent IP access list entry to be
temporary. 4 Click Confirm to save the changes. Delete IP Access List Entries Important When you remove an entry from the IP access list, existing connections
from the removed addresses may remain open for a variable amount of
time. How much time passes before Atlas closes the connection
depends on several factors, including: how the connection was established how the application or driver using the address behaves which protocol (like TCP or UDP ) the connection uses Atlas CLI Atlas Administration API Atlas UI To delete an IP access list from your project using the
Atlas CLI, run the following command: atlas accessLists delete <entry> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas accessLists delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI You can use the Atlas Administration API to delete
existing users . 1 In Atlas , go to the Network Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Network Access under
the Security heading. The Network Access page displays. 2 Go to IP Access List view. If it isn't already displayed, click the IP Access List tab. 3 Click Delete for the desired entry. 4 Click Delete again to confirm. Back Cluster Access Quickstart Next Network Peering
