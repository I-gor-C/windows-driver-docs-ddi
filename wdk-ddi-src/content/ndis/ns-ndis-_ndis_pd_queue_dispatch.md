---
UID: NS.NDIS._NDIS_PD_QUEUE_DISPATCH
title: _NDIS_PD_QUEUE_DISPATCH
author: windows-driver-content
description: This structure contains a provider's driver routines for receive or transmit queues.
old-location: netvista\ndis_pd_queue_dispatch.htm
old-project: NetVista
ms.assetid: F9738CF9-AAC8-413C-A890-D6FAD7EEFD54
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _NDIS_PD_QUEUE_DISPATCH, NDIS_PD_QUEUE_DISPATCH
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
---

# _NDIS_PD_QUEUE_DISPATCH structure



## -description
This structure contains a provider's driver routines for receive or transmit queues.



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

### -field Header

The <a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a> structure for the <b>NDIS_PD_QUEUE_DISPATCH</b> structure. Set the members of this structure as follows:

<ul>
<li><b>Type</b> = <b>NDIS_OBJECT_TYPE_DEFAULT</b></li>
<li><b>Revision</b> = <b>NDIS_PD_QUEUE_DISPATCH_REVISION_1</b></li>
<li><b>Size</b> = <b>NDIS_SIZEOF_PD_QUEUE_DISPATCH_REVISION_1</b></li>
</ul>

### -field Flags

This member is reserved and must be set to 0.


### -field PDPostAndDrainBufferList

A pointer to the provider's <a href="netvista.pdpostanddrainbufferlist">PDPostAndDrainBufferList</a> routine.


### -field PDQueryQueueDepth

A pointer to the provider's <a href="netvista.pdqueryqueuedepth">PDQueryQueueDepth</a> routine.


### -field PDFlushQueue

A pointer to the provider's <a href="netvista.pdflushqueue">PDFlushQueue</a> routine.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h</dt>
</dl>
</td>
</tr>
</table>