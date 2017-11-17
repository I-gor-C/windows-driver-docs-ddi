---
UID: NF.strmini.StreamClassGetNextEvent
title: StreamClassGetNextEvent
author: windows-driver-content
description: Minidrivers can use the StreamClassGetNextEvent routine to search the event queue of a device or of a particular stream.
old-location: stream\streamclassgetnextevent.htm
ms.assetid: a2f83163-4529-4627-8959-2b4cd6b88828
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StreamClassGetNextEvent
req.alt-loc: Stream.lib,Stream.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Stream.lib
req.dll: 
req.irql: 
ms.keywords: StreamClassGetNextEvent
req.iface: 
req.product: Windows 10 or later.
---

# StreamClassGetNextEvent function



## -description
<p>Minidrivers can use the <b>StreamClassGetNextEvent</b> routine to search the event queue of a device or of a particular stream.</p>


## -syntax

````
PKSEVENT_ENTRY StreamClassGetNextEvent(
  _In_opt_ PVOID             HwDeviceExtension,
  _In_opt_ PHW_STREAM_OBJECT HwStreamObject,
  _In_opt_ GUID              *EventGuid,
  _In_     ULONG             EventItem,
  _In_opt_ PKSEVENT_ENTRY    CurrentEvent
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in, optional]

<dd>
<p>Pointer to the minidriver's device extension. The minidriver specifies the size of this buffer in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="https://msdn.microsoft.com/library/windows/hardware/ff568263">StreamClassRegisterMinidriver</a>. The class driver then passes pointers to the buffer in the <b>HwDeviceExtension</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559702">HW_STREAM_REQUEST_BLOCK</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559697">HW_STREAM_OBJECT</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559706">HW_TIME_CONTEXT</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.</p>
</dd>

### -param <i>HwStreamObject</i> [in, optional]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559697">HW_STREAM_OBJECT</a>. Set to <b>NULL</b> to search the event queue of the device itself. To search the event queue of a particular stream, set to the stream's stream object.</p>
</dd>

### -param <i>EventGuid</i> [in, optional]

<dd>
<p>Specifies the event set to match when walking the queue, or <b>NULL</b> to match any event set.</p>
</dd>

### -param <i>EventItem</i> [in]

<dd>
<p>Specifies the event ID to match when walking the queue, or -1 to match any event.</p>
</dd>

### -param <i>CurrentEvent</i> [in, optional]

<dd>
<p>Pointer to an event in the event queue, or <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>If <i>CurrentEvent</i> is not <b>NULL</b>, <b>StreamClassGetNextEvent</b> returns the next matching event after <i>CurrentEvent</i> in the queue (or <b>NULL</b> if there is no such next event). If <i>CurrentEvent</i> is <b>NULL</b>, <b>StreamClassGetNextEvent</b> returns the first matching event in the queue.</p>

## -remarks
<p>The minidriver can call <b>StreamClassGetNextEvent</b> successively to loop through the event queue, examining one event at a time.</p>

<p>The caller may specify additional search criteria to match events on the event queue.</p>

<p>The minidriver can call <b>StreamClassGetNextEvent</b> successively to loop through the event queue, examining one event at a time.</p>

<p>The caller may specify additional search criteria to match events on the event queue.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Stream.lib</dt>
</dl>
</td>
</tr>
</table>