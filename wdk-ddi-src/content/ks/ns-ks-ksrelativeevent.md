---
UID: NS.ks.KSRELATIVEEVENT
title: KSRELATIVEEVENT
author: windows-driver-content
description: The KSPROPERTY_CONNECTION_STARTAT property is passed a KSRELATIVEEVENT structure.
old-location: stream\ksrelativeevent.htm
old-project: stream
ms.assetid: 4edb8b74-d5e5-49ee-85a7-9eb095f5a575
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KSRELATIVEEVENT, KSRELATIVEEVENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSRELATIVEEVENT
req.alt-loc: ks.h
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

# KSRELATIVEEVENT structure



## -description
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff565109">KSPROPERTY_CONNECTION_STARTAT</a> property is passed a KSRELATIVEEVENT structure.</p>


## -syntax

````
typedef struct {
  ULONG       Size;
  ULONG       Flags;
  union {
    HANDLE ObjectHandle;
    PVOID  ObjectPointer;
  };
  PVOID       Reserved;
  KSEVENT     Event;
  KSEVENTDATA EventData;
} KSRELATIVEEVENT;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the inclusive size of the structure, including any event specific data appended to the <b>EventData</b> member.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies what type of object is specified in the <b>ObjectHandle</b> and <b>ObjectPointer</b> union.</p>
</dd>

### -field <b>ObjectHandle</b>

<dd>
<p>Specifies the handle of the object supporting the event to be used if the <b>Flags</b> member contains the KSRELATIVEEVENT_FLAG_HANDLE flag.</p>
</dd>

### -field <b>ObjectPointer</b>

<dd>
<p>Specifies a pointer to the object supporting the event to be used if the Flags member contains the KSRELATIVEEVENT_FLAG_POINTER flag. This is valid only for kernel-mode clients.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved and set to zero.</p>
</dd>

### -field <b>Event</b>

<dd>
<p>A <a href="..\ks\nf-ks-ikscontrol-ksevent.md">KSEVENT</a> structure that contains the event to be used.</p>
</dd>

### -field <b>EventData</b>

<dd>
<p>A <a href="stream.kseventdata">KSEVENTDATA</a> structure that specifies the header for the event-specific data. The header itself is not actually used except as a starting point to access the event-specific data, and must be initialized to zero.</p>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>