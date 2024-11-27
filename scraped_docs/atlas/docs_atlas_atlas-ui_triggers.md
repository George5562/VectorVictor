# Atlas Triggers - MongoDB Atlas


Docs Home / MongoDB Atlas / Interact with Data Atlas Triggers On this page Trigger Types Limitations Atlas Function Constraints Apply Event Processing Throughput Number of Triggers Cannot Exceed Available Change Streams Diagnose Duplicate Events Atlas Triggers execute application and database logic. Triggers
can respond to events or use pre-defined schedules. Triggers listen for events of a configured type. Each Trigger links to a
specific Atlas Function .
When a Trigger observes an event that matches your
configuration, it "fires" . The Trigger passes this event object as the
argument to its linked Function. A Trigger might fire on: A specific operation type in a given Collection. A scheduled time. Atlas keeps track of the latest execution time for each Trigger and guarantees
that each event is processed at least once. Trigger Types Atlas supports these types of triggers: Database triggers respond to document insert, changes, or deletion. You can configure
Database Triggers for each linked MongoDB collection. Scheduled triggers execute functions according to a pre-defined schedule. Limitations Atlas Function Constraints Apply Triggers invoke Atlas Functions. This means they have the same
constraints as all Atlas Functions. Learn more about Atlas Function constraints . Event Processing Throughput Triggers process events when capacity becomes available. A Trigger's
capacity is determined by its event ordering configuration: Ordered triggers process events from the change stream one at a time
in sequence. The next event begins processing only after the previous
event finishes processing. Unordered triggers can process multiple events concurrently, up to
10,000 at once by default. If your Trigger data source is an M10+
Atlas cluster, you can configure individual unordered triggers to
exceed the 10,000 concurrent event threshold. To learn more, see Maximum Throughput Triggers . Trigger capacity is not a direct measure of throughput or a guaranteed
execution rate. Instead, it is a threshold for the maximum number of
events that a Trigger can process at one time. In practice, the rate at
which a Trigger can process events depends on the Trigger function's run
time logic and the number of events that it receives in a given
timeframe. To increase the throughput of a Trigger, you can try to: Optimize the Trigger function's run time behavior. For example, you
might reduce the number of network calls that you make. Reduce the size of each event object with the Trigger's projection filter . For the best
performance, limit the size of each change event to 2KB or less. Use a match filter to reduce the number of events that the Trigger
processes. For example, you might want to do something only if a
specific field changed. Instead of matching every update event and
checking if the field changed in your Function code, you can use the
Trigger's match filter to fire only if the field is included in the
event's updateDescription.updatedFields object. Number of Triggers Cannot Exceed Available Change Streams Atlas limits the total number of Database Triggers. The size of your
Atlas cluster drives this limit. Each Atlas cluster tier has a maximum number of supported change
streams. A Database Trigger requires its own change stream. Database Triggers
may not exceed the number of available change streams. Learn more about the number of supported change streams for Atlas tiers on the Service Limitations page . Diagnose Duplicate Events During normal Trigger operation, Triggers do not send duplicate events.
However, when some failure or error conditions occur, Triggers may deliver
duplicate events. You may see a duplicate Trigger event when: A server responsible for processing and tracking events experiences a
failure. This failure prevents the server from recording its progress in a
durable or long-term storage system, making it "forget" it has processed
some of the latest events. Using unordered processing where events 1 through 10 are sent simultaneously.
If event 9 fails and leads to Trigger suspension, events like event 10 might
get processed again when the system resumes from event 9. This can lead to
duplicates, as the system doesn't strictly follow the sequence of events and
may reprocess already-handled events. If you notice duplicate Trigger events, check the Trigger logs for suspended Triggers or server failures. Back Aggregation Pipelines Next Database Triggers
