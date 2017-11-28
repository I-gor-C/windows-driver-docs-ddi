---
UID: NS.rilapitypes.RILOPERATORINFO~r1
title: RILOPERATORINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riloperatorinfo_2.htm
old-project: netvista
ms.assetid: cf189a5a-8281-4d9a-bad8-a25a1294aec9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILOPERATORINFO,
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
req.alt-api: RILOPERATORINFO
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

# RILOPERATORINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILOPERATORINFO {
  DWORD                  cbSize;
  DWORD                  dwParams;
  DWORD                  dwIndex;
  RILOPERATORINFOSTATUS  dwStatus;
  RILOPERATORNAMES       ronNames;
} RILOPERATORINFO, RILOPERATORINFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwIndex</b>

<dd></dd>

### -field <b>dwStatus</b>

<dd></dd>

### -field <b>ronNames</b>

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