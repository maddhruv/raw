echo "Enter the filename"
read file_name
terminal=`tty`
exec < $file_name
l=0
w=0
while read line
do
l=`expr $l + 1`
set $line
w=`expr $w + $#`
done
f=$(stat -c%s "$file_name")
echo "no of lines: $l"
echo "no of words: $w"
echo "no of char: $f"