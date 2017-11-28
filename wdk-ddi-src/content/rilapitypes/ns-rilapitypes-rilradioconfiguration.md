---
UID: NS.rilapitypes.RILRADIOCONFIGURATION
title: RILRADIOCONFIGURATION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradioconfiguration_2.htm
old-project: netvista
ms.assetid: bdd43d7d-a526-4a3a-81fc-561ae99d467e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILRADIOCONFIGURATION, RILRADIOCONFIGURATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILRADIOCONFIGURATION
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

# RILRADIOCONFIGURATION structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILRADIOCONFIGURATION {
  DWORD                           dwConfigId;
  RILRADIOCONFIGURATIONRADIOTYPE  dwRadioType;
  DWORD [MAXNUM_EXECUTORS]        dwSystemTypes;
} RILRADIOCONFIGURATION, RILRADIOCONFIGURATION;
````


## -struct-fields
<dl>

### -field <b>dwConfigId</b>

<dd></dd>

### -field <b>dwRadioType</b>

<dd></dd>

### -field <b>dwSystemTypes</b>

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