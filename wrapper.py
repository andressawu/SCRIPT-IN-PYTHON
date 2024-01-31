import subprocess

matlab_executable = '/Applications/MATLAB_R2023b.app/bin/matlab'

matlab_process = subprocess.run([matlab_executable, "-batch", "run('matlab1.m'); pause(10);"]
, capture_output=True)

print("Running MATLAB CODE1")


#read from the input text file
with open('input.txt', 'r') as file:
	input_str = file.read().split()
	input_array = [int(value) for value in input_str]
	input_array = [str(value) for value in input_array]

#run c program
#compile the C program(assuming it's saved as ccode.c)
subprocess.run(["gcc", "ccode.c", "-o", "ccode"])

#run the compiled c program with the input array as arguments
process = subprocess.run(["./ccode"] + input_array, capture_output=True, text=True)

#store the output of the C program in a Python variable
output_variable =process.stdout.strip()

#run haskell program 
subprocess.run(['ghc', 'hcode.hs'])

#run the compiled haskell program witht the input arau as arguments
process = subprocess.run(['./hcode'] + [str(x) for x in input_array], text=True, capture_output=True)

haskell_output = process.stdout.strip()

#run prolog program 
prolog_input = "[" + ",".join(map(str, input_array)) + "]."

result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'prcode.pl'], input=prolog_input,
capture_output=True, text=True)

pl_result = result.stdout.strip()

#store output text file
#save the output_variable to a file
with open('c_output.txt', 'w') as f:
  f.write(output_variable)

#store output text file
with open('haskell_output.txt', 'w') as f:
   f.write(haskell_output)

#store output text file
with open('prolog_output.txt', 'w') as f:
   f.write(pl_result)

matlab_process = subprocess.run([matlab_executable, "-batch", "run('matlab2.m');pause(10)"],capture_output=True)

print("RUNNING MATLAB2")

