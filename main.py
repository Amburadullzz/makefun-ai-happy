# entry for make.fun
#!/usr/bin/env python3
"""Copy entry.png from this script's directory to $MAKEFUN_OUTPUT_DIR/entry.png.

Standard library only (Python 3.13+). The source image is resolved relative to
this file via os.path.dirname(__file__), the destination directory is created if
missing, and the bytes are copied verbatim so the output is byte-identical to
the source.
"""

from __future__ import annotations

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
CHUNK_SIZE = 1 << 20


def sha256_file(path: str) -> str:
    """Return the hex SHA-256 digest of a file."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), SOURCE_NAME)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    destination = os.path.join(output_dir, SOURCE_NAME)

    if not os.path.isfile(source):
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)

    # copyfile writes the raw bytes only: no metadata, no re-encoding.
    shutil.copyfile(source, destination)

    source_hash = sha256_file(source)
    destination_hash = sha256_file(destination)
    if source_hash != destination_hash:
        print(
            f"error: copy mismatch ({source_hash} != {destination_hash})",
            file=sys.stderr,
        )
        return 1

    size = os.path.getsize(destination)
    print(f"wrote {destination} ({size} bytes, sha256 {destination_hash})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
