# Troubleshooting - MongoDB Shell


Docs Home / MongoDB Shell / Snippets Troubleshooting On this page View npm Log Files Non-specific Error Message Error: Cannot find module Uninstalling a Snippet Fails Warning Experimental feature This feature is experimental. MongoDB does not provide support for
Snippets. This feature may be changed or removed at any time without
prior notice. Bugs are not expected, however should you encounter one, please open an
issue in the GitHub repository for this project. The following sections provide troubleshooting suggestions. View npm Log Files The npm log files are a good place to start if you encounter a
problem. The log file location will vary depending on your npm installation. It will be something like: /<NPM USER HOME>/.npm/_logs/2021-09-16T22_03_34_534Z-debug.log When you locate the log files, check the most recent one. Non-specific Error Message Problem : mongosh returns a non-specific error
message when you try to start the shell. Solution : Disable snippets, restart mongosh to
continue debugging. mongosh - - nodb - - eval 'config.set("snippetIndexSourceURLs", "")' Error: Cannot find module Problem : mongosh returns an error message like this when you try
to start the shell: Error : Cannot find module '/<PATH to USER HOME>/.mongodb/mongosh/snippets/node_modules/@<REGISTRY NAME>/bad-snippet-name' The npm log file may have lines like these: 36 error code ELSPROBLEMS 37 error missing : @ < REGISTRY NAME > / bad - snippet - name@ * , required by snippets@ Solution : Edit the ~/.mongodb/mongosh/snippets/package.json file to remove the line with the bad-snippet-name . In this example, do not forget to delete the trailing comma from the
line above as well. { "dependencies": { "@mongosh/snippet-analyze-schema": "^1.0.5", "@mongosh/snippet-spawn-mongod": "^1.0.1", "npm": "*", "@<REGISTRY NAME>/bad-snippet-name": "^1.0.7" } } Uninstalling a Snippet Fails Problem : Uninstall fails, but the error message refers to a
different snippet. The following error message below is reformatted for readability: Running uninstall... Uncaught: Error: Command failed: /usr/bin/mongosh /root/.mongodb/mongosh/snippets/node_modules/npm/bin/npm-cli.js --no-package-lock --ignore-scripts --registry=https://registry.npmjs.org uninstall --save @mongosh/snippet-mongocompat with exit code 1: \ npm ERR! code E404 npm ERR! 404 Not Found - GET https://registry.npmjs.org/@<REGISTRY NAME>%2fbad-snippet-name - Not found npm ERR! 404 npm ERR! 404  '@<REGISTRY NAME>/bad-snippet-namen@*' is not in this registry. Solution : Edit the package.json file to remove the missing
entry. In this example, delete the highlighted line and the trailing
comma from the line above. { "dependencies": { "@mongosh/snippet-analyze-schema": "^1.0.5", "@mongosh/snippet-spawn-mongod": "^1.0.1", "npm": "*", "@<REGISTRY NAME>/bad-snippet-name": "^1.0.7" } } Back Registries Next Reference
