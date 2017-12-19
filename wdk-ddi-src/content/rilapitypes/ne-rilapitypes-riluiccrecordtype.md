---
UID: NE.rilapitypes.RILUICCRECORDTYPE
title: RILUICCRECORDTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccrecordtype_2.htm
old-project: NetVista
ms.assetid: 2eb26355-25e9-4edf-9695-08b172593712
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILUICCRECORDTYPE, RILUICCRECORDTYPE
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
req.alt-api: RILUICCRECORDTYPE
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

# RILUICCRECORDTYPE enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILUICCRECORDTYPE { 
  RIL_UICCRECORDTYPE_TRANSPARENT,
  RIL_UICCRECORDTYPE_CYCLIC,
  RIL_UICCRECORDTYPE_LINEAR,
  RIL_UICCRECORDTYPE_BERTLV,
  RIL_UICCRECORDTYPE_MASTER,
  RIL_UICCRECORDTYPE_DEDICATED,
  RIL_UICCRECORDTYPE_MAX
} RILUICCRECORDTYPE;
````


## -enum-fields

### -field RIL_UICCRECORDTYPE_TRANSPARENT


### -field RIL_UICCRECORDTYPE_CYCLIC


### -field RIL_UICCRECORDTYPE_LINEAR


### -field RIL_UICCRECORDTYPE_BERTLV


### -field RIL_UICCRECORDTYPE_MASTER


### -field RIL_UICCRECORDTYPE_DEDICATED


### -field RIL_UICCRECORDTYPE_MAX


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