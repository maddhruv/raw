echo "Enter first no"
read a
echo "Enter 2nd no"
read b
p= 'expr $a * $b'
while [$b -ne 0]
do r= 'expr $a % $b'
a=$b b=$r
done
LCM = 'expr $p / $a'
echo "LCM = $LCM"
echo "Hcf = $a"