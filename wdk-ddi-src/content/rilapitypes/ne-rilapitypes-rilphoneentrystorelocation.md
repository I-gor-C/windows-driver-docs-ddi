---
UID: NE.rilapitypes.RILPHONEENTRYSTORELOCATION
title: RILPHONEENTRYSTORELOCATION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphoneentrystorelocation_2.htm
old-project: netvista
ms.assetid: f9166dfa-e895-4aca-8080-af3cfe9c143f
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILPHONEENTRYSTORELOCATION, RILPHONEENTRYSTORELOCATION
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
req.alt-api: RILPHONEENTRYSTORELOCATION
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

# RILPHONEENTRYSTORELOCATION enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


## -syntax

````
typedef enum _RILPHONEENTRYSTORELOCATION { 
  RIL_PBLOC_UICCFIXDIALING,
  RIL_PBLOC_OWNNUMBERS,
  RIL_PBLOC_UICCPHONEBOOK,
  RIL_PBLOC_UICCSERVICEDIALING,
  RIL_PBLOC_ALL
} RILPHONEENTRYSTORELOCATION;
````


## -enum-fields

### -field RIL_PBLOC_UICCFIXDIALING


### -field RIL_PBLOC_OWNNUMBERS


### -field RIL_PBLOC_UICCPHONEBOOK


### -field RIL_PBLOC_UICCSERVICEDIALING


### -field RIL_PBLOC_ALL


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