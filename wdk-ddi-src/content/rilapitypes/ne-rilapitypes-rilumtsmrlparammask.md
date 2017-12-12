---
UID: NE.rilapitypes.RILUMTSMRLPARAMMASK
title: RILUMTSMRLPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilumtsmrlparammask_2.htm
old-project: netvista
ms.assetid: d0450aeb-8b6e-4ab2-94b7-563503a83e76
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILUMTSMRLPARAMMASK, RILUMTSMRLPARAMMASK
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
req.alt-api: RILUMTSMRLPARAMMASK
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

# RILUMTSMRLPARAMMASK enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILUMTSMRLPARAMMASK { 
  RIL_PARAM_UMTSMRL_MNC,
  RIL_PARAM_UMTSMRL_LAC,
  RIL_PARAM_UMTSMRL_CELLID,
  RIL_PARAM_UMTSMRL_UARFCN,
  RIL_PARAM_UMTSMRL_PRIMARY_SC,
  RIL_PARAM_UMTSMRL_RSCP,
  RIL_PARAM_UMTSMRL_ECNO,
  RIL_PARAM_UMTSMRL_PATHLOSS,
  RIL_PARAM_UMTSMRL_ALL
} RILUMTSMRLPARAMMASK;
````


## -enum-fields

### -field RIL_PARAM_UMTSMRL_MNC


### -field RIL_PARAM_UMTSMRL_LAC


### -field RIL_PARAM_UMTSMRL_CELLID


### -field RIL_PARAM_UMTSMRL_UARFCN


### -field RIL_PARAM_UMTSMRL_PRIMARY_SC


### -field RIL_PARAM_UMTSMRL_RSCP


### -field RIL_PARAM_UMTSMRL_ECNO


### -field RIL_PARAM_UMTSMRL_PATHLOSS


### -field RIL_PARAM_UMTSMRL_ALL


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