"""Travellers Rest Desktop — A local helper for Travellers Rest tavern folders, cellar files, and inn photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='travellers_rest_desktop',
        description='A local helper for Travellers Rest tavern folders, cellar files, and inn photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Travellers Rest Desktop')
    print('Keep the tavern on disk before a guest update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
