# ccpe2017

Source codes and results of the "Energy Efficiency and I/O Performance of Low-Power Architectures"

Authors: Pablo Pavan, Ricardo Lorenzoni, Vinicius Machado, Jean Bez, Edson Padoin, Francieli Boito, Philippe Navaux and Jean-François Méhaut
Regional University of the Northest of Rio Grande do Sul (Brazil)
Federal University of Rio Grande do Sul (Brazil)
Federal University of Santa Catarina (Brazil)
Grenoble Alpes University (France)

## Summary

### Performance Results

The PC and the MPSoC were compared using bandwidth as the performance metric. Write performance was increased by using cache in all situations (up to 1818%). The increases were larger for HDDs than SSDs, and for random write than sequential write experiments. 

Large requests only resulted in higher sequential write performance than small ones in the MPSoC. Nonetheless, large requests resulted in
higher random write performance to most configurations. Increases were of up to 1259%, and were higher for random write than for sequential write. 
Higher read performance was obtained
with large requests than with small requests in sequential read experiments in SSDs and in all random read tests (up to 1279%). 

Higher bandwidth was achieved by sequential write than random write in most tests with
HDDs (up to 1977%). Differences were larger for experiments without cache and when using small requests. Higher bandwidth was achieved by sequential read than random read in all tests with HDDs
and in tests with small requests to SSDs (up to 1759%). 

Practically all devices presented lower write performance in the MPSoC than in the PC (performance was up to 1033% higher in the PC for writes and 522% for reads). Investigation showed that performance in the MPSoC was limited by an issue with its SATA bus.

### Power Demand Results

When busy, the same devices demanded up to 26% more power in the PC than in the MPSoC. Devices of the same type (HDD or SSD) behaved similarly. SSDs demanded less power than
HDDs, but this difference was smaller in the PC (and in the PC SSDs demanded more power than in
the MPSoC). Since the MPSoC environment does not allow the SSDs to perform at their maximum
speed, they also did not reach their peak power consumption.
Considering the power demand of a storage device is approximately 0.5 W, it is clear the
differences seen in the power of the whole system were not due to the device. Despite demanding approximately 3% of the power in the MPSoC and 1.4% in the PC, the storage
device behavior affects other components of the machine. We have shown this difference comes mainly from the CPU power demand.
Despite the fact SSDs demand less power than HDDs in the PC, when
using them the system demands more power. Since SSDs are faster,
they require more work from other components. This does not happen in the MPSoC, where SSDs
have lower performance.

Sequential read demanded more power at the storage device than random read in some
experiments, specially with HDDs (up to 12%). Sequential write demanded more
power at the storage device than random write in HDDs (up to 15%). Looking at the power demand of the whole system during read tests, the results are similar
to what was observed at the storage device. These results also show a similar tendency to performance results. In many situations, higher bandwidth from the device seems to increase power
demanded by the system.
Comparing write experiments, random write demanded more power than sequential write in
situations where higher performance was previously observed for random write (up to 15%).

At the device, large read requests demanded more power than small ones in most experiments (up to 16%). Considering the whole system, results for the MPSoC reflect directly the behavior observed
for the storage device. However, differently from the device behavior, small requests demanded more power than
large ones in most tests in the PC (up to 22%). Since small requests are processed faster, the process stays blocked for
shorter periods, impacting the choices of the DVFS mechanism.

The general behavior observed when looking at the power demand of the storage device is
that reading demanded more power in HDDs (up to 8%) and writing demanded more power
in SSDs (up to 12%). When looking at the power demand of the whole system, the situation is
not always the same as observed for the storage devices. With SSDs, writing demanded more power than reading in some situations where small
requests were issued (up to 18%). The opposite — reading demanding more power than writing — happened
in some experiments with large requests (up to 7%). Our analysis has shown that the differences were not caused by the DVFS mechanism. Analyzing power demands by CPU and
RAM memory, measured with PCM, we have observed the increases are due to CPU activity.

Considering the power demand of the whole system, in the MPSoC power demand was always
increased by using the cache (up to 11%). The same happened in the PC with large requests to
HDD1, SSD1, and SSD2 (up to 6%). Nonetheless, not using the cache demanded more power in the PC with small requests (up to 16%). The difference between these scenarios in the PC where using the cache varied the power
demand is the request size. In the PC, small requests
demanded more power than large ones in most experiments, and this difference happened mostly
in tests without cache. All
experiments with cache presented frequent peaks in power demand, but they did not increase the
mean power enough to surpass the highest power of the tests with small requests without cache.

## Energy Efficiency Results

We have compared all tested configurations using the bytes per Joule energy efficiency metric, calculated dividing each test’s
bandwidth (bytes/s) by its average power demand (Watts). 

Using the cache
led to higher energy efficiency in all experiments with small requests, and with large requests
to HDD1 in the MPSoC and to both HDDs in the PC (up to 1737%). 

Issuing large requests resulted in higher energy efficiency than small ones in all write
experiments without cache, and when using cache in random write experiments: with HDDs, SSD2, and in
the PC with SSD1 (up to 1277%). Issuing large read
requests was more energy-efficient in most situations (up to 1256%). In most cases, these differences were due to higher performance.

Higher energy efficiency was achieved in sequential write than in random write experiments
when using HDDs (up to 1671%), because higher performance was achieved for sequential write to HDDs. Sequential reads obtained higher energy efficiency than random reads with HDDs (up to
2836%) and issuing small requests to SSDs (up to 124%). These differences were caused by higher
performance in the sequential read experiments.

In all write experiments, using SSDs resulted in higher energy efficiency than using HDDs. SSDs provided higher energy efficiency than HDDs in all read experiments (up to 6658%), due to also providing higher performance.

In all experiments SSDs provided higher energy efficiency when used in the PC (up to
196%). This happened because performance is higher when they are used in the PC. Efficiency for read
experiments with HDDs was higher in the MPSoC than in the PC (up to 166%), despite the fact
that in many experiments performance was higher in the PC, because the lower power demand in
the MPSoC compensated the bandwidth difference. 






