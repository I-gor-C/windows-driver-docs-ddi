---
UID: NF.strmini.StreamClassCallAtNewPriority
title: StreamClassCallAtNewPriority
author: windows-driver-content
description: The StreamClassCallAtNewPriority routine schedules a routine to be called at a different priority.
old-location: stream\streamclasscallatnewpriority.htm
old-project: stream
ms.assetid: 86c4e9da-7c71-4d79-b8e2-f602489da647
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: StreamClassCallAtNewPriority
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StreamClassCallAtNewPriority
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
req.irql: (See Parameters section)
req.iface: 
req.product: Windows 10 or later.
---

# StreamClassCallAtNewPriority function



## -description
<p>The <b>StreamClassCallAtNewPriority</b> routine schedules a routine to be called at a different priority.</p>


## -syntax

````
VOID StreamClassCallAtNewPriority(
  _In_opt_ PHW_STREAM_OBJECT    StreamObject,
  _In_     PVOID                HwDeviceExtension,
  _In_     STREAM_PRIORITY      Priority,
  _In_     PHW_PRIORITY_ROUTINE PriorityRoutine,
  _In_     PVOID                Context
);
````


## -parameters
<dl>

### -param <i>StreamObject</i> [in, optional]

<dd>
<p>Pointer to an HW_STREAM_OBJECT structure specifying the stream is associated with the routine, or <b>NULL</b> if the routine is associated with the device as a whole. There can be only one routine per stream, and only one routine for the device. This parameter is optional.</p>
</dd>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the minidriver's device extension. The minidriver specifies the size of this buffer in the <a href="..\strmini\ns-strmini--hw-initialization-data.md">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="stream.streamclassregisterminidriver">StreamClassRegisterMinidriver</a>. The class driver then passes pointers to the buffer in the <b>HwDeviceExtension</b> member of the <a href="..\strmini\ns-strmini--hw-stream-request-block.md">HW_STREAM_REQUEST_BLOCK</a>, <a href="..\strmini\ns-strmini--hw-stream-object~r1.md">HW_STREAM_OBJECT</a>, <a href="..\strmini\ns-strmini--hw-time-context.md">HW_TIME_CONTEXT</a>, and <a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.</p>
</dd>

### -param <i>Priority</i> [in]

<dd>
<p>Specifies one of the values listed in the following table.</p>
<table>
<tr>
<th>Priority</th>
<th>Usage</th>
</tr>
<tr>
<td>
<p>High</p>
</td>
<td>
<p>The stream class driver calls the routine at the same priority as the minidriver's <b>StrMini</b><i>Xxx</i> callbacks. Do not use this setting unless the routine must be synchronized with the minidriver's interrupt service routine.</p>
</td>
</tr>
<tr>
<td>
<p>Dispatch</p>
</td>
<td>
<p>The stream class driver calls the routine at DISPATCH_LEVEL. Use this priority if the routine takes less than 1 millisecond to complete.</p>
</td>
</tr>
<tr>
<td>
<p>Low</p>
</td>
<td>
<p>The stream class driver calls the routine at PASSIVE_LEVEL. Use this priority if the routine takes less than 1 millisecond to complete.</p>
</td>
</tr>
<tr>
<td>
<p>LowToHigh</p>
</td>
<td>
<p>Used to allow a thread called at low priority to return to high priority so that other stream class driver services can be called.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>PriorityRoutine</i> [in]

<dd>
<p>Pointer to a minidriver-supplied <a href="stream.strminipriorityroutine">StrMiniPriorityRoutine</a> to be called at the specified priority level.</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>Specifies the parameter to be passed to the <i>PriorityRoutine</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks


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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>(See Parameters section)</p>
</td>
</tr>
</table>