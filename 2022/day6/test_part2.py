from day6.part2 import find_start_of_unique_message_marker

def test_find_start_of_unique_message_marker():
    assert find_start_of_unique_message_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
    assert find_start_of_unique_message_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
    assert find_start_of_unique_message_marker('nppdvjthqldpwncqszvftbrmjlhg') == 23
    assert find_start_of_unique_message_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
    assert find_start_of_unique_message_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26
