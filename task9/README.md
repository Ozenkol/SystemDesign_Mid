<h1>Global Student Portal</h1>
<h2>Functional requirements</h2>
<ol>
<li>Register disciplines</li>
<li>Show Schedule</li>
</ol>
<h2>Non-functional requirements</h2>
<ol>
<li><i>Scalable</i> - some university may join to out service</li>
<li><i>Availability</i>. The system should be reliable and available 99.99% of the time (Availability >> Consistency)</li>
<li>The redirection should occur with minimal delay (< 100ms)
</li>
<li># of Institutions - ~35 000<br>
# students in each - 20 000 
DAU - ~30%</li>
</ol>

<h2>Draft the API specification</h2>
<ol>
<li>GET and DELETE /discipline/{id}</li>
<li>GET and DELETE /discipline/{id}</li>
</ol>

<h2>Connections and processing between users and data</h2>
<h3>SQL database schema</h3>
<cite>When low latency is required, such as when responding to user queries, we usually use 
SQL or in-memory databases with low latency such as Redis. NoSQL databases that use 
distributed file systems such as HDFS are for large data-processing jobs. </cite>

According this cite we must use NoSQL database cause its scala

<h2>Design the data model</h2>
<ol>
<li>Student</li>
<li>University</li>
<li>Department</li>
<li>Instructor</li>
<li>Section</li>
<li>Course</li>
</ol>
<h2>Logging, monitoring, and alerting</h2>

<h2>Our app consist </h2>