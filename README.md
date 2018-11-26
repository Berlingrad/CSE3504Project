# CSE3504Project: LRJF and FCFS algorithms

<b>Sample run:</b>
<pre>python testCaseGenerator.py -s 100 -t 4 -c 6 -p ./source.csv</pre>
This command generates a csv file containing data for LRJF and FCFS comparison. 
<code>-s</code> indicates the size of the test data in terms of number of data items.
<code>-t</code> indicates number of threads applied in each data item
<code>-c</code> specifies case number according to Table 1 of supplementary file  2.
<code>-p</code> is the path to the output file, default if source.csv.
Use flag <code>-h</code> for detailed information

<pre>python LRJFvsFCFS.py source.csv</pre>
<code>LRJFvsFCFS.py</code> takes a csv file generated from <code> testCaseGenerator.py</code>
as input, display average process cost of each algorithm over test data items.

<b>Sample output:</b>
<pre>
Number of data items = 100
Average processing cost of LRJF =   308.92
Average processing cost of FCFS =   277.76
</pre>
