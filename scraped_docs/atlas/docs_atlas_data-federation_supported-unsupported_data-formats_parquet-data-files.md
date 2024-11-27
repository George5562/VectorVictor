# Parquet - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores / AWS S3 Bucket / Data Formats Parquet On this page About Parquet Format About Parquet for Atlas Data Federation About Parquet Format Apache Parquet is a free,
open-source file format that is popular for analytic workloads. Parquet
stores columns together, rather than rows. It's a fixed-schema format
with support for complex data structures like arrays and nested
documents. These features have the following advantages: Performant queries . Parquet is column-oriented, and therefore
queries on Parquet data can be extremely performant. For example, a
query that selects just one of thousands of columns can immediately
extract that data from the Parquet file, rather than trying to find
the desired value in each row. Efficient storage . Parquet stores columns contiguously, which
enables very efficient compression. Parquet requires that the values
in a given column must have the same type, and the values in a column
are generally more similar than values in other columns. This enables
a wider variety of encoding and compression schemes. Compatibility with analytics tools . Parquet files have a fixed
schema, and therefore Parquet data is compatible with many analytics
tools that require data in a tabular, fixed-schema format. About Parquet for Atlas Data Federation Atlas Data Federation can read from and write to Parquet data files. Reading Parquet . You can query Parquet data from S3 with
Atlas Data Federation. These queries might be more performant than queries on other
data formats. To learn more about why queries against Parquet data
might be more performant than other data formats, see About Parquet Format . Writing Parquet . Atlas Data Federation allows you to also write data to Parquet
using the $out to S3 stage. Atlas Data Federation
automatically infers what Parquet schema to use based on the MongoDB
data that you are writing to Parquet. You can transform your data to
Parquet data format if you want to query that data with another
analytics tool such as a data warehouse. To learn more about how Atlas Data Federation writes to Parquet file format during $out to S3 stage, see Parquet File Format . Back Data Formats Next CSV and TSV
