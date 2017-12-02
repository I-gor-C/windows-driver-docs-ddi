---
UID: NE.rilapitypes.RILTDSCDMAMRLPARAMMASK
title: RILTDSCDMAMRLPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riltdscdmamrlparammask_2.htm
old-project: netvista
ms.assetid: 7e23aa74-e811-4621-bdf7-a2d8b7715f9d
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
req.alt-api: RILTDSCDMAMRLPARAMMASK
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

# RILTDSCDMAMRLPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILTDSCDMAMRLPARAMMASK { 
  RIL_PARAM_TDSCDMAMRL_MNC,
  RIL_PARAM_TDSCDMAMRL_LAC,
  RIL_PARAM_TDSCDMAMRL_CELLID,
  RIL_PARAM_TDSCDMAMRL_UARFCN,
  RIL_PARAM_TDSCDMAMRL_CELLPARAM,
  RIL_PARAM_TDSCDMAMRL_RSCP,
  RIL_PARAM_TDSCDMAMRL_PATHLOSS,
  RIL_PARAM_TDSCDMAMRL_ALL
} RILTDSCDMAMRLPARAMMASK;
````


## -enum-fields
<dl>

### -field RIL_PARAM_TDSCDMAMRL_MNC

<dd></dd>

### -field RIL_PARAM_TDSCDMAMRL_LAC

<dd></dd>

### -field RIL_PARAM_TDSCDMAMRL_CELLID

<dd></dd>

### -field RIL_PARAM_TDSCDMAMRL_UARFCN

<dd></dd>

### -field RIL_PARAM_TDSCDMAMRL_CELLPARAM

<dd></dd>

### -field RIL_PARAM_TDSCDMAMRL_RSCP

<dd></dd>

### -field RIL_PARAM_TDSCDMAMRL_PATHLOSS

<dd></dd>

### -field RIL_PARAM_TDSCDMAMRL_ALL

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