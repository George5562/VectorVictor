# Configure Settings - MongoDB Shell


Docs Home / MongoDB Shell / Configure Configure Settings On this page Configurable Settings How to Configure Settings To specify certain shell behaviors, you can configure mongosh settings. Configurable Settings You can configure the following settings for mongosh : Key Type Default Description displayBatchSize integer 20 The number of items displayed per cursor iteration enableTelemetry boolean true Enables sending anonymized tracking and diagnostic data to
MongoDB. editor string null Designates an editor to use within the mongosh console. Overrides the EDITOR environment variable if set. forceDisableTelemetry boolean false Only available in the global configuration file. When true,
users cannot enable telemetry manually. historyLength integer 1000 The number of items to store in mongosh REPL's
history file. inspectCompact integer or boolean 3 The level of inner elements that mongosh outputs
on a single line. Short array elements are also grouped together
on a single line. If set to false , mongosh outputs each field
on its own line. inspectDepth integer or Infinity 6 The depth to which objects are printed. Setting inspectDepth to Infinity (the javascript object) prints all nested
objects to their full depth. redactHistory string remove Controls what information is recorded in the shell history.
Must be one of: keep : Retain all history. remove : Remove lines which contain sensitive information. remove-redact : Redact sensitive information. showStackTraces boolean false Controls display of a stack trace along with error messages. snippetAutoload boolean true If true , automatically load installed snippets at startup. snippetIndexSourceURLs string MongoDB Repository A semicolon-separated list of URLs that link to a snippet registry. snippetRegistryURL string npm Registry The npm registry used by the mongosh npm client
that installs snippet . How to Configure Settings To configure mongosh settings, you can either use: The config API A global configuration file Back Use an Editor Next Use the API
