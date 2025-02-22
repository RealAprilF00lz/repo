#!/bin/bash
#script for me to learn bash
echo what is your name? 
read name 
echo -e "hello, $name! the current date and time is `date`.\nplease type the path of a folder. i will tell you how many items are in it." 
read path 
echo the folder has `ls -A $path|wc -l` items in it, including hidden items.
correct=0
function math {
read number;if [ $number = $answer ];then echo correct!;correct=$[correct+1];else echo incorrect!;fi
}
echo what is 3+4? 
answer=7
math
echo 5 times x = 30. what is x?
answer=6
math
echo what is 10 divided by 3? round to the nearest tenth.
answer=3.3
math
echo what is the cube root of 27?
answer=3
math
echo what is 3.14 times 10 to the power of 4?
answer=31400
math
echo you got $correct/5 questions correct.
sleep 1 
echo countdown... 
sleep 1 
for countdown in {5..1};do echo $countdown;sleep 1;done
echo liftoff!
sleep 1
while true;do
echo do you want to view information about your system? type y for yes and n for no
read yn
case $yn in y|n)break;;*)echo invalid response;esac
done
if [ $yn = y ];then hostnamectl;echo desktop environment is $XDG_CURRENT_DESKTOP on $XDG_SESSION_TYPE;echo system has been `uptime -p`;fi
echo the script has finished. goodbye, $name!
