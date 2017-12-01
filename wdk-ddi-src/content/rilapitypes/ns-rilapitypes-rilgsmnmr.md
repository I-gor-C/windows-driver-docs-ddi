---
UID: NS.rilapitypes.RILGSMNMR
title: RILGSMNMR
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilgsmnmr_2.htm
old-project: netvista
ms.assetid: 9689a069-1235-4898-9610-3023f6e80dda
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILGSMNMR, RILGSMNMR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILGSMNMR
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
req.iface: 
req.product: Windows 10 or later.
---

# RILGSMNMR structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILGSMNMR {
  DWORD  dwParams;
  DWORD  dwMobileCountryCode;
  DWORD  dwMobileNetworkCode;
  DWORD  dwLocationAreaCode;
  DWORD  dwCellID;
  DWORD  dwARFCN;
  DWORD  dwBaseStationID;
  DWORD  dwRxLevel;
} RILGSMNMR, RILGSMNMR;
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

### -field <b>dwARFCN</b>

<dd></dd>

### -field <b>dwBaseStationID</b>

<dd></dd>

### -field <b>dwRxLevel</b>

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