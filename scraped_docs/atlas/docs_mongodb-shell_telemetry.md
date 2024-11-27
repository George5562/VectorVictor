# Configure Telemetry Options - MongoDB Shell


Docs Home / MongoDB Shell / Configure Configure Telemetry Options On this page Data Tracked by mongosh Toggle Telemetry Collection mongosh collects anonymous aggregated usage data to improve
MongoDB products. mongosh collects this information by default, but
you can disable this data collection at any time. Data Tracked by mongosh mongosh tracks the following data: The type of MongoDB mongosh is connected to. For example,
Enterprise Edition, Community Edition, or Atlas Data Lake. The methods run in mongosh . mongosh only tracks the names of
the methods, and does not track any arguments supplied to methods. Whether users run scripts with mongosh . Errors. mongosh does not track: IP addresses, hostnames, usernames, or credentials. Queries run in mongosh . Any data stored in your MongoDB deployment. Personal identifiable information. For more information, see MongoDB's Privacy Policy . Toggle Telemetry Collection Use the following methods in mongosh to toggle telemetry data
collection. disableTelemetry() Disable telemetry for mongosh . disableTelemetry ( ) The command response confirms that telemetry is disabled: Telemetry is now disabled. Tip You can also disable telemetry at startup by using the --eval startup option. The following command starts mongosh with telemetry disabled: mongosh - - nodb - - eval "disableTelemetry()" enableTelemetry() Enable telemetry for mongosh . enableTelemetry ( ) The command response confirms that telemetry is enabled: Telemetry is now enabled. Back Customize Prompt Next Run Commands
