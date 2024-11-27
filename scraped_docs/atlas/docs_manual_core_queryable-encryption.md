# Queryable Encryption - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Security / Encryption / In-Use Encryption Queryable Encryption On this page Introduction Considerations Compatibility MongoDB Support Limitations Features Installation Quick Start Fundamentals Tutorials Reference Introduction Queryable Encryption gives you the ability to perform the following tasks: Encrypt sensitive data fields from the client-side. Store sensitive data fields as fully randomized encrypted data on the database
server-side. Run expressive queries on the encrypted data. These tasks are all completed without the server having knowledge of the data
it's processing. Sensitive data is encrypted throughout its lifecycle - in-transit, at-rest, in-use,
in logs, and backups - and only ever decrypted on the client-side, since only you
have access to the encryption keys. Queryable Encryption introduces an industry-first fast, searchable encryption
scheme developed by the pioneers in encrypted search. The feature supports equality
and range searches, with additional query types such as prefix, suffix, and substring
planned for future releases. You can set up Queryable Encryption using the following mechanisms: Automatic Encryption: Enables you to perform encrypted read and
write operations without having to add explicit calls to encrypt and decrypt
fields. Explicit Encryption: Enables you to perform encrypted read and write
operations through your MongoDB driver's encryption library. You must
specify the logic for encryption with this library throughout your
application. Considerations When implementing an application that uses Queryable Encryption, consider the points listed
in Security Considerations . For other limitations, see Queryable Encryption limitations . Compatibility To learn which MongoDB server products and drivers support Queryable Encryption, see Queryable Encryption Compatibility . MongoDB Support Limitations Enabling Queryable Encryption on a collection redacts fields from some diagnostic
commands and omits some operations from the query log. This limits the
data available to MongoDB support engineers, especially when
analyzing query performance. To measure the impact of operations against
encrypted collections, use a third party application performance
monitoring tool to collect metrics. For details, see Redaction . Features To learn about the security benefits of Queryable Encryption for your
applications, see the Features page. Installation To learn what you must install to use Queryable Encryption, see
the Install a Queryable Encryption Compatible Driver and Install and Configure a Queryable Encryption Library pages. Quick Start To start using Queryable Encryption, see the Quick Start . Fundamentals To learn about encryption key management, see Encryption Keys and Key Vaults . To learn how Queryable Encryption works, see the Fundamentals section,
which contains the following pages: Encrypted Fields and Enabled Queries Create an Encryption Schema Encrypted Collections Explicit Encryption Rotate and Rewrap Encryption Keys Tutorials To learn how to perform specific tasks with Queryable Encryption, see the Tutorials section. Reference To view information to help you develop your Queryable Encryption enabled applications,
see the Reference section. The reference section contains the following pages: Supported Operations for Queryable Encryption MongoClient Options for Queryable Encryption Back KMS Providers Next Features
