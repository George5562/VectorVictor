# Configure Settings Using a Configuration File - MongoDB Shell


Docs Home / MongoDB Shell / Configure / Configure Settings Configure Settings Using a Configuration File On this page Configuration File Format Configuration File Location Configurable Settings Behavior with config API You can specify mongosh settings in a global configuration file.
When you specify settings in a configuration file, those settings are
applied at startup. After you create a configuration file, the settings
in the file take effect the next time you start mongosh . Configuration File Format The mongosh configuration file uses the YAML format. All options are
under the mongosh namespace. Example Configuration File The following configuration file sets: displayBatchSize to 50 inspectDepth to 20 redactHistory to remove-redact mongosh: displayBatchSize: 50 inspectDepth: 20 redactHistory: "remove-redact" Configuration File Location The file location where mongosh looks for the configuration file
depends on your operating system: Operating System File Location Windows mongosh.cfg , in the same directory as the mongosh.exe binary. macOS mongosh looks for a configuration file in the following
directories in the order they are listed: /usr/local/etc/mongosh.conf /opt/homebrew/etc/mongosh.conf /etc/mongosh.conf Once mongosh reads a configuration file in one of these
directories, any remaining directories in the list are not
checked and configuration files in those directories are ignored. Linux /etc/mongosh.conf Configurable Settings You can specify the following mongosh settings in your configuration
file: Key Type Default Description displayBatchSize integer 20 The number of items displayed per cursor iteration enableTelemetry boolean true Enables sending anonymized tracking and diagnostic data to
MongoDB. editor string null Designates an editor to use within the mongosh console. Overrides the EDITOR environment variable if set. forceDisableTelemetry boolean false Only available in the global configuration file. When true,
users cannot enable telemetry manually. historyLength integer 1000 The number of items to store in mongosh REPL's
history file. inspectCompact integer or boolean 3 The level of inner elements that mongosh outputs
on a single line. Short array elements are also grouped together
on a single line. If set to false , mongosh outputs each field
on its own line. inspectDepth integer or Infinity 6 The depth to which objects are printed. Setting inspectDepth to Infinity (the javascript object) prints all nested
objects to their full depth. redactHistory string remove Controls what information is recorded in the shell history.
Must be one of: keep : Retain all history. remove : Remove lines which contain sensitive information. remove-redact : Redact sensitive information. showStackTraces boolean false Controls display of a stack trace along with error messages. snippetAutoload boolean true If true , automatically load installed snippets at startup. snippetIndexSourceURLs string MongoDB Repository A semicolon-separated list of URLs that link to a snippet registry. snippetRegistryURL string npm Registry The npm registry used by the mongosh npm client
that installs snippet . Behavior with config API Settings specified with the config API : Override settings specified in the configuration file. Persist across restarts. Example Consider the following configuration file that sets the inspectDepth setting to 20 : mongosh: inspectDepth: 20 During your mongosh session you run the following command to set inspectDepth to 10 : config. set ( "inspectDepth" , 10 ) The value of inspectDepth becomes 10 , and will remain 10 even when mongosh is restarted. Back Use the API Next Customize Prompt
