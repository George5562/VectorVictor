# 2dsphere Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Geospatial 2dsphere Indexes On this page Use Cases Get Started Details sparse Property Compound 2dsphere Indexes Learn More 2dsphere indexes support geospatial queries on an earth-like sphere. For
example, 2dsphere indexes can: Determine points within a specified area. Calculate proximity to a specified point. Return exact matches on coordinate queries. The values of the indexed field must be either: GeoJSON objects Legacy coordinate pairs For legacy coordinate pairs, the 2dsphere index converts the data to GeoJSON points . To create a 2dsphere index, specify the string 2dsphere as the index
type: db. < collection > . createIndex ( { < location field > : "2dsphere" } ) Note When creating a a 2dsphere index , the first
value, or longitude, must be between -180 and 180, inclusive. The second value,
or latitude, must be between -90 and 90, inclusive. These coordinates "wrap"
around the sphere. For example, -179.9 and +179.9 are near neighbors. Use Cases Use 2dsphere indexes to query and perform calculations on location data
where the data points appear on Earth, or another spherical surface. For
example: A food delivery application uses 2dsphere indexes to support
searches for nearby restaurants. A route planning application uses 2dsphere indexes to calculate
the shortest distance between rest stops. A city planner uses 2dsphere indexes to find parks that exist within
city limits. Get Started To learn how to create and query 2dsphere indexes, see: Create a 2dsphere Index Query for Locations Bound by a Polygon Query for Locations Near a Point on a Sphere Query for Locations that Intersect a GeoJSON Object Query for Locations within a Circle on a Sphere Details 2dsphere indexes are always sparse and have
special behaviors when created as part of a compound index . sparse Property 2dsphere indexes are always sparse . When
you create a 2dsphere index, MongoDB ignores the sparse option. If an existing or newly inserted document does not contain a 2dsphere
index field (or the field is null or an empty array), MongoDB does
not add an entry for the document to the index. Compound 2dsphere Indexes For a compound index that includes a 2dsphere index key along with
keys of other types, only the 2dsphere index field determines
whether the index references a document. A compound 2dsphere index can reference multiple location and
non-location fields. In contrast, a compound 2d index can only reference one location field and one other field. Learn More Geospatial Queries Geospatial Query Operators Find Restaurants with Geospatial Queries Geospatial Index Restrictions Back Geospatial Next Create
