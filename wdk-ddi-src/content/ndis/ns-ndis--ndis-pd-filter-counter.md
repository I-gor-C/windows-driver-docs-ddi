---
UID: NS.ndis._NDIS_PD_FILTER_COUNTER
title: NDIS_PD_FILTER_COUNTER
author: windows-driver-content
description: This structure is used to hold counter information for a filter.
old-location: netvista\ndis_pd_filter_counter.htm
old-project: netvista
ms.assetid: 74660B47-0219-4724-AD7E-B20A2BB520EB
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_PD_FILTER_COUNTER, NDIS_PD_FILTER_COUNTER
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
req.alt-api: NDIS_PD_FILTER_COUNTER
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

# NDIS_PD_FILTER_COUNTER structure



## -description
<p>This structure is used to hold counter information for a filter.</p>


## -syntax

````
typedef struct _NDIS_PD_FILTER_COUNTER {
  ULONG64 PacketsMatched;
  ULONG64 BytesMatched;
} NDIS_PD_FILTER_COUNTER, *PNDIS_PD_FILTER_COUNTER;
````


## -struct-fields
<dl>

### -field <b>PacketsMatched</b>

<dd>
<p>The amount of packets that match.</p>
</dd>

### -field <b>BytesMatched</b>

<dd>
<p>The amount of bytes that match.</p>
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