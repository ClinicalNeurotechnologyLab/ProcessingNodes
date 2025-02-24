import numpy as np
from processingnodes.nodes import BurgSpectrumNode

def test_settings():

    ...


def test_output_dimensions():
    """
    Output shape should depend on input dimensions and number of bins.
    """

    fs = 100

    node = BurgSpectrumNode(["Ch1", "Ch2"], sfreq=fs, center_freq=10.0, nbins=5)

    data = np.random.normal(size=[1, 2, 100]).astype(np.float32)

    out_data, _ = node.process(data)

    assert out_data.shape == (1, 2, 5)
