import subprocess

#your input array
input_array = ["1","2","3","4","5"]

#compile the C program(assuming it's saved as ccode.c)
subprocess.run(["gcc", "ccode.c", "-o", "CProg"])

#run the compiled c program with the input array as arguments
process = subprocess.run(["./CProg"] + input_array, capture_output=True, text=True)

#store the output of the C program in a Python variable
output_variable=process.stdout.strip()

#print or use the store output
print("C program output:")
print(c_output_variable)

#command HASKELL
subprocess.run(['ghc', 'hprog.hs'])

process = subprocess.run(['./hprog'] + [str(x) for x in input_array], text=True, capture_output=True)

result = process.stdout.strip()
print("Haskell program output:")
print(haskell_output_variable)

#command prolog 
prolog_input = "[" + ",".join(map(str, input_array)) + "].”

result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'example.pl'], input=prolog_input,
capture_output=True, text=True)

output_result = result.stdout.strip()
print("Prolog program output:")
print(prolog_output_variable)
