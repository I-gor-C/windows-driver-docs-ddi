---
UID: NS.ndis._NDIS_PD_COUNTER_VALUE
title: NDIS_PD_COUNTER_VALUE
author: windows-driver-content
description: This structure is used to hold a counter value for a queue or filter counter.
old-location: netvista\ndis_pd_counter_value.htm
old-project: netvista
ms.assetid: 0C2424C5-F6EE-4D07-B5C3-CEC3520AFFDC
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_PD_COUNTER_VALUE, NDIS_PD_COUNTER_VALUE, *PNDIS_PD_COUNTER_VALUE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PD_COUNTER_VALUE
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

# NDIS_PD_COUNTER_VALUE structure



## -description
<p>This structure is used to hold a counter value for a queue or filter counter.</p>


## -syntax

````
typedef union _NDIS_PD_COUNTER_VALUE {
  NDIS_PD_RECEIVE_QUEUE_COUNTER  ReceiveQueue;
  NDIS_PD_TRANSMIT_QUEUE_COUNTER TransmitQueue;
  NDIS_PD_FILTER_COUNTER         Filter;
} NDIS_PD_COUNTER_VALUE, *PNDIS_PD_COUNTER_VALUE;
````


## -struct-fields
<dl>

### -field <b>ReceiveQueue</b>

<dd>
<p>See <a href="..\ndis\ns-ndis--ndis-pd-receive-queue-counter.md">NDIS_PD_RECEIVE_QUEUE_COUNTER</a>.</p>
</dd>

### -field <b>TransmitQueue</b>

<dd>
<p>See <a href="..\ndis\ns-ndis--ndis-pd-transmit-queue-counter.md">NDIS_PD_TRANSMIT_QUEUE_COUNTER</a>.</p>
</dd>

### -field <b>Filter</b>

<dd>
<p>See <a href="..\ndis\ns-ndis--ndis-pd-filter-counter.md">NDIS_PD_FILTER_COUNTER</a>.</p>
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