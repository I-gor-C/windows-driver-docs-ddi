---
UID: NS.rilapitypes.RILRFSTATE~r1
title: RILRFSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilrfstate_2.htm
old-project: netvista
ms.assetid: 1e185734-21d9-4047-9e74-cf5a765857ed
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILRFSTATE,
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
req.alt-api: RILRFSTATE
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

# RILRFSTATE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILRFSTATE {
  DWORD    cbSize;
  DWORD    dwParams;
  DWORD    dwRFState;
  DWORD    dwRFDataSize;
  BYTE [1] bRFData;
} RILRFSTATE, RILRFSTATE;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwRFState</b>

<dd></dd>

### -field <b>dwRFDataSize</b>

<dd></dd>

### -field <b>bRFData</b>

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