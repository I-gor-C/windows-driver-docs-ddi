---
UID: NE.strmini._STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
title: STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
author: windows-driver-content
description: .
old-location: stream\stream_minidriver_stream_notification_type.htm
old-project: stream
ms.assetid: 13D8152C-FE7E-46EB-9C7F-9CA0135A4B76
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
req.alt-api: STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
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

# STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE enumeration



## -description
<p></p>


## -syntax

````
typedef enum _STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE { 
  ReadyForNextStreamDataRequest,
  ReadyForNextStreamControlRequest,
  HardwareStarved,
  StreamRequestComplete,
  SignalMultipleStreamEvents,
  SignalStreamEvent,
  DeleteStreamEvent,
  StreamNotificationMaximum
} STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE, *PSTREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE;
````


## -enum-fields
<dl>

### -field ReadyForNextStreamDataRequest

<dd>
<p>Indicates that the minidriver is ready for the next stream data request.</p>
</dd>

### -field ReadyForNextStreamControlRequest

<dd>
<p>Indicates that the minidriver is ready for the next stream control request.</p>
</dd>

### -field HardwareStarved

<dd>
<p>Indicates that the hardware is starved for data.</p>
</dd>

### -field StreamRequestComplete

<dd>
<p>Indicates that the specified stream SRB has completed.</p>
</dd>

### -field SignalMultipleStreamEvents

<dd></dd>

### -field SignalStreamEvent

<dd></dd>

### -field DeleteStreamEvent

<dd></dd>

### -field StreamNotificationMaximum

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
<dt>Strmini.h</dt>
</dl>
</td>
</tr>
</table>