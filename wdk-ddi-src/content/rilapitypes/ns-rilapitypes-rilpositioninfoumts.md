---
UID: NS.RILAPITYPES.RILPOSITIONINFOUMTS
title: RILPOSITIONINFOUMTS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfoumts_2.htm
old-project: NetVista
ms.assetid: f0603990-d63c-433f-b5ac-c8d0efcc4243
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILPOSITIONINFOUMTS, RILPOSITIONINFOUMTS, *LPRILPOSITIONINFOUMTS
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
req.alt-api: RILPOSITIONINFOUMTS
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

# RILPOSITIONINFOUMTS structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef struct _RILPOSITIONINFOUMTS {
  DWORD  dwParams;
  DWORD  dwMobileCountryCode;
  DWORD  dwMobileNetworkCode;
  DWORD  dwLocationAreaCode;
  DWORD  dwCellID;
  DWORD  dwFrequencyInfoUL;
  DWORD  dwFrequencyInfoDL;
  DWORD  dwFrequencyInfoNT;
  DWORD  dwUARFCN;
  DWORD  dwPrimaryScramblingCode;
  LONG   dwRSCP;
  LONG   dwECNO;
  DWORD  dwPathLoss;
} RILPOSITIONINFOUMTS, RILPOSITIONINFOUMTS;
````


## -struct-fields

### -field dwParams


### -field dwMobileCountryCode


### -field dwMobileNetworkCode


### -field dwLocationAreaCode


### -field dwCellID


### -field dwFrequencyInfoUL


### -field dwFrequencyInfoDL


### -field dwFrequencyInfoNT


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