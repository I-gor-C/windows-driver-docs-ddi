---
UID: NE.poscx._POS_CX_EVENT_PRIORITY
title: POS_CX_EVENT_PRIORITY
author: windows-driver-content
description: The POS_CX_EVENT_PRIORITY defines the importance of the event and the order it will be delivered to the client application.
old-location: pos\pos_cx_event_priority.htm
ms.assetid: 835DC1E4-2D49-4D43-A545-5D4288412EC6
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: pos
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: POS_CX_EVENT_PRIORITY
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
ms.keywords: PCSTREAMRESOURCE_DESCRIPTOR, PCSTREAMRESOURCE_DESCRIPTOR, *PPCSTREAMRESOURCE_DESCRIPTOR
req.iface: 
req.product: Windows 10 or later.
---

# POS_CX_EVENT_PRIORITY enumeration



## -description
<p>The POS_CX_EVENT_PRIORITY defines the importance of the event and the order it will be delivered to the client application.</p>


## -syntax

````
typedef enum _POS_CX_EVENT_PRIORITY { 
  POS_CX_EVENT_PRIORITY_INVALID  = 0,
  POS_CX_EVENT_PRIORITY_DATA     = 1,
  POS_CX_EVENT_PRIORITY_CONTROL  = 2
} POS_CX_EVENT_PRIORITY;
````


## -enum-fields
<dl>

### -field <a id="POS_CX_EVENT_PRIORITY_INVALID"></a><a id="pos_cx_event_priority_invalid"></a><b>POS_CX_EVENT_PRIORITY_INVALID</b>

<dd>
<p>Invalid priority. This value should not be used.</p>
</dd>

### -field <a id="POS_CX_EVENT_PRIORITY_DATA"></a><a id="pos_cx_event_priority_data"></a><b>POS_CX_EVENT_PRIORITY_DATA</b>

<dd>
<p>Data level priority delivered in FIFO.</p>
</dd>

### -field <a id="POS_CX_EVENT_PRIORITY_CONTROL"></a><a id="pos_cx_event_priority_control"></a><b>POS_CX_EVENT_PRIORITY_CONTROL</b>

<dd>
<p>Control level priority delivered in FIFO.</p>
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