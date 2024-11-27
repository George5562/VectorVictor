# Verify Windows Packages - MongoDB Shell


Docs Home / MongoDB Shell / Install / Verify Package Integrity Verify Windows Packages On this page Before you Begin Steps Verify Packages with PowerShell Verify Packages by Checking Properties The MongoDB release team digitally signs MongoDB Shell packages to
certify that packages are a valid and unaltered MongoDB release. Before
you install MongoDB Shell, you can use the digital signature to validate
the package. This page describes how to verify Windows .exe and .msi packages. Before you Begin If you don't have MongoDB Shell installed, download the MongoDB Shell
binary from the Download Center . Steps To verify the MongoDB Shell package on Windows, you can use one of these
methods: Verify Packages with PowerShell Verify Packages by Checking Properties Verify Packages with PowerShell To verify Windows packages with PowerShell, run: powershell Get-AuthenticodeSignature -FilePath <path_to_mongosh_exe_or_msi> If the package is signed, the command returns: SignerCertificate     Status     Path -----------------     ------     ---- F2D7C28591847B...     Valid      <path_to_mongosh_exe_or_msi> Verify Packages by Checking Properties 1 Open the properties for your MongoDB Shell package 2 Check the package's digital signatures In the properties window, open the Digital Signatures tab. If the package is properly signed, the Digital Signatures show
these properties: Name of signer Digest algorithm Timestamp MONGODB, INC. sha256 <Timestamp> Back Verify RPM Packages (RHEL) Next Connect
