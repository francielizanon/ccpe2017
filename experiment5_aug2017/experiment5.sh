#!/bin/sh
# script de testes gerado automaticamente

sync

echo write_experiment5_32kreq_comcache_4 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_comcache_4.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=write --bs=32k --direct=0 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_comcache_4.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
sync

sleep 20 
echo randwrite_experiment5_32kreq_comcache_4 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_comcache_4.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randwrite --bs=32k --direct=0 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_comcache_4.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
sync

sleep 20 
echo write_experiment5_32kreq_semcache_2 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_semcache_2.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=write --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_semcache_2.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo read_experiment5_32kreq_semcache_2 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/read_experiment5_32kreq_semcache_2.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=read --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/read_experiment5_32kreq_semcache_2.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo randwrite_experiment5_32kreq_semcache_2 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_semcache_2.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randwrite --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_semcache_2.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo randread_experiment5_32kreq_semcache_2 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randread_experiment5_32kreq_semcache_2.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randread --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randread_experiment5_32kreq_semcache_2.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo write_experiment5_32kreq_comcache_2 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_comcache_2.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=write --bs=32k --direct=0 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_comcache_2.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
sync

sleep 20 
echo randwrite_experiment5_32kreq_comcache_2 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_comcache_2.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randwrite --bs=32k --direct=0 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_comcache_2.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
sync

sleep 20 
echo write_experiment5_32kreq_comcache_3 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_comcache_3.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=write --bs=32k --direct=0 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_comcache_3.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
sync

sleep 20 
echo randwrite_experiment5_32kreq_comcache_3 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_comcache_3.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randwrite --bs=32k --direct=0 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_comcache_3.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
sync

sleep 20 
echo write_experiment5_32kreq_semcache_3 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_semcache_3.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=write --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_semcache_3.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo read_experiment5_32kreq_semcache_3 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/read_experiment5_32kreq_semcache_3.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=read --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/read_experiment5_32kreq_semcache_3.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo randwrite_experiment5_32kreq_semcache_3 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_semcache_3.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randwrite --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_semcache_3.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo randread_experiment5_32kreq_semcache_3 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randread_experiment5_32kreq_semcache_3.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randread --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randread_experiment5_32kreq_semcache_3.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo write_experiment5_32kreq_semcache_1 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_semcache_1.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=write --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_semcache_1.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo read_experiment5_32kreq_semcache_1 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/read_experiment5_32kreq_semcache_1.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=read --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/read_experiment5_32kreq_semcache_1.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo randwrite_experiment5_32kreq_semcache_1 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_semcache_1.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randwrite --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_semcache_1.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo randread_experiment5_32kreq_semcache_1 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randread_experiment5_32kreq_semcache_1.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randread --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randread_experiment5_32kreq_semcache_1.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo write_experiment5_32kreq_comcache_1 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_comcache_1.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=write --bs=32k --direct=0 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_comcache_1.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
sync

sleep 20 
echo randwrite_experiment5_32kreq_comcache_1 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_comcache_1.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randwrite --bs=32k --direct=0 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_comcache_1.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
sync

sleep 20 
echo write_experiment5_32kreq_semcache_4 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_semcache_4.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=write --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/write_experiment5_32kreq_semcache_4.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo read_experiment5_32kreq_semcache_4 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/read_experiment5_32kreq_semcache_4.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=read --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/read_experiment5_32kreq_semcache_4.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo randwrite_experiment5_32kreq_semcache_4 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_semcache_4.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randwrite --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randwrite_experiment5_32kreq_semcache_4.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
echo randread_experiment5_32kreq_semcache_4 >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
echo start >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
pcm 1 -csv=/home/jlbez/experiment-5-draco/randread_experiment5_32kreq_semcache_4.pcm.csv -- fio --name=fioccpe --ioengine=sync --iodepth=1 --rw=randread --bs=32k --direct=1 --size=20G --numjobs=1 --runtime=60 --eta=never --output=/home/jlbez/experiment-5-draco/randread_experiment5_32kreq_semcache_4.out
echo end >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt
date >> /home/jlbez/experiment-5-draco/log_testes_experiment5.txt

sleep 20 
