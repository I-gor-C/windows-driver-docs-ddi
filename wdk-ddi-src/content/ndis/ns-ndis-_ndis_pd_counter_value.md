---
UID: NS.NDIS._NDIS_PD_COUNTER_VALUE
title: _NDIS_PD_COUNTER_VALUE
author: windows-driver-content
description: This structure is used to hold a counter value for a queue or filter counter.
old-location: netvista\ndis_pd_counter_value.htm
old-project: netvista
ms.assetid: 0C2424C5-F6EE-4D07-B5C3-CEC3520AFFDC
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _NDIS_PD_COUNTER_VALUE, NDIS_PD_COUNTER_VALUE, *PNDIS_PD_COUNTER_VALUE
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
---

# _NDIS_PD_COUNTER_VALUE structure



## -description
This structure is used to hold a counter value for a queue or filter counter.



## -syntax

````
typedef union _NDIS_PD_COUNTER_VALUE {
  NDIS_PD_RECEIVE_QUEUE_COUNTER  ReceiveQueue;
  NDIS_PD_TRANSMIT_QUEUE_COUNTER TransmitQueue;
  NDIS_PD_FILTER_COUNTER         Filter;
} NDIS_PD_COUNTER_VALUE, *PNDIS_PD_COUNTER_VALUE;
````


## -struct-fields

### -field ReceiveQueue

See <a href="netvista.ndis_pd_receive_queue_counter">NDIS_PD_RECEIVE_QUEUE_COUNTER</a>.


### -field TransmitQueue

See <a href="netvista.ndis_pd_transmit_queue_counter">NDIS_PD_TRANSMIT_QUEUE_COUNTER</a>.


### -field Filter

See <a href="netvista.ndis_pd_filter_counter">NDIS_PD_FILTER_COUNTER</a>.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
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