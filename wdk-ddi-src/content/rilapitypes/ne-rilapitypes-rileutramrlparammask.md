---
UID: NE.rilapitypes.RILEUTRAMRLPARAMMASK
title: RILEUTRAMRLPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rileutramrlparammask_2.htm
old-project: netvista
ms.assetid: 68f194f5-137e-45a3-94b1-71cd20a27ea3
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILEUTRAMRLPARAMMASK, RILEUTRAMRLPARAMMASK
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
req.alt-api: RILEUTRAMRLPARAMMASK
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

# RILEUTRAMRLPARAMMASK enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILEUTRAMRLPARAMMASK { 
  RIL_PARAM_EUTRAMRL_MNC,
  RIL_PARAM_EUTRAMRL_CELLID,
  RIL_PARAM_EUTRAMRL_EARFCN,
  RIL_PARAM_EUTRAMRL_PHYSCELLID,
  RIL_PARAM_EUTRAMRL_TAC,
  RIL_PARAM_EUTRAMRL_RSRP,
  RIL_PARAM_EUTRAMRL_RSRQ,
  RIL_PARAM_EUTRAMRL_ALL
} RILEUTRAMRLPARAMMASK;
````


## -enum-fields

### -field RIL_PARAM_EUTRAMRL_MNC


### -field RIL_PARAM_EUTRAMRL_CELLID


### -field RIL_PARAM_EUTRAMRL_EARFCN


### -field RIL_PARAM_EUTRAMRL_PHYSCELLID


### -field RIL_PARAM_EUTRAMRL_TAC


### -field RIL_PARAM_EUTRAMRL_RSRP


### -field RIL_PARAM_EUTRAMRL_RSRQ


### -field RIL_PARAM_EUTRAMRL_ALL


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