---
UID: NE.ks.KSPROPERTY_STREAM
title: KSPROPERTY_STREAM
author: windows-driver-content
description: .
old-location: stream\ksproperty_stream.htm
old-project: stream
ms.assetid: 1A7C7181-00AF-4AAB-822F-017F11DB9409
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_STREAM
req.alt-loc: Ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# KSPROPERTY_STREAM enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KSPROPERTY_STREAM_ALLOCATOR,
  KSPROPERTY_STREAM_QUALITY,
  KSPROPERTY_STREAM_DEGRADATION,
  KSPROPERTY_STREAM_MASTERCLOCK,
  KSPROPERTY_STREAM_TIMEFORMAT,
  KSPROPERTY_STREAM_PRESENTATIONTIME,
  KSPROPERTY_STREAM_PRESENTATIONEXTENT,
  KSPROPERTY_STREAM_FRAMETIME,
  KSPROPERTY_STREAM_RATECAPABILITY,
  KSPROPERTY_STREAM_RATE,
  KSPROPERTY_STREAM_PIPE_ID
} KSPROPERTY_STREAM;
````


## -enum-fields
<dl>

### -field KSPROPERTY_STREAM_ALLOCATOR

<dd>
<p>Specify if the pin allocates stream buffers or can provide an allocator.</p>
</dd>

### -field KSPROPERTY_STREAM_QUALITY

<dd>
<p>Specify if the pin generates Quality Management complaints.</p>
</dd>

### -field KSPROPERTY_STREAM_DEGRADATION

<dd>
<p>Specify if the pin allows degradation strategies.</p>
</dd>

### -field KSPROPERTY_STREAM_MASTERCLOCK

<dd>
<p>Specify if the pin uses or produces a master clock that can be used for synchronization.</p>
</dd>

### -field KSPROPERTY_STREAM_TIMEFORMAT

<dd>
<p>Specify to retrieve the time format used on a particular pin connection.</p>
</dd>

### -field KSPROPERTY_STREAM_PRESENTATIONTIME

<dd>
<p>Specify to retrieve and set the current presentation time of a filter pin.</p>
</dd>

### -field KSPROPERTY_STREAM_PRESENTATIONEXTENT

<dd>
<p>Specify to query the stream extent.</p>
</dd>

### -field KSPROPERTY_STREAM_FRAMETIME

<dd>
<p>Specify to determine the duration of the next frame based on the particular media stream, and use that information to step-frame a sequence.</p>
</dd>

### -field KSPROPERTY_STREAM_RATECAPABILITY

<dd>
<p>Specify to allow a graph manager to query all connection points involved in the flow of a particular stream (obtained through KSPROPERTY_PIN_DATAROUTING) for their capability in adjusting a requested rate to the nominal rate.</p>
</dd>

### -field KSPROPERTY_STREAM_RATE

<dd>
<p>Specify in conjunction with KSPROPERTY_STREAM_RATECAPABILITY and use this to set the rate of a segment after querying the capability of the pin.</p>
</dd>

### -field KSPROPERTY_STREAM_PIPE_ID

<dd>
<p>Used internally for communication between the KSProxy system driver and AVStream.</p>
</dd>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>