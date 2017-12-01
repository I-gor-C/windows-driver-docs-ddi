---
UID: NS.rilapitypes.RILCALLMODIFICATIONINFO~r1
title: RILCALLMODIFICATIONINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmodificationinfo_2.htm
old-project: netvista
ms.assetid: 2e17e480-325a-4a7c-84b8-07775ddd52bc
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILCALLMODIFICATIONINFO,
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
req.alt-api: RILCALLMODIFICATIONINFO
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

# RILCALLMODIFICATIONINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILCALLMODIFICATIONINFO {
  DWORD                                    cbSize;
  DWORD                                    dwParams;
  DWORD                                    dwExecutor;
  DWORD                                    dwID;
  RILCALLMODIFICATIONINFOMODIFICATIONTYPE  dwModificationType;
  RILCALLTYPE                              dwOldCallType;
  RILCALLTYPE                              dwNewCallType;
  RILADDRESS                               raAddress;
  RILALPHAIDENTIFIER                       aiIdentifier;
} RILCALLMODIFICATIONINFO, RILCALLMODIFICATIONINFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwExecutor</b>

<dd></dd>

### -field <b>dwID</b>

<dd></dd>

### -field <b>dwModificationType</b>

<dd></dd>

### -field <b>dwOldCallType</b>

<dd></dd>

### -field <b>dwNewCallType</b>

<dd></dd>

### -field <b>raAddress</b>

<dd></dd>

### -field <b>aiIdentifier</b>

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