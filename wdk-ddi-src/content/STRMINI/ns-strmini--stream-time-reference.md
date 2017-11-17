---
UID: NS.strmini._STREAM_TIME_REFERENCE
title: STREAM_TIME_REFERENCE
author: windows-driver-content
description: TBD.
old-location: stream\stream_time_reference.htm
ms.assetid: BC3839C0-AED6-470D-9C2B-B1529B2B3D1A
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: strmini.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STREAM_TIME_REFERENCE
req.alt-loc: Strmini.h
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
ms.keywords: STREAM_TIME_REFERENCE, STREAM_TIME_REFERENCE, *PSTREAM_TIME_REFERENCE
req.iface: 
req.product: Windows 10 or later.
---

# STREAM_TIME_REFERENCE structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _STREAM_TIME_REFERENCE {
  STREAM_TIMESTAMP CurrentOnboardClockValue;
  LARGE_INTEGER    OnboardClockFrequency;
  LARGE_INTEGER    CurrentSystemTime;
  ULONG            Reserved[2];
} STREAM_TIME_REFERENCE, *PSTREAM_TIME_REFERENCE;
````


## -struct-fields
<dl>

### -field <b>CurrentOnboardClockValue</b>

<dd>
<p>Current value of the adapter clock.</p>
</dd>

### -field <b>OnboardClockFrequency</b>

<dd>
<p>Frequency of the adapter clock.</p>
</dd>

### -field <b>CurrentSystemTime</b>

<dd>
<p>KeQueryPerformanceCounter time.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
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
<dt>Strmini.h</dt>
</dl>
</td>
</tr>
</table>