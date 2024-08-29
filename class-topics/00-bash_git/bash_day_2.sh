echo hello world > hello.txt
echo hello world >> hello.txt
echo hello world >> ~/Desktop/brb/hello2.txt
cat ~/Desktop/brb/hello2.txt
cat hello.txt hello2.txt
cat hello.txt hello2.txt > hello_cat.txt
wc hello.txt
wc -l hello.txt
cat hello.txt hello2.txt | wc -l
grep hello hello.txt
cat *.txt | grep hello
nano hello.txt