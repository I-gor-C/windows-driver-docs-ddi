---
UID: NS.rilapitypes.RILC2KMRL~r1
title: RILC2KMRL
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilc2kmrl_2.htm
old-project: netvista
ms.assetid: a06d81d1-9ecc-41da-b0ad-fa878fac382b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILC2KMRL,
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
req.iface: 
req.product: Windows 10 or later.
---

# RILC2KMRL structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dl>

### -field dwParams

<dd></dd>

### -field fServing

<dd></dd>

### -field dwNID

<dd></dd>

### -field dwSID

<dd></dd>

### -field dwBaseStationID

<dd></dd>

### -field dwBaseLat

<dd></dd>

### -field dwBaseLong

<dd></dd>

### -field dwRefPN

<dd></dd>

### -field dwGPSSeconds

<dd></dd>

### -field dwPilotStrength

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