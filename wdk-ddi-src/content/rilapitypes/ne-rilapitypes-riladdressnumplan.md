---
UID: NE.rilapitypes.RILADDRESSNUMPLAN
title: RILADDRESSNUMPLAN
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riladdressnumplan_2.htm
old-project: netvista
ms.assetid: 14c0f786-4616-49f1-aa9c-0e5c8d4f0197
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILADDRESSNUMPLAN, RILADDRESSNUMPLAN
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
req.alt-api: RILADDRESSNUMPLAN
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

# RILADDRESSNUMPLAN enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


## -syntax

````
typedef enum _RILADDRESSNUMPLAN { 
  RIL_NUMPLAN_TELEPHONE,
  RIL_NUMPLAN_DATA,
  RIL_NUMPLAN_TELEX,
  RIL_NUMPLAN_NATIONAL,
  RIL_NUMPLAN_PRIVATE,
  RIL_NUMPLAN_ERMES,
  RIL_NUMPLAN_MAX
} RILADDRESSNUMPLAN;
````


## -enum-fields

### -field RIL_NUMPLAN_TELEPHONE


### -field RIL_NUMPLAN_DATA


### -field RIL_NUMPLAN_TELEX


### -field RIL_NUMPLAN_NATIONAL


### -field RIL_NUMPLAN_PRIVATE


### -field RIL_NUMPLAN_ERMES


### -field RIL_NUMPLAN_MAX


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