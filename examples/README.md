# HID Format Examples

This directory contains example HID files and usage tutorials.

## Directory Structure

```
examples/
├── classical/     # Classical music examples
├── pop/          # Pop music examples
├── electronic/   # Electronic music examples
├── tutorials/    # Step-by-step tutorials
└── comparison/   # Format comparison demos
```

## Quick Examples

### 1. Basic Decoding

```python
from hid import HIDDecoder

# Decode a classical piece
decoder = HIDDecoder()
data = decoder.decode('classical/beethoven_moonlight.hid')
```

### 2. Batch Processing

```python
from pathlib import Path
from hid import HIDDecoder

decoder = HIDDecoder()
for hid_file in Path('classical').glob('*.hid'):
    data = decoder.decode(hid_file)
    print(f"{hid_file.name}: {len(data['tracks'])} tracks")
```

### 3. Format Comparison

See `comparison/` directory for side-by-side comparisons of:
- File sizes (HID vs MIDI vs MusicXML)
- Processing speed benchmarks
- Memory usage analysis

## Featured Examples

### Classical Music
- `beethoven_moonlight.hid` - Moonlight Sonata, 1st Movement
- `bach_invention_1.hid` - Bach Two-Part Invention No. 1
- `chopin_nocturne.hid` - Chopin Nocturne Op. 9 No. 2

### Pop Music
- `pop_ballad.hid` - Modern pop ballad structure
- `rock_anthem.hid` - Classic rock arrangement
- `synth_pop.hid` - 80s synthesizer patterns

### Electronic Music
- `edm_drop.hid` - EDM build-up and drop
- `ambient_pad.hid` - Ambient soundscape
- `drum_patterns.hid` - Various electronic drum patterns

## Compression Statistics

| File | MIDI Size | HID Size | Compression |
|------|-----------|----------|-------------|
| beethoven_moonlight.hid | 28.3 KB | 3.5 KB | 87.6% |
| pop_ballad.hid | 15.2 KB | 1.9 KB | 87.5% |
| edm_drop.hid | 42.1 KB | 5.2 KB | 87.6% |

## Tutorial Notebooks

Check the `tutorials/` directory for Jupyter notebooks:
- `01_basic_decoding.ipynb` - Getting started with HID
- `02_batch_processing.ipynb` - Processing multiple files
- `03_performance_analysis.ipynb` - Measuring performance gains
- `04_ai_integration.ipynb` - Using HID with AI models