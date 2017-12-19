---
UID: NE.rilapitypes.RILPOSITIONINFOUMTSPARAMMASK
title: RILPOSITIONINFOUMTSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfoumtsparammask_2.htm
old-project: NetVista
ms.assetid: c2e1bf17-130a-4e09-81e3-30100217e1b9
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILPOSITIONINFOUMTSPARAMMASK, RILPOSITIONINFOUMTSPARAMMASK
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
req.alt-api: RILPOSITIONINFOUMTSPARAMMASK
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

# RILPOSITIONINFOUMTSPARAMMASK enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef enum _RILPOSITIONINFOUMTSPARAMMASK { 
  RIL_PARAM_POSITION_UMTS_MNC,
  RIL_PARAM_POSITION_UMTS_LAC,
  RIL_PARAM_POSITION_UMTS_CELLID,
  RIL_PARAM_POSITION_UMTS_FREQINFO_UL,
  RIL_PARAM_POSITION_UMTS_FREQINFO_DL,
  RIL_PARAM_POSITION_UMTS_FREQINFO_NT,
  RIL_PARAM_POSITION_UMTS_UARFCN,
  RIL_PARAM_POSITION_UMTS_PRIMARY_SC,
  RIL_PARAM_POSITION_UMTS_RSCP,
  RIL_PARAM_POSITION_UMTS_ECNO,
  RIL_PARAM_POSITION_UMTS_PATHLOSS,
  RIL_PARAM_POSITION_UMTS_ALL
} RILPOSITIONINFOUMTSPARAMMASK;
````


## -enum-fields

### -field RIL_PARAM_POSITION_UMTS_MNC


### -field RIL_PARAM_POSITION_UMTS_LAC


### -field RIL_PARAM_POSITION_UMTS_CELLID


### -field RIL_PARAM_POSITION_UMTS_FREQINFO_UL


### -field RIL_PARAM_POSITION_UMTS_FREQINFO_DL


### -field RIL_PARAM_POSITION_UMTS_FREQINFO_NT


### -field RIL_PARAM_POSITION_UMTS_UARFCN


### -field RIL_PARAM_POSITION_UMTS_PRIMARY_SC


### -field RIL_PARAM_POSITION_UMTS_RSCP


### -field RIL_PARAM_POSITION_UMTS_ECNO


### -field RIL_PARAM_POSITION_UMTS_PATHLOSS


### -field RIL_PARAM_POSITION_UMTS_ALL


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