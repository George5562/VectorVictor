# Snippets - MongoDB Shell


Docs Home / MongoDB Shell Snippets On this page Introduction Components Get Started Warning Experimental feature This feature is experimental. MongoDB does not provide support for
Snippets. This feature may be changed or removed at any time without
prior notice. Bugs are not expected, however should you encounter one, please open an
issue in the GitHub repository for this project. Introduction A snippet is a script that is packaged and stored in a registry to
facilitate sharing and reuse. You can write your own scripts in mongosh to manipulate data or to perform administrative
tasks. Snippets are an improvement on locally stored scripts because
they can be easily shared and maintained. This page provides a high level introduction to working with snippets.
The links in each section go deeper into writing, managing, and working
with snippets. Components The Snippets feature has three main components: Scripts are code that can be used with mongosh . Packages are scripts that are bundled with metadata so they can be
managed more easily. Registries are collections of packages that can be shared. There are also built in commands to help you
work with snippets and utility scripts to help with packaging tasks . Get Started The fastest way to get started with snippets is to try one of the
snippets in the community registry maintained by MongoDB. You can also create your own snippets, package them for easier
management, and configure a registry to share them. Try an Existing Snippet . Install and run a snippet package from the community registry Create Your Own Snippet Package . Write the snippet code and supporting files. Then, publish the snippet package. Configure Snippet Registries . Use the community registry or configure a private registry. Back Considerations Next Use in the Console
