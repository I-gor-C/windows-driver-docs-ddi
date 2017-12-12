---
UID: NE.rilapitypes.RILREGSTAT
title: RILREGSTAT
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilregstat_2.htm
old-project: netvista
ms.assetid: 6ab187d9-7995-46ad-a12f-47d5b8fa40f0
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RILREGSTAT, RILREGSTAT
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
req.alt-api: RILREGSTAT
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

# RILREGSTAT enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


## -syntax

````
typedef enum _RILREGSTAT { 
  RIL_REGSTAT_UNREGISTERED,
  RIL_REGSTAT_HOME,
  RIL_REGSTAT_ATTEMPTING,
  RIL_REGSTAT_DENIED,
  RIL_REGSTAT_ROAMING,
  RIL_REGSTAT_ROAMING_DOMESTIC,
  RIL_REGSTAT_MAX
} RILREGSTAT;
````


## -enum-fields

### -field RIL_REGSTAT_UNREGISTERED


### -field RIL_REGSTAT_HOME


### -field RIL_REGSTAT_ATTEMPTING


### -field RIL_REGSTAT_DENIED


### -field RIL_REGSTAT_ROAMING


### -field RIL_REGSTAT_ROAMING_DOMESTIC


### -field RIL_REGSTAT_MAX


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