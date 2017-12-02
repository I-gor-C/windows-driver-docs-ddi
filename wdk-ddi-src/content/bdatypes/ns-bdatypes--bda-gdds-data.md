---
UID: NS.bdatypes._BDA_GDDS_DATA
title: BDA_GDDS_DATA
author: windows-driver-content
description: .
old-location: stream\bda_gdds_data.htm
old-project: stream
ms.assetid: 2BBF14E3-8E1A-42AF-9C26-7F886FD2B945
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDA_GDDS_DATA, BDA_GDDS_DATA, *P_BDA_GDDS_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_GDDS_DATA
req.alt-loc: Bdatypes.h
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
req.iface: 
---

# BDA_GDDS_DATA structure



## -description
<p></p>


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

### -field lResult

<dd></dd>

### -field ulDataLength

<dd></dd>

### -field ulPercentageProgress

<dd></dd>

### -field argbData

<dd></dd>
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