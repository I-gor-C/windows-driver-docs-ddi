---
UID: NS.RILAPITYPES.RILPOSITIONINFOTDSCDMA
title: RILPOSITIONINFOTDSCDMA
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfotdscdma_2.htm
old-project: NetVista
ms.assetid: 9b0ba2fc-bf8f-40c0-83a2-a791413e4783
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILPOSITIONINFOTDSCDMA, RILPOSITIONINFOTDSCDMA, *LPRILPOSITIONINFOTDSCDMA
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
req.product: Windows 10 or later.
---

# RILPOSITIONINFOTDSCDMA structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



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

### -field dwParams


### -field dwMobileCountryCode


### -field dwMobileNetworkCode


### -field dwLocationAreaCode


### -field dwCellID


### -field dwUARFCN


### -field dwCellParameterID


### -field dwTimingAdvance


### -field dwRSCP


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