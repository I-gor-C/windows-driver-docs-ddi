---
UID: NS.bdatypes._BDA_GDDS_DATA
title: BDA_GDDS_DATA
author: windows-driver-content
description: TBD.
old-location: stream\bda_gdds_data.htm
ms.assetid: 2BBF14E3-8E1A-42AF-9C26-7F886FD2B945
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_GDDS_DATA
req.alt-loc: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: BDA_GDDS_DATA, BDA_GDDS_DATA, *P_BDA_GDDS_DATA
req.iface: 
---

# BDA_GDDS_DATA structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _BDA_GDDS_DATA {
  PBDARESULT lResult;
  ULONG      ulDataLength;
  ULONG      ulPercentageProgress;
  ULONG      argbData[MIN_DIMENSION];
} BDA_GDDS_DATA, *P_BDA_GDDS_DATA;
````


## -struct-fields
<dl>

### -field <b>lResult</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulDataLength</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulPercentageProgress</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>argbData</b>

<dd>
<p>TBD</p>
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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>