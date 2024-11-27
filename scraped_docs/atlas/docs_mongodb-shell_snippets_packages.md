# Create and Share Snippets - MongoDB Shell


Docs Home / MongoDB Shell / Snippets Create and Share Snippets On this page Create a Snippet Package Publish a Snippet Install the New Snippet Package Contribute a Snippet Package to the MongoDB Community Warning Experimental feature This feature is experimental. MongoDB does not provide support for
Snippets. This feature may be changed or removed at any time without
prior notice. Bugs are not expected, however should you encounter one, please open an
issue in the GitHub repository for this project. You can write scripts to manipulate
data or carry out administrative tasks in mongosh .
Packaging a script as a snippet provides a way to easily share scripts
within your organization or across the MongoDB user community. This page discusses: Preparing a snippet package. Publishing the snippet package to a registry. For examples of scripts and the metadata files in snippet packages,
see the snippets in the community snippet registry on GitHub. Tip If you plan to submit your snippet to the community registry , be sure
to review the information in Contribute a Snippet Package to the MongoDB Community . Create a Snippet Package The steps in this section focus on packaging a script. For more details
on writing scripts see Write Scripts . Prepare the Files 1 Fork the Community Repository. If you plan to contribute to the community repository, fork the
snippets project repository . You do not have to fork the community repository if you want to
create a private repo, but you should manually recreate a
similar directory structure as you work through the following
steps. 2 Create a Package Directory. Create a directory for your snippet package under the snippets directory in the forked repository. This directory will
contain the code for your script and several metadata files. This example shows directories for two snippet packages, decrypt-cards and update-auth . The contents of the community snippets directories are omitted for clarity. mongo-snippets | âââ scripts âÂ Â  âââ make-index.js âÂ Â  âââ show-index.js âââ snippets âââ analyze-schema âââ decrypt-cards âÂ Â  âââ LICENSE-Community.txt âÂ Â  âââ README.md âÂ Â  âââ error-matchers.js âÂ Â  âââ index.js âÂ Â  âââ package.json âââ mock-collection âââ mongocompat âââ resumetoken âââ spawn-mongod âââ update-auth âââ LICENSE âââ README.md âââ index.js âââ package.json 3 Create README.md . Create a README.md . The README.md describes how to use your
code. This file is displayed when a user enters snippet help for
your snippet. 4 Create LICENSE . Create a LICENSE file. You will need to enter a license
identifier string later, so try to chose a license from the SPDX license list . 5 Create index.js . Create an index.js file. This file contains the entry point to your code that is exposed in
the mongosh console. The script is written in JavaScript and defines your new functions. The script can be in a single file or multiple files. The script can call other files and local or remote npm modules.
To require() a remote npm module use the construction: const localRequire = require ( 'module' ). createRequire ( __filename) ; ) For an example, see index.js in the resumetoken snippet. index.js is referenced in package.json . The MongoDB repository has example code . Tip If you have an existing script, either rename it index.js or
create an index.js file to load it. For an example of an index.js file that loads other scripts, see this one in the community repository . Prepare the package.json File package.json contains metadata that the package registry uses to
manage snippets. A minimal package.json file looks like this: { "name" : "@mongosh/snippet-resumetoken" , "snippetName" : "resumetoken" , "version" : "1.0.2" , "description" : "Resume token decoder script" , "main" : "index.js" , "license" : "Apache-2.0" , "publishConfig" : { "access" : "public" } } The parameters are: Field Description "name" The npm package that contains the snippet. "snippetName" The snippet name. This is the name used with commands like install . "version" The package version. This should be incremented when you update
your snippet. "description" A brief note about what your snippet does. Caution, if the
description is more than 50 or 60 characters long it may cause
display problems with some snippet commands . "main" This is the starting point for your code, index.js . Note
that functions in other files can be scoped so that they are
also available in the the mongosh shell. "license" The license for users of your code. If you want to contribute to
the shared registry, the license should be from the SPDX license list . See
also the MongoDB Contributor Agreement . "publishConfig" This value is used to control access to your snippet package. public is typical, but npm provides other options as well. Use this code to create a skeleton package.json file. Edit the file
and replace each UPDATE to insert the values for your snippet
package. { "name" : "@UPDATE/UPDATE" , "snippetName" : "UPDATE" , "version" : "UPDATE" , "description" : "UPDATE" , "main" : "UPDATE" , "license" : "UPDATE" , "publishConfig" : { "access" : "UPDATE" } } There are several examples of package.json files in the MongoDB
GitHub repository . Tip MongoDB uses npm as a package registry. npm relies on the package.json file to manage packages. Refer to
the npm package documentation for
more information about package.json . Publish a Snippet To share your snippet, you must publish you snippet package to a
registry. The package will contain: Your code README.md LICENSE file package.json When the files are complete, follow these steps to create and publish
your snippet package. 1 Create a registry index file. The registry index file is not the same as the index.js file
that contains your snippet code. The registry index file, index.bson.br , contains metadata for the snippet packages in
your registry. The registry index file must be compressed before it is uploaded for
use. The make-index.js utility in the scripts directory walks through your snippet source
directories gathering the information that is needed to create the
registry index file. After it creates the registry index file, make-index.js script also compresses it. Run make-index.js from the mongo-snippets directory create the index. node ./scripts/make-index.js The output of this script is a brotli-compressed registry
index file, index.bson.br . You can use show-index.js to view the compressed registry index file. Using make-index.js is the preferred way to create a registry
index, but you can also create a registry index manually . 2 Commit Your Snippet Commit your snippet and the registry index file to your GitHub
repository. 3 Publish Changes Publish your changes to your npm registry. npm publish --access public Install the New Snippet Package Follow these steps to install your new snippet package: 1 Refresh Metadata. Refresh the snippet metadata in your local mongosh . snippet refresh 2 Install the Snippet. Install the snippet. snippet install YOUR_NEW_SNIPPET Contribute a Snippet Package to the MongoDB Community If you have written a code snippet that might be
useful for other MongoDB users, you are invited to contribute it to the community repository hosted on GitHub. To submit a snippet to the shared MongoDB repository: 1 Complete the Contributor Agreement. Read and complete the MongoDB Contributor Agreement . 2 Clone the Repository. Fork and clone the snippet project repository from GitHub. 3 Create Your Package Directory. Add a new directory for your code under snippets/ .
Give it a descriptive name. 4 Create Your Package. Create your snippet package. Be sure it contains the following files: package.json index.js README.md LICENSE You do not have to create a registry index file. If your snippet
package is accepted, MongoDB will update the registry index file. 5 Commit your changes. Commit your changes to your GitHub repository. 6 Submit Your Snippet Code. Open a pull request against the snippet project repository . MongoDB will review your pull request. If it is accepted, we will: Merge your code into our GitHub repository. Publish it to the npm registry. Add it to the snippet index. Back Use in the Console Next Registries
