#!/usr/bin/python2

"""
--- Day 3: No Matter How You Slice It ---

The Elves managed to locate the chimney-squeeze prototype fabric for Santa's
suit (thanks to someone who helpfully wrote its box IDs on the wall of the
warehouse in the middle of the night). Unfortunately, anomalies are still
affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least
1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's
suit. All claims have an ID and consist of a single rectangle with edges
parallel to the edges of the fabric. Each claim's rectangle is defined as
follows:

- The number of inches between the left edge of the fabric and the left edge of
  the rectangle.
- The number of inches between the top edge of the fabric and the top edge of
  the rectangle.
- The width of the rectangle in inches.
- The height of the rectangle in inches.

A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3
inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4
inches tall. Visually, it claims the square inches of fabric represented by #
(and ignores the square inches of fabric represented by .) in the diagram
below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........

The problem is that many of the claims overlap, causing two or more claims to
cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2

Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........

The four square inches marked with X are claimed by both 1 and 2. (Claim 3,
while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough
fabric. How many square inches of fabric are within two or more claims?

--- Part Two ---

Amidst the chaos, you notice that exactly one claim doesn't overlap by even a
single square inch of fabric with any other claim. If you can somehow draw
attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are
made.

What is the ID of the only claim that doesn't overlap?
"""


import sys


def get_data(name):
    f = open(name, 'r')

    return f.readlines()


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)

    data = map(str.rstrip, get_data(sys.argv[1]))

    claims = []
    area = 0
    points = {}

    for line in data:
        overlaps = False
        id, rest = line.split(' @ ')
        id = int(id[1:])
        x_y, size = rest.split(': ')
        x1, y1 = map(int, x_y.split(','))
        width, height = map(int, size.split('x'))
        x2, y2 = x1 + width, y1 + height

        for c in claims:
            if x1 < c['x2'] and x2 > c['x1'] and y1 < c['y2'] and y2 > c['y1']:
                overlaps = True
                c['overlaps'] = True

                o_x1, o_y1 = max(x1, c['x1']), max(y1, c['y1'])
                o_x2, o_y2 = min(x2, c['x2']), min(y2, c['y2'])

                for i in range(o_x1, o_x2):
                    for j in range(o_y1, o_y2):
                        point = "%d;%d" % (i, j)

                        if point not in points:
                            points[point] = 1
                            area += 1

        claims.append({
            'id': id,
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2,
            'overlaps': overlaps,
        })

    non_overlaping_id = None

    for c in claims:
        if not c['overlaps']:
            non_overlaping_id = c['id']

    print("[Star 1] Overlapping area: %d" % area)
    print("[Star 2] Non-overlaping ID: %s" % non_overlaping_id)


if __name__ == '__main__':
    main()
