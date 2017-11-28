---
UID: NS.ntddrilapitypes.RILCALLLIST_V1
title: RILCALLLIST_V1
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcalllist_v1.htm
old-project: netvista
ms.assetid: 09b4f4e7-2688-4d6e-8512-a94c5ce25a79
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILCALLLIST_V1, RILCALLLIST_V1, *LPRILCALLLIST_V1
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
req.alt-api: RILCALLLIST_V1
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

# RILCALLLIST_V1 structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILCALLLIST_V1 {
  DWORD              dwNumberOfCalls;
  RILCALLINFO_V1 [1] rciCallInfo;
} RILCALLLIST_V1, RILCALLLIST_V1;
````


## -struct-fields
<dl>

### -field <b>dwNumberOfCalls</b>

<dd></dd>

### -field <b>rciCallInfo</b>

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