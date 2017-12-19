---
UID: NS.RILAPITYPES.RILUMTSMRL
title: RILUMTSMRL
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilumtsmrl_2.htm
old-project: NetVista
ms.assetid: 38235a1e-c9fd-4d4d-96a2-18559e4cf655
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILUMTSMRL, *LPRILUMTSMRL, RILUMTSMRL
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
req.alt-api: RILUMTSMRL
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
req.product: Windows 10 or later.
---

# RILUMTSMRL structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef struct _RILUMTSMRL {
  DWORD  dwParams;
  DWORD  dwMobileCountryCode;
  DWORD  dwMobileNetworkCode;
  DWORD  dwLocationAreaCode;
  DWORD  dwCellID;
  DWORD  dwUARFCN;
  DWORD  dwPrimaryScramblingCode;
  LONG   dwRSCP;
  LONG   dwECNO;
  DWORD  dwPathLoss;
} RILUMTSMRL, RILUMTSMRL;
````


## -struct-fields

### -field dwParams


### -field dwMobileCountryCode


### -field dwMobileNetworkCode


### -field dwLocationAreaCode


### -field dwCellID


### -field dwUARFCN


### -field dwPrimaryScramblingCode


### -field dwRSCP


### -field dwECNO


### -field dwPathLoss


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>