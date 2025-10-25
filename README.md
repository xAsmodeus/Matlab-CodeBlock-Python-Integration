# Matlab Function Block Python Integration
## Overview
                                         ** Runned and Tested in Matlab Simulink **
                                              
There has been a task that I had to deal with, in the early stages after joining HERMES Team. 
That includes a simple schema that uses Python and Matlab to create a type of subsystem that can utilize team's proexisting Python Code (Software) in the Matlab and Simulink Environment.

<img width="636" height="163" alt="Screenshot_1" src="https://github.com/user-attachments/assets/562bc987-8c12-4690-b172-f3bdc9c52983" />

## Approach

In general, my MATLAB required almost no modification to run Python. There are functions such as pyenv that are useful for setting up Python in MATLAB, as well as py.sys.version for checking whether the interface is working.
## Examples

1. Two inputs -> adds the numbers together -> displays the result. 

USED: Display block, constants(input)/output blocks, Matlab Function Block.

<img width="865" height="442" alt="image" src="https://github.com/user-attachments/assets/85ac40c9-0f6c-403c-9e28-14c07cd50496" />

2. An example with libraries (numpy) imported into Python code.

<img width="808" height="350" alt="image" src="https://github.com/user-attachments/assets/9b227248-c62a-442e-926b-be229df70d52" />

## Observations
1) No Problem with 1 / N inputs -----> 1 / M outputs
   The MATLAB function block automatically recognizes the model's inputs/outputs through the code and thus adjusts what is needed. Then you just need to tweak variables/dimensions/connections, etc.
   
2) Simulink may not directly support the Python language. Therefore, scripts that take blocks_of_code must be written exclusively in MATLAB functions. In other words, the code must be converted from Python => MATLAB.

3) Special attention must be paid to the dimensions of the variables, otherwise the model will not run. (They can be changed by clicking on function_block > Edit Data > Symbols ( & Property Inspector). 

## References

  1. https://chatgpt.com/share/6755fced-a7b4-8001-918d-66a337f7cdb4
  
