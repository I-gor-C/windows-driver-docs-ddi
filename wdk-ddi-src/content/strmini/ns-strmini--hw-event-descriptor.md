---
UID: NS.strmini._HW_EVENT_DESCRIPTOR
title: HW_EVENT_DESCRIPTOR
author: windows-driver-content
description: When the class driver calls one of the minidriver's StrMiniEvent routines, it passes a pointer to an HW_EVENT_DESCRIPTOR structure to describe the event as enabled or disabled.
old-location: stream\hw_event_descriptor.htm
old-project: stream
ms.assetid: c0efec37-4897-4ece-9f53-4a62204e5af3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: HW_EVENT_DESCRIPTOR, HW_EVENT_DESCRIPTOR, *PHW_EVENT_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HW_EVENT_DESCRIPTOR
req.alt-loc: strmini.h
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

# HW_EVENT_DESCRIPTOR structure



## -description
<p>When the class driver calls one of the minidriver's <a href="stream.strminievent">StrMiniEvent</a> routines, it passes a pointer to an HW_EVENT_DESCRIPTOR structure to describe the event as enabled or disabled. </p>


## -syntax

````
typedef struct _HW_EVENT_DESCRIPTOR {
  BOOLEAN        Enable;
  PKSEVENT_ENTRY EventEntry;
  PKSEVENTDATA   EventData;
  union {
    struct _HW_STREAM_OBJECT  *StreamObject;
    struct _HW_DEVICE_EXTENSION  *DeviceExtension;
  };
  ULONG          EnableEventSetIndex;
#if (NTDDI_VERSION >= NTDDI_WINXP)
  PVOID          HwInstanceExtension;
  ULONG          Reserved;
#else 
  ULONG          Reserved[2];
#endif 
} HW_EVENT_DESCRIPTOR, *PHW_EVENT_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Enable</b>

<dd>
<p>This is set to <b>TRUE</b> for an enabled event, and <b>FALSE</b> for a disabled event.</p>
</dd>

### -field <b>EventEntry</b>

<dd>
<p>Points to the <a href="..\ks\ns-ks--ksevent-entry.md">KSEVENT_ENTRY</a> structure that describes this event.</p>
</dd>

### -field <b>EventData</b>

<dd>
<p>Points to the <a href="stream.kseventdata">KSEVENTDATA</a> structure that describes this instance of the event.</p>
</dd>

### -field <b>StreamObject</b>

<dd>
<p>Points to the <a href="..\strmini\ns-strmini--hw-stream-object~r1.md">HW_STREAM_OBJECT</a> for the stream that owns the event that the class driver is enabling/disabling, or <b>NULL</b> if the event belongs to the driver as a whole.</p>
</dd>

### -field <b>DeviceExtension</b>

<dd>
<p>Points to the minidriver's device extension.</p>
</dd>

### -field <b>EnableEventSetIndex</b>

<dd>
<p>For stream events, this specifies the index of the event set within the <b>StreamEventsArray</b> member of the stream's <a href="..\strmini\ns-strmini--hw-stream-information.md">HW_STREAM_INFORMATION</a> structure.</p>
<p>For device events, this specifies the index of the event set within the <b>DeviceEventsArray</b> member of the minidriver's <a href="..\strmini\ns-strmini--hw-stream-header.md">HW_STREAM_HEADER</a> structure.</p>
</dd>

### -field <b>HwInstanceExtension</b>

<dd>
<p>Pointer to the minidriver's instance extension. The minidriver may use this buffer to record private information global to this instance of the minidriver. The minidriver sets the size of this buffer in the <a href="..\strmini\ns-strmini--hw-initialization-data.md">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="stream.streamclassregisterminidriver">StreamClassRegisterMinidriver</a>.

</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>

### -field <b>Reserved[2]</b>

<dd>
<p>Reserved for system use. Do not use.</p>
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
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
</table>