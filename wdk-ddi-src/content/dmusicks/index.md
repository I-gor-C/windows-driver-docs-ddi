---
UID: NA:
---

# Dmusicks.h header

## -description

This header is used by Audio. For more information, see
- [Audio](../_audio/index.md)

Dmusicks.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_DMUS_KERNEL_EVENT structure](ns-dmusicks-_dmus_kernel_event.md) | The DMUS_KERNEL_EVENT structure is used to package time-stamped music events. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [DMUS_STREAM_TYPE enumeration](ne-dmusicks-dmus_stream_type.md) | Used for a DirectMusic synthesizer device. |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IAllocatorMXF interface](nn-dmusicks-iallocatormxf~r1.md) | The IAllocatorMXF interface manages buffer storage for DirectMusic streams. |
| [IMXF interface](nn-dmusicks-imxf~r1.md) | The IMXF interface represents the DirectMusic stream on a MIDI transport filter (MXF). |
| [IMasterClock interface](nn-dmusicks-imasterclock.md) | The IMasterClock interface provides Microsoft DirectMusic streams with access to the current reference time from the master clock. |
| [IMiniportDMus interface](nn-dmusicks-iminiportdmus.md) | The IMiniportDMus interface is the primary interface for a DMus miniport driver for a DirectMusic synthesizer device. |
| [IPortDMus interface](nn-dmusicks-iportdmus.md) | The IPortDMus interface is the DMus port driver's primary interface. |
| [IPositionNotify interface](nn-dmusicks-ipositionnotify.md) | PositionNotify |
| [ISynthSinkDMus interface](nn-dmusicks-isynthsinkdmus.md) | The ISynthSinkDMus interface handles wave output for a DirectMusic synthesizer device. |
