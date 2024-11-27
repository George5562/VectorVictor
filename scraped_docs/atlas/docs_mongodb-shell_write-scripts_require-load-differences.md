# Differences Between require() and load() - MongoDB Shell


Docs Home / MongoDB Shell / Write Scripts Differences Between require() and load() On this page Types of Scripts in mongosh Availability of require() and load() File Paths for require() and load() require() Packaging Considerations Access to the mongosh API The require() and load() methods include files and modules in
your scripts for added functionality. However, require() and load() differ in their behaviors and availability. Types of Scripts in mongosh You can use the following types of scripts with mongosh : mongosh scripts, which can be any of the following: Code entered directly into the REPL. The mongoshrc.js file. Code loaded with the load() method. Node.js scripts, which are any scripts loaded with require() ,
including npm packages. These scripts are always files. Availability of require() and load() The require() and load() methods differ in availability
depending on the type of script you are using. In mongosh scripts, both require() and load() are available. In Node.js scripts, only require() is available. File Paths for require() and load() The type of script determines how you specify file paths with require() or load() . In mongosh scripts: require() uses the standard Node.js module resolution algorithm , starting from the current
working directory of the shell. load() takes either: An absolute path, or A relative path. When using a relative path, the path is always
interpreted as relative to the current working directory of the
shell. In Node.js scripts, require() uses the standard Node.js module resolution algorithm , starting from the file
where require() was called. Tip To return the current working directory of the shell, run the pwd() method from your script. To change the shell's working directory, use the cd() method in your script. Load External Code in a mongosh Script You can load external code in a mongosh script file, such as an npm
package or a separate mongosh script. To load a mongosh script from another mongosh script, use
the __dirname environment variable. The __dirname environment
variable returns the absolute path of the directory containing the
file being executed. Example To load a mongosh script named test-suite.js from another mongosh script, add the following line to your script: load ( __dirname + '/test-suite.js' ) Using the _dirname variable to specify an absolute path ensures
that the separate script you are loading is not affected by external
factors such as where mongosh started. To load a Node.js script from a mongosh script, use the require() method. Example To load the date-fns module from a mongosh script called test-suite2.js , add the
following lines to your script: const localRequire = require ( 'date-fns' ). createRequire ( __filename) ; const fileExports = localRequire ( './test-suite2.js' ) ; } require() Packaging Considerations There are two packaging standards for Node.js modules. Packaging Standard Works with require() CommonJS (CJS) Yes ECMAScript Module (ES Module) No You cannot require() an ES module in mongosh . If you want to use
functionality from an ES module, check to see if there is a CommonJS
version that you can use instead. For more information, see: Node.js module documentation Installing older versions of npm packages Access to the mongosh API mongosh scripts can use the mongosh API. Node.js scripts do not have access to the mongosh API. For example, the db global variable (used to display the current
database) is available inside of mongosh scripts. It is not
available inside of Node.js scripts. Important mongosh scripts and Node.js scripts run in different contexts .
They may exhibit different behaviors when the same command is run in
each type of script, such as returning different data types.
Therefore, you may observe unexpected results if you run mongosh code inside of a Node.js script. Generally, you should not keep mongosh-specific code inside Node.js
scripts. Back Include Files & Modules Next Code Scoping
