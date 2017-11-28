---
UID: NS.rilapitypes.RILCBMSGCONFIG
title: RILCBMSGCONFIG
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcbmsgconfig_2.htm
old-project: netvista
ms.assetid: 7cdab678-5c83-4590-b911-5961db89e7ce
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILCBMSGCONFIG, RILCBMSGCONFIG
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
req.alt-api: RILCBMSGCONFIG
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

# RILCBMSGCONFIG structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILCBMSGCONFIG {
  DWORD                                   cbSize;
  DWORD                                   dwParams;
  DWORD                                   dwGWLConfigInfoSize;
  RILCBGWLCONFIGINFO [RIL_CB_CONFIG_MAX]  GWLConfigInfo;
  DWORD                                   dwCDMAConfigInfoSize;
  RILCBCDMACONFIGINFO [RIL_CB_CONFIG_MAX] CDMAConfigInfo;
} RILCBMSGCONFIG, RILCBMSGCONFIG;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwGWLConfigInfoSize</b>

<dd></dd>

### -field <b>GWLConfigInfo</b>

<dd></dd>

### -field <b>dwCDMAConfigInfoSize</b>

<dd></dd>

### -field <b>CDMAConfigInfo</b>

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