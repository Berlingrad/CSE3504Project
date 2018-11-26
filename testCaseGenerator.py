import sys, random, csv, argparse


parser = argparse.ArgumentParser(description='generate source file for LRJF and FCFS comparison')
parser.add_argument('-s','--size', metavar='SIZE',
                    dest='s',
                    type = int,
                    help='size of test file inter terms of numberof test cases',
                    default = 10,
                    )
parser.add_argument('-t', '--threads', metavar="NUM of THREADS",
                     help='number of threads',
                     default = 4,
                    type = int,
                    dest='t'
                    )
parser.add_argument('-c', '--case', metavar = 'CASE #',
                     help='case number according to Table 1 of Supplementry file 2',
                     default = 1,
                     type = int,
                     dest='c'
                    )
parser.add_argument('-p','--path',
                    help='path to the output file',
                    type=str,
                    default="./test.csv",
                    dest='p'
                    )
args=parser.parse_args()

size = args.s
numofthreads = args.t
case = args.c
outfile = args.p



if case == 1: #case "= = =" according to Table 1 of Supplementary file 2
     with open(outfile, mode='w') as out:
         out_writer = csv.writer(out, delimiter = ',')
         for x in range(size):
             p = random.randint(0, 99)
             l = random.randint(0, 99)
             r = random.randint(0, 99)
             out_writer.writerow([p for i in range(numofthreads)])
             out_writer.writerow([l for i in range(numofthreads)])
             out_writer.writerow([x for i in range(numofthreads)])
             out_writer.writerow([])


elif case == 2: #case "= = <>"
     with open(outfile, mode='w') as out:
         out_writer = csv.writer(out, delimiter = ',')
         for x in range(size):
             p = random.randint(0, 99)
             l = random.randint(0, 99)
             r = random.randint(0, 99)
             out_writer.writerow([p for i in range(numofthreads)])
             out_writer.writerow([l for i in range(numofthreads)])
             out_writer.writerow([random.randint(0,99) for i in range(numofthreads)])
             out_writer.writerow([])

elif case == 3: #case "= <> ="
    with open(outfile, mode='w') as out:
         out_writer = csv.writer(out, delimiter = ',')
         for x in range(size):
             p = random.randint(0, 99)
             l = random.randint(0, 99)
             r = random.randint(0, 99)
             out_writer.writerow([p for i in range(numofthreads)])
             out_writer.writerow([random.randint(0, 99) for i in range(numofthreads)])
             out_writer.writerow([r for i in range(numofthreads)])
             out_writer.writerow([])

elif case == 4: #case "= <> <>"
    with open(outfile, mode='w') as out:
         out_writer = csv.writer(out, delimiter = ',')
         for x in range(size):
             p = random.randint(0, 99)
             l = random.randint(0, 99)
             r = random.randint(0, 99)
             out_writer.writerow([p for i in range(numofthreads)])
             out_writer.writerow([random.randint(0, 99) for i in range(numofthreads)])
             out_writer.writerow([random.randint(0, 99) for i in range(numofthreads)])
             out_writer.writerow([])

elif case == 5: #case "<> = ="
    with open(outfile, mode='w') as out:
         out_writer = csv.writer(out, delimiter = ',')
         for x in range(size):
             p = random.randint(0, 99)
             l = random.randint(0, 99)
             r = random.randint(0, 99)
             out_writer.writerow([random.randint(0, 99) for i in range(numofthreads)])
             out_writer.writerow([l for i in range(numofthreads)])
             out_writer.writerow([r for i in range(numofthreads)])
             out_writer.writerow([])

elif case == 6: #case "<> = <>"
    with open(outfile, mode='w') as out:
         out_writer = csv.writer(out, delimiter = ',')
         for x in range(size):
             p = random.randint(0, 99)
             l = random.randint(0, 99)
             r = random.randint(0, 99)
             out_writer.writerow([p for i in range(numofthreads)])
             out_writer.writerow([random.randint(0, 99) for i in range(numofthreads)])
             out_writer.writerow([r for i in range(numofthreads)])
             out_writer.writerow([])

elif case == 7: #case "<> <> ="
    with open(outfile, mode='w') as out:
         out_writer = csv.writer(out, delimiter = ',')
         for x in range(size):
             p = random.randint(0, 99)
             l = random.randint(0, 99)
             r = random.randint(0, 99)
             out_writer.writerow([random.randint(0, 99) for i in range(numofthreads)])
             out_writer.writerow([random.randint(0, 99) for i in range(numofthreads)])
             out_writer.writerow([r for i in range(numofthreads)])
             out_writer.writerow([])

elif case == 8: #case "<> <> <>"
    with open(outfile, mode='w') as out:
         out_writer = csv.writer(out, delimiter = ',')
         for x in range(size):
             p = random.randint(0, 99)
             l = random.randint(0, 99)
             r = random.randint(0, 99)
             out_writer.writerow([random.randint(0, 99) for i in range(numofthreads)])
             out_writer.writerow([random.randint(0, 99) for i in range(numofthreads)])
             out_writer.writerow([random.randint(0, 99) for i in range(numofthreads)])
             out_writer.writerow([])
else:
    raise Exception("invalid case")

