import numpy as np

def test_append_2d_array():
    # initialize the input arrays
    X = np.array([[1,2]])
    Y = np.array([[3,4],[5,6]])

    # get the number of rows in Y
    rows_in_Y = Y.shape[0]

    # append X as the last row of Y
    Y = np.vstack([Y, X])

    # get the number of rows in Y after appending X
    new_rows_in_Y = Y.shape[0]
    # check that the number of rows in Y has increased by 1
    assert new_rows_in_Y == rows_in_Y + 1
    # check that the last row in Y is equal to X
    assert np.array_equal(Y[-1], X[0])
    # check that the shape of Y is correct
    assert Y.shape == (rows_in_Y + 1, 2)