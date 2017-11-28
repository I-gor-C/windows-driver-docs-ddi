---
UID: NS.rilapitypes.RILDMCONFIGINFOVALUE
title: RILDMCONFIGINFOVALUE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildmconfiginfovalue_2.htm
old-project: netvista
ms.assetid: 6b917b11-a2f2-4b8b-9964-2d7b4a6a1871
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILDMCONFIGINFOVALUE, RILDMCONFIGINFOVALUE
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
req.alt-api: RILDMCONFIGINFOVALUE
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

# RILDMCONFIGINFOVALUE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILDMCONFIGINFOVALUE {
  DWORD                                cbSize;
  RILDMCONFIGINFOTYPE                  dwType;
  BOOL                                 fValue;
  DWORD                                dwValue;
  WCHAR [MAXLENGTH_DMCONFIGINFOSTRING] wszValue;
} RILDMCONFIGINFOVALUE, RILDMCONFIGINFOVALUE;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwType</b>

<dd></dd>

### -field <b>fValue</b>

<dd></dd>

### -field <b>dwValue</b>

<dd></dd>

### -field <b>wszValue</b>

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