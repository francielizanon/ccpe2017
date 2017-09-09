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

Practically all devices presented lower write performance in the MPSoC than in the PC (performance was up to 1033% higher in the PC for writes and 522% for reads).



