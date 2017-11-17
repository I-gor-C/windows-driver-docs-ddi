---
UID: NS.d3dkmthk._D3DKMT_CREATEBUNDLEOBJECT
title: D3DKMT_CREATEBUNDLEOBJECT
author: windows-driver-content
description: Holds information to create a bundle object.
old-location: display\d3dkmt-createbundleobject.htm
ms.assetid: dbb01112-9d28-4dbf-88c7-3304d9d6a661
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
req.alt-api: D3DKMT_CREATEBUNDLEOBJECT
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
ms.keywords: D3DKMT_CREATEBUNDLEOBJECT, D3DKMT_CREATEBUNDLEOBJECT
req.iface: 
---

# D3DKMT_CREATEBUNDLEOBJECT structure



## -description
<p>Holds information to create a bundle object.</p>


## -syntax

````
typedef struct _D3DKMT_CREATEBUNDLEOBJECT {
  UINT                cObjects;
  const D3DKMT_HANDLE *phObjects;
  POBJECT_ATTRIBUTES  *ppObjectAttributes;
  POBJECT_ATTRIBUTES  pBundleObjectAttributes;
  DWORD                dwBundleDesiredAccess;
  HANDLE              hNtBundleHandle;
} D3DKMT_CREATEBUNDLEOBJECT, D3DKMT_CREATEBUNDLEOBJECT;
````


## -struct-fields
<dl>

### -field <b>cObjects</b>

<dd>
<p>The number of the DXGK object to be bundled.</p>
</dd>

### -field <b>phObjects</b>

<dd>
<p>A pointer to the array of the DXGK object to be bundled.</p>
</dd>

### -field <b>ppObjectAttributes</b>

<dd>
<p>An array of pointers to object attributes for DXGK objects.</p>
</dd>

### -field <b>pBundleObjectAttributes</b>

<dd>
<p>Object attributes for the bundled object.</p>
</dd>

### -field <b> dwBundleDesiredAccess</b>

<dd>
<p>The desired access for bundle handle.</p>
</dd>

### -field <b>hNtBundleHandle</b>

<dd>
<p>The NT bundle handle.</p>
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