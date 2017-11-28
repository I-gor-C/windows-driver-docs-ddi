---
UID: NS.ntddrilapitypes.RILUICCAPPINFO
title: RILUICCAPPINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccappinfo.htm
old-project: netvista
ms.assetid: b3a688fe-928c-458e-ac47-59a9ae61bc5e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILUICCAPPINFO, RILUICCAPPINFO, *LPRILUICCAPPINFO
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
req.alt-api: RILUICCAPPINFO
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

# RILUICCAPPINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILUICCAPPINFO {
  DWORD           cbSize;
  DWORD           dwParams;
  HUICCAPP        hUiccApp;
  RILUICCAPPTYPE  dwUiccAppType;
  DWORD           dwAppIdLength;
  BYTE [32]       bAppId;
  DWORD           dwAppNameLength;
  char [256]      cszAppName;
  DWORD           dwNumPins;
  BYTE [8]        bPinRef;
} RILUICCAPPINFO, RILUICCAPPINFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>hUiccApp</b>

<dd></dd>

### -field <b>dwUiccAppType</b>

<dd></dd>

### -field <b>dwAppIdLength</b>

<dd></dd>

### -field <b>bAppId</b>

<dd></dd>

### -field <b>dwAppNameLength</b>

<dd></dd>

### -field <b>cszAppName</b>

<dd></dd>

### -field <b>dwNumPins</b>

<dd></dd>

### -field <b>bPinRef</b>

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