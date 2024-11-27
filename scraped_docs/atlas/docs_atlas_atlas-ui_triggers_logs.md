# Trigger Logs - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data / Triggers Trigger Logs On this page Error Logs Log Filters Log Lines Log Retention App Metrics Atlas Alerts Log Format Fields Error Fields Atlas keeps a log of Trigger, Function, and Change Stream events and
publishes notifications to your Atlas project's activity feed. Atlas saves
logs for 10 days, after which they are deleted. To learn how to view, filter, and analyze your application logs, see View Application Logs . Error Logs All log entries have one of the following statuses: OK , which represents a normal event that succeeded without an error. Error , which represents an event that did not run successfully for
any reason. For example, Atlas logs an error for any of the following
events: You attempt to access data stored in Atlas for which there is no
applicable rule. You throw or fail to handle an error or promise rejection in an Atlas
Function. You call context.services.get() for a service which does not exist. Log Filters For performance reasons, Atlas limits individual queries to a
maximum of 100 log entries per page. You can filter entries by type,
status, timestamp, user, and request ID to return only logs that are
relevant to your query. Log Lines Functions can log information using JavaScript's console.log() method. Atlas stringifies each console log and stores each string
as a single line. Atlas truncates lines to 512 bytes in length.
For ASCII character sets, this translates to 512 characters; depending
on the character set you use, you may see truncation at lower character
counts. Atlas saves only the first 25 log lines for a given log entry. Log Retention Atlas retains logs for 10 days, after which they are deleted. If you require logs older than 10 days, you can automatically forward logs to another service. You
can also download a dump of currently available logs from the UI or use
the Admin API Logging endpoints to
fetch logs before they expire. App Metrics Atlas measures usage and records aggregate metrics over time. You can access
and use the metrics to assess performance and identify usage trends. For
example, how much time was spent performing computations. To learn more about which metrics are available and how to access them,
see Metrics . Atlas Alerts Atlas events publish to your Atlas project's activity feed.
Alerts include Trigger failure events, which occur when a Trigger fails and
cannot restart automatically. To learn more, see Activity Feed & Atlas Alerts . Log Format Trigger log entries have the following form: Logs : [ <log line>, <log line>, ... ] See Function. See Trigger. Compute Used: <number> bytesâ¢ms Fields Field Description Compute Used Computational load of the operation. Logs List of console.log outputs. Atlas saves the first 512 bytes
of the last 25 console.log() calls. See Function. See Trigger. Links to the Trigger that launched this event as well as the Function
that was run by this event. Error Fields Log entries created by unsuccessful operations may feature the following additional
fields for debugging purposes: Field Description Error Brief description of an error. Back Define and Access Values Next Triggers Limitations
