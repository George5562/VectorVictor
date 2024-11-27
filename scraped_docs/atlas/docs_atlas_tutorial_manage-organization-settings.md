# Manage Organization Settings - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access / Authorization / Organization Access Manage Organization Settings On this page Required Access Add Security Contact Information Disable Generative AI Features Live Migration: Connect to Atlas Integrations Required Access To perform any of the following actions, you must have Organization Owner access to Atlas . Add Security Contact Information Specify a designated Atlas security contact to recieve
security-related notifications. Considerations You can specify only one email address to receive security-related
notifications including those from the MongoDB Security Team. We recommend that you create a mailing list that uses a single
address, and specify it as the security contact as a best practice.
A mailing list can also send these notifications to multiple users. Specifying a security contact does not grant them authorization or
access to Atlas for security decisions or approvals. If the account for the security contact gets deleted, the
security contact setting is cleared, and the former security
contact is shown as the modifier on the related notifications and
events. Procedure 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Specify an Atlas security contact. In the Atlas Security Contact Information section,
click . Specify an email address. Specifying a valid email address enables the Save button. Click Save . Delete an Existing Security Contact To delete the currently specified security contact: 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Specify an Atlas security contact. In the Atlas Security Contact Information section,
click . Delete the existing email address. Click Save . Disable Generative AI Features Generative AI features are enabled by default in Atlas .
When this setting is turned on, Project Owners can enable or disable individual AI features at the project level.
To learn more, see Generative AI FAQs . To disable generative AI features for all projects in your organization: 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Toggle the button next to Enable Atlas features that use generative AI to Off . This disables Atlas features that use generative AI across
all projects in the organization. Live Migration: Connect to Atlas You connect to an organization in Atlas when you live migrate your deployment from Cloud Manager or Ops Manager to Atlas . Integrations You can configure Atlas for the following integrations: Slack Vercel Configure Slack Workspaces 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Go to the Organization Integrations page. Click Integrations in the sidebar. The Organization Integrations page
displays. 3 Click Add to Slack . 4 Sign in to your Workspace. Type your workspace name into the field. Click Continue . Select your authentication method. Click Authorize . 5 Click Save . Important You can authorize only one Slack Workspace for each Organization. Select Organization to Remove Slack Authorization 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Go to the Organization Integrations page. Click Integrations in the sidebar. The Organization Integrations page
displays. 3 Click Remove Integration . Important This does not stop Atlas from sending alerts. To stop Atlas from sending alerts to Slack, you must delete the Slack alert
setting . Configure Vercel Integrations You can connect your Atlas clusters to applications that you
deploy using Vercel . To learn more, see Integrate with Vercel . Back Teams Next Project Access
