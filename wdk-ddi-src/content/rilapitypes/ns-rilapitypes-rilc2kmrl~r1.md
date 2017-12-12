---
UID: NS.RILAPITYPES.RILC2KMRL~R1
title: RILC2KMRL
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilc2kmrl_2.htm
old-project: netvista
ms.assetid: a06d81d1-9ecc-41da-b0ad-fa878fac382b
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILC2KMRL, *LPRILC2KMRL, RILC2KMRL
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
req.alt-api: RILC2KMRL
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

# RILC2KMRL structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef struct _RILC2KMRL {
  DWORD  dwParams;
  BOOL   fServing;
  DWORD  dwNID;
  DWORD  dwSID;
  DWORD  dwBaseStationID;
  DWORD  dwBaseLat;
  DWORD  dwBaseLong;
  DWORD  dwRefPN;
  DWORD  dwGPSSeconds;
  DWORD  dwPilotStrength;
} RILC2KMRL, RILC2KMRL;
````


## -struct-fields

### -field dwParams


### -field fServing


### -field dwNID


### -field dwSID


### -field dwBaseStationID


### -field dwBaseLat


### -field dwBaseLong


### -field dwRefPN


### -field dwGPSSeconds


### -field dwPilotStrength


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