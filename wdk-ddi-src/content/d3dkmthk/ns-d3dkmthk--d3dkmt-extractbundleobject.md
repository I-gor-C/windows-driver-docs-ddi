---
UID: NS.d3dkmthk._D3DKMT_EXTRACTBUNDLEOBJECT
title: D3DKMT_EXTRACTBUNDLEOBJECT
author: windows-driver-content
description: Used to extract the bundle object.
old-location: display\d3dkmt-extractbundleobject.htm
old-project: display
ms.assetid: 85112ddb-47e6-4874-bd64-a7e4d7ca0fd3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_EXTRACTBUNDLEOBJECT, D3DKMT_EXTRACTBUNDLEOBJECT
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

### -field hNtBundleHandle

<dd>
<p>The NT bundle handle.</p>
</dd>

### -field cObjects

<dd>
<p>The number of the DXGK object to be unbundled.</p>
</dd>

### -field pdwDesiredAccess

<dd>
<p>The desired access for each NT handle for DXGK objects.</p>
</dd>

### -field phNtHandles

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