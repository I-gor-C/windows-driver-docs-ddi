---
UID: NE.rilapitypes.RILC2KMRLPARAMMASK
title: RILC2KMRLPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilc2kmrlparammask_2.htm
old-project: netvista
ms.assetid: 267cd226-c1a9-4636-9709-01e3cc947349
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILC2KMRLPARAMMASK, RILC2KMRLPARAMMASK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILC2KMRLPARAMMASK
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

# RILC2KMRLPARAMMASK enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


## -syntax

````
typedef enum _RILC2KMRLPARAMMASK { 
  RIL_PARAM_C2KMRL_NID,
  RIL_PARAM_C2KMRL_SID,
  RIL_PARAM_C2KMRL_BSID,
  RIL_PARAM_C2KMRL_BASELAT,
  RIL_PARAM_C2KMRL_BASELONG,
  RIL_PARAM_C2KMRL_REFPN,
  RIL_PARAM_C2KMRL_GPSSECONDS,
  RIL_PARAM_C2KMRL_PILOTSTRENGTH,
  RIL_PARAM_C2KRML_ALL
} RILC2KMRLPARAMMASK;
````


## -enum-fields

### -field RIL_PARAM_C2KMRL_NID


### -field RIL_PARAM_C2KMRL_SID


### -field RIL_PARAM_C2KMRL_BSID


### -field RIL_PARAM_C2KMRL_BASELAT


### -field RIL_PARAM_C2KMRL_BASELONG


### -field RIL_PARAM_C2KMRL_REFPN


### -field RIL_PARAM_C2KMRL_GPSSECONDS


### -field RIL_PARAM_C2KMRL_PILOTSTRENGTH


### -field RIL_PARAM_C2KRML_ALL


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