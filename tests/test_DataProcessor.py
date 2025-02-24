import numpy as np

from processingnodes import DataProcessor


def test_process_returns_data_unchanged():
    """
    The base class "DataProcessor" should not modify data at all when calling .process.
    """

    dp = DataProcessor([])

    in_data = np.random.normal(size=[10, 10, 1000])
    in_timestamps = np.arange(1000)

    out_data, out_timestamps = dp.process(in_data, in_timestamps)

    assert type(out_data) is np.ndarray
    assert type(out_timestamps) is np.ndarray

    assert np.isclose(a=in_data, b=out_data, rtol=1e-4, atol=1e-5).all()
    assert np.isclose(a=in_timestamps, b=out_timestamps, rtol=1e-4, atol=1e-5).all()

