import numpy as np
from processingnodes.nodes import ReductionNode

def test_sum_reduction():
    """
    Tests reducing a serial of integers using the numpy.sum function.
    """

    data = np.array([1, 3, 5, 7, 9])[np.newaxis, np.newaxis, ...]

    node = ReductionNode(
        ["Ch1"],
        functions = [
            {
                "module": "numpy",
                "name": "sum",
                "args": {
                    "axis": -1,
                    "keepdims": True
                }
            }
        ] 
    )

    data_out, _ = node.process(data)

    assert type(data_out) is np.ndarray
    assert data_out.shape == (1, 1, 1)
    assert data_out.flatten().item() == 25
