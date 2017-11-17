---
UID: NE.ks.KSPROPERTY_STREAM
title: KSPROPERTY_STREAM
author: windows-driver-content
description: TBD.
old-location: stream\ksproperty_stream.htm
ms.assetid: 1A7C7181-00AF-4AAB-822F-017F11DB9409
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
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
ms.keywords: MIDL_IKeywordDetectorOemAdapter_0003, KEYWORDSELECTOR
req.iface: IKeywordDetectorOemAdapter
---

# KSPROPERTY_STREAM enumeration



## -description
<p>TBD</p>


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

### -field <a id="KSPROPERTY_STREAM_ALLOCATOR"></a><a id="ksproperty_stream_allocator"></a><b>KSPROPERTY_STREAM_ALLOCATOR</b>

<dd>
<p>Specify if the pin allocates stream buffers or can provide an allocator.</p>
</dd>

### -field <a id="KSPROPERTY_STREAM_QUALITY"></a><a id="ksproperty_stream_quality"></a><b>KSPROPERTY_STREAM_QUALITY</b>

<dd>
<p>Specify if the pin generates Quality Management complaints.</p>
</dd>

### -field <a id="KSPROPERTY_STREAM_DEGRADATION"></a><a id="ksproperty_stream_degradation"></a><b>KSPROPERTY_STREAM_DEGRADATION</b>

<dd>
<p>Specify if the pin allows degradation strategies.</p>
</dd>

### -field <a id="KSPROPERTY_STREAM_MASTERCLOCK"></a><a id="ksproperty_stream_masterclock"></a><b>KSPROPERTY_STREAM_MASTERCLOCK</b>

<dd>
<p>Specify if the pin uses or produces a master clock that can be used for synchronization.</p>
</dd>

### -field <a id="KSPROPERTY_STREAM_TIMEFORMAT"></a><a id="ksproperty_stream_timeformat"></a><b>KSPROPERTY_STREAM_TIMEFORMAT</b>

<dd>
<p>Specify to retrieve the time format used on a particular pin connection.</p>
</dd>

### -field <a id="KSPROPERTY_STREAM_PRESENTATIONTIME"></a><a id="ksproperty_stream_presentationtime"></a><b>KSPROPERTY_STREAM_PRESENTATIONTIME</b>

<dd>
<p>Specify to retrieve and set the current presentation time of a filter pin.</p>
</dd>

### -field <a id="KSPROPERTY_STREAM_PRESENTATIONEXTENT"></a><a id="ksproperty_stream_presentationextent"></a><b>KSPROPERTY_STREAM_PRESENTATIONEXTENT</b>

<dd>
<p>Specify to query the stream extent.</p>
</dd>

### -field <a id="KSPROPERTY_STREAM_FRAMETIME"></a><a id="ksproperty_stream_frametime"></a><b>KSPROPERTY_STREAM_FRAMETIME</b>

<dd>
<p>Specify to determine the duration of the next frame based on the particular media stream, and use that information to step-frame a sequence.</p>
</dd>

### -field <a id="KSPROPERTY_STREAM_RATECAPABILITY"></a><a id="ksproperty_stream_ratecapability"></a><b>KSPROPERTY_STREAM_RATECAPABILITY</b>

<dd>
<p>Specify to allow a graph manager to query all connection points involved in the flow of a particular stream (obtained through KSPROPERTY_PIN_DATAROUTING) for their capability in adjusting a requested rate to the nominal rate.</p>
</dd>

### -field <a id="KSPROPERTY_STREAM_RATE"></a><a id="ksproperty_stream_rate"></a><b>KSPROPERTY_STREAM_RATE</b>

<dd>
<p>Specify in conjunction with KSPROPERTY_STREAM_RATECAPABILITY and use this to set the rate of a segment after querying the capability of the pin.</p>
</dd>

### -field <a id="KSPROPERTY_STREAM_PIPE_ID"></a><a id="ksproperty_stream_pipe_id"></a><b>KSPROPERTY_STREAM_PIPE_ID</b>

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