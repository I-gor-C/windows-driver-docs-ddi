---
UID: NS.RILAPITYPES.RILPOSITIONINFOLTE
title: RILPOSITIONINFOLTE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfolte_2.htm
old-project: netvista
ms.assetid: 4910571e-af1d-4bcf-a2d9-0d5383530171
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILPOSITIONINFOLTE, *LPRILPOSITIONINFOLTE, RILPOSITIONINFOLTE
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
req.alt-api: RILPOSITIONINFOLTE
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

# RILPOSITIONINFOLTE structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


## -syntax

````
typedef struct _RILPOSITIONINFOLTE {
  DWORD  dwParams;
  DWORD  dwMobileCountryCode;
  DWORD  dwMobileNetworkCode;
  DWORD  dwCellID;
  DWORD  dwEARFCN;
  DWORD  dwPhysCellID;
  DWORD  dwTAC;
  LONG   dwRSRP;
  LONG   dwRSRQ;
  DWORD  dwTimingAdvance;
} RILPOSITIONINFOLTE, RILPOSITIONINFOLTE;
````


## -struct-fields

### -field dwParams


### -field dwMobileCountryCode


### -field dwMobileNetworkCode


### -field dwCellID


### -field dwEARFCN


### -field dwPhysCellID


### -field dwTAC


### -field dwRSRP


### -field dwRSRQ


### -field dwTimingAdvance


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