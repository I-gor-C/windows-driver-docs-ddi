---
UID: NE.rilapitypes.RILNETWORKCODEPARAMMASK
title: RILNETWORKCODEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilnetworkcodeparammask_2.htm
old-project: netvista
ms.assetid: 944a4974-cb1d-4c0c-bca6-2741f16d2b3e
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
req.alt-api: RILNETWORKCODEPARAMMASK
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

# RILNETWORKCODEPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILNETWORKCODEPARAMMASK { 
  RIL_PARAM_NETWORKCODE_MCC,
  RIL_PARAM_NETWORKCODE_MNC,
  RIL_PARAM_NETWORKCODE_SID,
  RIL_PARAM_NETWORKCODE_NID,
  RIL_PARAM_NETWORKCODE_RI,
  RIL_PARAM_NETWORKCODE_ALL
} RILNETWORKCODEPARAMMASK;
````


## -enum-fields
<dl>

### -field RIL_PARAM_NETWORKCODE_MCC

<dd></dd>

### -field RIL_PARAM_NETWORKCODE_MNC

<dd></dd>

### -field RIL_PARAM_NETWORKCODE_SID

<dd></dd>

### -field RIL_PARAM_NETWORKCODE_NID

<dd></dd>

### -field RIL_PARAM_NETWORKCODE_RI

<dd></dd>

### -field RIL_PARAM_NETWORKCODE_ALL

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