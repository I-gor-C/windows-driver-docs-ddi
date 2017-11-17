---
UID: NS.rilapitypes.RILPOSITIONINFOTDSCDMA
title: RILPOSITIONINFOTDSCDMA
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfotdscdma_2.htm
ms.assetid: 9b0ba2fc-bf8f-40c0-83a2-a791413e4783
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILPOSITIONINFOTDSCDMA
req.alt-loc: rilapitypes.h
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
ms.keywords: RILPOSITIONINFOTDSCDMA, RILPOSITIONINFOTDSCDMA
req.iface: 
req.product: Windows 10 or later.
---

# RILPOSITIONINFOTDSCDMA structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILPOSITIONINFOTDSCDMA {
  DWORD  dwParams;
  DWORD  dwMobileCountryCode;
  DWORD  dwMobileNetworkCode;
  DWORD  dwLocationAreaCode;
  DWORD  dwCellID;
  DWORD  dwUARFCN;
  DWORD  dwCellParameterID;
  DWORD  dwTimingAdvance;
  DWORD  dwRSCP;
  DWORD  dwPathLoss;
} RILPOSITIONINFOTDSCDMA, RILPOSITIONINFOTDSCDMA;
````


## -struct-fields
<dl>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwMobileCountryCode</b>

<dd></dd>

### -field <b>dwMobileNetworkCode</b>

<dd></dd>

### -field <b>dwLocationAreaCode</b>

<dd></dd>

### -field <b>dwCellID</b>

<dd></dd>

### -field <b>dwUARFCN</b>

<dd></dd>

### -field <b>dwCellParameterID</b>

<dd></dd>

### -field <b>dwTimingAdvance</b>

<dd></dd>

### -field <b>dwRSCP</b>

<dd></dd>

### -field <b>dwPathLoss</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>