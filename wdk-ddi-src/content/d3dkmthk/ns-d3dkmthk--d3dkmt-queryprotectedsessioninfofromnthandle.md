---
UID: NS.d3dkmthk._D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE
title: D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE
author: windows-driver-content
description: Used to query information on the protected session.
old-location: display\d3dkmt-queryprotectedsessioninfofromnthandle.htm
old-project: display
ms.assetid: e08d27e7-e9b7-45e7-9bbd-dcb9aa8f85ed
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE, D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE
req.alt-loc: d3dkmthk.h
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

# D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE structure



## -description
<p>Used to query information on the protected session.</p>


## -syntax

````
typedef struct _D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE {
  HANDLE     hNtHandle;
  const VOID *pPrivateDriverData;
  UINT       PrivateDriverDataSize;
  const VOID *pPrivateRuntimeData;
  UINT       PrivateRuntimeDataSize;
} D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE;
````


## -struct-fields
<dl>

### -field <b>hNtHandle</b>

<dd>
<p>The protected NT session handle.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>The private driver data.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>The size of the private driver data.</p>
</dd>

### -field <b>pPrivateRuntimeData</b>

<dd>
<p>The private runtime data.</p>
</dd>

### -field <b>PrivateRuntimeDataSize</b>

<dd>
<p>The size of the private runtime data.</p>
</dd>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>