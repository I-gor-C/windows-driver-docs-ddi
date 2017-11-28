---
UID: NS.rilapitypes.RILSUBSCRIBERINFO~r1
title: RILSUBSCRIBERINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsubscriberinfo_2.htm
old-project: netvista
ms.assetid: 4afb3184-0534-43b1-9b88-4aac04d26c4a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILSUBSCRIBERINFO,
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
req.alt-api: RILSUBSCRIBERINFO
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

# RILSUBSCRIBERINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILSUBSCRIBERINFO {
  DWORD                         cbSize;
  DWORD                         dwParams;
  RILADDRESS                    raAddress;
  WCHAR [MAXLENGTH_DESCRIPTION] wszDescription;
  RILSUBSCRIBERINFOSERVICE      dwService;
} RILSUBSCRIBERINFO, RILSUBSCRIBERINFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>raAddress</b>

<dd></dd>

### -field <b>wszDescription</b>

<dd></dd>

### -field <b>dwService</b>

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