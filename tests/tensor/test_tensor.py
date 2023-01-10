import flamb
from flamb import Tensor
from copy import deepcopy

l_ref = [[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]]


def test_shape():
    global l_ref
    l = deepcopy(l_ref)
    l = Tensor(l)
    assert l.shape == (2, 2, 4), f"Shape is {l.shape} but should be (2,2,4)"


def test_read_value():
    global l_ref
    l = deepcopy(l_ref)
    l = Tensor(l)
    assert l[1][1][2] == 15, f"l[1][1][2] should be 15, but it is {l[1][1][2]}"

    assert l[(1, 1, 2)] == 15, f"l[(1,1,2)] should be 15, but it is {l[(1,1,2)]}"


def test_modify_value():
    global l_ref
    l = deepcopy(l_ref)
    l = Tensor(l)
    l[(0, 1, 2)] = 50
    assert (
        l[(0, 1, 2)] == 50
    ), f"l[0][1][2] should be have been modified to 50, but it is {l[0][1][2]}"

    l = deepcopy(l_ref)
    l = Tensor(l)
    l[0][1][2] = 50
    # assert (l[0][1][2] == 50), f"l[0][1][2] should be have been modified to 50, but it is {l[0][1][2]}"


def test_loop_on_indicies():
    shape = (2, 2)
    l = [deepcopy(index) for index in Tensor._loop_on_indicies(shape)]

    assert l == [[0, 0], [0, 1], [1, 0], [1, 1]], "The loop on indicies does not work"

    shape = (2, 2, 2)
    l = [deepcopy(index) for index in Tensor._loop_on_indicies(shape)]
    # I don't know why we need deepcopy but if we don't use it, all the elements of the list are similar

    assert l == [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1],
    ], "The loop on indicies does not work"


def test_sum():
    global l_ref
    l = deepcopy(l_ref)
    l = Tensor(l)
    l2 = l + l
    assert (
        l2[(0, 1, 2)] == l[(0, 1, 2)] * 2
    ), f"l[(0,1,2)] should be have been equal to {l[(0,1,2)]*2}, but it is {l2[(0,1,2)]}"


if __name__ == "__main__":
    test_shape()
    test_read_value()
    test_modify_value()
    test_loop_on_indicies()
    test_sum()
