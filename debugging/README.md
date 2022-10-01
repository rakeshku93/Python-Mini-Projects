# Debugging In Python:

The IDEs like (VSCode, PyCharm, etc.) have debugger functionality with these features: 
1. Continue
2. Step Over
3. Step In
4. Step Out
5. Stop button

## Continue
Clicking the Continue button will cause the program to execute normally
until it terminates or reaches a breakpoint. If you are done debugging and want the program to continue
normally, click the Continue button.

## Step In
Clicking the Step In button will cause the debugger to execute the next line
of code and then pause again. If the next line of code is a function call, the
debugger will `step into` that function and jump to the first line of code of
that function.

## Step Over
Step Over will execute the next line of code, similar to the Step In button. 
However, if the next line of code is a function call, the Step Over button will `step over` the code in the function. The function's code will be executed at full speed, and the debugger will pause as soon as
the function call returns.

## Step Out
Clicking the Step Out button will cause the debugger to execute lines of
code at full speed until it returns from the current function. If you have
stepped into a function call with the Step In button and now simply want to
keep executing instructions until you get back out, click the Out button to
“step out” of the current function call.

## Stop
If you want to stop debugging entirely and not bother to continue executing
the rest of the program, click the Stop button. The Stop button will immediately
terminate the program.