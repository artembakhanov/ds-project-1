
echo "Starting killing your computer... hahah"
for i in $(seq 1 $1); do
	yes > /dev/null &
done
echo "All processes are run. If you reach 100 C cpu temperature please turn this off"
while :;do 
	sleep 300
done
