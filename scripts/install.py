#!/usr/bin/env python3
"""Install Bruno packages without modifying app settings or other pets."""
import argparse
from datetime import datetime
import os
from pathlib import Path
import shutil
import tempfile

from check_packages import VARIANTS, check_package


def identical(source, destination):
    return destination.is_dir() and not destination.is_symlink() and all(
        (destination / filename).is_file()
        and (source / filename).read_bytes() == (destination / filename).read_bytes()
        for filename in ('pet.json', 'spritesheet.png')
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('variants', nargs='*', metavar='VARIANT',
                        help='bruno, bruno-judoka, bruno-chef; default: all three')
    parser.add_argument('--dest', type=Path,
                        help='Destination pets directory; default: CODEX_HOME/pets or ~/.codex/pets')
    parser.add_argument('--force', action='store_true',
                        help='Back up and replace a different existing package')
    args = parser.parse_args()
    selected = list(dict.fromkeys(args.variants or VARIANTS))
    unknown = set(selected) - set(VARIANTS)
    if unknown:
        parser.error('Unknown variant(s): ' + ', '.join(sorted(unknown)))
    codex_home = Path(os.environ.get('CODEX_HOME') or (Path.home() / '.codex')).expanduser()
    destination = (args.dest or (codex_home / 'pets')).expanduser().resolve()
    # Verify every selected package and conflict before writing anything.
    sources = {slug: check_package(slug) for slug in selected}
    for slug, source in sources.items():
        target = destination / slug
        if (target.exists() or target.is_symlink()) and not identical(source, target) and not args.force:
            parser.error(f'{target} already exists with different files. Use --force to preserve a backup and replace it.')
    destination.mkdir(parents=True, exist_ok=True)
    for slug, source in sources.items():
        target = destination / slug
        if identical(source, target):
            print(f'Already installed: {target}')
            continue
        backup = None
        with tempfile.TemporaryDirectory(prefix='.bruno-install-', dir=destination) as temp:
            staged = Path(temp) / slug
            shutil.copytree(source, staged)
            if target.exists() or target.is_symlink():
                stamp = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
                backup = destination / f'{slug}.backup-{stamp}'
                target.rename(backup)
            try:
                staged.rename(target)
            except BaseException:
                if backup is not None and not target.exists():
                    backup.rename(target)
                raise
        print(f'Installed: {target}')
        if backup:
            print(f'Previous package saved: {backup}')
    print('Refresh Settings > Pets and select your Bruno. Selection was not changed.')


if __name__ == '__main__':
    main()
