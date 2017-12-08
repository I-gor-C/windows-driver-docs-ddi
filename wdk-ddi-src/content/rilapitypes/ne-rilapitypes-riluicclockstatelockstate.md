---
UID: NE.rilapitypes.RILUICCLOCKSTATELOCKSTATE
title: RILUICCLOCKSTATELOCKSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluicclockstatelockstate_2.htm
old-project: netvista
ms.assetid: e97ef5bc-e3da-46ca-b593-59dc93e9cb8e
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILUICCLOCKSTATELOCKSTATE, RILUICCLOCKSTATELOCKSTATE
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
req.alt-api: RILUICCLOCKSTATELOCKSTATE
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

# RILUICCLOCKSTATELOCKSTATE enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


## -syntax

````
typedef enum _RILUICCLOCKSTATELOCKSTATE { 
  RIL_UICCLOCKSTATE_VERIFIED,
  RIL_UICCLOCKSTATE_ENABLED,
  RIL_UICCLOCKSTATE_BLOCKED,
  RIL_UICCLOCKSTATE_ALL
} RILUICCLOCKSTATELOCKSTATE;
````


## -enum-fields

### -field RIL_UICCLOCKSTATE_VERIFIED


### -field RIL_UICCLOCKSTATE_ENABLED


### -field RIL_UICCLOCKSTATE_BLOCKED


### -field RIL_UICCLOCKSTATE_ALL


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