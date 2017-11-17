---
UID: NE.strmini._STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
title: STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
author: windows-driver-content
description: TBD.
old-location: stream\stream_minidriver_stream_notification_type.htm
ms.assetid: 13D8152C-FE7E-46EB-9C7F-9CA0135A4B76
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
req.header: strmini.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE
req.alt-loc: 
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
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
req.iface: 
req.product: Windows 10 or later.
---

# STREAM_MINIDRIVER_STREAM_NOTIFICATION_TYPE enumeration



## -description
<p>TBD</p>


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

### -field <a id="ReadyForNextStreamDataRequest"></a><a id="readyfornextstreamdatarequest"></a><a id="READYFORNEXTSTREAMDATAREQUEST"></a><b>ReadyForNextStreamDataRequest</b>

<dd>
<p>Indicates that the minidriver is ready for the next stream data request.</p>
</dd>

### -field <a id="ReadyForNextStreamControlRequest"></a><a id="readyfornextstreamcontrolrequest"></a><a id="READYFORNEXTSTREAMCONTROLREQUEST"></a><b>ReadyForNextStreamControlRequest</b>

<dd>
<p>Indicates that the minidriver is ready for the next stream control request.</p>
</dd>

### -field <a id="HardwareStarved"></a><a id="hardwarestarved"></a><a id="HARDWARESTARVED"></a><b>HardwareStarved</b>

<dd>
<p>Indicates that the hardware is starved for data.</p>
</dd>

### -field <a id="StreamRequestComplete"></a><a id="streamrequestcomplete"></a><a id="STREAMREQUESTCOMPLETE"></a><b>StreamRequestComplete</b>

<dd>
<p>Indicates that the specified stream SRB has completed.</p>
</dd>

### -field <a id="SignalMultipleStreamEvents"></a><a id="signalmultiplestreamevents"></a><a id="SIGNALMULTIPLESTREAMEVENTS"></a><b>SignalMultipleStreamEvents</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="SignalStreamEvent"></a><a id="signalstreamevent"></a><a id="SIGNALSTREAMEVENT"></a><b>SignalStreamEvent</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="DeleteStreamEvent"></a><a id="deletestreamevent"></a><a id="DELETESTREAMEVENT"></a><b>DeleteStreamEvent</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="StreamNotificationMaximum"></a><a id="streamnotificationmaximum"></a><a id="STREAMNOTIFICATIONMAXIMUM"></a><b>StreamNotificationMaximum</b>

<dd>
<p>TBD</p>
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