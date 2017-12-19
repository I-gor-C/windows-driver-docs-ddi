---
UID: NE.ntddrilapitypes.RILTDSCDMAKIND
title: RILTDSCDMAKIND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riltdscdmakind.htm
old-project: NetVista
ms.assetid: 61b5d7f8-bd45-448b-b7a1-3e52909a63cb
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILTDSCDMAKIND, RILTDSCDMAKIND
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILTDSCDMAKIND
req.alt-loc: ntddrilapitypes.h
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
---

# RILTDSCDMAKIND enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef enum _RILTDSCDMAKIND { 
  RIL_TDSCDMAKIND_HSDPA,
  RIL_TDSCDMAKIND_HSUPA,
  RIL_TDSCDMAKIND_HSPAPLUS,
  RIL_TDSCDMAKIND_DC_HSPAPLUS,
  RIL_TDSCDMAKIND_MAX
} RILTDSCDMAKIND;
````


## -enum-fields

### -field RIL_TDSCDMAKIND_HSDPA


### -field RIL_TDSCDMAKIND_HSUPA


### -field RIL_TDSCDMAKIND_HSPAPLUS


### -field RIL_TDSCDMAKIND_DC_HSPAPLUS


### -field RIL_TDSCDMAKIND_MAX


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>