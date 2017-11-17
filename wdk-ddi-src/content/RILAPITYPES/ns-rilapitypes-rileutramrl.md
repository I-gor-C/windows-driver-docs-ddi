---
UID: NS.rilapitypes.RILEUTRAMRL
title: RILEUTRAMRL
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rileutramrl_2.htm
ms.assetid: 77a57c67-90ff-489c-a791-56ac0afbec59
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
req.alt-api: RILEUTRAMRL
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
ms.keywords: RILEUTRAMRL, RILEUTRAMRL
req.iface: 
req.product: Windows 10 or later.
---

# RILEUTRAMRL structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILEUTRAMRL {
  DWORD  dwParams;
  DWORD  dwMobileCountryCode;
  DWORD  dwMobileNetworkCode;
  DWORD  dwCellID;
  DWORD  dwEARFCN;
  DWORD  dwPhysCellID;
  DWORD  dwTAC;
  LONG   dwRSRP;
  LONG   dwRSRQ;
} RILEUTRAMRL, RILEUTRAMRL;
````


## -struct-fields
<dl>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwMobileCountryCode</b>

<dd></dd>

### -field <b>dwMobileNetworkCode</b>

<dd></dd>

### -field <b>dwCellID</b>

<dd></dd>

### -field <b>dwEARFCN</b>

<dd></dd>

### -field <b>dwPhysCellID</b>

<dd></dd>

### -field <b>dwTAC</b>

<dd></dd>

### -field <b>dwRSRP</b>

<dd></dd>

### -field <b>dwRSRQ</b>

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