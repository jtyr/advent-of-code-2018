#!/usr/bin/python2

"""
--- Day 5: Alchemical Reduction ---

You've managed to sneak in to the prototype suit manufacturing lab. The
Elves are making decent progress, but are still struggling with the
suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved
their problem eventually, you can do better. You scan the chemical
composition of the suit's material and discover that it is formed by
extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with
each other such that two adjacent units of the same type and opposite
polarity are destroyed. Units' types are represented by letters; units'
polarity is represented by capitalization. For instance, r and R are
units with the same type but opposite polarity, whereas r and s are
entirely different types and do not react.

For example:

- In aA, a and A react, leaving nothing behind.
- In abBA, bB destroys itself, leaving aA. As above, this then destroys
  itself, leaving nothing.
- In abAB, no two adjacent units are of the same type, and so nothing
  happens.
- In aabAAB, even though aa and AA are of the same type, their polarities
  match, and so nothing happens.

Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.

After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned?
(Note: in this puzzle and others, the input is large; if you copy/paste
your input, make sure you get the whole thing.)

--- Part Two ---

Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer
from collapsing as much as it should. Your goal is to figure out which
unit type is causing the most problems, remove all instances of it
(regardless of polarity), fully react the remaining polymer, and measure
its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

- Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer
  produces dbCBcD, which has length 6.
- Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this
  polymer produces daCAcaDA, which has length 8.
- Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer
  produces daDA, which has length 4.
- Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this
  polymer produces abCBAc, which has length 6.

In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing
all units of exactly one type and fully reacting the result?
"""


import sys


def get_data(name):
    f = open(name, 'r')

    return f.read()


def react(data):
    while True:
        changed = False

        for i, ch in enumerate(data):
            if i > 0 and abs(ord(ch) - ord(data[i-1])) == 32:
                del data[i-1:i+1]
                changed = True

        if not changed:
            break


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)

    data = get_data(sys.argv[1]).rstrip()
    data1 = list(data)

    react(data1)

    print("[Star 1] Polymer length: %d" % len(data1))

    shortest = 99999
    chrs = []

    for ch in data:
        ch = ch.lower()

        if ch not in chrs:
            chrs.append(ch)

    for ch in chrs:
        data2 = list(data.replace(ch, '').replace(ch.upper(), ''))

        react(data2)

        cur_len = len(data2)

        if cur_len < shortest:
            shortest = cur_len

    print("[Star 2] Shortest polymer: %d" % shortest)


if __name__ == '__main__':
    main()
