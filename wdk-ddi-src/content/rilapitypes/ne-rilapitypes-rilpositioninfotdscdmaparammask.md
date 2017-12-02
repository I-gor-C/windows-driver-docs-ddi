---
UID: NE.rilapitypes.RILPOSITIONINFOTDSCDMAPARAMMASK
title: RILPOSITIONINFOTDSCDMAPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfotdscdmaparammask_2.htm
old-project: netvista
ms.assetid: c5609649-8e7b-4ec3-8feb-f363536068c6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RIL_WritePhonebookEntry
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
req.alt-api: RILPOSITIONINFOTDSCDMAPARAMMASK
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
req.iface: 
req.product: Windows 10 or later.
---

# RILPOSITIONINFOTDSCDMAPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILPOSITIONINFOTDSCDMAPARAMMASK { 
  RIL_PARAM_POSITION_TDSCDMA_MNC,
  RIL_PARAM_POSITION_TDSCDMA_LAC,
  RIL_PARAM_POSITION_TDSCDMA_CELLID,
  RIL_PARAM_POSITION_TDSCDMA_UARFCN,
  RIL_PARAM_POSITION_TDSCDMA_CELLPARAM,
  RIL_PARAM_POSITION_TDSCDMA_TA,
  RIL_PARAM_POSITION_TDSCDMA_RSCP,
  RIL_PARAM_POSITION_TDSCDMA_PATHLOSS,
  RIL_PARAM_POSITION_TDSCDMA_ALL
} RILPOSITIONINFOTDSCDMAPARAMMASK;
````


## -enum-fields
<dl>

### -field RIL_PARAM_POSITION_TDSCDMA_MNC

<dd></dd>

### -field RIL_PARAM_POSITION_TDSCDMA_LAC

<dd></dd>

### -field RIL_PARAM_POSITION_TDSCDMA_CELLID

<dd></dd>

### -field RIL_PARAM_POSITION_TDSCDMA_UARFCN

<dd></dd>

### -field RIL_PARAM_POSITION_TDSCDMA_CELLPARAM

<dd></dd>

### -field RIL_PARAM_POSITION_TDSCDMA_TA

<dd></dd>

### -field RIL_PARAM_POSITION_TDSCDMA_RSCP

<dd></dd>

### -field RIL_PARAM_POSITION_TDSCDMA_PATHLOSS

<dd></dd>

### -field RIL_PARAM_POSITION_TDSCDMA_ALL

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>