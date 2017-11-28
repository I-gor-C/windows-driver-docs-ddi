---
UID: NS.ntddrilapitypes.RILMSGSERVICEINFO
title: RILMSGSERVICEINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgserviceinfo.htm
old-project: netvista
ms.assetid: 21b1c6ef-b8f3-4230-bc3f-7ac19c6cb2d1
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILMSGSERVICEINFO, RILMSGSERVICEINFO, *LPRILMSGSERVICEINFO
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
req.alt-api: RILMSGSERVICEINFO
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

# RILMSGSERVICEINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILMSGSERVICEINFO {
  DWORD  cbSize;
  DWORD  dwParams;
  DWORD  dwMsgSupport;
  DWORD  dwStoreUsed;
  DWORD  dwStoreTotal;
} RILMSGSERVICEINFO, RILMSGSERVICEINFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwMsgSupport</b>

<dd></dd>

### -field <b>dwStoreUsed</b>

<dd></dd>

### -field <b>dwStoreTotal</b>

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