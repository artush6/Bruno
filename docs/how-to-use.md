# How to use Bruno

![The three bears](images/bruno-family.png)

## Requirements

Use a Codex-compatible desktop build that supports local custom v2 pets. Installation needs Python 3.9 or newer, with no extra packages. These are image-and-manifest packages; no API key, image generation, or server is needed.

## Install with the script

From the repository root:

```bash
python3 scripts/install.py
```

On Windows, use `py -3 scripts/install.py` if your Python command is `py`.

Install one or several variants by their folder names:

```bash
python3 scripts/install.py bruno
python3 scripts/install.py bruno-judoka bruno-chef
```

The default destination is the `pets` folder inside `CODEX_HOME`, or `~/.codex/pets` when that variable is unset. To choose a different location:

```bash
python3 scripts/install.py --dest /path/to/codex-home/pets
```

The installer verifies package checksums before copying. Identical installations are skipped. If a different package already occupies a variant's destination, use `--force`; the installer preserves the old folder as a timestamped backup beside it.

## Manual installation

Copy each desired folder from `pets/` into your Codex home directory's `pets/` folder. Keep each manifest next to its sprite sheet:

```text
~/.codex/pets/
├── bruno/
│   ├── pet.json
│   └── spritesheet.png
├── bruno-judoka/
│   ├── pet.json
│   └── spritesheet.png
└── bruno-chef/
    ├── pet.json
    └── spritesheet.png
```

The included manifest uses `spriteVersionNumber: 2`. Preserve this field so the runtime reads all eleven rows.

## Select and show your pet

In the desktop app, open **Settings → Pets**, refresh the list, then choose Bruno. Enter `/pet` or use **Show pet** to display the floating companion. Adjust its size under **Customize → Pet size**. Availability depends on the app and workspace. [Official Pets documentation](https://learn.chatgpt.com/docs/pets).

In a compatible Codex CLI session, enter `/pets` and select an installed variant. `/pets off` disables it. Terminal image support is required; the IDE extension has no pet picker. [Official Pets documentation](https://learn.chatgpt.com/docs/pets).

This installer prepares local packages. It does not upload pets to a cloud account or select one automatically. Historical account-specific pet IDs are not required.

## Update

```bash
git pull
python3 scripts/install.py --force
```

Refresh the pet list after updating. Keep or remove the installer's backup folders once you are happy with the update.

## Remove

Choose another pet, then remove only the installed variant folder(s) from your Codex home's `pets` directory. Your cloned repository and other pets are independent of those folders.

## Check the download

```bash
python3 scripts/check_packages.py
```

This verifies the shipped checksums, manifest fields, PNG dimensions, and alpha-capable encoding. Detailed artwork QA is preserved under `qa/` and `sources/`.

If a pet pauses while work continues, see [known issues](known-issues.md). The installer does not modify app animation code.
