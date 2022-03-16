@echo off
set xv_path=D:\\XLINX\\Vivado\\2015.4\\bin
call %xv_path%/xsim a_behav -key {Behavioral:sim_1:Functional:a} -tclbatch a.tcl -log simulate.log
if "%errorlevel%"=="0" goto SUCCESS
if "%errorlevel%"=="1" goto END
:END
exit 1
:SUCCESS
exit 0
