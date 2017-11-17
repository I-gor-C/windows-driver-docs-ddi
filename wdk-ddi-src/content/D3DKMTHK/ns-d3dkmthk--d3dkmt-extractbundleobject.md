---
UID: NS.d3dkmthk._D3DKMT_EXTRACTBUNDLEOBJECT
title: D3DKMT_EXTRACTBUNDLEOBJECT
author: windows-driver-content
description: Used to extract the bundle object.
old-location: display\d3dkmt-extractbundleobject.htm
ms.assetid: 85112ddb-47e6-4874-bd64-a7e4d7ca0fd3
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_EXTRACTBUNDLEOBJECT
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
ms.keywords: D3DKMT_EXTRACTBUNDLEOBJECT, D3DKMT_EXTRACTBUNDLEOBJECT
req.iface: 
---

# D3DKMT_EXTRACTBUNDLEOBJECT structure



## -description
<p>Used to extract the bundle object.</p>


## -syntax

````
typedef struct _D3DKMT_EXTRACTBUNDLEOBJECT {
  HANDLE hNtBundleHandle;
  UINT   cObjects;
  DWORD  *pdwDesiredAccess;
  HANDLE *phNtHandles;
} D3DKMT_EXTRACTBUNDLEOBJECT;
````


## -struct-fields
<dl>

### -field <b>hNtBundleHandle</b>

<dd>
<p>The NT bundle handle.</p>
</dd>

### -field <b>cObjects</b>

<dd>
<p>The number of the DXGK object to be unbundled.</p>
</dd>

### -field <b>pdwDesiredAccess</b>

<dd>
<p>The desired access for each NT handle for DXGK objects.</p>
</dd>

### -field <b>phNtHandles</b>

<dd>
<p>The pointer to an array of NT handles for each DXGK object.</p>
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