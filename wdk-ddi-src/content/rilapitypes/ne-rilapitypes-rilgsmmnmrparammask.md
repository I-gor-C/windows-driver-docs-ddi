---
UID: NE.rilapitypes.RILGSMMNMRPARAMMASK
title: RILGSMMNMRPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilgsmmnmrparammask_2.htm
old-project: netvista
ms.assetid: 9e58bd61-9cb7-40fb-a6e5-1e8a8d428774
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILGSMMNMRPARAMMASK, RILGSMMNMRPARAMMASK
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
req.alt-api: RILGSMMNMRPARAMMASK
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

# RILGSMMNMRPARAMMASK enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILGSMMNMRPARAMMASK { 
  RIL_PARAM_GSMNMR_MNC,
  RIL_PARAM_GSMNMR_LAC,
  RIL_PARAM_GSMNMR_CELLID,
  RIL_PARAM_GSMNMR_ARFCN,
  RIL_PARAM_GSMNMR_BSID,
  RIL_PARAM_GSMNMR_RXLEVEL,
  RIL_PARAM_GSMNMR_ALL
} RILGSMMNMRPARAMMASK;
````


## -enum-fields

### -field RIL_PARAM_GSMNMR_MNC


### -field RIL_PARAM_GSMNMR_LAC


### -field RIL_PARAM_GSMNMR_CELLID


### -field RIL_PARAM_GSMNMR_ARFCN


### -field RIL_PARAM_GSMNMR_BSID


### -field RIL_PARAM_GSMNMR_RXLEVEL


### -field RIL_PARAM_GSMNMR_ALL


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