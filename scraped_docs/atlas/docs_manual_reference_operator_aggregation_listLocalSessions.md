# $listLocalSessions - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $listLocalSessions On this page Definition Restrictions Examples Definition $listLocalSessions Lists the sessions cached in memory by the mongod or mongos instance. Important When a user creates a session on a mongod or mongos instance, the record of the session initially
exists only in-memory on the instance; i.e. the record is local
to the instance. Periodically, the instance will sync its cached
sessions to the system.sessions collection in the config database, at which time, they are
visible to $listSessions and all members of the
deployment. Until the session record exists in the system.sessions collection, you can only list the session via
the $listLocalSessions operation. The $listLocalSessions operation uses the db.aggregate() method and not the db.collection.aggregate() . To run $listLocalSessions , it must be the first stage in
the pipeline. The stage has the following syntax: { $listLocalSessions : < document > } The $listLocalSessions stage takes a document with one
of the following contents: Field Description { } If running with access control, returns all sessions for the
current authenticated user. If running without access control, returns all sessions. { users: [ { user: <user>, db: <db> }, ... ] } Returns all sessions for the specified users. If running with
access control, the authenticated user must have privileges
with listSessions action on the cluster to list
sessions for other users. { allUsers: true } Returns all sessions for all users. If running with access
control, the authenticated user must have privileges with listSessions action on the cluster. Restrictions $listLocalSessions is not allowed in transactions . Examples List All Local Sessions From the connected mongod / mongos instance's
in-memory cache of sessions, the following aggregation operation lists
all sessions: Note If running with access control, the current user must have
privileges with listSessions action on the cluster. db. aggregate ( [ { $listLocalSessions : { allUsers : true } } ] ) List All Local Sessions for the Specified Users From the connected mongod / mongos instance's
in-memory cache, the following aggregation operation lists all the
sessions for the specified user myAppReader@test : Note If running with access control and the current user is not the
specified user, the current user must
have privileges with listSessions action on the cluster. db. aggregate ( [ { $listLocalSessions : { users : [ { user : "myAppReader" , db : "test" } ] } } ] ) List All Local Sessions for the Current User From the connected mongod / mongos instance's
in-memory cache, the following aggregation operation lists all sessions
for the current user if run with access control: db. aggregate ( [ { $listLocalSessions : { } } ] ) If run without access control, the operation lists all local
sessions. Back $limit Next $listSampledQueries
