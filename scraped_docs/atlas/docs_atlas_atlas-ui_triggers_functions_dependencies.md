# External Dependencies - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data / Triggers / Functions External Dependencies On this page Add an External Package Add Packages by Name and Version Upload a Dependency Directory Import a Package in a Function Import a Full Module Import a Module Subfolder An external dependency is a library that includes code that you
can't or don't want to implement yourself. For example, you might use an
official library for an external service or a custom implementation of
a data structure or algorithm. Atlas automatically transpiles dependencies and also
supports most built-in Node.js modules. Note Create Your Own Modules Though most npm modules are written by third parties, you can also
create and publish your own npm modules to house logic specific to
your application. You can make your modules available to the Node.js
community or reserve them for private use. For more information,
check out npm's guide on Contributing packages to the registry . Add an External Package To import and use an external dependency, you first need to add the
dependency to your application. You can either add packages by
name or upload a directory of
dependencies . Important Override Existing Dependencies You can only use one method at a time to specify the external
packages your app can use. The most recent method that you used to
specify dependencies is the source of truth and overrides previous
specifications. For example, a package added by name through the UI overrides any
copies of the same package that you've added previously, including
those in an uploaded dependency directory . Add Packages by Name and Version You can add packages from the npm registry to your app by
name. You can either add a specific version or use the latest version. 1 Navigate to Dependencies in the Atlas UI Navigate to the Triggers Page If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Triggers under
the Services heading. The Triggers page displays. Select the Trigger that you want to add the dependency to. On the Edit Trigger page, go to the Function section and click Add Dependency . 2 Add Dependency Information In the Add Dependency modal window, include the following
information: Field Description Define a Package Name The name of the npm package. Package Version Optional. Specific version of the dependency to use.
By default, Atlas functions use the latest version available. Click Add to add the package. You can track the status of adding the dependency in the progress tracker
at the bottom of the window. The progress tracker provides a message letting
you know if the package succeeded or failed. Failure messages contain additional
information about why the package could not be added. 3 Check Operation Success When you successfully add the dependency, you'll see it on the
list of dependencies in the Dependencies tab on the main Triggers page. Upload a Dependency Directory You can upload a zipped node_modules directory of packages to your
app. Zipped dependency directories may not exceed 15MB. Important Existing Dependencies Overwritten When you import an archive, any existing dependencies will be removed. 1 Locally Install External Dependencies To upload external dependencies, you first need a local node_modules folder containing at least one Node.js package. You
can use the following code snippet to install a dependency locally
you would like to upload: npm install <package name> If the node_modules folder does not already exist, this command
automatically creates it. Note Alternative Methods of Installation You can also configure a package.json and run the npm install command to install all packages (and their
dependencies) listed in your package.json . To learn more about npm and node_modules , consult the npm documentation . 2 Create a Dependency Archive Now that you've downloaded all of your npm modules, you need to
package them up in an archive so you can upload them to Atlas . Atlas supports .tar , .tar.gz , .tgz , and .zip archive formats. Create an archive containing the node_modules folder: tar -czf node_modules.tar.gz node_modules/ 3 Upload the Dependency Archive After you create an archive containing your dependencies, you can upload
your dependency archive using the Atlas UI: Navigate to the Triggers Page If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Triggers under
the Services heading. The Triggers page displays. Select the Dependencies tab. Click Upload Folder . In the modal, click Upload Folder , then select the node_modules.tar.gz archive you
just created. Click Add . Atlas uploads the
archive file, which may take several minutes depending on the
speed of your internet connection and the size of your dependency
archive. Atlas displays a banner
indicating the success or failure of the operation.
If successful, the Dependencies tab displays a list of the
dependencies that you included in your dependency archive. If drafts are enabled, you must also click Review & Deploy to apply these changes. If drafts are disabled, the change will take effect within 5 to 60
seconds, depending on the size of your dependency archive. Import a Package in a Function You can import built-in modules and external packages that you've added
to your app and then use them in your functions. To import a package,
call require() with the package name from within the function body. Important Where Do I Import Modules? Node.js projects commonly place require() calls in the global
scope of each file, but Atlas does not support this
pattern. You must place require() calls within a function scope. Import a Full Module exports = () => { const R = require ( "ramda" ) ; return R. map ( x => x * 2 , [ 1 , 2 , 3 ]) ; } Import a Module Subfolder exports = function ( arg ) { const cloneDeep = require ( "lodash/cloneDeep" ) ; var original = { name : "Deep" } ; var copy = cloneDeep ( original) ; copy. name = "John" ; console . log ( `original: ${original.name} ` ) ; console . log ( `copy: ${copy.name} ` ) ; return ( original ! = copy) ; } ; Back Global Modules Next Handle Errors
