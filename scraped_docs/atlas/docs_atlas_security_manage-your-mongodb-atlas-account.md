# Manage Your MongoDB Atlas Account - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access Manage Your MongoDB Atlas Account On this page Find Your MongoDB Atlas Account Change Your Atlas Email Address Change Your Name in Atlas Unlink Your MongoDB Atlas Account from Your GitHub Account Unlink Your MongoDB Atlas Account from Your Google Account Delete an Atlas Account Find Your MongoDB Atlas Account You can manage your Atlas account's settings, unlink your account
from your Google or GitHub account, and configure multi-factor
authentication for your Atlas account. To find your MongoDB Atlas account: 1 Click your account's name in the Atlas top menu. 2 Click Manage your MongoDB Account . The Overview page opens. From here, you can: Access the MongoDB Atlas login page . Access Support to view active support cases and
speak to the Support team. Visit the MongoDB University to take free courses to become a certified expert on MongoDB. Visit the MongoDB Community Forums to meet other MongoDB developers. From the left-side navigation bar, you can also: Provide your personal information in Profile Info . If you manage your account through your Google Account, visit your Google Account to manage
your personal information. If you manage your account through your GitHub Account, visit your GitHub Account to
manage your personal information. Unlink your MongoDB Atlas account from Google or GitHub in Profile Info . Manage Your Multi-Factor Authentication
Options in Security . Change Your Atlas Email Address You can change the email address that you use to log in to your MongoDB Atlas account. Note If your login information is managed by an identity provider with Federated Authentication ,
contact your company's administrator instead. If you log in with Google SSO, you must unlink your account before you change your email address. To change your email address: 1 Click your account's name in the Atlas top menu. 2 Click Manage your MongoDB Account . 3 Click Profile Info in the navigation bar. 4 Change your email address. Click Change Email Address under your current email
address. Enter your password. If you have MFA enabled, authenticate with
your MFA method. Enter a new email address. Note You can't use an email address associated with another account
or with a deleted account. Click Save Changes . Note After you save your changes, a banner at the top of the page
asks you to verify your email. If you want to cancel your
change and continue using your original email address, click Cancel Request on the banner. 5 Confirm your new email account. A verification email is sent to your new email address once you save
your changes. In that email, click Verify Email to
update your email address.
The project activity feed records your update. 6 Log in to Atlas . Use your updated email address to log in to Atlas . Change Your Name in Atlas You can change the name in your MongoDB Atlas account. Note If your personal information is managed by an identity provider with Federated Authentication ,
contact your company's administrator instead. To change your name: 1 Click your account's name in the Atlas top menu. 2 Click Manage your MongoDB Account . 3 Click Profile Info in the navigation bar. 4 Change your name. Under the profile section, update the First Name and/or Last Name fields. Click Save Changes . Unlink Your MongoDB Atlas Account from Your GitHub Account If you linked your MongoDB Atlas account to your Github Account, you can unlink it using the following
procedure. To unlink your MongoDB Atlas account from your Github Account: 1 Unlink your account from the GitHub account. Click Manage your MongoDB Account . Click Profile Info .
The console indicates that: Your Atlas account is linked to your GitHub account. If you intend to unlink your account, you must change your
password for your Atlas account. Click Unlink from GitHub . Click Confirm . Atlas sends you an email to your
email account. This message has instructions to reset your Atlas account password. 2 Reset your password. Log in to email and locate the Password Reset email. Note If you don't reset your password within two hours, submit
a new request. Click the password reset link in the email to complete
the password reset process. Type your email. Type your new Atlas password. Note Atlas Password Policy Your Atlas user account password must: Contain at least eight characters. Exclude your email address and Atlas username. Differ from your previous twenty four passwords. Differ from the most commonly used passwords. Retype your new password to confirm it. Click Save .
When your password meets the requirements and
matches in both fields, you have reset your password. Atlas displays a success message with a link to
log in. 3 Log in to Atlas . Click Log in to continue. Type your email. Type your new password. Unlink Your MongoDB Atlas Account from Your Google Account If you linked your MongoDB Atlas account to your Google Account, you can unlink it using the following
procedure. To unlink your MongoDB Atlas account from your Google Account: 1 Unlink your account from the Google account. Click Manage your MongoDB Account . Click Profile Info .
The console indicates that: Your Atlas account is linked to your Google
account. If you intend to unlink your account, you
must change your password for your Atlas account. Click Unlink from Google . Click Confirm . Atlas sends you an email to your
Gmail account. This message has instructions to reset your Atlas account password. 2 Reset your password. Log in to Gmail and locate the Password Reset email. Note If you don't reset your password within two hours, submit
a new request. Click the password reset link in the email to complete
the password reset process. Type your email. Type your new Atlas password. Note Atlas Password Policy Your Atlas user account password must: Contain at least eight characters. Exclude your email address and Atlas username. Differ from your previous twenty four passwords. Differ from the most commonly used passwords. Retype your new password to confirm it. Click Save .
When your password meets the requirements and
matches in both fields, you have reset your password. Atlas displays a success message with a link to
log in. 3 Log in to Atlas . Click Log in to continue. Type your email. Type your new password. Delete an Atlas Account This section walks you through deleting your Atlas account. Prerequisites To delete your Atlas account, you must ensure that you have no: Outstanding invoices Active clusters Projects Organizations Important If you log in to Atlas through an identity provider, you can't
delete your account yourself. Contact your identity provider
to delete your Atlas account. Delete All Projects Delete a Project To delete a project for an organization: You must either have the Owner role for the project or have
the Organization Owner role for the project's organization. The project must have no outstanding invoices. The project must have no active clusters. To learn how
to view your project's invoices, see Manage Invoices . Terminate All Clusters Warning Terminating a cluster also deletes any backup snapshots for that
cluster. See Snapshot Schedule . To terminate an Atlas cluster: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 If you enabled Termination Protection , disable it. Click next to the cluster you want to disable Termination Protection for. Click Edit Config from the drop-down menu. Click Additional Settings . Toggle Termination Protection to Off . Click Review Changes . Click Apply Changes . 3 Click next to the cluster you want to terminate. 4 Click Terminate from the drop-down menu. 5 (Optional) Keep existing snapshots after termination. If you have a Backup Compliance Policy enabled and
you terminate a cluster, Atlas automatically maintains all
existing snapshots after the termination according to the backup
policy. Atlas retains the oplog for restoring a point in time with continuous cloud backup in a static state until Atlas can no longer use them for continuous cloud backup. Otherwise, if you have Cloud Backup enabled, you can toggle Keep existing snapshots after termination to On . If you have Cloud Backup disabled, this option is unavilable. 6 Confirm the termination. Enter the cluster name. Click Terminate . To terminate an Atlas Serverless instance: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 If you enabled termination protection , disable it. Click Edit Config . Select the Serverless instance you want to terminate from the drop-down menu. Click Additional Settings and set the Termination Protection toggle to off . Click Review Changes . Click Apply Changes . 3 Click next to the Serverless instance you want to terminate. 4 Click Terminate . Atlas executes the terminate operation after completing any
in-progress deployment changes. Delete the Project You can delete a project for an organization either from the
organization's Projects view or the project's Project Setting view: Delete from Projects view Delete from Project Setting view 1 In Atlas , go to the Projects page for your organization. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Do one of the following steps: Click the Leaf icon in the upper left corner of the
page. Click the Organization Settings icon next to the Organizations menu, then click Projects in the sidebar. Expand the Projects menu in the navigation bar,
then click View All Projects . The Projects page displays. 2 For the project you want to delete, click . 3 Click Delete Project . 4 If Manage Your Multi-Factor Authentication Options is enabled, enter the verification code. After verifying, click Delete Project again. 1 In Atlas , go to the Project Settings page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Settings . The Project Settings page
displays. 2 In the Delete Project section, click Delete . 3 Click Delete Project to confirm. 4 If Manage Your Multi-Factor Authentication Options is enabled, enter the verification code. After verifying, click Delete Project again. Leave or Delete All Organizations Leave an Organization Note If you are the only Organization Owner in an
organization, you must promote
another member to Organization Owner before you can
leave an organization. 1 View all of your organizations. Expand the Organizations menu in the navigation bar. Click View All Organizations . 2 Leave organization. For the organization you wish to leave, click its Leave button to bring up the Leave Organization dialog box. 3 Click Leave Organization in the Leave Organization dialog box. Delete an Organization Note To delete an organization, you must have the Organization Owner role for the organization. You cannot delete an organization that has active projects. You must
delete the organization's projects before you can delete the
organization. 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 In the General Settings tab, click Delete .
This displays the Delete Organization dialog box. 3 Click Delete Organization to confirm. Once you delete all active clusters, projects, and
organizations, you are no longer billed for any Atlas activity
and no longer receive Atlas alerts. Delete your Atlas Account Note Once you delete your account there's no way to recover it. Atlas requires up to two weeks to fully process an account deletion.
Until then, you can't create a new Atlas account with the email address
associated with your deleted account. 1 Navigate to your Profile Info . Click your name in the top right corner of the Atlas UI. Click Manage your MongoDB Account . Click Profile Info in the left navigation panel. 2 Click Delete Account . 3 Confirm that you want to delete your account. Acknowledge the implications of deleting your Atlas account. Click Confirm Account Deletion . Note If there are any requirements you have not yet met, you are
prompted to complete them before deleting your account. 4 Verify your identity. You are prompted to verify your identity: If you use MFA , you are prompted verify your identity with your
chosen MFA authentication method. If you use Google SSO, MongoDB
sends a code to your email address. Use that code to verify your
identity. Accounts that use Google SSO are automatically
unlinked as part of the account deletion process. If you don't have MFA configured and don't use Google SSO,
you are prompted to re-verify your password. Then, MongoDB sends a
code to your email address. Use that code to finish verifying your
identity. Your account is deleted. Back View Activity Feed Next Personalize the UI
