if test -f "rop_file.txt"; 
then
    rm "rop_file.txt"
fi

ROPgadget --binary $1 > rop_file.txt

if [ -s "rop_file.txt" ]
then
    echo "Success! ROP gadgets stored at rop_file.txt"
else
    echo "Failed!"
fi