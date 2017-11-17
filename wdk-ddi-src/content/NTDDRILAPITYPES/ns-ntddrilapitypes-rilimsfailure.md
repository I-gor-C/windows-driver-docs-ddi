---
UID: NS.ntddrilapitypes.RILIMSFAILURE
title: RILIMSFAILURE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimsfailure.htm
ms.assetid: 8be10470-3761-4120-8987-00d6fcc9a989
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
req.alt-api: RILIMSFAILURE
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
ms.keywords: RILIMSFAILURE, RILIMSFAILURE, *LPRILIMSFAILURE
req.iface: 
---

# RILIMSFAILURE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILIMSFAILURE {
  DWORD                     cbSize;
  DWORD                     dwParams;
  DWORD                     dwExecutor;
  RILIMSFAILUREMESSAGETYPE  dwMessageType;
  DWORD                     dwMessageSubType;
  DWORD                     dwErrorCode;
  WCHAR [256]               wszErrorString;
} RILIMSFAILURE, RILIMSFAILURE;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwExecutor</b>

<dd></dd>

### -field <b>dwMessageType</b>

<dd></dd>

### -field <b>dwMessageSubType</b>

<dd></dd>

### -field <b>dwErrorCode</b>

<dd></dd>

### -field <b>wszErrorString</b>

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