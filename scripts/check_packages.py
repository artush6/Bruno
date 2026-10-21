#!/usr/bin/env python3
"""Check shipped package integrity using only Python's standard library."""
from pathlib import Path
import hashlib
import json
import struct

ROOT = Path(__file__).resolve().parents[1]
VARIANTS = ('bruno', 'bruno-judoka', 'bruno-chef')


def check_package(slug):
    if slug not in VARIANTS:
        raise ValueError(f'Unknown variant: {slug}')
    package = ROOT / 'pets' / slug
    checksums = json.loads((ROOT / 'qa/SHA256SUMS.json').read_text())
    for filename in ('pet.json', 'spritesheet.png'):
        file = package / filename
        key = file.relative_to(ROOT).as_posix()
        if hashlib.sha256(file.read_bytes()).hexdigest() != checksums.get(key):
            raise ValueError(f'Checksum mismatch: {key}')
    manifest = json.loads((package / 'pet.json').read_text())
    if manifest.get('id') != slug or not manifest.get('displayName'):
        raise ValueError(f'Invalid identity: {slug}')
    if manifest.get('spriteVersionNumber') != 2:
        raise ValueError(f'{slug} must use spriteVersionNumber 2')
    if manifest.get('spritesheetPath') != 'spritesheet.png':
        raise ValueError(f'Unexpected spritesheetPath: {slug}')
    png = (package / 'spritesheet.png').read_bytes()
    if png[:8] != b'\x89PNG\r\n\x1a\n' or png[12:16] != b'IHDR':
        raise ValueError(f'Invalid PNG header: {slug}')
    if struct.unpack('>II', png[16:24]) != (1536, 2288):
        raise ValueError(f'Wrong atlas dimensions: {slug}')
    if png[25] not in (4, 6):
        raise ValueError(f'PNG must have an alpha channel: {slug}')
    return package


def main():
    for slug in VARIANTS:
        check_package(slug)
        print(f'OK {slug}: checksum, manifest, 1536x2288 PNG with alpha')


if __name__ == '__main__':
    main()
