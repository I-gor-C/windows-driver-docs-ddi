---
UID: NS.rilapitypes.RILREMOTEPARTYINFO~r1
title: RILREMOTEPARTYINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilremotepartyinfo_2.htm
old-project: netvista
ms.assetid: 0ca17e70-1e50-4b62-89ec-0e92ad6e846b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILREMOTEPARTYINFO,
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
req.alt-api: RILREMOTEPARTYINFO
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

# RILREMOTEPARTYINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILREMOTEPARTYINFO {
  DWORD                         cbSize;
  DWORD                         dwParams;
  DWORD                         dwExecutor;
  RILADDRESS                    raAddress;
  RILSUBADDRESS                 rsaSubAddress;
  WCHAR [MAXLENGTH_DESCRIPTION] wszDescription;
  RILREMOTEPARTYINFOVALUE       dwNumberPresentationIndicator;
  RILREMOTEPARTYINFOVALUE       dwNamePresentationIndicator;
  DWORD                         dwID;
} RILREMOTEPARTYINFO, RILREMOTEPARTYINFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwExecutor</b>

<dd></dd>

### -field <b>raAddress</b>

<dd></dd>

### -field <b>rsaSubAddress</b>

<dd></dd>

### -field <b>wszDescription</b>

<dd></dd>

### -field <b>dwNumberPresentationIndicator</b>

<dd></dd>

### -field <b>dwNamePresentationIndicator</b>

<dd></dd>

### -field <b>dwID</b>

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