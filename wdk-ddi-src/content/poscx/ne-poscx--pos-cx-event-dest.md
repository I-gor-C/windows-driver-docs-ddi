---
UID: NE.poscx._POS_CX_EVENT_DEST
title: POS_CX_EVENT_DEST
author: windows-driver-content
description: The POS_CX_EVENT_DEST defines which applications receive this event.
old-location: pos\pos_cx_event_dest.htm
old-project: pos
ms.assetid: 63D16B9E-82CC-4171-B80A-D0FA6F2066E2
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PCSTREAMRESOURCE_DESCRIPTOR, PCSTREAMRESOURCE_DESCRIPTOR, *PPCSTREAMRESOURCE_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: POS_CX_EVENT_DEST
req.alt-loc: poscx.h
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

# POS_CX_EVENT_DEST enumeration



## -description
<p>The POS_CX_EVENT_DEST defines which applications receive this event.</p>


## -syntax

````
typedef enum _POS_CX_EVENT_DEST { 
  POS_CX_EVENT_DEST_INVALID       = 0,
  POS_CX_EVENT_DEST_DEVICE_OWNER  = 1,
  POS_CX_EVENT_DEST_ALL           = 2
} POS_CX_EVENT_DEST;
````


## -enum-fields
<dl>

### -field POS_CX_EVENT_DEST_INVALID

<dd>
<p>Specifies that no devices will receive this event.  This value should not be used.</p>
</dd>

### -field POS_CX_EVENT_DEST_DEVICE_OWNER

<dd>
<p>Specifies that only the current claim owner will receive this event.</p>
</dd>

### -field POS_CX_EVENT_DEST_ALL

<dd>
<p>Specifies that the event will be broadcast to all client handles.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Product</p>
</th>
<td width="70%">
<p>Windows 10 or later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Poscx.h (include Poscx.h)</dt>
</dl>
</td>
</tr>
</table>