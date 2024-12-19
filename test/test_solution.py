from typing import List, Optional
import pytest
from src.data_structures.list_node import ListNode
from src.data_structures.node import Node
from src.data_structures.tree_node import TreeNode
from src.leetcode.solution import Solution
from src.util import Util


class TestSolution:
    @pytest.mark.parametrize(
        "test_input, target, expected",
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([2, 7, 11, 15], 3, []),
        ],
    )
    def test_two_sum(self, test_input: List[int], target: int, expected: List[int]):
        actual = Solution.two_sum(test_input, target)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input1, test_input2, expected",
        [
            (
                Util.generate_list_node([2, 4, 3]),
                Util.generate_list_node([5, 6, 4]),
                "7->0->8",
            ),
            (
                Util.generate_list_node([0]),
                Util.generate_list_node([0]),
                "0",
            ),
            (
                Util.generate_list_node([9, 9, 9, 9, 9, 9, 9]),
                Util.generate_list_node([9, 9, 9, 9]),
                "8->9->9->9->0->0->0->1",
            ),
        ],
    )
    def test_add_two_numbers(
        self,
        test_input1: Optional[ListNode],
        test_input2: Optional[ListNode],
        expected: str,
    ):
        head = Solution.add_two_numbers(test_input1, test_input2)
        actual = Util.list_node_to_string(head)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected", [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0)]
    )
    def test_longest_substring_without_repeat(self, test_input: str, expected: int):
        actual = Solution.longest_substring_without_repeat(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input1, test_input2, expected",
        [
            ([1, 2, 3, 4], [5, 6, 7, 8], 4.5),
            ([1, 3], [2], 2.0),
            ([0, 0], [0, 0], 0.0),
            ([], [1], 1.0),
            ([2], [], 2.0),
        ],
    )
    def test_find_median_sorted_arrays(
        self, test_input1: List[int], test_input2: List[int], expected: float
    ):
        actual = Solution.find_median_sorted_arrays(test_input1, test_input2)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("babad", "bab"),
            ("cbbd", "bb"),
            ("a", "a"),
            ("ac", "a"),
        ],
    )
    def test_longest_palindrome(self, test_input: str, expected: str):
        actual = Solution.longest_palindrome(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, num_rows, expected",
        [
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("A", 1, "A"),
        ],
    )
    def test_z_convert(self, test_input: str, num_rows: int, expected: str):
        actual = Solution.z_convert(test_input, num_rows)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (123, 321),
            (-123, -321),
            (120, 21),
            (100, 1),
            (120, 21),
            (-(2**31), 0),
            (2**31 - 1, 0),
        ],
    )
    def test_reverse_int(self, test_input: int, expected: str):
        actual = Solution.reverse_int(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        "s, expected",
        [("42", 42), ("   -42", -42), ("4193 with words", 4193)],
    )
    def test_my_atoi(self, s: str, expected: int):
        actual = Solution.my_atoi(s)
        assert actual == expected

    @pytest.mark.parametrize(
        "x, expected",
        [(121, True), (-121, False), (10, False)],
    )
    def test_is_palindrome(self, x: int, expected: bool):
        actual = Solution.is_palindrome(x)
        assert actual == expected

    @pytest.mark.parametrize(
        "s, p, expected", [("aa", "a", False), ("aa", "a*", True), ("aa", ".*", True)]
    )
    def test_is_match(self, s: str, p: str, expected: bool):
        actual = Solution.is_match(s, p)
        assert expected == actual

    @pytest.mark.parametrize(
        "height, expected", [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)]
    )
    def test_max_area(self, height: List[int], expected: int):
        actual = Solution.max_area(height)
        assert expected == actual

    @pytest.mark.parametrize(
        "num, expected", [(3, "III"), (58, "LVIII"), (1994, "MCMXCIV")]
    )
    def test_int_to_roman(self, num: int, expected: str):
        actual = Solution.int_to_roman(num)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected", [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]
    )
    def test_roman_to_int(self, s: str, expected: int):
        actual = Solution.roman_to_int(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "strs, expected",
        [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
            (["", ""], ""),
            (None, ""),
        ],
    )
    def test_longest_common_prefix(self, strs: List[str], expected: str):
        actual = Solution.longest_common_prefix(strs)
        assert expected == actual

    @pytest.mark.parametrize(
        "head, n, expected",
        [
            (
                Util.generate_list_node([1, 2, 3, 4, 5]),
                2,
                "1->2->3->5",
            ),
            (Util.generate_list_node([1]), 1, ""),
            (Util.generate_list_node([1, 2]), 1, "1"),
        ],
    )
    def test_remove_nth_from_end(self, head: Optional[ListNode], n: int, expected: str):
        head = Solution.remove_nth_from_end(head, n)
        actual = Util.list_node_to_string(head)
        assert expected == actual

    @pytest.mark.parametrize(
        "list1, list2, expected",
        [
            (
                Util.generate_list_node([1, 2, 4]),
                Util.generate_list_node([1, 3, 4]),
                "1->1->2->3->4->4",
            ),
            (Util.generate_list_node([]), Util.generate_list_node([]), ""),
            (
                Util.generate_list_node([]),
                Util.generate_list_node([0]),
                "0",
            ),
        ],
    )
    def test_merge_two_lists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
        expected: str,
    ):
        head = Solution.merge_two_lists(list1, list2)
        actual = Util.list_node_to_string(head)
        assert expected == actual

    @pytest.mark.parametrize(
        "lists, expected",
        [
            (
                [
                    Util.generate_list_node([1, 4, 5]),
                    Util.generate_list_node([1, 3, 4]),
                    Util.generate_list_node([2, 6]),
                ],
                "1->1->2->3->4->4->5->6",
            ),
            ([], ""),
            ([Util.generate_list_node([])], ""),
        ],
    )
    def test_merge_k_lists(self, lists: List[Optional[ListNode]], expected: str):
        head = Solution.merge_k_lists(lists)
        actual = Util.list_node_to_string(head)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 1, 2], 2),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ],
    )
    def test_remove_duplicates(self, nums: List[int], expected: int):
        actual = Solution.remove_duplicates(nums)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, val, expected",
        [
            ([3, 2, 2, 3], 3, 2),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
        ],
    )
    def test_remove_element(self, nums: List[int], val: int, expected: int):
        actual = Solution.remove_element(nums, val)
        assert expected == actual
        assert val not in nums[0:actual]

    @pytest.mark.parametrize(
        "strs, expected",
        [
            (
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            ),
            ([""], [[""]]),
            (["a"], [["a"]]),
        ],
    )
    def test_group_anagrams(self, strs: List[str], expected: List[List[str]]):
        actual = Solution.group_anagrams(strs)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
        ],
    )
    def test_merge(self, test_input: List[List[int]], expected: List[List[int]]):
        actual = Solution.merge(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (3, 3, "213"),
            (4, 9, "2314"),
            (3, 1, "123"),
        ],
    )
    def test_get_permutation(self, n: int, k: int, expected: str):
        actual = Solution.get_permutation(n, k)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
            (
                [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
                [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            ),
        ],
    )
    def test_set_zeroes(self, test_input: List[List[int]], expected: List[List[int]]):
        Solution.set_zeroes(test_input)
        assert expected == test_input

    @pytest.mark.parametrize(
        "test_input, target, expected",
        [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([1], 0, -1),
        ],
    )
    def test_eval(self, test_input: List[int], target: int, expected: int):
        actual = Solution.search(test_input, target)
        assert expected == actual

    @pytest.mark.parametrize(
        "candidates, target, expected",
        [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            ([2], 1, []),
        ],
    )
    def test_combination_sum(
        self, candidates: List[int], target: int, expected: List[List[int]]
    ):
        actual = Solution.combination_sum(candidates, target)
        actual.sort()
        expected.sort()
        assert expected == actual

    @pytest.mark.parametrize(
        "matrix, target, expected",
        [
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ],
    )
    def test_search_matrix(self, matrix: List[List[int]], target: int, expected: bool):
        actual = Solution.search_matrix(matrix, target)
        assert expected == actual

    @pytest.mark.parametrize(
        "head, left, right, expected",
        [
            (
                Util.generate_list_node([1, 2, 3, 4, 5]),
                2,
                4,
                "1->4->3->2->5",
            ),
            (
                Util.generate_list_node([1, 2, 3, 4, 5]),
                1,
                5,
                "5->4->3->2->1",
            ),
        ],
    )
    def test_reverse_between(
        self, head: ListNode, left: int, right: int, expected: str
    ):
        head = Solution.reverse_between(head, left, right)
        actual = Util.list_node_to_string(head)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (Util.generate_tree_node([3, 9, 20, None, None, 15, 7]), 2),
            (Util.generate_tree_node([2, None, 3, None, 4, None, 5, None, 6]), 5),
        ],
    )
    def test_min_depth(self, test_input: TreeNode, expected: int):
        actual = Solution.min_depth(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, target_num, expected",
        [
            (
                Util.generate_tree_node(
                    [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
                ),
                22,
                [[5, 4, 11, 2], [5, 8, 4, 5]],
            ),
            (Util.generate_tree_node([1, 2, 3]), 5, []),
        ],
    )
    def test_path_sum(
        self, test_input: TreeNode, target_num: int, expected: List[List[int]]
    ):
        actual = Solution.path_sum(test_input, target_num)
        assert actual == expected

    @pytest.mark.parametrize(
        "row_number, expected",
        [
            (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
            (1, [[1]]),
        ],
    )
    def test_generate(self, row_number: int, expected: List[List[int]]):
        actual = Solution.generate(row_number)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, target, expected",
        [([2, 7, 11, 15], 9, [1, 2]), ([2, 3, 4], 6, [1, 3]), ([-1, 0], -1, [1, 2])],
    )
    def test_two_sum_ii(self, test_input: List[int], target: int, expected: List[int]):
        actual = Solution.two_sum_ii(test_input, target)
        assert actual == expected

    @pytest.mark.parametrize(
        "actual, k, expected",
        [
            ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
            ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ],
    )
    def test_rotate_array(self, actual: List[int], k: int, expected: List[int]):
        Solution.rotate(actual, k)
        assert actual == expected

    @pytest.mark.parametrize(
        "k, n, expected",
        [
            (3, 7, [[1, 2, 4]]),
            (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
            (4, 1, []),
        ],
    )
    def test_combination_sum3(self, k: int, n: int, expected: List[List[int]]):
        actual = Solution.combination_sum3(k, n)
        actual.sort()
        expected.sort()
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [("1 + 1", 2), (" 2-1 + 2 ", 3), ("(1+(4+5+2)-3)+(6+8)", 23)],
    )
    def test_calculate(self, test_input: str, expected: int):
        actual = Solution.calculate(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected", [([0], [0]), ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])]
    )
    def test_move_zeroes(self, test_input: List[int], expected: List[int]):
        Solution.move_zeroes(test_input)
        assert test_input == expected

    @pytest.mark.parametrize(
        "test_input, expected", [([1, 3, 4, 2, 2], 2), ([3, 1, 3, 4, 2], 3)]
    )
    def test_find_duplicate(self, test_input: List[int], expected: int):
        actual = Solution.find_duplicate(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "preorder, expected",
        [("9,3,4,#,#,1,#,#,2,#,6,#,#", True), ("1,#", False), ("9,#,#,1", False)],
    )
    def test_find_duplicate(self, preorder: str, expected: bool):
        actual = Solution.is_valid_serialization(preorder)
        assert expected == actual

    @pytest.mark.parametrize("test_input, expected", [(2, 91), (0, 1)])
    def test_count_numbers_with_unique_digits(self, test_input: int, expected: int):
        actual = Solution.count_numbers_with_unique_digits(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected", [([1, 9], 10), ([-1, 9], 8), ([1, 2], 3)]
    )
    def test_get_sum(self, test_input: List[int], expected: int):
        actual = Solution.get_sum(test_input[0], test_input[1])
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [(13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]), (2, [1, 2])],
    )
    def test_lexical_order(self, test_input: int, expected: List[int]):
        actual = Solution.lexical_order(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected", [([197, 130, 1], True), ([235, 140, 4], False)]
    )
    def test_valid_utf8(self, test_input: List[int], expected: bool):
        actual = Solution.valid_utf8(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 3, 2, 6], 26),
            ([100], 0),
        ],
    )
    def test_max_rotate_function(self, nums: list[int], expected: int):
        actual = Solution.max_rotate_function(nums)
        assert expected == actual

    @pytest.mark.parametrize("test_input, expected", [("Hello, my name is John", 5)])
    def test_count_segment(self, test_input: str, expected: int):
        actual = Solution.count_segment(test_input)
        assert expected == actual

    @pytest.mark.parametrize("p, expected", [("a", 1), ("cac", 2), ("zab", 6)])
    def test_find_substring_wraparound_string(self, p: str, expected: int):
        actual = Solution.find_substring_wraparound_string(p)
        assert expected == actual

    @pytest.mark.parametrize(
        "query_ip, expected",
        [
            ("172.16.254.1", "IPv4"),
            ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
            ("256.256.256.256", "Neither"),
        ],
    )
    def test_valid_ip_address(self, query_ip: str, expected: str):
        actual = Solution.valid_ip_address(query_ip)
        assert expected == actual

    @pytest.mark.parametrize(
        "n, expected",
        [
            (6, 3),
            (1, 1),
        ],
    )
    def test_magical_string(self, n: int, expected: int):
        actual = Solution.magical_string(n)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
            ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ],
    )
    def test_find_diagonal_order(
        self, test_input: List[List[int]], expected: List[int]
    ):
        actual = Solution.find_diagonal_order(test_input)
        assert actual == expected

    @pytest.mark.parametrize("test_input, expected", [(100, "202"), (-7, "-10")])
    def test_convert_to_base7(self, test_input: int, expected: int):
        actual = Solution.convert_to_base7(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "amount, coins, expected", [(5, [1, 2, 5], 4), (3, [2], 0), (10, [10], 1)]
    )
    def test_change(self, amount: int, coins: List[int], expected: int):
        actual = Solution.change(amount, coins)
        assert expected == actual

    @pytest.mark.parametrize(
        "a, b, expected", [("aba", "cdc", 3), ("aaa", "bbb", 3), ("aaa", "aaa", -1)]
    )
    def test_find_lus_length(self, a: str, b: str, expected: int):
        actual = Solution.find_lus_length(a, b)
        assert expected == actual

    @pytest.mark.parametrize(
        "input1, input2, expected",
        [("1+1i", "1+1i", "0+2i"), ("1+-1i", "1+-1i", "0+-2i")],
    )
    def test_complex_number_multiply(self, input1: str, input2: str, expected: str):
        actual = Solution.complex_number_multiply(input1, input2)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [([1000, 100, 10, 2], "1000/(100/10/2)")],
    )
    def test_optimal_division(self, test_input: List[int], expected: str):
        actual = Solution.optimal_division(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "candy_type, expected",
        [([1, 1, 2, 2, 3, 3], 3), ([1, 1, 2, 3], 2), ([6, 6, 6, 6], 1)],
    )
    def test_distribute_candies(self, candy_type: List[int], expected: int):
        actual = Solution.distribute_candies(candy_type)
        assert expected == actual

    @pytest.mark.parametrize(
        "root, expected",
        [
            (
                Util.generate_n_tree_node([1, None, 3, 2, 4, None, 5, 6]),
                [1, 3, 5, 6, 2, 4],
            ),
            (
                Util.generate_n_tree_node(
                    [
                        1,
                        None,
                        2,
                        3,
                        4,
                        5,
                        None,
                        None,
                        6,
                        7,
                        None,
                        8,
                        None,
                        9,
                        10,
                        None,
                        None,
                        11,
                        None,
                        12,
                        None,
                        13,
                        None,
                        None,
                        14,
                    ]
                ),
                [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10],
            ),
        ],
    )
    def test_n_preorder(self, root: Node, expected: List[int]):
        actual = Solution.preorder(root)
        assert expected == actual

    @pytest.mark.parametrize(
        "root, expected",
        [
            (
                Util.generate_n_tree_node([1, None, 3, 2, 4, None, 5, 6]),
                [5, 6, 3, 2, 4, 1],
            ),
            (
                Util.generate_n_tree_node(
                    [
                        1,
                        None,
                        2,
                        3,
                        4,
                        5,
                        None,
                        None,
                        6,
                        7,
                        None,
                        8,
                        None,
                        9,
                        10,
                        None,
                        None,
                        11,
                        None,
                        12,
                        None,
                        13,
                        None,
                        None,
                        14,
                    ]
                ),
                [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1],
            ),
        ],
    )
    def test_n_postorder(self, root: Node, expected: List[int]):
        actual = Solution.postorder(root)
        assert expected == actual

    @pytest.mark.parametrize(
        "l1, l2, expected",
        [
            (
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                [
                    "Piatti",
                    "The Grill at Torrey Pines",
                    "Hungry Hunter Steakhouse",
                    "Shogun",
                ],
                ["Shogun"],
            ),
            (
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["KFC", "Shogun", "Burger King"],
                ["Shogun"],
            ),
        ],
    )
    def test_find_restaurant(self, l1: List[str], l2: List[str], expected: List[str]):
        actual = Solution.find_restaurant(l1, l2)
        assert expected == actual

    @pytest.mark.parametrize(
        "root, val, depth, expected",
        [
            (
                Util.generate_tree_node([4, 2, 6, 3, 1, 5]),
                1,
                2,
                Util.generate_tree_node([4, 1, 1, 2, None, None, 6, 3, 1, 5]),
            ),
            (
                Util.generate_tree_node([4, 2, None, 3, 1]),
                1,
                3,
                Util.generate_tree_node([4, 2, None, 1, 1, 3, None, None, 1]),
            ),
        ],
    )
    def test_add_one_row(
        self,
        root: Optional[TreeNode],
        val: int,
        depth: int,
        expected: Optional[TreeNode],
    ):
        actual = Solution.add_one_row(root, val, depth)
        assert Util.level_traverse(actual) == Util.level_traverse(expected)

    @pytest.mark.parametrize(
        "pairs, expected",
        [([[1, 2], [2, 3], [3, 4]], 2), ([[1, 2], [7, 8], [4, 5]], 3)],
    )
    def test_find_longest_chain(self, pairs: List[List[int]], expected: int):
        actual = Solution.find_longest_chain(pairs)
        assert expected == actual

    @pytest.mark.parametrize(
        "root, expected",
        [
            (
                Util.generate_tree_node([1, 2, 3, 4, None, 2, 4, None, None, 4]),
                [Util.generate_tree_node([2, 4]), Util.generate_tree_node([4])],
            ),
            (Util.generate_tree_node([2, 1, 1]), [Util.generate_tree_node([1])]),
            (
                Util.generate_tree_node([2, 2, 2, 3, None, 3, None]),
                [Util.generate_tree_node([3]), Util.generate_tree_node([2, 3])],
            ),
        ],
    )
    def test_find_duplicate_subtrees(
        self, root: Optional[TreeNode], expected: List[Optional[TreeNode]]
    ):
        actual = Solution.find_duplicate_subtrees(root)
        actual_level_traverse = sorted([Util.level_traverse(node) for node in actual])
        expected_level_traverse = sorted([Util.level_traverse(node) for node in expected])
        assert actual_level_traverse == expected_level_traverse

    @pytest.mark.parametrize(
        "root, expected",
        [
            (Util.generate_tree_node([1, 2]), [["", "1", ""], ["2", "", ""]]),
            (
                Util.generate_tree_node([1, 2, 3, None, 4]),
                [
                    ["", "", "", "1", "", "", ""],
                    ["", "2", "", "", "", "3", ""],
                    ["", "", "4", "", "", "", ""],
                ],
            ),
        ],
    )
    def test_print_tree(self, root: Optional[TreeNode], expected: List[List[str]]):
        actual = Solution.print_tree(root)
        assert expected == actual

    @pytest.mark.parametrize(
        "arr, k, x, expected",
        [([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]), ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4])],
    )
    def test_find_closest_elements(
        self, arr: List[int], k: int, x: int, expected: List[int]
    ):
        actual = Solution.find_closest_elements(arr, k, x)
        assert expected == actual

    @pytest.mark.parametrize(
        "root, expected",
        [
            (Util.generate_tree_node([1, 3, 2, 5, 3, None, 9]), 4),
            (Util.generate_tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7]), 7),
            (Util.generate_tree_node([1, 3, 2, 5]), 2),
        ],
    )
    def test_width_of_binary_tree(self, root: Optional[TreeNode], expected: int):
        actual = Solution.width_of_binary_tree(root)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 2, 3], True),
            ([4, 2, 1], False),
        ],
    )
    def test_check_possibility(self, nums: list[int], expected: bool):
        actual = Solution.check_possibility(nums)
        assert expected == actual

    @pytest.mark.parametrize(
        "n, k, expected",
        [(3, 1, [1, 2, 3]), (3, 2, [1, 3, 2])],
    )
    def test_construct_array(self, n: int, k: int, expected: List[int]):
        actual = Solution.construct_array(n, k)
        assert expected == actual

    @pytest.mark.parametrize(
        "root, low, high, expected",
        [
            (
                Util.generate_tree_node([1, 0, 2]),
                1,
                2,
                Util.generate_tree_node([1, None, 2]),
            ),
            (
                Util.generate_tree_node([3, 0, 4, None, 2, None, None, 1]),
                1,
                3,
                Util.generate_tree_node([3, 2, None, 1]),
            ),
        ],
    )
    def test_trim_bst(
        self,
        root: Optional[TreeNode],
        low: int,
        high: int,
        expected: Optional[TreeNode],
    ):
        actual = Solution.trim_bst(root, low, high)
        assert Util.level_traverse(actual) == Util.level_traverse(expected)

    @pytest.mark.parametrize("num, expected", [(2736, 7236), (9973, 9973)])
    def test_maximum_swap(self, num: int, expected: int):
        actual = Solution.maximum_swap(num)
        assert expected == actual

    @pytest.mark.parametrize(
        "n, presses, expected",
        [
            (1, 1, 2),
            (2, 1, 3),
            (3, 1, 4),
        ],
    )
    def test_flip_lights(self, n: int, presses: int, expected: int):
        actual = Solution.flip_lights(n, presses)
        assert expected == actual

    @pytest.mark.parametrize(
        "root, expected",
        [
            (Util.generate_tree_node([5, 4, 5, 1, 1, None, 5]), 2),
            (Util.generate_tree_node([1, 4, 5, 4, 4, None, 5]), 2),
        ],
    )
    def test_longest_univalue_path(self, root: Optional[TreeNode], expected: int):
        actual = Solution.longest_univalue_path(root)
        assert expected == actual

    @pytest.mark.parametrize(
        "left, right, expected",
        [
            (1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
            (47, 85, [48, 55, 66, 77]),
        ],
    )
    def test_self_dividing_number(self, left: int, right: int, expected: List[int]):
        actual = Solution.self_dividing_number(left, right)
        assert expected == actual

    @pytest.mark.parametrize(
        "letters, target, expected",
        [
            (["c", "f", "j"], "a", "c"),
            (["c", "f", "j"], "c", "f"),
            (["c", "f", "j"], "d", "f"),
        ],
    )
    def test_next_greatest_letter(self, letters: List[str], target: str, expected: str):
        actual = Solution.next_greatest_letter(letters, target)
        assert expected == actual

    @pytest.mark.parametrize(
        "target, expected",
        [(2, 3), (3, 2)],
    )
    def test_reach_number(self, target: int, expected: int):
        actual = Solution.reach_number(target)
        assert expected == actual

    @pytest.mark.parametrize(
        "n, mines, expected",
        [(5, [[4, 2]], 2), (1, [[0, 0]], 0)],
    )
    def test_order_of_largest_plus_sign(
        self, n: int, mines: List[List[int]], expected: int
    ):
        actual = Solution.order_of_largest_plus_sign(n, mines)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected",
        [([1, 0, 2], True), ([1, 2, 0], False)],
    )
    def test_is_ideal_permutation(self, nums: List[int], expected: bool):
        actual = Solution.is_ideal_permutation(nums)
        assert expected == actual

    @pytest.mark.parametrize(
        "arr, expected",
        [([4, 3, 2, 1, 0], 1), ([1, 0, 2, 3, 4], 4)],
    )
    def test_max_chunks_to_sorted(self, arr: List[int], expected: int):
        actual = Solution.max_chunks_to_sorted(arr)
        assert expected == actual

    @pytest.mark.parametrize(
        "n, k, expected",
        [(1, 1, 0), (2, 1, 0), (2, 2, 1)],
    )
    def test_kth_grammar(self, n: int, k: int, expected: int):
        actual = Solution.kth_grammar(n, k)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [("a1b2", ["a1b2", "a1B2", "A1b2", "A1B2"]), ("3z4", ["3z4", "3Z4"])],
    )
    def test_letter_case_permutation(self, s: str, expected: List[str]):
        actual = Solution.letter_case_permutation(s)
        actual.sort()
        expected.sort()
        assert expected == actual

    @pytest.mark.parametrize(
        "n, expected",
        [(3, 5), (1, 1)],
    )
    def test_num_tilings(self, n: int, expected: int):
        actual = Solution.num_tilings(n)
        assert expected == actual

    @pytest.mark.parametrize(
        "order, s, expected",
        [("cba", "abcd", "cbad"), ("cbafg", "abcd", "cbad")],
    )
    def test_custom_sort_string(self, order: str, s: str, expected: str):
        actual = Solution.custom_sort_string(order, s)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, words, expected",
        [
            ("abcde", ["a", "bb", "acd", "ace"], 3),
            ("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"], 2),
        ],
    )
    def test_num_matching_subseq(self, s: str, words: List[str], expected: int):
        actual = Solution.num_matching_subseq(s, words)
        assert expected == actual

    @pytest.mark.parametrize(
        "k, expected",
        [(0, 5), (5, 0), (3, 5)],
    )
    def test_preimage_size_fzf(self, k: int, expected: int):
        actual = Solution.preimage_size_fzf(k)
        assert expected == actual

    @pytest.mark.parametrize(
        "poured, query_row, query_glass, expected",
        [(1, 1, 1, 0.00000), (2, 1, 1, 0.50000), (100000009, 33, 17, 1.00000)],
    )
    def test_champagne_tower(
        self, poured: int, query_row: int, query_glass: int, expected: float
    ):
        actual = Solution.champagne_tower(poured, query_row, query_glass)
        assert abs(expected - actual) <= 0.0000001

    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([1, 3, 5, 4], [1, 2, 3, 7], 1),
            ([0, 3, 5, 8, 9], [2, 1, 4, 6, 9], 1),
        ],
    )
    def test_min_swap(self, nums1: List[int], nums2: List[int], expected: int):
        actual = Solution.min_swap(nums1, nums2)
        assert expected == actual

    @pytest.mark.parametrize(
        "words, expected",
        [(["gin", "zen", "gig", "msg"], 2), (["a"], 1)],
    )
    def test_unique_morse_representations(self, words: List[str], expected: int):
        actual = Solution.unique_morse_representations(words)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected",
        [([1, 2, 3, 4, 5, 6, 7, 8], True), ([3, 1], False)],
    )
    def test_split_array_same_average(self, nums: List[int], expected: bool):
        actual = Solution.split_array_same_average(nums)
        assert expected == actual

    @pytest.mark.parametrize(
        "widths, s, expected",
        [
            (
                [
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                ],
                "abcdefghijklmnopqrstuvwxyz",
                [3, 60],
            ),
            (
                [
                    4,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                ],
                "bbbcccdddaaa",
                [2, 4],
            ),
        ],
    )
    def test_number_of_lines(self, widths: List[int], s: str, expected: List[int]):
        actual = Solution.number_of_lines(widths, s)
        assert expected == actual

    @pytest.mark.parametrize(
        "cpdomains, expected",
        [
            (
                ["9001 discuss.leetcode.com"],
                {"9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"},
            ),
            (
                [
                    "900 google.mail.com",
                    "50 yahoo.com",
                    "1 intel.mail.com",
                    "5 wiki.org",
                ],
                {
                    "901 mail.com",
                    "50 yahoo.com",
                    "900 google.mail.com",
                    "5 wiki.org",
                    "5 org",
                    "1 intel.mail.com",
                    "951 com",
                },
            ),
        ],
    )
    def test_subdomain_in_visits(self, cpdomains: List[str], expected: set[str]):
        actual = set(Solution.subdomain_visits(cpdomains))
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("(123)", ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"]),
            (
                "(0123)",
                [
                    "(0, 1.23)",
                    "(0, 12.3)",
                    "(0, 123)",
                    "(0.1, 2.3)",
                    "(0.1, 23)",
                    "(0.12, 3)",
                ],
            ),
            ("(00011)", ["(0, 0.011)", "(0.001, 1)"]),
        ],
    )
    def test_ambiguous_coordinates(self, s: str, expected: List[str]):
        actual = Solution.ambiguous_coordinates(s)
        expected.sort()
        actual.sort()
        assert expected == actual

    @pytest.mark.parametrize(
        "head, nums, expected",
        [
            (Util.generate_list_node([0, 1, 2, 3]), [0, 1, 3], 2),
            (Util.generate_list_node([0, 1, 2, 3, 4]), [0, 3, 1, 4], 2),
        ],
    )
    def test_num_components(
        self, head: Optional[ListNode], nums: List[int], expected: int
    ):
        actual = Solution.num_components(head, nums)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [("ABC", 10), ("ABA", 8), ("LEETCODE", 92)],
    )
    def test_unique_letter_string(self, s: str, expected: int):
        actual = Solution.unique_letter_string(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [("()", 1), ("(())", 2), ("()()", 2)],
    )
    def test_score_of_parentheses(self, s: str, expected: int):
        actual = Solution.score_of_parentheses(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "quality, wage, k, expected",
        [
            ([10, 20, 5], [70, 50, 30], 2, 105.00000),
            ([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3, 30.66667),
        ],
    )
    def test_min_cost_to_hire_worker(
        self, quality: List[int], wage: List[int], k: int, expected: float
    ):
        actual = Solution.min_cost_to_hire_worker(quality, wage, k)
        actual = round(actual, 5)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1], 1, 1),
            ([1, 2], 4, -1),
            ([2, -1, 2], 3, 3),
        ],
    )
    def test_min_shortest_subarray(self, nums: List[int], k: int, expected: int):
        actual = Solution.shortest_subarray(nums, k)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([2, 7, 11, 15], [1, 10, 4, 11], [2, 11, 7, 15]),
            ([12, 24, 8, 32], [13, 25, 32, 11], [24, 32, 8, 12]),
        ],
    )
    def test_advantage_count(
        self, nums1: List[int], nums2: List[int], expected: List[int]
    ):
        actual = Solution.advantage_count(nums1, nums2)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                Util.generate_list_node([1, 2, 3, 4, 5, 6]),
                "4->5->6",
            ),
            (Util.generate_list_node([1, 2, 3, 4, 5]), "3->4->5"),
        ],
    )
    def test_middle_node(self, test_input: ListNode, expected: str):
        head = Solution.middle_node(test_input)
        actual = Util.list_node_to_string(head)
        assert expected == actual

    @pytest.mark.parametrize(
        "people, limit, expected",
        [([1, 2], 3, 1), ([3, 2, 2, 1], 3, 3), ([3, 5, 3, 4], 5, 4)],
    )
    def test_num_rescue_boats(self, people: List[int], limit: int, expected: int):
        actual = Solution.num_rescue_boats(people, limit)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [([[1, 2], [3, 4]], 17), ([[2]], 5), ([[1, 0], [0, 2]], 8)],
    )
    def test_projection_area(self, test_input: List[List[int]], expected: int):
        actual = Solution.projection_area(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
            ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ],
    )
    def test_sorted_squares(self, test_input: List[int], expected: List[int]):
        actual = Solution.sorted_squares(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ([4, 3, 10, 9, 8], [10, 9]),
            ([4, 4, 7, 6, 7], [7, 7, 6]),
            ([6], [6]),
        ],
    )
    def test_min_subsequence(self, test_input: List[int], expected: List[int]):
        actual = Solution.min_subsequence(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("a0b1c2", ["0a1b2c", "a0b1c2", "0a1b2c", "0c2a1b"]),
            ("leetcode", [""]),
            ("1229857369", [""]),
        ],
    )
    def test_reformat(self, test_input: str, expected: List[str]):
        actual = Solution.reformat(test_input)
        assert actual in expected

    @pytest.mark.parametrize(
        "target, n, expected",
        [
            ([1, 3], 3, ["Push", "Push", "Pop", "Push"]),
            ([1, 2, 3], 3, ["Push", "Push", "Push"]),
            ([1, 2], 4, ["Push", "Push"]),
        ],
    )
    def test_build_array(self, target: List[int], n: int, expected: int):
        actual = Solution.build_array(target, n)
        assert actual == expected

    @pytest.mark.parametrize(
        "start_time, end_time, query_time, expected",
        [
            ([1, 2, 3], [3, 2, 7], 4, 1),
            ([4], [4], 4, 1),
        ],
    )
    def test_busy_student(
        self, start_time: List[int], end_time: List[int], query_time: int, expected: int
    ):
        actual = Solution.busy_student(start_time, end_time, query_time)
        assert actual == expected

    @pytest.mark.parametrize(
        "sentence, search_word, expected",
        [
            ("i love eating burger", "burg", 4),
            ("this problem is an easy problem", "pro", 2),
            ("i am tired", "you", -1),
        ],
    )
    def test_is_prefix_of_word(self, sentence: str, search_word: str, expected: int):
        actual = Solution.is_prefix_of_word(sentence, search_word)
        assert actual == expected

    @pytest.mark.parametrize(
        "target, arr, expected",
        [
            ([1, 2, 3, 4], [2, 4, 1, 3], True),
            ([7], [7], True),
            ([3, 7, 9], [3, 7, 11], False),
        ],
    )
    def test_can_be_equal(self, target: List[int], arr: List[int], expected: bool):
        actual = Solution.can_be_equal(target, arr)
        assert actual == expected

    @pytest.mark.parametrize(
        "nums, n, expected",
        [
            ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
            ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
            ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
        ],
    )
    def test_shuffle(self, nums: List[int], n: int, expected: List[int]):
        actual = Solution.shuffle(nums, n)
        assert actual == expected

    @pytest.mark.parametrize(
        "prices, expected",
        [
            ([8, 4, 6, 2, 3], [4, 2, 4, 2, 3]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([10, 1, 1, 6], [9, 0, 1, 6]),
        ],
    )
    def test_final_prices(self, prices: List[int], expected: List[int]):
        actual = Solution.final_prices(prices)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ([3, 5, 1], True),
            ([1, 2, 4], False),
        ],
    )
    def test_can_make_arithmetic_progression(
        self, test_input: List[int], expected: bool
    ):
        actual = Solution.can_make_arithmetic_progression(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        "root, val, expected",
        [
            (
                Util.generate_tree_node([4, 1, 3, None, None, 2]),
                5,
                Util.generate_tree_node([5, 4, None, 1, 3, None, None, 2]),
            ),
            (
                Util.generate_tree_node([5, 2, 4, None, 1]),
                3,
                Util.generate_tree_node([5, 2, 4, None, 1, None, 3]),
            ),
            (
                Util.generate_tree_node([5, 2, 3, None, 1]),
                4,
                Util.generate_tree_node([5, 2, 4, None, 1, 3]),
            ),
        ],
    )
    def test_insert_into_max_tree(
        self, root: Optional[TreeNode], val: int, expected: Optional[TreeNode]
    ):
        actual = Solution.insert_into_max_tree(root, val)
        assert Util.level_traverse(actual) == Util.level_traverse(expected)

    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("&(|(f))", False),
            ("|(f,f,f,t)", True),
            ("!(&(f,t))", True),
        ],
    )
    def test_parse_bool_expr(self, expression: str, expected: bool):
        actual = Solution.parse_bool_expr(expression)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("lee(t(c)o)de)", "lee(t(c)o)de"),
            ("a)b(c)d", "ab(c)d"),
            ("))((", ""),
        ],
    )
    def test_min_remove_to_make_valid(self, test_input: str, expected: str):
        actual = Solution.min_remove_to_make_valid(test_input)
        assert expected == actual

    @pytest.mark.parametrize(
        "mat, expected",
        [
            ([[1, 0, 0], [0, 0, 1], [1, 0, 0]], 1),
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        ],
    )
    def test_num_special(self, mat: List[List[int]], expected: int):
        actual = Solution.num_special(mat)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("  this   is  a sentence ", "this   is   a   sentence"),
            (" practice   makes   perfect", "practice   makes   perfect "),
        ],
    )
    def test_reorder_spaces(self, s: str, expected: str):
        actual = Solution.reorder_spaces(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "logs, expected",
        [
            (["d1/", "d2/", "../", "d21/", "./"], 2),
            (["d1/", "d2/", "./", "d3/", "../", "d31/"], 3),
            (["d1/", "../", "../", "../"], 0),
        ],
    )
    def test_min_operations(self, logs: List[str], expected: int):
        actual = Solution.min_operations(logs)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected", [([3, 5], 2), ([0, 0], -1), ([0, 4, 3, 0, 4], 3)]
    )
    def test_special_array(self, nums: List[int], expected: int):
        actual = Solution.special_array(nums)
        assert expected == actual

    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3], 2.00000),
            ([6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0], 4.00000),
            (
                [
                    6,
                    0,
                    7,
                    0,
                    7,
                    5,
                    7,
                    8,
                    3,
                    4,
                    0,
                    7,
                    8,
                    1,
                    6,
                    8,
                    1,
                    1,
                    2,
                    4,
                    8,
                    1,
                    9,
                    5,
                    4,
                    3,
                    8,
                    5,
                    10,
                    8,
                    6,
                    6,
                    1,
                    0,
                    6,
                    10,
                    8,
                    2,
                    3,
                    4,
                ],
                4.77778,
            ),
        ],
    )
    def test_trim_mean(self, arr: List[int], expected: float):
        actual = Solution.trim_mean(arr)
        assert actual - expected <= 0.00001

    @pytest.mark.parametrize(
        "towers, radius, expected",
        [
            ([[1, 2, 5], [2, 1, 7], [3, 1, 9]], 2, [2, 1]),
            ([[23, 11, 21]], 9, [23, 11]),
            ([[1, 2, 13], [2, 1, 7], [0, 1, 9]], 2, [1, 2]),
        ],
    )
    def test_best_coordinate(
        self, towers: List[List[int]], radius: int, expected: List[int]
    ):
        actual = Solution.best_coordinate(towers, radius)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aa", 0),
            ("abca", 2),
            ("cbzxy", -1),
        ],
    )
    def test_max_length_between_equal_characters(self, s: str, expected: int):
        actual = Solution.max_length_between_equal_characters(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 1, 2, 2, 2, 3], [3, 1, 1, 2, 2, 2]),
            ([2, 3, 1, 3, 2], [1, 3, 3, 2, 2]),
            ([-1, 1, -6, 4, 5, -6, 1, 4, 1], [5, -1, 4, 4, -6, -6, 1, 1, 1]),
        ],
    )
    def test_frequency_sort(self, nums: List[int], expected: List[int]):
        actual = Solution.frequency_sort(nums)
        assert expected == actual

    @pytest.mark.parametrize(
        "word1, word2, expected",
        [
            (["ab", "c"], ["a", "bc"], True),
            (["a", "cb"], ["ab", "c"], False),
            (["abc", "d", "defg"], ["abcddefg"], True),
        ],
    )
    def test_array_strings_are_equal(
        self, word1: List[str], word2: List[str], expected: bool
    ):
        actual = Solution.array_strings_are_equal(word1, word2)
        assert expected == actual

    @pytest.mark.parametrize(
        "sequence, word, expected",
        [
            ("ababc", "ab", 2),
            ("ababc", "ba", 1),
            ("ababc", "ac", 0),
        ],
    )
    def test_max_repeating(self, sequence: str, word: str, expected: int):
        actual = Solution.max_repeating(sequence, word)
        assert expected == actual

    @pytest.mark.parametrize(
        "command, expected",
        [
            ("G()(al)", "Goal"),
            ("G()()()()(al)", "Gooooal"),
            ("(al)G(al)()()G", "alGalooG"),
        ],
    )
    def test_interpret(self, command: str, expected: str):
        actual = Solution.interpret(command)
        assert expected == actual

    @pytest.mark.parametrize(
        "allowed, words, expected",
        [
            ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
            ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
            ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4),
        ],
    )
    def test_count_consistent_strings(
        self, allowed: str, words: List[str], expected: int
    ):
        actual = Solution.count_consistent_strings(allowed, words)
        assert expected == actual

    @pytest.mark.parametrize(
        "number, expected",
        [
            ("1-23-45 6", "123-456"),
            ("123 4-567", "123-45-67"),
            ("123 4-5678", "123-456-78"),
        ],
    )
    def test_reformat_number(self, number: str, expected: str):
        actual = Solution.reformat_number(number)
        assert expected == actual

    @pytest.mark.parametrize(
        "students, sandwiches, expected",
        [
            ([1, 1, 0, 0], [0, 1, 0, 1], 0),
            ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3),
        ],
    )
    def test_count_students(
        self, students: List[int], sandwiches: List[int], expected: int
    ):
        actual = Solution.count_students(students, sandwiches)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("book", True),
            ("textbook", False),
        ],
    )
    def test_halves_are_alike(self, s: str, expected: bool):
        actual = Solution.halves_are_alike(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "box_types, truck_size, expected",
        [
            ([[1, 3], [2, 2], [3, 1]], 4, 8),
            ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91),
        ],
    )
    def test_maximum_units(
        self, box_types: List[List[int]], truck_size: int, expected: int
    ):
        actual = Solution.maximum_units(box_types, truck_size)
        assert expected == actual

    @pytest.mark.parametrize(
        "gain, expected",
        [
            ([-5, 1, 5, 0, -7], 1),
            ([-4, -3, -2, -1, 4, 3, 2], 0),
        ],
    )
    def test_largest_altitude(self, gain: List[int], expected: int):
        actual = Solution.largest_altitude(gain)
        assert expected == actual

    @pytest.mark.parametrize(
        "low_limit, high_limit, expected",
        [
            (1, 10, 2),
            (5, 15, 2),
            (19, 28, 2),
        ],
    )
    def test_count_balls(self, low_limit: int, high_limit: int, expected: int):
        actual = Solution.count_balls(low_limit, high_limit)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("ca", 2),
            ("cabaabac", 0),
            ("aabccabba", 3),
        ],
    )
    def test_minimum_length(self, s: str, expected: int):
        actual = Solution.minimum_length(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "word1, word2, expected",
        [
            ("abc", "pqr", "apbqcr"),
            ("ab", "pqrs", "apbqrs"),
            ("abcd", "pq", "apbqcd"),
        ],
    )
    def test_merge_alternately(self, word1: str, word2: str, expected: str):
        actual = Solution.merge_alternately(word1, word2)
        assert expected == actual

    @pytest.mark.parametrize(
        "items, rule_key, rule_value, expected",
        [
            (
                [
                    ["phone", "blue", "pixel"],
                    ["computer", "silver", "lenovo"],
                    ["phone", "gold", "iphone"],
                ],
                "color",
                "silver",
                1,
            ),
            (
                [
                    ["phone", "blue", "pixel"],
                    ["computer", "silver", "phone"],
                    ["phone", "gold", "iphone"],
                ],
                "type",
                "phone",
                2,
            ),
        ],
    )
    def test_count_matches(
        self, items: List[List[str]], rule_key: str, rule_value: str, expected: int
    ):
        actual = Solution.count_matches(items, rule_key, rule_value)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("1001", False),
            ("110", True),
        ],
    )
    def test_check_ones_segment(self, s: str, expected: bool):
        actual = Solution.check_ones_segment(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "s1, s2, expected",
        [
            ("bank", "kanb", True),
            ("attack", "defend", False),
            ("kelb", "kelb", True),
        ],
    )
    def test_are_almost_equal(self, s1: str, s2: str, expected: bool):
        actual = Solution.are_almost_equal(s1, s2)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([10, 20, 30, 5, 10, 50], 65),
            ([10, 20, 30, 40, 50], 150),
            ([12, 17, 15, 13, 10, 11, 12], 33),
        ],
    )
    def test_max_ascending_sum(self, nums: List[int], expected: int):
        actual = Solution.max_ascending_sum(nums)
        assert expected == actual

    @pytest.mark.parametrize(
        "n, index, max_sum, expected",
        [
            (4, 2, 6, 2),
            (6, 1, 10, 3),
        ],
    )
    def test_max_value(self, n: int, index: int, max_sum: int, expected: int):
        actual = Solution.max_value(n, index, max_sum)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([-1, -2, -3, -4, 3, 2, 1], 1),
            ([1, 5, 0, 2, -3], 0),
            ([-1, 1, -1, 1, -1], -1),
        ],
    )
    def test_array_sign(self, nums: List[int], expected: int):
        actual = Solution.array_sign(nums)
        assert expected == actual

    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (5, 2, 3),
            (6, 5, 1),
        ],
    )
    def test_find_the_winner(self, n: int, k: int, expected: int):
        actual = Solution.find_the_winner(n, k)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ([2, 3, -1, 8, 4], 3),
            ([1, -1, 4], 2),
            ([2, 5], -1),
        ],
    )
    def test_pivot_index(self, test_input: List[int], expected: int):
        actual = Solution.pivot_index(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        "next_visit, expected",
        [
            ([0, 0], 2),
            ([0, 0, 2], 6),
            ([0, 1, 2, 0], 6),
        ],
    )
    def test_first_daya_been_in_all_rooms(self, next_visit: List[int], expected: int):
        actual = Solution.first_daya_been_in_all_rooms(next_visit)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, k, expected",
        [
            ([1, 2, 2, 1], 1, 4),
            ([1, 3], 3, 0),
            ([3, 2, 1, 5, 4], 2, 3),
        ],
    )
    def test_count_k_difference(self, test_input: List[int], k: int, expected: int):
        actual = Solution.count_k_difference(test_input, k)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ([7, 1, 5, 4], 4),
            ([9, 4, 3, 2], -1),
            ([1, 5, 2, 10], 9),
        ],
    )
    def test_maximum_difference(self, test_input: List[int], expected: int):
        actual = Solution.maximum_difference(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        "n, dislikes, expected",
        [
            (4, [[1, 2], [1, 3], [2, 4]], True),
            (3, [[1, 2], [1, 3], [2, 3]], False),
            (5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], False),
        ],
    )
    def test_possible_bipartition(
        self, n: int, dislikes: List[List[int]], expected: bool
    ):
        actual = Solution.possible_bipartition(n, dislikes)
        assert actual == expected

    @pytest.mark.parametrize(
        "fruits, expected",
        [
            ([1, 2, 1], 3),
            ([0, 1, 2, 2], 3),
            ([1, 2, 3, 2, 2], 4),
        ],
    )
    def test_total_fruit(self, fruits: List[int], expected: int):
        actual = Solution.total_fruit(fruits)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ([3, 1, 4, 2], [2, 4, 1, 3]),
            ([0], [0]),
        ],
    )
    def test_sort_array_by_parity(self, test_input: List[int], expected: List[int]):
        actual = Solution.sort_array_by_parity(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([3, 1, 2, 4], 17),
            ([11, 81, 94, 43, 3], 444),
        ],
    )
    def test_sum_subarray_mins(self, arr: List[int], expected: int):
        actual = Solution.sum_subarray_mins(arr)
        assert actual == expected

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([5, 0, 3, 8, 6], 3),
            ([1, 1, 1, 0, 6, 12], 4),
        ],
    )
    def test_partition_disjoint(self, nums: List[int], expected: int):
        actual = Solution.partition_disjoint(nums)
        assert actual == expected

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("())", 1),
            ("(((", 3),
        ],
    )
    def test_min_add_to_make_valid(self, s: str, expected: int):
        actual = Solution.min_add_to_make_valid(s)
        assert actual == expected

    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1, 0, 1, 0, 1], [0, 3]),
            ([1, 1, 0, 1, 1], [-1, -1]),
            ([1, 1, 0, 0, 1], [0, 2]),
        ],
    )
    def test_min_three_equal_parts(self, arr: List[int], expected: List[int]):
        actual = Solution.three_equal_parts(arr)
        assert actual == expected

    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 1], [1, 0]], 1),
            ([[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2),
            (
                [
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                ],
                1,
            ),
        ],
    )
    def test_shortest_bridge(self, grid: List[List[int]], expected: int):
        actual = Solution.shortest_bridge(grid)
        assert actual == expected

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abc", 7),
            ("aba", 6),
            ("aaa", 3),
        ],
    )
    def test_distinct_subseq_ii(self, s: str, expected: int):
        actual = Solution.distinct_subseq_ii(s)
        assert actual == expected

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("IDID", [0, 4, 1, 3, 2]),
            ("III", [0, 1, 2, 3]),
            ("DDI", [3, 2, 0, 1]),
        ],
    )
    def test_di_string_match(self, s: str, expected: List[int]):
        actual = Solution.di_string_match(s)
        assert actual == expected

    @pytest.mark.parametrize(
        "strs, expected",
        [
            (["cba", "daf", "ghi"], 1),
            (["a", "b"], 0),
            (["zyx", "wvu", "tsr"], 3),
        ],
    )
    def test_min_deletion_size(self, strs: List[str], expected: int):
        actual = Solution.min_deletion_size(strs)
        assert actual == expected

    @pytest.mark.parametrize(
        "pushed, popped, expected",
        [
            ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
            ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
        ],
    )
    def test_validate_stack_sequences(
        self, pushed: List[int], popped: List[int], expected: bool
    ):
        actual = Solution.validate_stack_sequences(pushed, popped)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 3], 3),
            ([2, 1, 2, 5, 3, 2], 2),
            ([5, 1, 5, 2, 5, 3, 5, 4], 5),
        ],
    )
    def test_repeated_n_times(self, nums: List[int], expected: int):
        actual = Solution.repeated_n_times(nums)
        assert actual == expected

    @pytest.mark.parametrize(
        "operations, expected",
        [
            (["--X", "X++", "X++"], 1),
            (["++X", "++X", "X++"], 3),
            (["X++", "++X", "--X", "X--"], 0),
        ],
    )
    def test_final_value_after_operations(self, operations: List[str], expected: int):
        actual = Solution.final_value_after_operations(operations)
        assert actual == expected

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("XXX", 1),
            ("XXOX", 2),
            ("OOOO", 0),
        ],
    )
    def test_minimum_moves(self, s: str, expected: int):
        actual = Solution.minimum_moves(s)
        assert actual == expected

    @pytest.mark.parametrize(
        "nums1, nums2, nums3, expected",
        [
            ([1, 1, 3, 2], [2, 3], [3], [3, 2]),
            ([3, 1], [2, 3], [1, 2], [2, 3, 1]),
            ([1, 2, 2], [4, 3, 3], [5], []),
        ],
    )
    def test_two_out_of_three(
        self, nums1: List[int], nums2: List[int], nums3: List[int], expected: List[int]
    ):
        actual = Solution.two_out_of_three(nums1, nums2, nums3)
        actual.sort()
        expected.sort()
        assert expected == actual

    @pytest.mark.parametrize(
        "seats, students, expected",
        [
            ([3, 1, 5], [2, 7, 4], 4),
            ([4, 1, 5, 9], [1, 3, 2, 6], 7),
            ([2, 2, 6, 6], [1, 3, 2, 6], 4),
        ],
    )
    def test_min_moves_to_seat(
        self, seats: List[int], students: List[int], expected: int
    ):
        actual = Solution.min_moves_to_seat(seats, students)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("1 box has 3 blue 4 red 6 green and 12 yellow marbles", True),
            ("hello world 5 x 5", False),
            (
                "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s",
                False,
            ),
        ],
    )
    def test_are_number_ascending(self, s: str, expected: bool):
        actual = Solution.are_number_ascending(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ([3, 1], 2),
            ([2, 2, 2], 7),
            ([3, 2, 1, 5], 6),
        ],
    )
    def test_count_max_or_subsets(self, test_input: List[int], expected: int):
        actual = Solution.count_max_or_subsets(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        "test_input, queries, expected",
        [
            ("**|**|***|", [[2, 5], [5, 9]], [2, 3]),
            (
                "***|**|*****|**||**|*",
                [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]],
                [9, 0, 0, 0, 0],
            ),
        ],
    )
    def test_plates_between_candles(
        self, test_input: str, queries: List[List[int]], expected: List[int]
    ):
        actual = Solution.plates_between_candles(test_input, queries)
        assert actual == expected

    @pytest.mark.parametrize(
        "num, expected",
        [
            (4, 2),
            (30, 14),
        ],
    )
    def test_count_even(self, num: int, expected: int):
        actual = Solution.count_even(num)
        assert expected == actual

    @pytest.mark.parametrize(
        "words, pref, expected",
        [
            (["pay", "attention", "practice", "attend"], "at", 2),
            (["leetcode", "win", "loops", "success"], "code", 0),
        ],
    )
    def test_prefix_count(self, words: List[str], pref: str, expected: int):
        actual = Solution.prefix_count(words, pref)
        assert expected == actual

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abccbaacz", "c"),
            ("abcdd", "d"),
            ("aa", "a"),
            ("zz", "z"),
        ],
    )
    def test_repeated_character(self, s: str, expected: str):
        actual = Solution.repeated_character(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "ranges, expected",
        [
            ([[6, 10], [5, 15]], 2),
            ([[1, 3], [10, 20], [2, 5], [4, 8]], 4),
        ],
    )
    def test_count_ways(self, ranges: List[List[int]], expected: int):
        actual = Solution.count_ways(ranges)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, divisors, expected",
        [
            ([4, 7, 9, 3, 9], [5, 2, 3], 3),
            ([20, 14, 21, 10], [5, 7, 5], 5),
            ([12], [10, 16], 10),
        ],
    )
    def test_max_div_score(self, nums: List[int], divisors: List[int], expected: int):
        actual = Solution.max_div_score(nums, divisors)
        assert expected == actual

    @pytest.mark.parametrize(
        "num, t, expected",
        [
            (4, 1, 6),
            (3, 2, 7),
        ],
    )
    def test_the_maximum_achievable_x(self, num: int, t: int, expected: int):
        actual = Solution.the_maximum_achievable_x(num, t)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([8, 6, 1, 5, 3], 9),
            ([5, 4, 8, 7, 10, 2], 13),
            ([6, 5, 4, 3, 4, 5], -1),
        ],
    )
    def test_count_ways(self, nums: List[int], expected: int):
        actual = Solution.minimum_sum(nums)
        assert expected == actual

    @pytest.mark.parametrize("s, expected", [("101", 1), ("100", 2), ("0111", 0)])
    def test_minimum_steps(self, s: str, expected: int):
        actual = Solution.minimum_steps(s)
        assert expected == actual

    @pytest.mark.parametrize(
        "coins, target, expected",
        [
            ([1, 4, 10], 19, 2),
            ([1, 4, 10, 5, 7, 19], 19, 1),
            (
                [1, 1, 1],
                20,
                3,
            ),
        ],
    )
    def test_minimum_added_coins(self, coins: List[int], target: int, expected: int):
        actual = Solution.minimum_added_coins(coins, target)
        assert expected == actual

    @pytest.mark.parametrize(
        "nums, k, multiplier, expected",
        [
            ([2, 1, 3, 5, 6], 5, 2, [8, 4, 6, 5, 6]),
            ([1, 2], 3, 4, [16, 8]),
        ],
    )
    def test_get_final_state(self, nums: List[int], k: int, multiplier: int, expected: List[int]):
        actual = Solution.get_final_state(nums, k, multiplier)
        assert expected == actual
