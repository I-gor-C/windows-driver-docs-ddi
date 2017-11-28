---
UID: NS.ndis._NDIS_PD_QUEUE_DISPATCH
title: NDIS_PD_QUEUE_DISPATCH
author: windows-driver-content
description: This structure contains a provider's driver routines for receive or transmit queues.
old-location: netvista\ndis_pd_queue_dispatch.htm
old-project: netvista
ms.assetid: F9738CF9-AAC8-413C-A890-D6FAD7EEFD54
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_PD_QUEUE_DISPATCH, NDIS_PD_QUEUE_DISPATCH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PD_QUEUE_DISPATCH
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NDIS_PD_QUEUE_DISPATCH structure



## -description
<p>This structure contains a provider's driver routines for receive or transmit queues.</p>


## -syntax

````
typedef struct _NDIS_PD_QUEUE_DISPATCH {
  NDIS_OBJECT_HEADER                         Header;
  ULONG                                      Flags;
  NDIS_PD_POST_AND_DRAIN_BUFFER_LIST_HANDLER PDPostAndDrainBufferList;
  NDIS_PD_QUERY_QUEUE_DEPTH_HANDLER          PDQueryQueueDepth;
  NDIS_PD_FLUSH_QUEUE_HANDLER                PDFlushQueue;
} NDIS_PD_QUEUE_DISPATCH, *PNDIS_PD_QUEUE_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the <b>NDIS_PD_QUEUE_DISPATCH</b> structure. Set the members of this structure as follows:</p>
<ul>
<li><b>Type</b> = <b>NDIS_OBJECT_TYPE_DEFAULT</b></li>
<li><b>Revision</b> = <b>NDIS_PD_QUEUE_DISPATCH_REVISION_1</b></li>
<li><b>Size</b> = <b>NDIS_SIZEOF_PD_QUEUE_DISPATCH_REVISION_1</b></li>
</ul>
</dd>

### -field <b>Flags</b>

<dd>
<p>This member is reserved and must be set to 0.</p>
</dd>

### -field <b><a href="netvista.pdpostanddrainbufferlist">PDPostAndDrainBufferList</a></b>

<dd>
<p>A pointer to the provider's <a href="netvista.pdpostanddrainbufferlist">PDPostAndDrainBufferList</a> routine.</p>
</dd>

### -field <b><a href="netvista.pdqueryqueuedepth">PDQueryQueueDepth</a></b>

<dd>
<p>A pointer to the provider's <a href="netvista.pdqueryqueuedepth">PDQueryQueueDepth</a> routine.</p>
</dd>

### -field <b><a href="netvista.pdflushqueue">PDFlushQueue</a></b>

<dd>
<p>A pointer to the provider's <a href="netvista.pdflushqueue">PDFlushQueue</a> routine.</p>
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
<dt>Ndis.h</dt>
</dl>
</td>
</tr>
</table>