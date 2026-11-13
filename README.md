# entry-happy
`main.py` (Python 3.13 stdlib) copies `entry.png` from its own directory to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), creating the output directory if needed.
The copy is raw binary, so the output is byte-identical to the 1024x1024 source; run `MAKEFUN_OUTPUT_DIR=/tmp/hout python3 main.py`. MIT, © 2026 Amburadullzz.
