---
UID: NS.oemrilapitypes.RILGBATOKEN
title: RILGBATOKEN
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilgbatoken.htm
old-project: netvista
ms.assetid: f842d945-1d1e-4f0b-9cc9-82a8401c170a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILGBATOKEN, RILGBATOKEN, *LPRILGBATOKEN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: oemrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILGBATOKEN
req.alt-loc: oemrilapitypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# RILGBATOKEN structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILGBATOKEN {
  DWORD   cbSize;
  DWORD   cbBTIDSize;
  DWORD   dwBTIDOffset;
  DWORD   cbNAFKeyLifetimeSize;
  DWORD   dwNAFKeyLifetimeOffset;
  DWORD   cbNAFKeySize;
  DWORD   dwNAFKeyOffset;
  BYTE [] bData;
} RILGBATOKEN, *LPRILGBATOKEN;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>cbBTIDSize</b>

<dd></dd>

### -field <b>dwBTIDOffset</b>

<dd></dd>

### -field <b>cbNAFKeyLifetimeSize</b>

<dd></dd>

### -field <b>dwNAFKeyLifetimeOffset</b>

<dd></dd>

### -field <b>cbNAFKeySize</b>

<dd></dd>

### -field <b>dwNAFKeyOffset</b>

<dd></dd>

### -field <b>bData</b>

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
<dt>Oemrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>