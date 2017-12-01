---
UID: NS.rilapitypes.RILPOSITIONINFOGSM
title: RILPOSITIONINFOGSM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfogsm_2.htm
old-project: netvista
ms.assetid: 6f98e5c7-41f5-434f-a18b-8615494aa220
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILPOSITIONINFOGSM, RILPOSITIONINFOGSM
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
req.alt-api: RILPOSITIONINFOGSM
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

# RILPOSITIONINFOGSM structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILPOSITIONINFOGSM {
  DWORD  dwParams;
  DWORD  dwMobileCountryCode;
  DWORD  dwMobileNetworkCode;
  DWORD  dwLocationAreaCode;
  DWORD  dwCellID;
  DWORD  dwTimingAdvance;
  DWORD  dwARFCN;
  DWORD  dwBaseStationID;
  DWORD  dwRxLevel;
} RILPOSITIONINFOGSM, RILPOSITIONINFOGSM;
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

### -field <b>dwTimingAdvance</b>

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