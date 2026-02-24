from mytools.resources.argparser import parse_args
import sys
import random
import math


def generate_confetti_svg(
    size_x, size_y, count, min_stroke, max_stroke, filename="confetti.svg", background=None
):
    colors = ["#ff0000", "#7c9635", "#834c85", "#549ca5"]

    svg = []
    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{size_x}" height="{size_y}" '
        f'viewBox="0 0 {size_x} {size_y}">'
    )
    if background:
        svg.append(f'<rect width="100%" height="100%" "{background}"/>')

    for _ in range(count):
        # start point
        x1 = random.random() * size_x
        y1 = random.random() * size_y

        # direction & length
        length = random.uniform(5, 10)
        angle = random.random() * 2 * math.pi

        # end point
        x2 = x1 + length * math.cos(angle)
        y2 = y1 + length * math.sin(angle)

        # midpoint
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2

        # slight perpendicular bend (NOT too round)
        bend = random.uniform(-4, 4)
        cx = mx + bend * math.cos(angle + math.pi / 2)
        cy = my + bend * math.sin(angle + math.pi / 2)

        stroke_width = random.uniform(min_stroke, max_stroke)
        color = random.choice(colors)

        svg.append(
            f'<path d="M {x1:.2f} {y1:.2f} '
            f'Q {cx:.2f} {cy:.2f} {x2:.2f} {y2:.2f}" '
            f'stroke="{color}" stroke-width="{stroke_width:.2f}" '
            f'fill="none" stroke-linecap="round" />'
        )

    svg.append("</svg>")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))


def main():
    args, opts = parse_args()

    if opts.get("help") or "h" in opts:
        print(
            """usage: konfetti.py size count [Options]
              Options:
              --min_stroke <minimal confetti line width>
              --max_stroke <maximal confetti line width>
              --background <background color> (default: transparent)
              --out filename (default: confetti-<size>x<size>-<count>.svg)]"""
        )

        return 0

    assert len(args) == 3, "Size and count are required arguments"

    try:
        size_x, size_y, count = map(int, args[:3])

        min_stroke = int(opts["min_stroke"]) if "min_stroke" in opts else 4
        max_stroke = int(opts["max_stroke"]) if "max_stroke" in opts else 8

    except ValueError:
        print("Invalid argument type")
        return 1

    #assert size > 0 and count > 0, "Size and count must be positive integers"
    assert max_stroke >= min_stroke > 0, "Stroke widths must be positive and max >= min"

    filename = opts.get("out") or f"confetti-{size_x}x{size_y}-{count}.svg"
    background = opts.get("background") or None

    generate_confetti_svg(size_x, size_y, count, min_stroke, max_stroke, filename, background)


if __name__ == "__main__":
    sys.exit(main())
