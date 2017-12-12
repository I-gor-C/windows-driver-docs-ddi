---
UID: NE.rilapitypes.RILNETWORKCODEPARAMMASK
title: RILNETWORKCODEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilnetworkcodeparammask_2.htm
old-project: netvista
ms.assetid: 944a4974-cb1d-4c0c-bca6-2741f16d2b3e
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILNETWORKCODEPARAMMASK, RILNETWORKCODEPARAMMASK
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
req.alt-api: RILNETWORKCODEPARAMMASK
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

# RILNETWORKCODEPARAMMASK enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILNETWORKCODEPARAMMASK { 
  RIL_PARAM_NETWORKCODE_MCC,
  RIL_PARAM_NETWORKCODE_MNC,
  RIL_PARAM_NETWORKCODE_SID,
  RIL_PARAM_NETWORKCODE_NID,
  RIL_PARAM_NETWORKCODE_RI,
  RIL_PARAM_NETWORKCODE_ALL
} RILNETWORKCODEPARAMMASK;
````


## -enum-fields

### -field RIL_PARAM_NETWORKCODE_MCC


### -field RIL_PARAM_NETWORKCODE_MNC


### -field RIL_PARAM_NETWORKCODE_SID


### -field RIL_PARAM_NETWORKCODE_NID


### -field RIL_PARAM_NETWORKCODE_RI


### -field RIL_PARAM_NETWORKCODE_ALL


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