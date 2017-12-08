---
UID: NE.rilapitypes.RILPOSITIONINFOGSMPARAMMASK
title: RILPOSITIONINFOGSMPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfogsmparammask_2.htm
old-project: netvista
ms.assetid: 7c5fc8bc-6d0c-429c-944f-5f26b7582fa7
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
req.alt-api: RILPOSITIONINFOGSMPARAMMASK
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

# RILPOSITIONINFOGSMPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILPOSITIONINFOGSMPARAMMASK { 
  RIL_PARAM_POSITION_GSM_MNC,
  RIL_PARAM_POSITION_GSM_LAC,
  RIL_PARAM_POSITION_GSM_CELLID,
  RIL_PARAM_POSITION_GSM_TA,
  RIL_PARAM_POSITION_GSM_ARFCN,
  RIL_PARAM_POSITION_GSM_BSID,
  RIL_PARAM_POSITION_GSM_RXLEVEL,
  RIL_PARAM_POSITION_GSM_ALL
} RILPOSITIONINFOGSMPARAMMASK;
````


## -enum-fields
<dl>

### -field RIL_PARAM_POSITION_GSM_MNC

<dd></dd>

### -field RIL_PARAM_POSITION_GSM_LAC

<dd></dd>

### -field RIL_PARAM_POSITION_GSM_CELLID

<dd></dd>

### -field RIL_PARAM_POSITION_GSM_TA

<dd></dd>

### -field RIL_PARAM_POSITION_GSM_ARFCN

<dd></dd>

### -field RIL_PARAM_POSITION_GSM_BSID

<dd></dd>

### -field RIL_PARAM_POSITION_GSM_RXLEVEL

<dd></dd>

### -field RIL_PARAM_POSITION_GSM_ALL

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