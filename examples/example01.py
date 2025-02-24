import numpy as np
import matplotlib.pyplot as plt
from processingnodes.nodes import IIRFilterNode

# use a sampling frequency of 250Hz and a sinusoid of 15Hz
fs = 250
f_sine = 15

# generate the time series data
timestamps = np.arange(fs) / fs
noisy_signal = np.sin(2*np.pi*f_sine*timestamps) + (-1 + 2 * np.random.random(size=timestamps.size))

# create an IIR filter node with a bandpass from 13 to 17 Hz
node = IIRFilterNode(
    in_channel_labels=["Ch1"],
    sfreq=fs,
    order=3,
    btype="bandpass",
    ftype="butter",
    fpass=[13, 17],
    fstop=[10, 20]
)

# apply the filter
filtered_sine, _ = node.process(noisy_signal)

# plot results
fig, axes = plt.subplots(2, 1, sharex="all", figsize=[10,4])

axes[0].plot(timestamps, noisy_signal)
axes[1].plot(timestamps, filtered_sine)

axes[0].set_title("raw signal")
axes[1].set_title("filtered signal")
plt.xlabel("time [s]")
plt.tight_layout()
plt.show()



