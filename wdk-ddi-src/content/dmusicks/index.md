---
UID: NA:dmusicks
ms.assetid: c45b3cd8-75b9-3c2a-99f7-976310a605af
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# dmusicks.h header



dmusicks.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [IAllocatorMXF](nn-dmusicks-iallocatormxf.md) | The IAllocatorMXF interface manages buffer storage for DirectMusic streams. |
| [IMasterClock](nn-dmusicks-imasterclock.md) | The IMasterClock interface provides Microsoft DirectMusic streams with access to the current reference time from the master clock. |
| [IMiniportDMus](nn-dmusicks-iminiportdmus.md) | The IMiniportDMus interface is the primary interface for a DMus miniport driver for a DirectMusic synthesizer device. |
| [IMXF](nn-dmusicks-imxf.md) | The IMXF interface represents the DirectMusic stream on a MIDI transport filter (MXF). |
| [IPortDMus](nn-dmusicks-iportdmus.md) | The IPortDMus interface is the DMus port driver's primary interface. |
| [IPositionNotify](nn-dmusicks-ipositionnotify.md) | PositionNotify |
| [ISynthSinkDMus](nn-dmusicks-isynthsinkdmus.md) | The ISynthSinkDMus interface handles wave output for a DirectMusic synthesizer device. |





## Structures
| Title | Description |
| ---- |:---- |
| [_DMUS_KERNEL_EVENT](ns-dmusicks-_dmus_kernel_event.md) | The DMUS_KERNEL_EVENT structure is used to package time-stamped music events. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [DMUS_STREAM_TYPE](ne-dmusicks-dmus_stream_type.md) | Used for a DirectMusic synthesizer device. |