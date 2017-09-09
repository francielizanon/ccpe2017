sleep 20
echo "start test"
date
pcm 1 -csv=/home/jlbez/teste1.pcm.csv -- fio --name=test1 --ioengine=sync --iodepth=1 --rw=write --bs=4m --direct=0 --size=100G --numjobs=1 --runtime=20 --eta=never --output=/home/jlbez/fio-output-test1
echo "finished test"
date
sleep 20
echo "start test"
date
pcm 1 -csv=/home/jlbez/teste2.pcm.csv -- fio --name=test2 --ioengine=sync --iodepth=1 --rw=write --bs=4m --direct=0 --size=100G --numjobs=1 --runtime=20 --eta=never --output=/home/jlbez/fio-output-test2
echo "finished test"
date
sleep 20
echo "start test"
date
pcm 1 -csv=/home/jlbez/teste3.pcm.csv -- fio --name=test3 --ioengine=sync --iodepth=1 --rw=write --bs=4m --direct=0 --size=100G --numjobs=1 --runtime=20 --eta=never --output=/home/jlbez/fio-output-test3
echo "finished test"
date
