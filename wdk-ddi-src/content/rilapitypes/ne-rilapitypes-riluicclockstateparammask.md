---
UID: NE.rilapitypes.RILUICCLOCKSTATEPARAMMASK
title: RILUICCLOCKSTATEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluicclockstateparammask_2.htm
old-project: NetVista
ms.assetid: 88bdeb85-1ce8-43df-8cf1-4563d90a46ad
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILUICCLOCKSTATEPARAMMASK, RILUICCLOCKSTATEPARAMMASK
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
req.alt-api: RILUICCLOCKSTATEPARAMMASK
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

# RILUICCLOCKSTATEPARAMMASK enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILUICCLOCKSTATEPARAMMASK { 
  RIL_PARAM_UICCLOCKSTATE_LOCKSTATE,
  RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT,
  RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT,
  RIL_PARAM_UICCLOCKSTATE_ALL
} RILUICCLOCKSTATEPARAMMASK;
````


## -enum-fields

### -field RIL_PARAM_UICCLOCKSTATE_LOCKSTATE


### -field RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT


### -field RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT


### -field RIL_PARAM_UICCLOCKSTATE_ALL


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