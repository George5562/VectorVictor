# Variables in Aggregation Expressions - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference Variables in Aggregation Expressions On this page User Variables System Variables Aggregation expressions can use both
user-defined and system variables. Variables can hold any BSON type data .
To access the value of the variable, prefix the variable name with
double dollar signs ( $$ ); i.e. "$$<variable>" . If the variable references an object, to access a specific field in the
object, use the dot notation; i.e. "$$<variable>.<field>" . User Variables User variable names can contain the ascii characters [_a-zA-Z0-9] and any non-ascii character. User variable names must begin with a lowercase ascii letter [a-z] or a non-ascii character. System Variables MongoDB offers the following system variables: Variable Description NOW A variable that returns the current datetime value. NOW returns the same value for all members of the
deployment and remains the same throughout all stages of the
aggregation pipeline. CLUSTER_TIME A variable that returns the current timestamp value. CLUSTER_TIME is only available on replica sets and
sharded clusters. CLUSTER_TIME returns the same value for all members
of the deployment and remains the same throughout all stages of
the pipeline. ROOT References the root document, i.e. the top-level document, currently
being processed in the aggregation pipeline stage. CURRENT References the start of the field path being processed in the
aggregation pipeline stage. Unless documented otherwise, all
stages start with CURRENT the same as ROOT . CURRENT is modifiable. However, since $<field> is equivalent to $$CURRENT.<field> , rebinding CURRENT changes the meaning of $ accesses. REMOVE A variable which evaluates to the missing value. Allows for the
exclusion of fields in $addFields and $project stages. For examples that use $$REMOVE , see: Remove Fields Conditionally Exclude Fields DESCEND One of the allowed results of a $redact expression. PRUNE One of the allowed results of a $redact expression. KEEP One of the allowed results of a $redact expression. SEARCH_META A variable that stores the metadata results of an Atlas
Search query. In all supported aggregation
pipeline stages, a field set to the variable $$SEARCH_META returns the metadata results for the query. For an example of its usage, see Atlas Search facet and count . USER_ROLES Returns the roles assigned to the current user. For use cases that include USER_ROLES , see the find , aggregation , view , updateOne , updateMany , and findAndModify examples. New in version 7.0 . Tip See also: $let $redact $map Back Commands Comparison Next SQL to Aggregation
