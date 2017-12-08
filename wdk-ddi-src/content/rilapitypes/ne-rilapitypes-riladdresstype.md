---
UID: NE.rilapitypes.RILADDRESSTYPE
title: RILADDRESSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riladdresstype_2.htm
old-project: netvista
ms.assetid: de21f647-9372-4572-bf45-581361032911
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILADDRESSTYPE, RILADDRESSTYPE
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
req.alt-api: RILADDRESSTYPE
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

# RILADDRESSTYPE enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


## -syntax

````
typedef enum _RILADDRESSTYPE { 
  RIL_ADDRTYPE_INTERNATIONAL,
  RIL_ADDRTYPE_NATIONAL,
  RIL_ADDRTYPE_NETWKSPECIFIC,
  RIL_ADDRTYPE_SUBSCRIBER,
  RIL_ADDRTYPE_ALPHANUM,
  RIL_ADDRTYPE_ABBREV,
  RIL_ADDRTYPE_IP,
  RIL_ADDRTYPE_EMAIL,
  RIL_ADDRTYPE_URI,
  RIL_ADDRTYPE_MAX
} RILADDRESSTYPE;
````


## -enum-fields

### -field RIL_ADDRTYPE_INTERNATIONAL


### -field RIL_ADDRTYPE_NATIONAL


### -field RIL_ADDRTYPE_NETWKSPECIFIC


### -field RIL_ADDRTYPE_SUBSCRIBER


### -field RIL_ADDRTYPE_ALPHANUM


### -field RIL_ADDRTYPE_ABBREV


### -field RIL_ADDRTYPE_IP


### -field RIL_ADDRTYPE_EMAIL


### -field RIL_ADDRTYPE_URI


### -field RIL_ADDRTYPE_MAX


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