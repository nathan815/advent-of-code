from day6.part1 import find_start_of_packet_marker

def test_find_start_of_packet_marker():
    assert find_start_of_packet_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert find_start_of_packet_marker('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert find_start_of_packet_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert find_start_of_packet_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
