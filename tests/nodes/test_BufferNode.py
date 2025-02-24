import numpy as np
from processingnodes.nodes import BufferNode


def test_returns_correct_datatype():

    buffer_len = 10
    node = BufferNode(["Ch1"], buffer_len, 1)

    test_data = np.random.normal(size=[1, 1, 100]).astype(np.float16)

    out_data, _ = node.process(test_data)

    assert type(out_data) is np.ndarray
    assert out_data.dtype == np.float16



