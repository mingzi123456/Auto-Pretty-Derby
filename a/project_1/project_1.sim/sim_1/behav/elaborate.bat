@echo off
set xv_path=D:\\XLINX\\Vivado\\2015.4\\bin
call %xv_path%/xelab  -wto ae2474b96fb44350a1bb1df7b37820a6 -m64 --debug typical --relax --mt 2 -L xil_defaultlib -L unisims_ver -L unimacro_ver -L secureip --snapshot a_behav xil_defaultlib.a xil_defaultlib.glbl -log elaborate.log
if "%errorlevel%"=="0" goto SUCCESS
if "%errorlevel%"=="1" goto END
:END
exit 1
:SUCCESS
exit 0
