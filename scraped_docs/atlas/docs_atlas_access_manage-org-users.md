# Manage Organization Users - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access / Authorization / Organization Access Manage Organization Users On this page Required Access Add Users to an Organization View Active Users and Outgoing Invitations in an Organization Edit User's Role in an Organization Remove Users from an Organization You can grant Atlas users access to Atlas organizations. Assign user roles to enforce permission levels for Atlas users. It is recommended that you create a minimum of two users with the Organization Owner role to ensure that access to an
organization does not depend on a single user. Important Project Invitation Deprecation The Atlas release on September 13, 2023 deprecates project
invitations. When you invite an organization member to projects within the
organization, the user is automatically granted access to
those projects and doesn't receive any invitations. When you invite a
user to projects in an organization that the user doesn't belong to,
the user receives a single invitation to the organization, which
includes access to all of the projects that you grant them access to.
Invitations expire after 30 days. Required Access To perform any of the following actions, you must have Organization Owner access to Atlas . Add Users to an Organization Important Atlas limits Atlas user membership to a maximum of 500 Atlas users per organization. Atlas CLI Atlas UI To invite a user to your organization using the
Atlas CLI, run the following command: atlas users invite [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas users invite . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To invite users to an organization using the Atlas UI: 1 In Atlas , go to the Organization Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Select Organization Access from the Access Manager menu in the navigation bar. Click Access Manager in the sidebar. The Organization Access Manager page
displays. 2 Invite Users to the organization. Click Invite Users . From the Add Users page, enter the new user's email
address or Jira username in the combo box. After typing in the email address, either press Enter or click on the email address beneath the New User header under the combo box. Repeat for any additional users. 3 Choose the roles for the new Users. By default, each user is given the Organization Member role. To change or add additional roles for each user, click the
role dropdown menu, then select the checkboxes for each role you want the user to have in the organization. 4 Invite the Users. Click Add Users to Organization . When you invite an organization member to projects within the
organization, the user is automatically granted access to
those projects and doesn't receive any invitations. When you invite a
user to projects in an organization that the user doesn't belong to,
the user receives a single invitation to the organization, which
includes access to all of the projects that you grant them access to.
Invitations expire after 30 days. View Active Users and Outgoing Invitations in an Organization Atlas CLI Atlas UI View Active Users To list all users in your organization using the Atlas CLI, run the following command: atlas organizations users list [options] To return the details for a user you specify using the Atlas CLI, run the following command: atlas users describe [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas organizations users list and atlas users describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI View Pending User Invitations To list all pending invitations to the organization you specify using the Atlas CLI, run the following command: atlas organizations invitations list [options] To return the details for one pending invitation to the organization you specify using the Atlas CLI, run the following command: atlas organizations invitations describe <invitationId> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas organizations invitations list and atlas organizations invitations describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI Modify or Cancel a Pending User Invitation To update one pending invitation to the organization you specify using the Atlas CLI, run the following command: atlas organizations invitations update [invitationId] [options] To delete one pending invitation to the organization you specify using the Atlas CLI, run the following command: atlas organizations invitations delete <invitationId> [options] To learn more about the syntax and parameters for the previous commands, see the Atlas CLI documentation for atlas organizations invitations update and atlas organizations invitations delete . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view users in an organization using the Atlas UI: 1 In Atlas , go to the Organization Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Select Organization Access from the Access Manager menu in the navigation bar. Click Access Manager in the sidebar. The Organization Access Manager page
displays. 2 If it is not already displayed, click the Users tab. This page lists: Users who are members of your Atlas organization. Pending users who have not accepted the invitation to join
the organization or its project within the organization. To cancel an invitation, click to the right of
the pending user. Edit User's Role in an Organization Note You can't edit roles for specific users on the Access Manager page if you configure role mappings for IdP groups. To edit a user's role in an organization: 1 In Atlas , go to the Organization Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Select Organization Access from the Access Manager menu in the navigation bar. Click Access Manager in the sidebar. The Organization Access Manager page
displays. 2 If it is not already displayed, click the Users tab. 3 For the organization user to modify, click Edit Permissions . 4 Select the new role or roles for the user from the menu. 5 Click the checkmark to save your changes. Remove Users from an Organization Note You cannot remove the last Organization Owner from an
organization. To remove a user from an organization: 1 In Atlas , go to the Organization Access Manager page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Select Organization Access from the Access Manager menu in the navigation bar. Click Access Manager in the sidebar. The Organization Access Manager page
displays. 2 If it is not already displayed, click the Users tab. 3 Click to the right of the user to remove. 4 To confirm a user removal, click Remove User from Organization . Back Organizations Next Teams
