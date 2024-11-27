# Verify Packages with GPG (Linux and macOS) - MongoDB Shell


Docs Home / MongoDB Shell / Install / Verify Package Integrity Verify Packages with GPG (Linux and macOS) On this page Before you Begin Steps The MongoDB release team digitally signs MongoDB Shell packages to
certify that packages are a valid and unaltered MongoDB release. Before
you install MongoDB Shell, you can use the digital signature to validate
the package. This page describes how to use GPG to verify Linux and macOS packages. Before you Begin If you don't have MongoDB Shell installed, download the MongoDB Shell
binary from the Download Center . Steps 1 Import the MongoDB Shell public key curl https://pgp.mongodb.com/mongosh.asc | gpg --import If the key imports successfully, the command returns: gpg: key CEED0419D361CB16: public key "Mongosh Release Signing Key <packaging@mongodb.com>" imported gpg: Total number processed: 1 gpg:               imported: 1 If you have previously imported the key, the command returns: gpg: key A8130EC3F9F5F923: "Mongosh Release Signing Key <packaging@mongodb.com>" not changed gpg: Total number processed: 1 gpg:              unchanged: 1 2 Download the MongoDB Shell public signature To download the MongoDB Shell public signature, go to the mongosh
Releases page
on GitHub and download the corresponding .sig file for your
version and variant. For example, if you are running mongodb-mongosh_2.3.2_amd64.deb , download mongodb-mongosh_2.3.2_amd64.deb.sig Note Make sure that you select the correct version in the GitHub
releases page when you download the signature. 3 Verify the package gpg --verify <path_to_signature_file> <path_to_mongosh_executable> If the package is signed by MongoDB, the command returns: gpg: Signature made Mon Jan 22 10:22:53 2024 CET gpg:                using RSA key AB1B92FFBE0D3740425DAD16A8130EC3F9F5F923 gpg: Good signature from "Mongosh Release Signing Key <packaging@mongodb.com>" [unknown] If the package is signed but the signing key is not added to your
local trustdb , the command returns: gpg: WARNING: This key is not certified with a trusted signature! gpg:          There is no indication that the signature belongs to the owner. If the package is not properly signed, the command returns an
error message: gpg: Signature made Mon Jan 22 10:22:53 2024 CET gpg:                using RSA key AB1B92FFBE0D3740425DAD16A8130EC3F9F5F923 gpg: BAD signature from "Mongosh Release Signing Key <packaging@mongodb.com>" [unknown] Back Use Disk Imge Verification (macOS) Next Verify RPM Packages (RHEL)
