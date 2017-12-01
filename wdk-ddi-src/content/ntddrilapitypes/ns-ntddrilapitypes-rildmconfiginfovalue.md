---
UID: NS.ntddrilapitypes.RILDMCONFIGINFOVALUE
title: RILDMCONFIGINFOVALUE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildmconfiginfovalue.htm
old-project: netvista
ms.assetid: dda43544-4609-4674-9616-8e09939f0c39
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILDMCONFIGINFOVALUE, RILDMCONFIGINFOVALUE, *LPRILDMCONFIGINFOVALUE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILDMCONFIGINFOVALUE
req.alt-loc: ntddrilapitypes.h
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
---

# RILDMCONFIGINFOVALUE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILDMCONFIGINFOVALUE {
  DWORD                cbSize;
  RILDMCONFIGINFOTYPE  dwType;
  BOOL                 fValue;
  DWORD                dwValue;
  WCHAR [256]          wszValue;
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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>