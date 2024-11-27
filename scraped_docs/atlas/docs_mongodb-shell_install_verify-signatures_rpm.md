# Verify RPM Packages (RHEL) - MongoDB Shell


Docs Home / MongoDB Shell / Install / Verify Package Integrity Verify RPM Packages (RHEL) On this page Before you Begin Steps The MongoDB release team digitally signs MongoDB Shell packages to
certify that packages are a valid and unaltered MongoDB release. Before
you install MongoDB Shell, you can use the digital signature to validate
the package. This page describes how to verify .rpm packages on RHEL operating
systems. Before you Begin If you don't have MongoDB Shell installed, download the MongoDB Shell
binary from the Download Center . Steps 1 Import the MongoDB Shell public key in gpg and rpm curl https://pgp.mongodb.com/mongosh.asc | gpg --import rpm --import https://pgp.mongodb.com/mongosh.asc If the key imports successfully, the command returns: gpg: key CEED0419D361CB16: public key "Mongosh Release Signing Key <packaging@mongodb.com>" imported gpg: Total number processed: 1 gpg:               imported: 1 If you have previously imported the key, the command returns: gpg: key A8130EC3F9F5F923: "Mongosh Release Signing Key <packaging@mongodb.com>" not changed gpg: Total number processed: 1 gpg:              unchanged: 1 2 Verify the rpm file rpm --checksig <path_to_mongosh_rpm_file> If the file is signed, the command returns: <path_to_mongosh_rpm_file> digests signatures OK Back Use GPG (Linux & macoS) Next Verify Windows Packages
