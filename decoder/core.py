"""
HID Format Decoder Core Implementation
This is the open-source decoder for HID format files.
"""

import struct
from typing import List, Dict, Any, BinaryIO
from dataclasses import dataclass
import numpy as np


@dataclass
class HIDHeader:
    """HID file header structure"""
    version: int
    tracks: int
    ticks_per_beat: int
    duration: int
    compression_flags: int


class HIDDecoder:
    """
    HID Format Decoder

    Decodes HID binary files into standard MIDI representation.
    This decoder is open-source and free to use.
    """

    MAGIC = b'HID\x00'
    VERSION = 3

    def __init__(self):
        self.header = None
        self.tracks = []
        self.events = []

    def decode(self, filepath: str) -> Dict[str, Any]:
        """
        Decode a HID file to MIDI structure

        Args:
            filepath: Path to HID file

        Returns:
            Dictionary containing decoded MIDI data
        """
        with open(filepath, 'rb') as f:
            return self._decode_stream(f)

    def _decode_stream(self, stream: BinaryIO) -> Dict[str, Any]:
        """Decode from binary stream"""
        # Read and validate magic number
        magic = stream.read(4)
        if magic != self.MAGIC:
            raise ValueError(f"Invalid HID file: wrong magic number")

        # Read header
        self.header = self._read_header(stream)

        # Read track data
        for track_idx in range(self.header.tracks):
            track = self._read_track(stream, track_idx)
            self.tracks.append(track)

        return self._to_midi_structure()

    def _read_header(self, stream: BinaryIO) -> HIDHeader:
        """Read HID header"""
        version, tracks, tpb, duration, flags = struct.unpack('>BHHHH', stream.read(9))

        if version != self.VERSION:
            raise ValueError(f"Unsupported HID version: {version}")

        return HIDHeader(
            version=version,
            tracks=tracks,
            ticks_per_beat=tpb,
            duration=duration,
            compression_flags=flags
        )

    def _read_track(self, stream: BinaryIO, track_idx: int) -> Dict[str, Any]:
        """Read a single track"""
        track_size = struct.unpack('>I', stream.read(4))[0]
        track_data = stream.read(track_size)

        # Decode events based on compression flags
        events = self._decode_events(track_data, self.header.compression_flags)

        return {
            'index': track_idx,
            'events': events,
            'name': f"Track {track_idx + 1}"
        }

    def _decode_events(self, data: bytes, flags: int) -> List[Dict[str, Any]]:
        """
        Decode event data based on compression flags

        This is the core decompression logic that reverses
        the patented HID compression algorithm.
        """
        events = []
        offset = 0

        while offset < len(data):
            # Read event type and parameters
            event_type = data[offset]
            offset += 1

            if event_type == 0x90:  # Note On
                time, pitch, velocity, duration = self._read_note(data, offset, flags)
                events.append({
                    'type': 'note',
                    'time': time,
                    'pitch': pitch,
                    'velocity': velocity,
                    'duration': duration
                })
                offset += self._get_note_size(flags)

            elif event_type == 0xFF:  # Meta event
                meta_type, length = struct.unpack('>BB', data[offset:offset+2])
                offset += 2
                meta_data = data[offset:offset+length]
                offset += length

                events.append({
                    'type': 'meta',
                    'meta_type': meta_type,
                    'data': meta_data
                })

        return events

    def _read_note(self, data: bytes, offset: int, flags: int) -> tuple:
        """Read compressed note data"""
        if flags & 0x01:  # High compression mode
            # Unpack using bit fields
            packed = struct.unpack('>I', data[offset:offset+4])[0]
            time = (packed >> 20) & 0xFFF
            pitch = (packed >> 13) & 0x7F
            velocity = (packed >> 6) & 0x7F
            duration = packed & 0x3F
        else:  # Standard mode
            time, pitch, velocity, duration = struct.unpack('>HBBB', data[offset:offset+5])

        return time, pitch, velocity, duration

    def _get_note_size(self, flags: int) -> int:
        """Get size of note based on compression flags"""
        return 4 if flags & 0x01 else 5

    def _to_midi_structure(self) -> Dict[str, Any]:
        """Convert to standard MIDI structure"""
        return {
            'format': 1,
            'ticks_per_beat': self.header.ticks_per_beat,
            'tracks': [
                {
                    'name': track['name'],
                    'events': self._convert_events_to_midi(track['events'])
                }
                for track in self.tracks
            ]
        }

    def _convert_events_to_midi(self, events: List[Dict]) -> List[Dict]:
        """Convert HID events to MIDI events"""
        midi_events = []
        current_time = 0

        for event in events:
            delta_time = event['time'] - current_time
            current_time = event['time']

            if event['type'] == 'note':
                # Note On
                midi_events.append({
                    'delta_time': delta_time,
                    'type': 'note_on',
                    'channel': 0,
                    'pitch': event['pitch'],
                    'velocity': event['velocity']
                })

                # Note Off
                midi_events.append({
                    'delta_time': event['duration'],
                    'type': 'note_off',
                    'channel': 0,
                    'pitch': event['pitch'],
                    'velocity': 0
                })

        return midi_events