echo "Enter a number: "
read num
i=2
f=0
while [ $i -le `expr $num / 2` ]
do
if [ `expr $num % $i` -eq 0 ]
then
f=1
fi
i=`expr $i + 1`
done
if [ $f -eq 1 ]
then
echo "The number is composite"
else
echo "The number is Prime"
fi