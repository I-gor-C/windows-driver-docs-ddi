---
UID: NE.rilapitypes.RILPHONEBOOKENTRYPARAMMASK
title: RILPHONEBOOKENTRYPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookentryparammask_2.htm
old-project: netvista
ms.assetid: c7c82022-b82d-4f8e-a736-3912d3286189
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
req.alt-api: RILPHONEBOOKENTRYPARAMMASK
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

# RILPHONEBOOKENTRYPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILPHONEBOOKENTRYPARAMMASK { 
  RIL_PARAM_PBE_ADDRESS,
  RIL_PARAM_PBE_TEXT,
  RIL_PARAM_PBE_SECONDNAME,
  RIL_PARAM_PBE_GROUPIDCOUNT,
  RIL_PARAM_PBE_GROUPID,
  RIL_PARAM_PBE_ADDITIONALNUMCOUNT,
  RIL_PARAM_PBE_ADDITIONALNUMSIZE,
  RIL_PARAM_PBE_ADDITIONALNUMOFFSET,
  RIL_PARAM_PBE_EMAILCOUNT,
  RIL_PARAM_PBE_EMAILSIZE,
  RIL_PARAM_PBE_EMAILOFFSET,
  RIL_PARAM_PBE_ALL
} RILPHONEBOOKENTRYPARAMMASK;
````


## -enum-fields
<dl>

### -field RIL_PARAM_PBE_ADDRESS

<dd></dd>

### -field RIL_PARAM_PBE_TEXT

<dd></dd>

### -field RIL_PARAM_PBE_SECONDNAME

<dd></dd>

### -field RIL_PARAM_PBE_GROUPIDCOUNT

<dd></dd>

### -field RIL_PARAM_PBE_GROUPID

<dd></dd>

### -field RIL_PARAM_PBE_ADDITIONALNUMCOUNT

<dd></dd>

### -field RIL_PARAM_PBE_ADDITIONALNUMSIZE

<dd></dd>

### -field RIL_PARAM_PBE_ADDITIONALNUMOFFSET

<dd></dd>

### -field RIL_PARAM_PBE_EMAILCOUNT

<dd></dd>

### -field RIL_PARAM_PBE_EMAILSIZE

<dd></dd>

### -field RIL_PARAM_PBE_EMAILOFFSET

<dd></dd>

### -field RIL_PARAM_PBE_ALL

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