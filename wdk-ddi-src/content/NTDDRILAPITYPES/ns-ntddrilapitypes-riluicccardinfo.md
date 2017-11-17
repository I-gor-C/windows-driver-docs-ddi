---
UID: NS.ntddrilapitypes.RILUICCCARDINFO
title: RILUICCCARDINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluicccardinfo.htm
ms.assetid: 761f1ab6-75e6-4c40-b79c-01f2e92df495
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILUICCCARDINFO
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
ms.keywords: RILUICCCARDINFO, RILUICCCARDINFO, *LPRILUICCCARDINFO
req.iface: 
---

# RILUICCCARDINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILUICCCARDINFO {
  DWORD              cbSize;
  DWORD              dwParams;
  BOOL               fIsVirtualCard;
  BYTE [10]          IccId;
  DWORD              dwNumApps;
  RILUICCAPPINFO [1] AppInfo;
} RILUICCCARDINFO, RILUICCCARDINFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>fIsVirtualCard</b>

<dd></dd>

### -field <b>IccId</b>

<dd></dd>

### -field <b>dwNumApps</b>

<dd></dd>

### -field <b>AppInfo</b>

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