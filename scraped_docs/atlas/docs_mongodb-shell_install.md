# Install mongosh - MongoDB Shell


Docs Home / MongoDB Shell Install mongosh On this page Prerequisites Compatibility Considerations Procedure Next Steps Prerequisites To use the MongoDB Shell , you must have a MongoDB deployment to connect
to. For a free cloud-hosted deployment, you can use MongoDB Atlas . To learn how to run a local MongoDB deployment, see Install MongoDB . Supported MongoDB Versions You can use the MongoDB Shell to connect to MongoDB version 4.2 or
greater. Supported Operating Systems You can install MongoDB Shell 2.0.0 on these operating systems: Operating System Supported Versions macOS 11+ (x64 and ARM64) Microsoft Windows Microsoft Windows Server 2016+ Microsoft Windows 10+ Linux Red Hat Enterprise Linux (RHEL) 8+ (x64, ARM64, ppc64le, and s390x) Ubuntu 20.04+ (x64 and ARM64) Amazon Linux 2023 (x64 and ARM64) Amazon Linux 2 (x64 and ARM64) Debian 11+ SLES 15 Oracle Linux 8+ running the Red Hat Compatible Kernel (RHCK). MongoDB Shell does not support the Unbreakable Enterprise Kernel (UEK). Compatibility Considerations Starting in mongosh 2.0.0: Amazon Linux 1, Debian 9, and macOS 10.14 aren't supported. Red Hat Enterprise Linux (RHEL) 7, Amazon Linux 2, SUSE Linux
Enterprise Server (SLES) 12, and Ubuntu 18.04 support is deprecated
and might be removed in a later mongosh release. If you must use Node.js 16 with mongosh , install Node.js and then install mongosh through npm . The ability to run mongosh installed with npm and use Node.js 16 might be
removed during the lifetime of mongosh 2.x. Procedure Select the appropriate tab for your operating system: Windows macOS Linux Note On Windows, mongosh preferences and configuration options
are stored in the %APPDATA%/mongodb/mongosh directory. Install from MSI 1 Open the MongoDB Shell download page. Open the MongoDB Download Center . 2 In the Platform dropdown, select Windows 64-bit (8.1+) (MSI) 3 Click Download . 4 Double-click the installer file. 5 Follow the prompts to install mongosh . Install from .zip File 1 Open the MongoDB Shell download page. Open the MongoDB Download Center . 2 Download the mongosh installation archive for your operating system. Download mongosh from the MongoDB Download Center . 3 Extract the files from the downloaded archive. Open a cmd terminal and run the following command from the
directory that has the mongosh .zip archive: tar -xf mongosh-2.3.2-win32-x64.zip The extracted archive has a bin folder that contains two files, mongosh.exe and mongosh_crypt_v1.dll . 4 Add the mongosh binary to your PATH environment variable. Ensure that the extracted MongoDB Shell binary is in the desired
location in your filesystem, then add that location to your PATH environment variable. To add the MongoDB Shell binary's location to your PATH environment variable: Open the Control Panel . In the System and Security category, click System . Click Advanced system settings . The System
Properties modal displays. Click Environment Variables . In the System variables section, select Path and click Edit . The Edit environment variable modal
displays. Click New and add the filepath to your mongosh binary. Click OK to confirm your changes. On each other
modal, click OK to confirm your changes. To confirm that your PATH environment variable is correctly
configured to find mongosh , open a command prompt and enter the mongosh --help command. If your PATH is configured
correctly, a list of valid commands displays. Install with Homebrew Important To view the complete list of system requirements for Homebrew,
see the Homebrew Website . The Homebrew package manager is the recommended installation
method for mongosh on macOS. To learn how to manually
install mongosh from an archive instead, see Install from .zip File . Considerations mongosh installed with Homebrew does not support automatic client-side field level encryption . Procedure To install mongosh with Homebrew: 1 Install Homebrew. Refer to the Homebrew website
for the steps to install Homebrew on macOS. 2 Install the mongosh package. Issue the following command from the terminal to install the mongosh package: brew install mongosh Install from .zip File To manually install mongosh using a downloaded .zip file: 1 Open the MongoDB Shell download page. Open the MongoDB Download Center . 2 Download the mongosh installation archive for your operating system. Download the appropriate version of mongosh for your operating
system. MongoDB provides versions of mongosh for Intel and ARM
architectures. 3 Extract the files from the downloaded archive. Go to the directory that contains the mongosh .zip archive,
then unpack the .zip file. If your computer is Intel based, run: unzip mongosh-2.3.2-darwin-x64.zip If your computer is ARM based (M1 or M2), run: unzip mongosh-2.3.2-darwin-arm64.zip The extracted archive has a bin folder that contains two files, mongosh and mongosh_crypt_v1.dylib . If your web browser automatically extracts the archive as part of the
download, or if you extract the archive without using the unzip command, you may need to make the binary executable. To make the binary executable, run the following command in the
directory where you extracted the archive: chmod +x bin/mongosh 4 Add the downloaded binaries to your PATH environment variable. You can either: Copy the mongosh binary into a directory listed in your PATH variable, such as /usr/local/bin . Run the following
commands from the directory where you extracted the download file: sudo cp mongosh /usr/local/bin/ sudo cp mongosh_crypt_v1.so /usr/local/lib/ Create symbolic links to the MongoDB Shell . Switch to the
directory where you extracted the files from the .tgz archive.
Run the following command to create links to a directory already
in your PATH such as /usr/local/bin . sudo ln -s $(pwd)/bin/* /usr/local/bin/ 5 Allow macOS to run mongosh . macOS may prevent mongosh from running after installation. If
you receive a security error when starting mongosh indicating
that the developer could not be identified or verified, perform
the following actions: Open System Preferences . Select the Security and Privacy pane. Under the General tab, click the button to the right of the
message about mongosh , labelled either Open Anyway or Allow Anyway depending on your version of macOS. Select the appropriate tab based on your Linux distribution and
desired package from the tabs below: To install the .deb package on Ubuntu 22.04 (Jammy), Ubuntu
20.04 (Focal), Ubuntu 18.04 (Bionic), or Debian, click the .deb tab. To install the .rpm package on RHEL , Amazon Linux 2023, or Amazon
Linux 2, click the .rpm tab. To install the .tgz tarball, click the .tgz tab. .deb .rpm .tgz Supported Platforms mongosh is available as a PPA for the following platforms: Ubuntu 22.04 (Jammy) Ubuntu 20.04 (Focal) Ubuntu 18.04 (Bionic) Procedure 1 Import the public key used by the package management system. From a terminal, issue the following command to import the
MongoDB public GPG key from https://www.mongodb.org/static/pgp/server-8.0.asc : wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc The previous command writes the GPG key to your system's /etc/apt/trusted.gpg.d folder and prints the key to your
terminal. You do not need to copy or save the key that is printed to
the terminal. If you receive an error indicating that gnupg is not installed,
perform the following steps: Install gnupg and its required libraries using the following command: sudo apt-get install gnupg Retry importing the key: wget -qO- https://www.mongodb.org/static/pgp/server-8.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-8.0.asc 2 Create a list file for MongoDB. Create the list file /etc/apt/sources.list.d/mongodb-org-8.0.list for your
version of Ubuntu. Click on the appropriate tab for your version of Ubuntu.
If you are unsure of what Ubuntu version the host is running,
open a terminal or shell on the host and run lsb_release -dc . Ubuntu 22.04 (Jammy) Ubuntu 20.04 (Focal) Ubuntu 18.04 (Bionic) The following instruction is for Ubuntu 22.04 (Jammy) .
For other Ubuntu releases, click the appropriate tab. Create the /etc/apt/sources.list.d/mongodb-org-8.0.list file for Ubuntu 22.04 (Jammy): echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list The following instruction is for Ubuntu 20.04 (Focal) .
For other Ubuntu releases, click the appropriate tab. Create the /etc/apt/sources.list.d/mongodb-org-8.0.list file for Ubuntu 20.04 (Focal): echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list The following instruction is for Ubuntu 18.04
(Bionic) . For other Ubuntu releases, click the
appropriate tab. Create the /etc/apt/sources.list.d/mongodb-org-8.0.list file for Ubuntu 18.04 (Bionic): echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list 3 Reload local package database. Issue the following command to reload the local package database: sudo apt-get update 4 Install the mongosh package. mongosh supports OpenSSL. You can also configure mongosh to use
your system's OpenSSL installation. To install the latest stable version of mongosh with the included
OpenSSL libraries: sudo apt-get install -y mongodb-mongosh To install mongosh with your OpenSSL 1.1 libraries: sudo apt-get install -y mongodb-mongosh-shared-openssl11 To install mongosh with your OpenSSL 3.0 libraries: sudo apt-get install -y mongodb-mongosh-shared-openssl3 5 Confirm that mongosh installed successfully. To confirm that mongosh installed successfully, run the following
command: mongosh --version Your terminal should respond with the version of mongosh you have
installed. Supported Platforms mongosh is available as yum package for the
following platforms: RHEL Amazon Linux 2023 Amazon Linux 2 Procedure 1 Configure the package management system ( yum ). Create a /etc/yum.repos.d/mongodb-org-8.0.repo file so that
you can install mongosh directly using yum . There are .rpm distributions for RHEL and Amazon Linux. Choose the tab to select the file for your distribution. Copy the contents of the tab. Paste the contents into the .repo file. RHEL Amazon Linux [mongodb-org-8.0] name=MongoDB Repository baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/8.0/$basearch/ gpgcheck=1 enabled=1 gpgkey=https://www.mongodb.org/static/pgp/server-8.0.asc You can also download the .rpm files directly from the MongoDB repository .
Downloads are organized in the following order: Red Hat or CentOS version (for example, 8 ) MongoDB edition (for example, mongodb-enterprise ) MongoDB release version (for example, 8.0 ) Architecture (for example, x86_64 ) [mongodb-org-8.0] name=MongoDB Repository baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/8.0/$basearch/ gpgcheck=1 enabled=1 gpgkey=https://www.mongodb.org/static/pgp/server-8.0.asc Note If your system uses Amazon Linux 2, replace 2023 with 2 in the baseurl. You can also download the .rpm files directly from the MongoDB repository . Downloads are
organized in the following order: Amazon Linux version (for example, 2023 ) MongoDB release version (for example, 8.0 ) Architecture (for example, x86_64 ) 2 Install mongosh . mongosh supports OpenSSL. You can also configure mongosh to use
your system's OpenSSL installation. To install the latest stable version of mongosh with the included
OpenSSL libraries: sudo yum install -y mongodb-mongosh To install mongosh with your OpenSSL 1.1 libraries: sudo yum install -y mongodb-mongosh-shared-openssl11 To install mongosh with your OpenSSL 3.0 libraries: sudo yum install -y mongodb-mongosh-shared-openssl3 Procedure 1 Open the MongoDB Shell download page. Open the MongoDB Download Center . 2 Download the Linux 64-bit .tgz package. Download the appropriate version of mongosh for your operating
system. MongoDB also provides versions of mongosh that use your
system's OpenSSL installation. See the MongoDB Download Center . 3 Extract the files from the downloaded archive. Go to the directory that contains the .tgz archive, then unpack
the archive. The name of the .tgz package varies depending on the version you
downloaded. Replace the .tgz package name in the following
command with the name of the package you downloaded and run the
command. tar -zxvf mongosh-2.3.2-linux-x64.tgz The extracted archive has a bin folder that contains two files, mongosh and mongosh_crypt_v1.so . If your web browser automatically extracts the archive as part of the
download, or if you extract the archive without using the tar command, you may need to make the binary executable. To make the binary executable, run the following command in the
directory where you extracted the archive: chmod +x bin/mongosh 4 Add the downloaded binaries to your PATH environment variable. You can either: Copy the mongosh binary into a directory listed in your PATH variable, such as /usr/local/bin . Run the following
commands from the directory where you extracted the download file: sudo cp mongosh /usr/local/bin/ sudo cp mongosh_crypt_v1.so /usr/local/lib/ Create symbolic links to the MongoDB Shell . Switch to the
directory where you extracted the files from the .tgz archive.
Run the following command to create links to a directory already
in your PATH such as /usr/local/bin . sudo ln -s $(pwd)/bin/* /usr/local/bin/ Next Steps Once you successfully install mongosh , learn how to connect to your MongoDB deployment . MongoDB provides a programmatically accessible list of mongosh downloads that
can be accessed through your application. Back Welcome to MongoDB Shell (mongosh) Next Verify Package Integrity
