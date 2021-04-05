
echo "Attemptng to disassemble $1"

# Clear out file if it exists
if test -f "symbols.txt"; 
then
    rm "symbols.txt"
fi

objdump --syms $1 > symbols.txt

if [ -s "symbols.txt" ]
then
    echo "Success! Table stored at symbols.txt"
else
    echo "Failed!"
fi
