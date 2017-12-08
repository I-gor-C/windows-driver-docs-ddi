---
UID: NE.dmusicks.DMUS_STREAM_TYPE
title: DMUS_STREAM_TYPE
author: windows-driver-content
description: Used for a DirectMusic synthesizer device.
old-location: audio\dmus_stream_type.htm
old-project: audio
ms.assetid: C4218B83-6D6D-4F3B-A90F-B92D08D80E24
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PDXGK_BRIGHTNESS_INTERFACE, DXGK_BRIGHTNESS_INTERFACE, *PDXGK_BRIGHTNESS_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dmusicks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DMUS_STREAM_TYPE
req.alt-loc: Dmusicks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DMUS_STREAM_TYPE enumeration



## -description
<p>Used for a DirectMusic synthesizer device. </p>


## -syntax

````
typedef enum  { 
  DMUS_STREAM_MIDI_INVALID  = -1,
  DMUS_STREAM_MIDI_RENDER   = 0,
  DMUS_STREAM_MIDI_CAPTURE,
  DMUS_STREAM_WAVE_SINK
} DMUS_STREAM_TYPE;
````


## -enum-fields
<dl>

### -field DMUS_STREAM_MIDI_INVALID

<dd></dd>

### -field DMUS_STREAM_MIDI_RENDER 

<dd></dd>

### -field DMUS_STREAM_MIDI_CAPTURE

<dd></dd>

### -field DMUS_STREAM_WAVE_SINK

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dmusicks.h</dt>
</dl>
</td>
</tr>
</table>