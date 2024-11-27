# Set up Workload Identity Federation with OAuth 2.0 - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features / Authentication / OIDC/OAuth2.0 Set up Workload Identity Federation with OAuth 2.0 On this page How it Works Built-in Authentication Callback Authentication Procedures Prepare Your External Identity Provider Configure Workload Identity Federation Authentication Add a Database User Using Workload Identity Federation Authentication Connect an Application to MongoDB with Workload Identity Federation Manage an Existing Workload Identity Federation Configuration Revoke JWKS Delete Workload Identity Federation Configuration Workload Identity Federation lets your applications access MongoDB Atlas clusters using external programmatic identities such as Azure Service
Principals, Azure Managed Identities and Google Service
Accounts. You can enable any number of workload identity providers for one
or more organizations. When you enable a Workload Identity Provider in an Atlas organization, you can use it in all the projects in that
organization for database access. Atlas supports Workload Identity Federation on only dedicated clusters (M10 and above)
running MongoDB version 7.0.11 and above, and only by selected drivers. To learn more about implementing Workload Identity Federation access with your chosen
driver, see Connect an Application to MongoDB with Workload Identity Federation . How it Works Workload Identity Federation allows your applications access to MongoDB
clusters with OAuth2.0 access tokens. The access tokens can be issued by
any external Identity Provider including Azure Entra ID and Google Cloud
Platform. Atlas stores the user identifiers and privileges, but
not the secrets. This authentication mechanism for your applications
is only supported by MongoDB drivers. Other MongoDB tools like mongosh and MongoDB Compass don't support this authentication mechanism. MongoDB Drivers support two types of authentication flow for Workload Identity Federation :
Built-in Authentication and Callback Authentication. Built-in Authentication You can use built-in authentication if you deploy your application on a
supported infrastructure with a supported principal type. Your application
can access Atlas clusters without supplying a password or
manually requesting a JWT from your cloud provider's metadata service. Instead,
your chosen MongoDB driver uses your existing principal identifier to request a
JWT access token under the hood, which is then passed to the Atlas cluster
automatically when your application connects. For more implementation details, see your chosen Driver's documentation . Built-in Authentication Supported Infrastructure and Principal Types Cloud Provider Infrastructure Type Principal Type GCP Compute Engine GCP Service Accounts App Engine Standard Environment App Engine Flexible Environment Cloud Functions Cloud Run Google Kubernetes Engine Cloud Build Azure Azure VM Azure Managed Identities (User and System assigned) Callback Authentication You can use callback authentication with any service supporting OAuth2.0
access tokens. Workload Identity Federation calls a callback method, in which you can request
the required JWT from your authorization server or cloud provider that you must
pass when your application connects to Atlas with Workload Identity Federation . Please review your chosen driver's documentation for additional
implementation details. Procedures To configure MongoDB's Workload Identity Federation: Configure Workload Identity Provider (one-time setup) . Configure your external identity provider. Configure Workload Identity Provider in Atlas and
enable it for your Atlas organization(s). Grant external identities (service principals) or groups access to MongoDB clusters . Connect your application to Atlas with a MongoDB Driver . Prepare Your External Identity Provider Azure GCP In order to access MongoDB Atlas clusters with Azure Managed Identities
or Azure Service Principals, you need to register an Azure Entra ID
application. If you have an existing application registration for Workforce (human user) access, we recommended that you register a separate
application for Workload access. 1 Register an application. Navigate to App registrations . In your Azure portal account, search and click Microsoft Entra ID . In the Manage section of the left navigation, click App registrations . Click New registration . Apply the following values. Field Value Name Atlas Database - Workload Supported Account Types Accounts in this organizational directory only (single tenant) Redirect URI Web 2 (Optional) Add groups claim. It is a best practice to use service principal identifiers as MongoDB user
identifiers while defining access rights in Atlas. If you plan to
use this common approach, skip this step. However, if you prefer to use
group identifiers such as Azure AD Security Group identifier
instead, you can set groups claim in your application registration
with below steps. Navigate to Token Configuration . In the Manage section of the left navigation,
click Token Configuration . Click Add groups claim . In the Edit groups claim modal, select Security . What groups you select depend on the type of groups you configured
in your Azure environment. You may need to select a different
type of group to send the appropriate group information. In the Customize token properties by type section, ensure that you only select Group ID . When you select Group Id , Azure sends the
security group's Object ID. Click Add . To learn more about adding a group claim, see Azure Documentation . 3 Enable an Application ID URI. Navigate to Expose an API in the left sidebar and enable Application ID URI. Enable an Application ID URI. Keep the default Application ID URI assigned by Azure,
which is <application_client_id> . Copy and store this value,
as MongoDB Atlas and all MongoDB drivers require this value
for Workload Identity Federation configuration. 4 Update the manifest. In the Manage section of the left navigation, click Manifest . Update the accessTokenAcceptedVersion from null to 2 . The number 2 represents Version 2 of Microsoft's access
tokens. Other applications can use this as a signed
attestation of the Active Directory-managed user's identity.
Version 2 ensures that the token is a JSON Web Token that
MongoDB understands. Click Save . To learn more about adding an optional claim, see Azure Documentation . 5 Remember metadata. In the left navigation, click Overview . Copy the Application (client) ID value. In the top navigation, click Endpoints . Copy the OpenID Connect metadata document value
without the /.well-known/openid-configuration part. You can also retrieve this value by following the OpenID Connect metadata document URL and
copying the value for issuer . The following table shows what these Microsoft Entra ID UI values map to in our Atlas Configuration Properties: Microsoft Entra ID UI Atlas Configuration Property OpenID Connect metadata document (without /.well-known/openid-configuration) Issuer URI . Application (client) ID Client ID . Application ID URI (<Application ID>) Audience You don't need to make any configuration changes in your Google Cloud account. Configure Workload Identity Federation Authentication Note Prerequisite This procedure requires you to have Organization Owner access and assumes you have already configured your external IdP . To learn
how to configure an IdP , see Configure An External Identity Provider Application . You can configure Workload Identity Federation for database access in Atlas from the Federation Management Console . Azure GCP To configure a Workload Identity Federation Identity Provider with Azure Entra ID in Atlas : 1 Navigate to Organization settings. Click on Open Federation Management App . 2 Click Identity Providers on the left sidebar. Click Set Up Identity Provider or Configure Identity Provider Select Workload Identity Provider and click Continue . 3 Enter the following Workload Identity Federation settings. Setting Necessity Value Configuration Name Required Specify a human-readable label that identifies this configuration.
This label is visible to Atlas users. Configuration Description Optional Describe this configuration. Issuer URI Required Specify the issuer URI value provided by your Microsoft Entra ID application
registration. To learn more, see the table in Prepare your External Identity . Audience Required Specify the application ID URI value from your Azure Entra ID application
registration. To learn more, see the table in Prepare your External Identity . Authorization Type Required Select Group Membership to grant authorization based on group
membership, or select User ID to authorize an individual user. It is more common to use User ID for application access. Groups Claim Conditional Specify the identifier of the claim that includes the principal's IdP user group membership information. If you
select Groups Membership as authorization type, you must
specify this field. Leave the value set to the default, groups . Default : groups User Claim Required Don't modify the default value, sub . Default : sub 4 Click Save and Finish . 5 Enable your Workload Identity for an organization. Click Connect Organizations . For the organization that you want to connect to Workload Identity Federation, click Configure Access . Click Connect Identity Provider . Note If you already configured another IdP , Atlas displays
a Connect Identity Provider(s) button instead. 6 Select a Workload Identity Provider. In the Connect Identity Provider(s) modal, select
a Workload Identity Provider where the Purpose is Workload Identity Federation . 7 Click Connect . When you connect your Workload Identity Provider to an
organization, Atlas enables Workload Identity Federation for all the
projects within that organization. To configure a Workload Identity Federation Identity Provider with Google Cloud in Atlas : 1 Navigate to Organization settings. Click on Open Federation Management App . 2 Click Identity Providers on the left sidebar. Click Set Up Identity Provider or Configure Identity Provider Select Workload Identity Provider and click Continue . 3 Enter the following Workload Identity Federation settings. Setting Necessity Value Configuration Name Required Specify a human-readable label that identifies this configuration.
This label is visible to Atlas users. Configuration Description Optional Describe this configuration. Issuer URI Required Enter the URI https://accounts.google.com . Audience Required Specify any custom value. Audience is used
while calling MongoDB drivers. Authorization Type Required Select Group Membership to grant authorization based on group
membership, or select User ID to authorize individual users. It is more common to use User ID for application access. User Claim Required Don't modify the default value, sub . Default : sub 4 Click Save and Finish . 5 Enable your Workload Identity in an organization. Click Connect Organizations . For the organization you want to connect to Workload Identity Federation , click Configure Access . Click Connect Identity Provider . Note If you already configured another IdP , Atlas displays
a Connect Identity Provider(s) button instead. 6 Select a Workload Identity Provider. In the Connect Identity Provider(s) modal, select
a Workload Identity Provider where the Purpose is Workload Identity Federation . 7 Click Connect . When you connect your Workload Identity Provider to an
organization, Atlas enables Workload Identity Federation for all the
projects within that organization. Add a Database User Using Workload Identity Federation Authentication Prerequisites Before you begin, you must have the following to add a database user: Project Owner access Workload Identity Federation configured in Atlas and enabled for your Organization. 1 Open the Add New Database User or Group dialog box. 2 Select Federated Auth . In the Authentication Method section, select Federated Auth . Note Until you enable Workload IdP for your organization ,
you can't select this box. 3 Select an Identity Provider and Identifier. In the Select Identity Provider section, select a configured
Workload Identity Provider. Specify either the user identifier or group identifier associated with
your configured Workload Identity Provider . Note For Azure Entra ID users, this value maps to the Object Id
of your Azure user group rather than user group name. For GCP users, this value maps to the Unique Id of your
GCP Service Account. 4 Assign user or group privileges. 5 Add the new database user or group. If you added a user, click the Add User button. If you added a group, click the Add Group button. Connect an Application to MongoDB with Workload Identity Federation Use the listed version or higher of the following MongoDB Drivers to connect an
application to MongoDB with Workload Identity Federation authentication: Java v5.1+ C#/.NET v2.25+ Go v1.17+ PyMongo v4.7+ Node / Typescript v6.7+ Kotlin v5.1+ Manage an Existing Workload Identity Federation Configuration Revoke JWKS Note This procedure is only for users who manage their own signing keys. Don't use this feature to rotate your signing keys. When you rotate
your Workload Identity Federation signing keys, MongoDB fetches
the JWKS automatically upon expiration of the existing access tokens. If your private key is compromised, you can immediately revoke your JSON
Web Key Sets (JWKS) cached in MongoDB nodes: 1 Update your signing keys in your Workload Identity provider. 2 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 3 Navigate to the Federation Management App. In the Setup Federated Login or Manage
Federation Settings section, click Visit Federation
Management App . 4 Click Identity Providers in the left sidebar. 5 Scroll to the Workload Identity Federation card. 6 Click the Revoke button under the Manage dropdown. After you click Revoke , MongoDB fetches the new keys
through your JWKS endpoint. You must restart your clients (such as mongosh or Compass ) after you revoke JWKS. Delete Workload Identity Federation Configuration To delete your Workload Identity Federation configuration: 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Navigate to the Federation Management App. In the Setup Federated Login or Manage
Federation Settings section, click Visit Federation
Management App . 3 Disconnect each organization you connected to your Workload Identity Provider. Click Organizations in the left sidebar. Click the organization that has Workload Identity Federation enabled. Click Disconnect under the Manage dropdown on the Workload Identity Federation card. In the Disconnect identity provider? modal, click Disconnect . When you disconnect an IdP , users who authenticate using the IdP lose access to Workload Identity Federation in the Atlas projects
listed in the Project table. 4 Click Identity Providers in the left side navigation
bar. 5 In the Workload Identity Federation card, click Delete . 6 In the Delete Identity Provider? modal, click Delete . Back Workforce (Humans) Next X.509
