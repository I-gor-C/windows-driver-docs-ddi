---
UID: NE.strmini._STREAM_PRIORITY
title: STREAM_PRIORITY
author: windows-driver-content
description: TD.
old-location: stream\stream_priority.htm
old-project: stream
ms.assetid: 790A00A5-1107-4686-B690-80D07B69AF62
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: strmini.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STREAM_PRIORITY
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
req.iface: 
req.product: Windows 10 or later.
---

# STREAM_PRIORITY enumeration



## -description
<p>TD</p>


## -syntax

````
typedef enum _STREAM_PRIORITY { 
  High,
  Dispatch,
  Low,
  LowToHigh                   
} STREAM_PRIORITY, *PSTREAM_PRIORITY
;
````


## -enum-fields
<dl>

### -field <a id="High"></a><a id="high"></a><a id="HIGH"></a><b>High</b>

<dd>
<p>Highest priority, IRQL equal to the adapter's ISR.</p>
</dd>

### -field <a id="Dispatch"></a><a id="dispatch"></a><a id="DISPATCH"></a><b>Dispatch</b>

<dd>
<p>Medium priority, IRQL equal to dispatch level.</p>
</dd>

### -field <a id="Low"></a><a id="low"></a><a id="LOW"></a><b>Low</b>

<dd>
<p>Lowest priority, IRQL equal to passive or APC level.</p>
</dd>

### -field <a id="LowToHigh___________________"></a><a id="lowtohigh___________________"></a><a id="LOWTOHIGH___________________"></a><b>LowToHigh                   </b>

<dd>
<p>Go from low priority to high priority.</p>
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