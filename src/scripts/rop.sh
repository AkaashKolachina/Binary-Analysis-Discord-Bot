if test -f "src/results/rop_file.txt"; 
then
    rm "src/results/rop_file.txt"
fi

ROPgadget --binary $1 > src/results/rop_file.txt

if [ -s "src/results/rop_file.txt" ]
then
    echo "Success! ROP gadgets stored at rop_file.txt"
else
    echo "Failed!"
fi