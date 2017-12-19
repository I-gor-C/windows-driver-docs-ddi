---
UID: NE.rilapitypes.RILPOSITIONINFOLTEPARAMMASK
title: RILPOSITIONINFOLTEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfolteparammask_2.htm
old-project: NetVista
ms.assetid: 9c71420f-8b85-4f31-9a08-7f363be75cc0
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILPOSITIONINFOLTEPARAMMASK, RILPOSITIONINFOLTEPARAMMASK
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
req.alt-api: RILPOSITIONINFOLTEPARAMMASK
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

# RILPOSITIONINFOLTEPARAMMASK enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILPOSITIONINFOLTEPARAMMASK { 
  RIL_PARAM_POSITION_LTE_MNC,
  RIL_PARAM_POSITION_LTE_CELLID,
  RIL_PARAM_POSITION_LTE_EARFCN,
  RIL_PARAM_POSITION_LTE_PHYSCELLID,
  RIL_PARAM_POSITION_LTE_TAC,
  RIL_PARAM_POSITION_LTE_RSRP,
  RIL_PARAM_POSITION_LTE_RSRQ,
  RIL_PARAM_POSITION_LTE_TA,
  RIL_PARAM_POSITION_LTE_ALL
} RILPOSITIONINFOLTEPARAMMASK;
````


## -enum-fields

### -field RIL_PARAM_POSITION_LTE_MNC


### -field RIL_PARAM_POSITION_LTE_CELLID


### -field RIL_PARAM_POSITION_LTE_EARFCN


### -field RIL_PARAM_POSITION_LTE_PHYSCELLID


### -field RIL_PARAM_POSITION_LTE_TAC


### -field RIL_PARAM_POSITION_LTE_RSRP


### -field RIL_PARAM_POSITION_LTE_RSRQ


### -field RIL_PARAM_POSITION_LTE_TA


### -field RIL_PARAM_POSITION_LTE_ALL


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