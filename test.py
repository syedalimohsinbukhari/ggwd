"""Created on Mar 04 10:56:22 2025"""

from pycbc.catalog import Merger

event_name = "GW191103_012549-V1"  # Example event
event = Merger(event_name)

# Manually provide GWOSC data location
strain_H1 = event.strain('H1', sample_rate=4096)
strain_L1 = event.strain('L1', sample_rate=4096)

strain = {'H1': strain_H1, 'L1': strain_L1}
