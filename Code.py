#install pycirclize
import matplotlib.pyplot as plt
from pycirclize import Circos
from pycirclize.utils import load_prokaryote_example_file
from pycirclize.parser import Genbank

# Load Genbank file
gbk_file = ("enterobacteria.gbk")
gbk = Genbank(gbk_file)
# Initialize circos sector by genome size
circos = Circos(sectors={gbk.name: gbk.range_size})
circos.text("Enterobacteria phage\n(NC_000902)", size=15)
sector = circos.sectors[0]
# Outer track
outer_track = sector.add_track((98, 100))
outer_track.axis(fc="lightgrey")
outer_track.xticks_by_interval(5000, label_formatter=lambda v: f"{v / 1000:.0f} Kb")
outer_track.xticks_by_interval(1000, tick_length=1, show_label=False)
# Plot forward & reverse CDS genomic features
cds_track = sector.add_track((90, 95))
cds_track.genomic_features(gbk.extract_features("CDS", 1), plotstyle="arrow", fc="salmon")
cds_track.genomic_features(gbk.extract_features("CDS", -1), plotstyle="arrow", fc="skyblue")

fig = circos.plotfig()


plt.show()
