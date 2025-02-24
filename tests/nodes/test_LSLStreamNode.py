import random, string, time
import numpy as np
import pylsl

from processingnodes.nodes import LSLStreamNode


def test_stream_name():
    """
    Tests whether the published LSL stream is published under the specified stream name.
    """

    stream_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

    node = LSLStreamNode(["Ch1"], stream_name=stream_name)

    available_streams = pylsl.resolve_byprop("name", stream_name, timeout=5.0)

    assert len(available_streams) > 0


def test_correct_data_is_sent():
    """
    Test sending a number of random samples and whether the same data can be received from the created LSL stream.
    """

    stream_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

    node = LSLStreamNode(["Ch1", "Ch2", "Ch3"], stream_name=stream_name)

    inlet = pylsl.StreamInlet(
        pylsl.resolve_byprop("name", stream_name)[0]
    )
    inlet.open_stream()

    time.sleep(0.1)

    data = np.random.normal(size=[1, 3, 1000]).astype(np.float64)

    for i in range(data.shape[-1]):
        node.process(data[..., i:i+1])

    samples_received = []

    while True:

        sample, _ = inlet.pull_sample(timeout=1.0)

        if sample is None:
            break

        samples_received.append(sample)

    data_received = np.array(samples_received).T[np.newaxis, ...]

    assert data_received.shape == data.shape 
    assert np.isclose(data, data_received, rtol=1e-5, atol=1e-5).all()


def test_lsl_settings():
    """
    Test if specified parameters for LSL outlet are stored in settings correctly.
    """

    node = LSLStreamNode(
        ["Ch1", "Ch2", "Ch6"],
        stream_name = "SomeStreamName",
        source_id="SomeSourceID",
        channel_format=pylsl.cf_int8,
        chunk_size=22,
        max_buffered=323
    )

    node.close()
  
    print(node.settings)

    assert type(node.settings) is dict
    assert "stream_name" in node.settings.keys() and node.settings.get("stream_name") == "SomeStreamName"
    assert "source_id" in node.settings.keys() and node.settings.get("source_id") == "SomeSourceID"
    assert "channel_format" in node.settings.keys() and node.settings.get("channel_format") == pylsl.cf_int8
    assert "chunk_size" in node.settings.keys() and node.settings.get("chunk_size") == 22
    assert "max_buffered" in node.settings.keys() and node.settings.get("max_buffered") == 323

def test_correct_labels():
    """
    Test whether specified channel labels are correctly assigned to LSL channels
    """

    channel_labels = [f"Ch{i}" for i in range(10)]

    node = LSLStreamNode(channel_labels)

    node.close()

    # TODO: actually check labels by extracting from stream xml metadata

    assert True
    

    
