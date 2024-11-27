# Verify Packages with Disk Image Verification (macOS) - MongoDB Shell


Docs Home / MongoDB Shell / Install / Verify Package Integrity Verify Packages with Disk Image Verification (macOS) On this page Before you Begin Steps The MongoDB release team digitally signs MongoDB Shell packages to
certify that packages are a valid and unaltered MongoDB release. Before
you install MongoDB Shell, you can use the digital signature to validate
the package. This page describes how to verify .dmg packages on macOS. Before you Begin If you don't have MongoDB Shell installed, download the MongoDB Shell
binary from the Download Center . Steps To verify the MongoDB Shell package, run: codesign -dv --verbose=4 <path_to_mongosh_executable> If the package is signed by MongoDB, the output includes the following
information: Authority=Developer ID Application: MongoDB, Inc. (4XWMY46275) Authority=Developer ID Certification Authority Authority=Apple Root CA Back Verify Package Integrity Next Use GPG (Linux & macoS)
