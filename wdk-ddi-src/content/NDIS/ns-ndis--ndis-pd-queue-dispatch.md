---
UID: NS.ndis._NDIS_PD_QUEUE_DISPATCH
title: NDIS_PD_QUEUE_DISPATCH
author: windows-driver-content
description: This structure contains a provider's driver routines for receive or transmit queues.
old-location: netvista\ndis_pd_queue_dispatch.htm
ms.assetid: F9738CF9-AAC8-413C-A890-D6FAD7EEFD54
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: NDIS_PD_QUEUE_DISPATCH, NDIS_PD_QUEUE_DISPATCH
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

### -field <b><a href="https://msdn.microsoft.com/5EAAEEEC-740E-4F65-B13E-E174A0DF4546">PDPostAndDrainBufferList</a></b>

<dd>
<p>A pointer to the provider's <a href="https://msdn.microsoft.com/5EAAEEEC-740E-4F65-B13E-E174A0DF4546">PDPostAndDrainBufferList</a> routine.</p>
</dd>

### -field <b><a href="https://msdn.microsoft.com/0061E269-4A19-4D65-B988-29DB582BA960">PDQueryQueueDepth</a></b>

<dd>
<p>A pointer to the provider's <a href="https://msdn.microsoft.com/0061E269-4A19-4D65-B988-29DB582BA960">PDQueryQueueDepth</a> routine.</p>
</dd>

### -field <b><a href="https://msdn.microsoft.com/885EC5F7-1C7E-473F-BA2A-B4DDD54A59D2">PDFlushQueue</a></b>

<dd>
<p>A pointer to the provider's <a href="https://msdn.microsoft.com/885EC5F7-1C7E-473F-BA2A-B4DDD54A59D2">PDFlushQueue</a> routine.</p>
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