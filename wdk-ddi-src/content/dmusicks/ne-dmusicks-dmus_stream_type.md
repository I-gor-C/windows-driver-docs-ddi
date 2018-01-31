---
UID : NE:dmusicks.DMUS_STREAM_TYPE
title : DMUS_STREAM_TYPE
author : windows-driver-content
description : Used for a DirectMusic synthesizer device.
old-location : audio\dmus_stream_type.htm
old-project : audio
ms.assetid : C4218B83-6D6D-4F3B-A90F-B92D08D80E24
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : dmusicks/DMUS_STREAM_WAVE_SINK, DMUS_STREAM_MIDI_INVALID, DMUS_STREAM_WAVE_SINK, audio.dmus_stream_type, dmusicks/DMUS_STREAM_TYPE, DMUS_STREAM_TYPE enumeration [Audio Devices], dmusicks/DMUS_STREAM_MIDI_RENDER, dmusicks/DMUS_STREAM_MIDI_INVALID, dmusicks/DMUS_STREAM_MIDI_CAPTURE, DMUS_STREAM_TYPE, DMUS_STREAM_MIDI_RENDER, DMUS_STREAM_MIDI_CAPTURE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : dmusicks.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DMUS_STREAM_TYPE
---

# DMUS_STREAM_TYPE Enumeration
Used for a DirectMusic synthesizer device.

## Syntax
````
typedef enum  { 
  DMUS_STREAM_MIDI_INVALID  = -1,
  DMUS_STREAM_MIDI_RENDER   = 0,
  DMUS_STREAM_MIDI_CAPTURE,
  DMUS_STREAM_WAVE_SINK
} DMUS_STREAM_TYPE;
````

## Constants

<table>

<tr>
<td>DMUS_STREAM_MIDI_CAPTURE</td>
<td></td>
</tr>

<tr>
<td>DMUS_STREAM_MIDI_INVALID</td>
<td></td>
</tr>

<tr>
<td>DMUS_STREAM_MIDI_RENDER</td>
<td></td>
</tr>

<tr>
<td>DMUS_STREAM_WAVE_SINK</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dmusicks.h |