---
UID: NS.rilapitypes.RILUICCAPPINFO~r1
title: RILUICCAPPINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccappinfo_2.htm
old-project: netvista
ms.assetid: 7673163e-3663-4dc0-b454-bf358b87d62d
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILUICCAPPINFO,
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
req.alt-api: RILUICCAPPINFO
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

# RILUICCAPPINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILUICCAPPINFO {
  DWORD                    cbSize;
  DWORD                    dwParams;
  HUICCAPP                 hUiccApp;
  RILUICCAPPTYPE           dwUiccAppType;
  DWORD                    dwAppIdLength;
  BYTE [MAXLENGTH_APPID]   bAppId;
  DWORD                    dwAppNameLength;
  char [MAXLENGTH_APPNAME] cszAppName;
  DWORD                    dwNumPins;
  BYTE [MAXNUM_PINREF]     bPinRef;
} RILUICCAPPINFO, RILUICCAPPINFO;
````


## -struct-fields
<dl>

### -field cbSize

<dd></dd>

### -field dwParams

<dd></dd>

### -field hUiccApp

<dd></dd>

### -field dwUiccAppType

<dd></dd>

### -field dwAppIdLength

<dd></dd>

### -field bAppId

<dd></dd>

### -field dwAppNameLength

<dd></dd>

### -field cszAppName

<dd></dd>

### -field dwNumPins

<dd></dd>

### -field bPinRef

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