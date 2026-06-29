# Claude-Beats
# 🧠 Claude Beats – Producer OS

**Claude Beats** is your 16‑year veteran production engineer and Hip‑Hop Producer OS. This repository automates chord progression to MIDI generation for GarageBand iOS production.

## Quick Start

1. Add your chord progression to `chords/progression.txt`
2. Push to GitHub
3. GitHub Actions generates MIDI automatically
4. Download and import to GarageBand

## Repository Structure
claude-beats/
├── .github/
│   └── workflows/
│       └── generate_midi.yml
├── chords/
│   └── progression.txt
├── midi/
│   └── output.mid
├── scripts/
│   └── chord_to_midi.py
└── templates/
└── conductor_daringer.txt

## Default Settings

| Parameter | Value |
|-----------|-------|
| Tempo | 78 BPM |
| Key | C Minor |
| Style | Cinematic boom‑bap |
| Mastering | -9 LUFS / -1dB True Peak |

## Example Progression

Cm, Ab, Fm, G, Cm, Ab, Bb, G
## How to Use

1. Open `chords/progression.txt`
2. Paste your chord progression (one line, comma-separated)
3. Commit and push
4. Download the generated MIDI from Actions
5. Import to GarageBand
6. 
