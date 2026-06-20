# Puzzles

This repository is a small collection of puzzle pages, visualizations, and supporting assets. Most of the pages are standalone HTML files that can be opened directly in a browser from the local filesystem.

The main entry point is [index.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/index.html), which links to the currently exposed pages.

## Contents

- [index.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/index.html): Landing page for the puzzle collection.
- [chessboard.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/chessboard.html): Chessboard page using the SVG chess piece assets in `chess-pieces/`.
- [card_numbers.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/card_numbers.html): Interactive page for the card numbers puzzle.
- [earth_rope.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/earth_rope.html): Rope-to-space visualization. This page uses version-pinned CDN scripts for React, Babel, and Tailwind.
- [igni.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/igni.html): Animated circular-text fire page based on the palindrome `In girum imus nocte et consumimur igni`, with built-in video export.
- [palindromes.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/palindromes.html): Interactive palindrome finder for sentence input.
- [rotating_circles.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/rotating_circles.html): Small-circle rolling simulation inside or outside a larger circle.
- [slinky_drop.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/slinky_drop.html): Falling slinky visualization with a two-phase collapse-and-drop animation and explanatory formulas.
- [trees.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/trees.html): Interactive tree grid puzzle.

## Supporting Files

- [card_numbers.py](/Users/rupendrabandyopadhyay/Documents/Puzzles/card_numbers.py) and [palindromes.py](/Users/rupendrabandyopadhyay/Documents/Puzzles/palindromes.py): Python helpers related to the corresponding puzzle pages.
- `chess-pieces/`: SVG assets used by the chessboard page.
- [slinky-realistic-white.png](/Users/rupendrabandyopadhyay/Documents/Puzzles/slinky-realistic-white.png): Slinky image asset used by the falling slinky page.
- [Trees.svg](/Users/rupendrabandyopadhyay/Documents/Puzzles/Trees.svg), [Trees_Initial.svg](/Users/rupendrabandyopadhyay/Documents/Puzzles/Trees_Initial.svg), [Area.svg](/Users/rupendrabandyopadhyay/Documents/Puzzles/Area.svg): Drawing assets.
- [Hex_Question.ggb](/Users/rupendrabandyopadhyay/Documents/Puzzles/Hex_Question.ggb), [Hex_Answer.ggb](/Users/rupendrabandyopadhyay/Documents/Puzzles/Hex_Answer.ggb), [Hex.pdf](/Users/rupendrabandyopadhyay/Documents/Puzzles/Hex.pdf): Hex puzzle source and export files.

## How To Use

For most pages:

1. Open [index.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/index.html) in a browser.
2. Choose the page you want from the menu.

You can also open any standalone HTML file directly.

## Notes

- Most pages are self-contained and work offline.
- [earth_rope.html](/Users/rupendrabandyopadhyay/Documents/Puzzles/earth_rope.html) depends on external CDN scripts, so it requires network access unless it is later converted to a fully local page.
- Exported media files such as `.webm`, `.gif`, `.mov`, and `.mp4` are ignored by the current `.gitignore`.
