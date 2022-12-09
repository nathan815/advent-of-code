from day6.part1 import find_start_of_packet_market

def test_find_start_of_packet_market():
    assert find_start_of_packet_market('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert find_start_of_packet_market('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert find_start_of_packet_market('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert find_start_of_packet_market('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
