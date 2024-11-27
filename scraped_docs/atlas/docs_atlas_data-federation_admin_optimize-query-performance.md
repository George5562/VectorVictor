# Optimize Query Performance - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores / AWS S3 Bucket Optimize Query Performance On this page Data Structure in S3 Data File Size Data File Format The performance of your federated database instance is affected by the following factors: The structure of your data in S3 and how you represent it in your
federated database instance configuration . The size of your data files. The format and structure of your data files. Data Structure in S3 For easier management, ensure that your data is logically grouped
into partitions. Atlas Data Federation utilizes partitions you create with the field
values that you specify in your partition syntax . You can improve your federated database instance's performance by
ensuring that your partition structure maps to your query patterns and
the partition structure is defined in your databases.[n].collections.[n].dataSources.[n].path .
For the partition, choose fields that you query frequently and order
them from the most frequently queried in the first position to the
least queried field in the last position. The order of fields listed in the databases.[n].collections.[n].dataSources.[n].path is important in the same way as it is in Compound Indexes . The specified path corresponds to data that
is partitioned first by the value of the first field, and then by the
value of the next field, and so on. Example Consider a collection with the software , computer , and OS fields and partitions on the S3 bucket named metrics first for the software field, followed by  the computer field, and then the OS field. metrics |--software |--computer |--OS Atlas Data Federation uses the partitions for queries on the these fields: the software field, the software field and the computer field, the software field and the computer field and the OS field. Atlas Data Federation can use the partitions to support a query on the software and OS fields. However, in this case, Atlas Data Federation is
not as efficient for the query as it would be if the query was on
the software and computer fields only. Partitions are parsed
in order; if a query omits a particular partition, Atlas Data Federation is less
efficient in making use of any partitions that follow the partition.
Because a query on software and OS omits computer ,
Atlas Data Federation uses the software partition more efficiently than the OS partition to support this query. Atlas Data Federation can't use the partitions to support queries on fields not
specified in the databases.[n].collections.[n].dataSources.[n].path .
Also, Atlas Data Federation can't use the partitions to support queries that
include the following fields without the software field: the computer field, the OS field, or the computer and OS fields. You can use partitions to improve Data Federation performance by mapping
them to partition attributes in your configuration . By mapping your partition attributes (the parts of your S3 prefix that looks like a folder) to a query
attribute, Atlas Data Federation can selectively open the files that contain data
related to your query. This reduces the amount of time a query takes
and decreases cost, because Data Federation reads and downloads less files from AWS . Example Consider an S3 bucket metrics with the following structure: metrics |--hardware |--software |--computer |--phone You can set a partition attribute for "metric type" by defining /metrics/{metric_type string}/* in your configuration. If
you issue a query that contains {metric_type: software} ,
Data Federation only processes the files with the prefix /software and ignores files with the prefix /hardware . You can then set a partition attribute for "software type" by
defining /metrics/{metric_type string}/{software_type string} in
your configuration . If you issue a query that contains {metric_type: software, software_type: computer} ,
Data Federation ignores files with the prefix /phone . For more information on mapping partition attributes to a collection databases.[n].collections.[n].dataSources.[n].path , see Define Path for S3 Data . Data File Size Each file that Atlas Data Federation handles requires a certain amount of compute
resources. If your federated database instance store contains many small data
files, the resources required compound and can reduce performance.
Alternatively, many large data files are problematic as
Data Federation then downloads and processes unnecessary data. For most use cases, a performant file size is 100 to 200 MB . Data File Format Federated Database Instances support several data file formats . You can improve performance by compressing
certain file formats or by optimizing file contents for your queries. Compression When you compress data files, they take less time to download. Reduced
download time has a greater performance benefit than parsing
uncompressed data. You can compress the following file formats using gzip : JSON BSON CSV TSV File Structure Parquet , Avro , and ORC files contain metadata about the file
itself so that an application can traverse the file contents in
different ways. If you structure your data file to align with the
queries you want to run, Atlas Data Federation can leverage this metadata to quickly
jump to the right data. Of these formats, Parquet files provide the
best performance and space efficiency for federated database instance, as it is
optimized to parse row and column groups for Parquet . Back Define Path for S3 Data Next Configure S3 Encryption
