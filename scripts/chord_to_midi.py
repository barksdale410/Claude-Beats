#!/usr/bin/env python3
"""
Chord Progression to MIDI Converter
Converts comma-separated chord progression .txt files to MIDI
"""

import argparse
import pretty_midi

# Chord to note mapping (root in MIDI numbers, C4 = 60)
CHORD_MAP = {
    'C': 60, 'C#': 61, 'Db': 61, 'D': 62, 'D#': 63, 'Eb': 63,
    'E': 64, 'F': 65, 'F#': 66, 'Gb': 66, 'G': 67, 'G#': 68,
    'Ab': 68, 'A': 69, 'A#': 70, 'Bb': 70, 'B': 71, 'Cb': 71
}

# Chord type intervals (semitones from root)
CHORD_TYPES = {
    'maj': [0, 4, 7],
    'min': [0, 3, 7],
    '7': [0, 4, 7, 10],
    'm7': [0, 3, 7, 10],
    'maj7': [0, 4, 7, 11],
    'm9': [0, 3, 7, 10, 14],
    '9': [0, 4, 7, 10, 14],
    'maj9': [0, 4, 7, 11, 14],
    'sus4': [0, 5, 7],
    'sus2': [0, 2, 7],
    'dim': [0, 3, 6],
    'aug': [0, 4, 8],
    'm7b5': [0, 3, 6, 10],
    'dim7': [0, 3, 6, 9],
    '6': [0, 4, 7, 9],
    'm6': [0, 3, 7, 9],
}

def parse_chord(chord_str):
    """Parse chord string into root and type"""
    chord_str = chord_str.strip()
    
    if '/' in chord_str:
        chord_str = chord_str.split('/')[0]
    
    for i in range(len(chord_str), 0, -1):
        root_candidate = chord_str[:i]
        if root_candidate in CHORD_MAP:
            root = root_candidate
            type_str = chord_str[i:]
            break
    else:
        root = chord_str[0]
        type_str = chord_str[1:]
    
    if not type_str or type_str == 'maj':
        chord_type = 'maj'
    elif type_str == 'm':
        chord_type = 'min'
    elif type_str == 'maj7':
        chord_type = 'maj7'
    elif type_str == '7':
        chord_type = '7'
    elif type_str == 'm7':
        chord_type = 'm7'
    elif type_str == 'm9':
        chord_type = 'm9'
    elif type_str == '9':
        chord_type = '9'
    elif type_str == 'maj9':
        chord_type = 'maj9'
    elif type_str == 'sus4':
        chord_type = 'sus4'
    elif type_str == 'sus2':
        chord_type = 'sus2'
    elif type_str == 'dim':
        chord_type = 'dim'
    elif type_str == 'aug':
        chord_type = 'aug'
    elif type_str == 'm7b5':
        chord_type = 'm7b5'
    elif type_str == 'dim7':
        chord_type = 'dim7'
    elif type_str == '6':
        chord_type = '6'
    elif type_str == 'm6':
        chord_type = 'm6'
    else:
        chord_type = 'maj'
    
    return root, chord_type

def generate_midi(chords, output_path, bpm=78):
    """Generate MIDI file from chord progression"""
    midi = pretty_midi.PrettyMIDI(initial_tempo=bpm)
    
    piano = pretty_midi.Instrument(program=0, name='Acoustic Grand Piano')
    
    seconds_per_bar = 60 / bpm * 4
    chord_duration = seconds_per_bar
    
    for i, chord_str in enumerate(chords):
        root, chord_type = parse_chord(chord_str)
        root_note = CHORD_MAP[root]
        intervals = CHORD_TYPES.get(chord_type, CHORD_TYPES['maj'])
        
        start_time = i * chord_duration
        end_time = start_time + chord_duration
        
        for interval in intervals:
            note = root_note + interval
            if interval > 7:
                note -= 12
            
            note_obj = pretty_midi.Note(
                velocity=100,
                pitch=note,
                start=start_time,
                end=end_time
            )
            piano.notes.append(note_obj)
    
    midi.instruments.append(piano)
    midi.write(output_path)
    print(f"MIDI saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Convert chord progression to MIDI')
    parser.add_argument('--input', required=True, help='Input .txt file with chord progression')
    parser.add_argument('--output', required=True, help='Output .mid file path')
    parser.add_argument('--bpm', type=int, default=78, help='BPM tempo')
    
    args = parser.parse_args()
    
    with open(args.input, 'r') as f:
        content = f.read().strip()
    
    chords = [c.strip() for c in content.replace('\n', ',').split(',') if c.strip()]
    
    print(f"Generating MIDI for {len(chords)} chords at {args.bpm} BPM")
    print(f"Chords: {chords}")
    
    generate_midi(chords, args.output, args.bpm)

if __name__ == '__main__':
    main()