# Atlas UI Authentication - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access Atlas UI Authentication On this page Federated Authentication Multi-Factor Authentication Authenticate with the Atlas CLI Atlas offers the following options for Atlas UI authentication. Federated Authentication You can link your IdP to Atlas if you provide each with the
appropriate metadata. After you link your IdP to Atlas , you can
map domains, organizations, and roles to your IdP . To learn more, see Configure Federated Authentication . Multi-Factor Authentication Atlas supports MFA to help you control access to your Atlas accounts. To set up MFA , see Manage Your Multi-Factor Authentication Options . Authenticate with the Atlas CLI Log In from the Atlas CLI To authenticate with Atlas using the
Atlas CLI, run the following command: atlas auth login [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas auth login . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI For step-by-step instructions on logging in using the
Atlas CLI, see Connect from the Atlas CLI . Log Out from the Atlas CLI To log out of your Atlas account using the
Atlas CLI, run the following command: atlas auth logout [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas auth logout . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI View Your Authentication Status from the Atlas CLI To verify and display information about your authentication state using the
Atlas CLI, run the following command: atlas auth whoami [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas auth whoami . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI Back Configure UI Access Next Federated
