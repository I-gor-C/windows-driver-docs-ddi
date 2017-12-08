---
UID: NE.rilapitypes.RILIMSSYSTEMTYPE
title: RILIMSSYSTEMTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimssystemtype_2.htm
old-project: netvista
ms.assetid: 94c37721-372f-448f-8cd9-d4c64dd285cb
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILIMSSYSTEMTYPE, RILIMSSYSTEMTYPE
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
req.alt-api: RILIMSSYSTEMTYPE
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

# RILIMSSYSTEMTYPE enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


## -syntax

````
typedef enum _RILIMSSYSTEMTYPE { 
  RIL_IMSSYSTEMTYPE_WIFI,
  RIL_IMSSYSTEMTYPE_LTE,
  RIL_IMSSYSTEMTYPE_MAX
} RILIMSSYSTEMTYPE;
````


## -enum-fields

### -field RIL_IMSSYSTEMTYPE_WIFI


### -field RIL_IMSSYSTEMTYPE_LTE


### -field RIL_IMSSYSTEMTYPE_MAX


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