# Manage Organizations - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access / Authorization / Organization Access Manage Organizations On this page Create an Organization View Organizations Leave an Organization Rename an Organization Delete an Organization In the organizations and projects hierarchy, an organization can
contain multiple projects (previously referred to as groups). Under
this structure: Billing happens at the organization level while preserving visibility
into usage in each project. You can view all projects within an organization. You can use teams to bulk assign organization users to projects within the
organization. If you need to scale beyond the existing project limits , you can create multiple organizations . Create an Organization When you create an organization, you are added as an Organization Owner for the organization. 1 View all of your organizations. Expand the Organizations menu in the navigation bar. Click View All Organizations . 2 Click New Organization . 3 Enter the name for your organization. Important Don't include sensitive information in
your organization name. 4 Select Atlas and click Next . You have the option of adding a new Cloud Manager organization or a new Atlas organization. For more information on Cloud Manager see the documentation . 5 Add members. For existing Atlas users, enter their username. Usually, this is
the email the person used to register. For new Atlas users, enter their email address to send an invitation. 6 Specify the access for the members. 7 (Optional) Disable the IP access list requirement for the Atlas Administration API. When you create a new organization with the Atlas UI, Atlas requires IP access lists for the Atlas Administration API by default. If
you require an IP access list, your Atlas Administration API keys can
make API requests only from the location-based IP or CIDR addresses that you specify in the IP access list. To disable the IP access list requirement and allow your
Atlas Administration API keys to make requests from any address on the internet, toggle Require IP Access List for the Atlas Administration API to OFF . To learn more, see Optional: Require an IP Access List for the Atlas Administration API . 8 Click Create Organization . View Organizations Atlas CLI Atlas UI To list all organizations using the Atlas CLI, run the following command: atlas organizations list [options] To return the details for the organization you specify using the Atlas CLI, run the following command: atlas organizations describe <ID> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas organizations list and atlas organizations describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI 1 Expand the Organizations menu in the navigation bar. 2 Click View All Organizations . Leave an Organization Important To leave an organization, at least another user must exist as an
Owner for the organization. 1 View all of your organizations. Expand the Organizations menu in the navigation bar. Click View All Organizations . 2 Leave organization. For the organization you wish to leave, click its Leave button to bring up the Leave Organization dialog box. 3 Click Leave Organization in the Leave Organization dialog box. Rename an Organization You must have the Organization Owner role for an
organization to rename it. 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Click next to the organization name. 3 Enter the new name for the organization. 4 Click Save . Delete an Organization Important To delete an organization, you must have Organization Owner role for the organization. You can't delete an organization that has active projects. You must
delete the organization's projects before you can delete the
organization. You can't delete an organization with outstanding payments. To
learn more, see Troubleshoot Invoices and Payments . If you have a Backup Compliance Policy enabled , you
can't delete a project if any snapshots
exists. If you can't remove all projects, you can't delete the organization . Atlas CLI Atlas UI To delete an organization using the
Atlas CLI, run the following command: atlas organizations delete <ID> [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas organizations delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 In the General Settings tab, click Delete .
This displays the Delete Organization dialog box. 3 Click Delete Organization to confirm. Back Organization Access Next Users
