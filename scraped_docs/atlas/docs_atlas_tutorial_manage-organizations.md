# Manage Organization Access - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access / Authorization Manage Organization Access On this page Required Access Require Multi-Factor Authentication Require IP Access List for the Atlas Administration API Require IP Access List for the Atlas UI As the Organization Owner , you can control access to your
organization in the following ways: Require Multi-Factor Authentication Require IP Access List for the Atlas Administration API Require IP Access List for the Atlas UI Required Access To perform any of the following actions, you must have Organization Owner access to Atlas . Require Multi-Factor Authentication If you enable multi-factor authentication on
your own Atlas account, you can require that all Atlas users in your organization enable MFA for their Atlas accounts. Procedure 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Toggle Require Multi-Factor Authentication (MFA) to On . Require IP Access List for the Atlas Administration API You can configure Atlas to require API access lists at the organization
level. When you enable IP access list for the Atlas Administration API, all API calls
in that organization must originate from a valid entry in the associated
Atlas Administration API key access list. See also API Access Lists endpoint . Procedure 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Toggle Require IP Access List for the Atlas Administration API to On . Require IP Access List for the Atlas UI Important To enable the configuration of IP access list for the Atlas UI
for your organizations, contact Atlas support . You can configure Atlas to require Atlas UI access lists at the
organization level. When you enable the IP access list for the Atlas UI,
all access to the Atlas UI in that organization must originate from
an entry in that list. You can: Configure and Enable IP Access List for the Atlas UI Edit IP Access List for the Atlas UI Disable IP Access List for the Atlas UI Configure and Enable IP Access List for the Atlas UI To enable IP address access list for an organization, you must add a
CIDR range that includes your own IP address, or your own IP address to
the list. Once you add your IP address or add a CIDR block that contains
this address, Atlas activates the Enable button. You can
then add other IP addresses and CIDR ranges, as needed. 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Configure IP access list for the Atlas UI. Navigate to Define IP Access List for the Atlas User Interface . Click Configure . The IP Access List for the Atlas UI page opens where you can configure, enable, and make changes to the
IP access list for the Atlas UI for your organization. 3 Add IP addresses or CIDR blocks to the IP list for the Atlas UI. Enter an IP address or a CIDR range block in the table. You can: Add IPv4 or IPv6 addresses, such as 1.1.1.2 , for IPv4, and 3ffe:1900:fe21:4545:0000:0000:0000:0000 , for IPv6, or CIDR block
ranges, such as 2.1.1.1/16 , and their descriptions to the list. Click to delete an entered address or range
and enter a new one instead. Atlas validates IP addresses and CIDR blocks that you enter and flags
the invalid entries. You can't: Delete all addresses or your own IP address from the list. If you
attempt to delete these addresses, Atlas prevents you from saving
changes. Add invalid IP addresses, such as malformed or out of range addresses
for the entered CIDR ranges. Add duplicate addresses. You can, however, add a CIDR range that has
a particular IP address and also enter that IP address itself. Edit addresses or CIDR blocks in the table. To edit an entry, delete
it and add a new entry. Add an optional description. Click Add Entry to add an IP address or a CIDR range for
users in your organization, or click Add my Current IP Address . The IP access list table identifies your current IP address or a
CIDR range containing it as yours and adds their descriptions, even
if you didn't provide descriptions for these entries. 4 Enable IP access list for the Atlas UI. To activate the Enable button that enables IP access list
restrictions, you, as an Organization Owner must add your current
IP address or a CIDR range with your current IP address to the list. If the list is empty, or if Atlas detects that the list doesn't have
your IP address, Atlas deactivates the Enable button to
prevent locking you out of the organization. Click Enable . Atlas asks you for a confirmation. Click Enable to confirm, or Cancel to cancel. Once you enable IP access list for the Atlas UI, only the defined
IP addresses and ranges can access this organization's Atlas UI.
If a user's IP address isn't on the list, Atlas disables (grays out)
all organizations with restricted access for this user in its organizations
list. If this user attempts to access an Atlas UI page for any
restricted organization, Atlas displays the following warning: You don't have permission to view the <url-with-organizationID> in the Atlas UI. To gain access, ask the organization owner to add your IP address to the IP access list. API keys that inherit from this IP access list use the list for
IP access restrictions. Edit IP Access List for the Atlas UI If you enable IP access list for the Atlas UI,
the IP Access List for the Atlas UI menu on the
changes from Configure to the following options: Edit and Disable . 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Configure IP access list for the Atlas UI. Go to Define IP Access List for the Atlas User Interface . Click Configure .
The IP Access List for the Atlas UI page opens where you
can make changes to the IP access list for the Atlas UI for your organization. 3 Edit IP addresses or CIDR blocks to the IP access list for the Atlas UI. Click Edit .
The IP list table opens that allows you to add additional IP addresses
or CIDR block ranges. You can: Add IPv4 or IPv6 addresses, such as 1.1.1.2 , for IPv4, and 3ffe:1900:fe21:4545:0000:0000:0000:0000 , for IPv6, or CIDR block
ranges, such as 2.1.1.1/16 , and their descriptions to the list. Click to delete an entered address or range
and enter a new one instead. Atlas validates IP addresses and CIDR blocks that you enter and flags
invalid entries. You can't: Delete all addresses or your own IP address from the list. If you
attempt to delete these addresses, Atlas prevents you from saving changes. Add invalid IP addresses, such as malformed or out of range addresses
for the entered CIDR ranges. Add duplicate addresses. You can, however, add a CIDR range that contains
a particular IP address and also enter that IP address itself. Edit addresses or CIDR blocks in the table. To edit an entry,
delete it and add a new entry. Add an optional description. Click Add Entry to add an IP address or a CIDR range, or
click Add my Current IP Address . 4 Save the edited IP access list. Atlas disables the Save button in the upper-right corner
if you delete your own IP address or a CIDR block with your IP address
from the list. To activate the Save button, add a CIDR block with your
current IP address (or your IP address) to the list, in addition to any
other addresses or CIDR ranges that you or other organization owners
have already added. Click Save. Atlas shows a confirmation message that it successfully saved changes. API keys that inherit from this IP access list use the list for IP access
restrictions. Disable IP Access List for the Atlas UI 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Click Define IP Access List for the Atlas User Interface . Go to Define IP Access List for the Atlas User Interface . 3 Click Configure . The IP Access List for the Atlas UI page opens. If the
list was previously enabled, the Atlas UI shows Enabled next to the page title. 4 Click Disable . Atlas asks you to confirm. If you disable the IP access list, Atlas : Disables all IP restrictions for the Atlas UI` for the organization. Retains the IP access list that you had previously configured.
API keys that inherit from this IP access list no longer use the list
for IP access restrictions. 5 Confirm that you want to disable IP access list. Click Disable to confirm. The Atlas UI shows Disabled next to the page title. Back User Roles Next Organizations
