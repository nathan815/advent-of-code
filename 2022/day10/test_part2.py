from pathlib import Path
from day10.part2 import run, CRT

def test_run_with_sample():
    expected = '''
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
'''.strip()
    assert run(Path(__file__).parent / 'sample_input.txt') == expected


class TestCRT:
    def test_draw_no_move_sprite(self):
        crt = CRT()
        # Sprite: ###....
        crt.draw(1)
        crt.draw(1)
        crt.draw(1)
        assert crt.render()[0] == '###' + ('.' * 37)
        assert crt.render()[1:] == ['.' * 40] * 5

    def test_draw_moving_sprite(self):
        crt = CRT()

        # Sprite: ###....
        # CRT:    x.......
        crt.draw(1)
        # CRT:    .x......
        crt.draw(1)

        # Sprite: ...###....
        # CRT:    ..x.....
        crt.draw(5)

        # Sprite: ###....
        # CRT:    ...x.....
        crt.draw(0)

        # Sprite: ...###....
        # CRT:    ....x....
        crt.draw(5)
        # CRT:    .....x....
        crt.draw(5)

        assert crt.render()[0] == '##..##' + ('.' * 34)
        assert crt.render()[1:] == ['.' * 40] * 5

    def test_draw_multi_lines(self):
        crt  = CRT()

        for i in range(0, 60):
            crt.draw(i % crt.width) # moving sprite every time so every pixel we draw is within sprite
        
        assert crt.render()[0] == '#' * 40
        assert crt.render()[1] == ('#' * 20) + ('.' * 20)
        assert crt.render()[2:] == ['.' * 40] * 4
