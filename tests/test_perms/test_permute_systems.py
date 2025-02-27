"""Test permute_systems."""
import numpy as np

from toqito.perms import permute_systems


def test_permute_systems_vec():
    """Permute system for perm = [2,1] and vector [1, 2, 3, 4]."""
    test_input_mat = np.array([1, 2, 3, 4])
    expected_res = np.array([1, 3, 2, 4])

    res = permute_systems(test_input_mat, [2, 1])

    bool_mat = np.isclose(res, expected_res)
    np.testing.assert_equal(np.all(bool_mat), True)


def test_permute_systems_m2_m2():
    """Permute system for perm = [2,1] and dim = [2, 2]."""
    test_input_mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

    expected_res = np.array([[1, 3, 2, 4], [9, 11, 10, 12], [5, 7, 6, 8], [13, 15, 14, 16]])

    res = permute_systems(test_input_mat, [2, 1], [2, 2])

    bool_mat = np.isclose(res, expected_res)
    np.testing.assert_equal(np.all(bool_mat), True)


def test_permute_systems_m2_m2_np_array():
    """Permute system for perm = np.array([2,1])."""
    test_input_mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

    expected_res = np.array([[1, 3, 2, 4], [9, 11, 10, 12], [5, 7, 6, 8], [13, 15, 14, 16]])

    res = permute_systems(test_input_mat, np.array([2, 1]))

    bool_mat = np.isclose(res, expected_res)
    np.testing.assert_equal(np.all(bool_mat), True)


def permute_systems_test_2_3_1():
    """Test permute systems for perm = [2,3,1]."""
    test_input_mat = np.array(
        [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15, 16],
            [17, 18, 19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30, 31, 32],
            [33, 34, 35, 36, 37, 38, 39, 40],
            [41, 42, 43, 44, 45, 46, 47, 48],
            [49, 50, 51, 52, 53, 54, 55, 56],
            [57, 58, 59, 60, 61, 62, 63, 64],
        ]
    )

    expected_res = np.array(
        [
            [1, 5, 2, 6, 3, 7, 4, 8],
            [33, 37, 34, 38, 35, 39, 36, 40],
            [9, 13, 10, 14, 11, 15, 12, 16],
            [41, 45, 42, 46, 43, 47, 44, 48],
            [17, 21, 18, 22, 19, 23, 20, 24],
            [49, 53, 50, 54, 51, 55, 52, 56],
            [25, 29, 26, 30, 27, 31, 28, 32],
            [57, 61, 58, 62, 59, 63, 60, 64],
        ]
    )

    res = permute_systems(test_input_mat, [2, 3, 1])

    bool_mat = np.isclose(res, expected_res)
    np.testing.assert_equal(np.all(bool_mat), True)


def test_permute_systems_16_by_16():
    """Permute systems of dimension 16-by-16."""
    rho = np.array(
        [
            [1, 2, 33, 34, 65, 66, 97, 98, 9, 10, 41, 42, 73, 74, 105, 106],
            [17, 18, 49, 50, 81, 82, 113, 114, 25, 26, 57, 58, 89, 90, 121, 122],
            [3, 4, 35, 36, 67, 68, 99, 100, 11, 12, 43, 44, 75, 76, 107, 108],
            [19, 20, 51, 52, 83, 84, 115, 116, 27, 28, 59, 60, 91, 92, 123, 124],
            [5, 6, 37, 38, 69, 70, 101, 102, 13, 14, 45, 46, 77, 78, 109, 110],
            [21, 22, 53, 54, 85, 86, 117, 118, 29, 30, 61, 62, 93, 94, 125, 126],
            [7, 8, 39, 40, 71, 72, 103, 104, 15, 16, 47, 48, 79, 80, 111, 112],
            [23, 24, 55, 56, 87, 88, 119, 120, 31, 32, 63, 64, 95, 96, 127, 128],
            [129, 130, 161, 162, 193, 194, 225, 226, 137, 138, 169, 170, 201, 202, 233, 234],
            [145, 146, 177, 178, 209, 210, 241, 242, 153, 154, 185, 186, 217, 218, 249, 250],
            [131, 132, 163, 164, 195, 196, 227, 228, 139, 140, 171, 172, 203, 204, 235, 236],
            [147, 148, 179, 180, 211, 212, 243, 244, 155, 156, 187, 188, 219, 220, 251, 252],
            [133, 134, 165, 166, 197, 198, 229, 230, 141, 142, 173, 174, 205, 206, 237, 238],
            [149, 150, 181, 182, 213, 214, 245, 246, 157, 158, 189, 190, 221, 222, 253, 254],
            [135, 136, 167, 168, 199, 200, 231, 232, 143, 144, 175, 176, 207, 208, 239, 240],
            [151, 152, 183, 184, 215, 216, 247, 248, 159, 160, 191, 192, 223, 224, 255, 256],
        ]
    )
    perm = [2, 3, 1, 4]
    dim = [[2, 2, 2, 2], [2, 2, 2, 2]]

    res = permute_systems(rho, perm, dim, True, False)
    expected_res = np.array(
        [
            [1, 2, 33, 34, 65, 66, 97, 98, 9, 10, 41, 42, 73, 74, 105, 106],
            [17, 18, 49, 50, 81, 82, 113, 114, 25, 26, 57, 58, 89, 90, 121, 122],
            [129, 130, 161, 162, 193, 194, 225, 226, 137, 138, 169, 170, 201, 202, 233, 234],
            [145, 146, 177, 178, 209, 210, 241, 242, 153, 154, 185, 186, 217, 218, 249, 250],
            [3, 4, 35, 36, 67, 68, 99, 100, 11, 12, 43, 44, 75, 76, 107, 108],
            [19, 20, 51, 52, 83, 84, 115, 116, 27, 28, 59, 60, 91, 92, 123, 124],
            [131, 132, 163, 164, 195, 196, 227, 228, 139, 140, 171, 172, 203, 204, 235, 236],
            [147, 148, 179, 180, 211, 212, 243, 244, 155, 156, 187, 188, 219, 220, 251, 252],
            [5, 6, 37, 38, 69, 70, 101, 102, 13, 14, 45, 46, 77, 78, 109, 110],
            [21, 22, 53, 54, 85, 86, 117, 118, 29, 30, 61, 62, 93, 94, 125, 126],
            [133, 134, 165, 166, 197, 198, 229, 230, 141, 142, 173, 174, 205, 206, 237, 238],
            [149, 150, 181, 182, 213, 214, 245, 246, 157, 158, 189, 190, 221, 222, 253, 254],
            [7, 8, 39, 40, 71, 72, 103, 104, 15, 16, 47, 48, 79, 80, 111, 112],
            [23, 24, 55, 56, 87, 88, 119, 120, 31, 32, 63, 64, 95, 96, 127, 128],
            [135, 136, 167, 168, 199, 200, 231, 232, 143, 144, 175, 176, 207, 208, 239, 240],
            [151, 152, 183, 184, 215, 216, 247, 248, 159, 160, 191, 192, 223, 224, 255, 256],
        ]
    )
    bool_mat = np.isclose(res, expected_res)
    np.testing.assert_equal(np.all(bool_mat), True)

    res = permute_systems(rho, perm, dim, False, True)
    expected_res = np.array(
        [
            [1, 2, 65, 66, 9, 10, 73, 74, 33, 34, 97, 98, 41, 42, 105, 106],
            [17, 18, 81, 82, 25, 26, 89, 90, 49, 50, 113, 114, 57, 58, 121, 122],
            [5, 6, 69, 70, 13, 14, 77, 78, 37, 38, 101, 102, 45, 46, 109, 110],
            [21, 22, 85, 86, 29, 30, 93, 94, 53, 54, 117, 118, 61, 62, 125, 126],
            [129, 130, 193, 194, 137, 138, 201, 202, 161, 162, 225, 226, 169, 170, 233, 234],
            [145, 146, 209, 210, 153, 154, 217, 218, 177, 178, 241, 242, 185, 186, 249, 250],
            [133, 134, 197, 198, 141, 142, 205, 206, 165, 166, 229, 230, 173, 174, 237, 238],
            [149, 150, 213, 214, 157, 158, 221, 222, 181, 182, 245, 246, 189, 190, 253, 254],
            [3, 4, 67, 68, 11, 12, 75, 76, 35, 36, 99, 100, 43, 44, 107, 108],
            [19, 20, 83, 84, 27, 28, 91, 92, 51, 52, 115, 116, 59, 60, 123, 124],
            [7, 8, 71, 72, 15, 16, 79, 80, 39, 40, 103, 104, 47, 48, 111, 112],
            [23, 24, 87, 88, 31, 32, 95, 96, 55, 56, 119, 120, 63, 64, 127, 128],
            [131, 132, 195, 196, 139, 140, 203, 204, 163, 164, 227, 228, 171, 172, 235, 236],
            [147, 148, 211, 212, 155, 156, 219, 220, 179, 180, 243, 244, 187, 188, 251, 252],
            [135, 136, 199, 200, 143, 144, 207, 208, 167, 168, 231, 232, 175, 176, 239, 240],
            [151, 152, 215, 216, 159, 160, 223, 224, 183, 184, 247, 248, 191, 192, 255, 256],
        ]
    )
    bool_mat = np.isclose(res, expected_res)
    np.testing.assert_equal(np.all(bool_mat), True)


def test_permute_systems_invalid_perm_vector():
    """Invalid input for permute systems."""
    with np.testing.assert_raises(ValueError):
        test_input_mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        permute_systems(test_input_mat, [0, 1])


def test_permute_systems_invalid_empty_input():
    """Invalid input for input matrix for permute systems."""
    with np.testing.assert_raises(ValueError):
        test_input_mat = np.array([[]])
        permute_systems(test_input_mat, [2, 1])


def test_permute_systems_invalid_dim_mismatch_perm():
    """Invalid length of permutation must be equal to the length of dimension."""
    with np.testing.assert_raises(ValueError):
        test_input_mat = np.array([1, 2, 3, 4])
        permute_systems(test_input_mat, [2, 1, 3, 4])


if __name__ == "__main__":
    np.testing.run_module_suite()
