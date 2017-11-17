---
UID: NS.ndis._NDIS_PD_RECEIVE_QUEUE_COUNTER
title: NDIS_PD_RECEIVE_QUEUE_COUNTER
author: windows-driver-content
description: This structure is used to hold counter information for a receive queue.
old-location: netvista\ndis_pd_receive_queue_counter.htm
ms.assetid: E42705A4-D018-435E-BA98-3EE5BA5EDE66
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PD_RECEIVE_QUEUE_COUNTER
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
ms.keywords: NDIS_PD_RECEIVE_QUEUE_COUNTER, NDIS_PD_RECEIVE_QUEUE_COUNTER
req.iface: 
---

# NDIS_PD_RECEIVE_QUEUE_COUNTER structure



## -description
<p>This structure is used to hold counter information for a receive queue.</p>


## -syntax

````
typedef struct _NDIS_PD_RECEIVE_QUEUE_COUNTER {
  ULONG64 PacketsReceived;
  ULONG64 BytesReceived;
  ULONG64 PacketsDropped;
} NDIS_PD_RECEIVE_QUEUE_COUNTER, *PNDIS_PD_RECEIVE_QUEUE_COUNTER;
````


## -struct-fields
<dl>

### -field <b>PacketsReceived</b>

<dd>
<p>The amount of packets received.</p>
</dd>

### -field <b>BytesReceived</b>

<dd>
<p>The amount of bytes received.</p>
</dd>

### -field <b>PacketsDropped</b>

<dd>
<p>The amount of packets dropped.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
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