"""
This file takes a csv file generated from "testCaseGenerator.py" as input. it run LRJF and FCFS respectively on all
input data items and take an average.
"""

import project, copy, time, argparse, csv

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='This file takes a csv file generate from  testCaseGenerator.py'
                                                 'as an input and compare procesing cost'
                                                 'between LRJF and FCFS algorithms under various'
                                                 'test cases')
    parser.add_argument('infile', metavar='INFILE',
                        type=str,
                        help="path to a input file"
                        )
    arg = parser.parse_args()
    infile = arg.infile

    input = [[]]
    line_count = 0
    with open(infile) as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        for row in reader:
            if row != []:
                if line_count == 2:

                    input.append([])
                    line_count = 0
                else:
                    line_count += 1
                line = [int(i) for i in row]
                input[-1].append(line)


    del input[-1]
    runtime_L = [] ##Run time of LRJF on all test cases
    runtime_F = [] ##Run time of FCFS on all test cases

    cputime_L = []
    cputime_F = []

    for t in input:
        lo = project.LRJF(t)
        fo = project.FCFS(t)
        start_time = time.time()
        runtime_L.append(project.totalTime(lo))
        time_lapse_L = time.time() - start_time
        cputime_L.append(time_lapse_L)

        start_time = time.time()
        runtime_F.append(project.totalTime(fo))
        time_lapse_F = time.time() - start_time
        cputime_F.append(time_lapse_F)

    print("Number of data items = %d" % (len(input)))
    print("Average processing cost of LRJF = %8.2f" % (sum(runtime_L) / len(runtime_L)))
    print("Average processing cost of FCFS = %8.2f" % (sum(runtime_F) / len(runtime_F)))
    print("Average cpu time of LRJF = ", (sum(cputime_L)/float(len(cputime_L))))
    print("Average cpu time of FCFS = ", (sum(cputime_F)/float(len(cputime_F))))
