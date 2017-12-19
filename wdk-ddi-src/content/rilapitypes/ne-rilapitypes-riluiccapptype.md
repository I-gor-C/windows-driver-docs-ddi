---
UID: NE.rilapitypes.RILUICCAPPTYPE
title: RILUICCAPPTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccapptype_2.htm
old-project: NetVista
ms.assetid: 85c8ee9c-4126-4fd1-96a1-3e3036066258
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILUICCAPPTYPE, RILUICCAPPTYPE
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
req.alt-api: RILUICCAPPTYPE
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

# RILUICCAPPTYPE enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILUICCAPPTYPE { 
  RIL_UICCAPPTYPE_MF,
  RIL_UICCAPPTYPE_MF_SIM,
  RIL_UICCAPPTYPE_MF_RUIM,
  RIL_UICCAPPTYPE_USIM,
  RIL_UICCAPPTYPE_CSIM,
  RIL_UICCAPPTYPE_ISIM,
  RIL_UICCAPPTYPE_MAX
} RILUICCAPPTYPE;
````


## -enum-fields

### -field RIL_UICCAPPTYPE_MF


### -field RIL_UICCAPPTYPE_MF_SIM


### -field RIL_UICCAPPTYPE_MF_RUIM


### -field RIL_UICCAPPTYPE_USIM


### -field RIL_UICCAPPTYPE_CSIM


### -field RIL_UICCAPPTYPE_ISIM


### -field RIL_UICCAPPTYPE_MAX


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