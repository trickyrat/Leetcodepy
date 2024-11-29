import pytest
from src.leetcode.all_one import AllOne


class TestAllOne:
    def test_all_one(self):
        all_one = AllOne()
        all_one.inc("hello")
        all_one.inc("hello")
        max_key = all_one.get_max_key()
        min_key = all_one.get_min_key()

        assert max_key == "hello"
        assert min_key == "hello"

        all_one.inc("leet")
        max_key = all_one.get_max_key()
        min_key = all_one.get_min_key()

        assert max_key == "hello"
        assert min_key == "leet"

        all_one.inc("leet")
        all_one.dec("hello")
        max_key = all_one.get_max_key()
        min_key = all_one.get_min_key()

        assert max_key == "leet"
        assert min_key == "hello"

    def test_init(self):
        all_one = AllOne()
        assert all_one.get_max_key() == ""
        assert all_one.get_min_key() == ""

    def test_inc_empty_key(self):
        all_one = AllOne()
        all_one.inc("a")
        assert "a" in all_one.root.next.keys
        assert all_one.get_max_key() == "a"
        assert all_one.get_min_key() == "a"

    def test_inc_existing_key(self):
        all_one = AllOne()
        all_one.inc("a")
        all_one.inc("a")
        assert all_one.get_max_key() == "a"
        assert all_one.get_min_key() == "a"

    def test_dec_to_one(self):
        all_one = AllOne()
        all_one.inc("a")
        all_one.dec("a")
        assert all_one.get_max_key() == ""
        assert all_one.get_min_key() == ""

    def test_dec_below_one(self):
        all_one = AllOne()
        all_one.inc("a")
        all_one.dec("a")
        with pytest.raises(KeyError):
            all_one.dec("a")

    def test_inc_multiple_keys(self):
        all_one = AllOne()
        all_one.inc("a")
        all_one.inc("b")
        all_one.inc("a")
        all_one.inc("c")
        max_key = all_one.get_max_key()
        min_key = all_one.get_min_key()

        assert max_key == "a"
        assert min_key == "b" or min_key == "c"

    def test_dec_multiple_keys(self):
        all_one = AllOne()
        all_one.inc("a")
        all_one.inc("b")
        all_one.inc("a")
        all_one.inc("c")
        all_one.dec("a")
        all_one.dec("b")
        max_key = all_one.get_max_key()
        min_key = all_one.get_min_key()

        assert max_key == "a" or max_key == "b" or max_key == "c"
        assert min_key == "a" or min_key == "b" or min_key == "c"

    def test_remove_node_with_no_keys(self):
        all_one = AllOne()
        all_one.inc("a")
        all_one.inc("b")
        all_one.inc("a")
        all_one.dec("a")
        all_one.dec("a")
        max_key = all_one.get_max_key()
        min_key = all_one.get_min_key()

        assert max_key == "b"
        assert min_key == "b"

    def test_remove_root_node(self):
        all_one = AllOne()
        all_one.inc("a")
        all_one.dec("a")
        assert all_one.root.next is all_one.root
        assert all_one.root.prev is all_one.root
