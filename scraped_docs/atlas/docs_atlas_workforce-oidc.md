# Set up Workforce Identity Federation with OIDC - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Authentication / OIDC/OAuth2.0 Set up Workforce Identity Federation with OIDC On this page Required Access Procedures Configure An External Identity Provider Application Configure Workforce Identity Federation Authentication Add a Database User using Workforce Authentication Connect an Application to MongoDB with Workforce Identity Federation Manage an Existing Workforce Identity Federation Configuration Revoke JWKS Delete a Workforce Identity Provider Configuration In MongoDB 7.0 and later, Workforce Identity Federation lets you use an
external Identity Provider (IdP), such as your corporate IdP , to authenticate
and authorize a given workforce, such as employees, partners,
and contractors. With Workforce Identity Federation, you can: Manage your workforce access to MongoDB deployments through your
existing IdP . Enforce security policies such as password complexity, credential
rotation, and MFA within your IdP . Grant access for a group of users or a single user . After you configure your external IdP and add it to your
Workforce Identity Federation one time, you can enable Workforce Identity Provider for multiple Atlas organizations. After you enable Workforce Identity Federation
in a given organization, you can use it in all projects in that organization
for database access. Workforce Identity Federation is supported by Atlas dedicated clusters
(M10 and above) running MongoDB version 7.0.11 and above. You need to use
MongoDB Shell or Compass to access Atlas with Workforce Identity Federation. To learn more about implementing Workforce Identity Federation access, see Connect an Application to MongoDB with Workforce Identity Federation . Required Access To manage Workforce Identity Federation configuration, you must have Organization Owner access to Atlas . Procedures To access Atlas clusters with Workforce Identity Federation, complete the following steps: Configure a Workforce Identity Provider (one-time setup). Configure your external identity provider . Configure Workforce Identity Provider in Atlas and
enable it for your |service| organization(s) . Grant external identities (user principals) or groups access
to MongoDB clusters. Authenticate to your Atlas clusters with MongoDB Shell or Compass. Configure An External Identity Provider Application To configure Workforce Identity Federation with OIDC , register your OIDC application with an IdP that supports OIDC standard, such
as Microsoft Entra ID , Okta, or
Ping Identity. Note Workforce Identity Federation supports only JWT for authentication. It doesn't
support opaque access tokens. You can configure your OIDC application for the following grant types: Authorization Code Flow with PKCE Device Authorization Flow MongoDB recommends that you use Authorization Code Flow with PKCE for increased
security. Use Device Authorization Flow only if your users need
to access the database from machines with no browser. The OIDC application registration steps can vary based on your IdP . Ensure that you complete the following items during
your registration process: 1 Register a new application for Atlas . Select public client/native application as the client type. 2 Set the Redirect URL value to http://localhost:27097/redirect . 3 (Conditional) Add or enable a groups claim if you authenticate with groups. For groups, this step ensures that your access tokens contain the group
membership information of the user authenticating. MongoDB uses the
values sent in a groups claim for authorization. 4 (Optional) Allow refresh tokens if you want MongoDB clients to
refresh the tokens for a better user experience. 5 (Optional) Configure the access token lifetime ( exp claim) to align with
your database connection session time. After you register your application, save the issuer , clientId , and audience values to use in the next stage of the Atlas Workforce IdP configuration . To register your OIDC application with Microsoft Entra ID : 1 Register an application. Navigate to App registrations . In your Azure portal account, search and click Microsoft Entra ID . In the Manage section of the left navigation, click App registrations . Click New registration . Apply the following values. Field Value Name Atlas Database - Workforce Supported Account Types Accounts in this organizational directory only (single tenant) Redirect URI - Public client/native (mobile & desktop) - http://localhost:27097/redirect Click Register . To learn more about registering an application, see Azure Documentation . 2 Add a group claim. Navigate to Token Configuration . In the Manage section of the left navigation,
click Token Configuration . Click Add groups claim . In the Edit groups claim modal, select Security . What groups you select depend on the type of groups you configured
in your Azure environment. You may need to select a different
type of group to send the appropriate group information. In the Customize token properties by type section, only select Group ID . Click Add . To learn more about adding a group claim, see Azure Documentation . 3 Add a user identifier claim to the access token. Click Add optional claim . In the Add optional claim modal, select Access . Select a claim that carries a user identifier that you can
refer to in MongoDB access logs such as an email. You can use the UPN claim to identify users with their email address. Click Add . In the Microsoft Graph Permissions note, check the box, and click Add . To learn more, see Azure Documentation . 4 Update the manifest. In the Manage section of the left navigation, click Manifest . Update the accessTokenAcceptedVersion from null to 2 . The number 2 represents Version 2 of Microsoft's access
tokens. Other applications can use this as a signed
attestation of the Active Directory-managed user's identity.
Version 2 ensures that the token is a JSON Web Token that
MongoDB understands. Click Save . To learn more about adding an optional claim, see Azure Documentation . 5 Remember metadata. In the left navigation, click Overview . Copy the Application (client) ID value. In the top navigation, click Endpoints . Copy the OpenID Connect metadata document value
without the /.well-known/openid-configuration part. You can also get this value by copying the value for issuer in the OpenID Connect metadata document URL . The following table shows what these Microsoft Entra ID UI values map to in our Atlas Configuration Properties: Microsoft Entra ID UI Atlas Configuration Property Application (client) ID Client ID Audience OpenID Connect metadata document (without /.well-known/openid-configuration) Issuer URI . Configure Workforce Identity Federation Authentication Note Prerequisite This procedure requires you to have Organization Owner access and assumes you already have an OIDC application
created in your IdP . To learn
how to configure an IdP , see Configure An External Identity Provider Application . You can configure Workforce Identity Federation with OIDC for database access in Atlas from the Federation Management Console . To configure a Workforce Identity Provider in Atlas : 1 Go to the Federation Management Console. Navigate to Organization settings. Click on Open Federation Management App . 2 Add and verify domain ownership. You must verify ownership of the domain that you register with your IdP .
You can skip this step if you've already registered your
domain for SAML SSO with Atlas . Select Domains in the left sidebar. Click the Add Domain button. Enter a display name in the Display Name box. Enter a domain name in the Domain Name box. Select the method you would like to use to verify that you are the owner
of your domain by clicking either the HTML File Upload or DNS Record button. If you selected HTML File Upload , download the provided
HTML file and upload it to your domain so that it is accessible at https://<your-domain/mongodb-site-verification.html> . If you selected DNS Record , copy the provided TXT Record ,
and upload it to your domain provider. Click Continue . Finally, in the Domains page, click the Verify button for your newly added domain. 3 Configure identify providers. Click Identity Providers in the left sidebar. Do one of the following steps: If you do not have any Identity Providers configured yet, click Setup Identity Provider . Otherwise, on the Identity Providers screen, click Configure Identity Provider(s) . Select Workforce Identity Provider and click Continue . Select OIDC for Data Access . 4 Enter the following Workforce Identity Provider Protocol Settings. Setting Necessity Value Configuration Name Required Human-readable label that identifies this configuration. This label
is visible to your Atlas users. Configuration Description Optional Human-readable label that describes this configuration. Issuer URI Required Issuer value provided by your registered IdP application.
Using this URI, MongoDB finds an OpenID Provider Configuration
Document, which should be available in the /.wellknown/open-id-configuration endpoint. Client ID Required Unique identifier for your registered application. Enter
the clientId value from the app you registered
with external Identity Provider . Audience Required Entity that your external identity provider intends the token for. Enter
the audience value from the app you registered
with external Identity Provider . Generally, this value is the same as the Client ID . Authorization Type Required Select Group Membership to grant authorization based on IdP user group membership, or select User ID to grant an individual
user authorization. Requested Scopes Optional Tokens that give users permission to request data
from the authorization endpoint. If you plan to support refresh tokens,
this field must include the value offline_access . If your identity provider is Microsoft Entra ID , Atlas requires
this setting. Add default scope, which is <application client id>/.default . For each additional scope you
want to add, click Add more scopes . User Claim Required Identifier of the claim that includes the user principal
identity. Accept the default value unless your IdP uses a
different claim. Default : sub Groups Claim Required Identifier of the claim that includes the principal's IdP user group membership information. Accept the default value
unless your IdP uses a different claim, or you need a custom
claim. This field is only required if you select Groups Membership . Default : groups 5 Click Save and Finish . 6 Associate at least one domain to your Workforce IdP . In your Workforce Identity Provider card, click Associate Domains . In the Associate Domains with Identity Provider modal,
select one or more domains. Click Submit . 7 Enable your Workforce Identity Provider in an organization. Click Connect Organizations . For the organization you want to connect to Workforce Identity Provider,
click Configure Access . Click Connect Identity Provider . Note If you have another IdP configured, this button says Connect Identity Provider(s) . 8 Select Workforce Identity Federation for Data Access . In the Connect Identity Provider(s) modal, select  a
Workforce Identity Provider where the Purpose is Workforce Identity Federation . 9 Click Connect . When you connect your Workforce Identity Provider to an organization, Atlas enables your Workforce Identity Provider for all the projects within that organization. Add a Database User using Workforce Authentication 1 In Atlas , go to the Database Access page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Database Access under
the Security heading. The Database Access page
displays. 2 Open the Add New Database User or Group dialog box. Click Add New Database User or Group . Note Until you apply your Workforce IdP to Atlas , this button says Add New Database User . 3 Select Federated Auth . In the Authentication Method section, select Federated Auth . Note Until you enable Workforce IdP for your organization ,
you can't select this box. 4 Select Identity Provider and Identifier a. In the Select Identity Provider section, select a configured OIDC Identity Provider . Specify either the user identifier or group identifier associated with
your configured Workforce Identity Provider . Note For Azure Entra ID users, this value maps to the Object Id of your
Azure user group rather than user group name. 5 Assign user or group privileges. To assign privileges to the new user or group, do one or more of the
following tasks: Select a built-in role from the Built-in Role dropdown menu. You can select one built-in role per database group in the Atlas UI. If you delete the default option, you can click Add Built-in Role to select a new built-in role. Select or add custom roles . If you have any custom roles defined, you can expand
the Custom Roles section and select
one or more roles from the Custom Roles dropdown menu. Click Add Custom Role to add more custom roles. Click the Custom Roles link to see the custom
roles for your project. Add privileges . Expand the Specific Privileges section and select one or more
privileges from the Specific Privileges dropdown menu. Click Add Specific Privilege to add more privileges. This assigns
the group specific privileges on individual databases and collections. Remove an applied role or privilege. Click Delete next to the role or privilege to delete. Note Atlas doesn't display the Delete icon
next to your Built-in Role , Custom Role , or Specific Privilege selection if you selected only one option. You
can delete the selected role or privilege once you apply another role or privilege. Atlas can apply a built-in role, multiple custom roles, and multiple specific
privileges to a database group. To learn more about authorization, see Role-Based
Access Control and Built-in
Roles in the MongoDB manual. 6 Specify the resources in the project that the user or group can access. By default, groups can access all the clusters and federated database instances in the
project. To restrict access to specific clusters and federated database instances: Toggle Restrict Access to Specific Clusters/Federated
Database Instances to On . Select the clusters and federated database instances to grant the group access to
from the Grant Access To list. 7 Save as a temporary user or group. Toggle Temporary User or Temporary Group to On and choose a time after which Atlas can delete the user
or group from the Temporary User Duration or Temporary Group Duration dropdown. You can select one of the
following time periods for the group to exist: 6 hours 1 day 1 week In the Database Users tab, temporary users or groups display
the time remaining until Atlas deletes the users or group. After Atlas deletes the user or group, any client or application that uses
the temporary user's or group's credentials loses access to the cluster. 8 Add the new database user or group. Do one of the following steps: If you added a user, click the Add User button. If you added a group, click the Add Group button. Connect an Application to MongoDB with Workforce Identity Federation The following lists the ways you can connect an application to MongoDB
with Workforce Identity Federation authentication: Compass v1.38+ MongoDB Shell v2.14+ Manage an Existing Workforce Identity Federation Configuration Revoke JWKS Note Use the following procedure only if you manage your own signing keys. Don't use this feature to rotate your signing keys. When you rotate
your Workforce Identity Provider signing keys, MongoDB fetches the JWKS automatically
when the existing access tokens expire. If your private key is compromised, you can immediately revoke your JSON
Web Key Sets (JWKS) cached in MongoDB nodes: 1 Update your signing keys in your Workforce identity provider. 2 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 3 Navigate to the Federation Management App. In the Setup Federated Login or Manage
Federation Settings section, click Visit Federation
Management App . 4 Click Identity Providers in the left sidebar. 5 Scroll to the Workforce Identity Provider card. 6 Click the Revoke button. After you click Revoke , MongoDB fetches the new keys
through your JWKS endpoint. You must restart your clients (such as mongosh or Compass ) after you revoke JWKS. Delete a Workforce Identity Provider Configuration To delete your Workforce Identity Provider configuration: 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Navigate to the Federation Management App. In the Setup Federated Login or Manage
Federation Settings section, click Visit Federation
Management App . 3 Disconnect each organization you connected to your Workforce Identity Provider . Click Organizations in the left sidebar. Click the organization that has Workforce Identity Federation enabled. Click Disconnect under the Manage dropdown on the Workforce Identity Federation card. In the Disconnect identity provider? modal, click Disconnect . When you disconnect an IdP , users who authenticate using the IdP lose access to Workforce Identity Federation in the Atlas projects
listed in the Project table. 4 Click Identity Providers in the left sidebar. 5 In the Workforce Identity Provider card, click Delete . 6 In the Delete Identity Provider? modal, click Delete . Back OIDC/OAuth2.0 Next Workload (Applications)
