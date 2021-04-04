
echo "Attemptng to disassemble $1"

objdump --syms $1 > $1.symbols.txt

if [ -s "$1.symbols.txt" ]
then
    echo "Success! Table stored at $1.symbols.txt"
else
    echo "Failed!"
fi
