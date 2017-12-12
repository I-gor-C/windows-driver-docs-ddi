---
UID: NE.rilapitypes.RILUICCSLOTSTATE
title: RILUICCSLOTSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccslotstate_2.htm
old-project: netvista
ms.assetid: 472f7354-4b51-4fac-857e-d93083f160e8
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILUICCSLOTSTATE, RILUICCSLOTSTATE
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
req.alt-api: RILUICCSLOTSTATE
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

# RILUICCSLOTSTATE enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILUICCSLOTSTATE { 
  RIL_UICCSLOT_OFF,
  RIL_UICCSLOT_EMPTY,
  RIL_UICCSLOT_NOT_READY,
  RIL_UICCSLOT_ACTIVE,
  RIL_UICCSLOT_ERROR,
  RIL_UICCSLOT_MAX
} RILUICCSLOTSTATE;
````


## -enum-fields

### -field RIL_UICCSLOT_OFF


### -field RIL_UICCSLOT_EMPTY


### -field RIL_UICCSLOT_NOT_READY


### -field RIL_UICCSLOT_ACTIVE


### -field RIL_UICCSLOT_ERROR


### -field RIL_UICCSLOT_MAX


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