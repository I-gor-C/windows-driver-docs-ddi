---
UID: NS.d3dkmthk._D3DKMT_UMDFILENAMEINFO
title: D3DKMT_UMDFILENAMEINFO
author: windows-driver-content
description: The D3DKMT_UMDFILENAMEINFO structure contains the name of an OpenGL ICD that is based on the specified version of the DirectX runtime.
old-location: display\d3dkmt_umdfilenameinfo.htm
old-project: display
ms.assetid: 456aef5a-f297-4670-8a83-b468569d23ad
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_UMDFILENAMEINFO, D3DKMT_UMDFILENAMEINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_UMDFILENAMEINFO
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

# D3DKMT_UMDFILENAMEINFO structure



## -description
<p>The D3DKMT_UMDFILENAMEINFO structure contains the name of an OpenGL ICD that is based on the specified version of the DirectX runtime. </p>


## -syntax

````
typedef struct _D3DKMT_UMDFILENAMEINFO {
  KMTUMDVERSION Version;
  WCHAR         UmdFileName[MAX_PATH];
} D3DKMT_UMDFILENAMEINFO;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>[in] A KMTUMDVERSION-typed value that indicates the version of the DirectX runtime to retrieve the name of an OpenGL ICD for. The following table lists the possible values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KMTUMDVERSION_DX9 (0)</p>
</td>
<td>
<p>DirectX version 9.0</p>
</td>
</tr>
<tr>
<td>
<p>KMTUMDVERSION_DX10 (1)</p>
</td>
<td>
<p>DirectX version 10.0</p>
</td>
</tr>
<tr>
<td>
<p>KMTUMDVERSION_DX11 (2)</p>
</td>
<td>
<p>DirectX version 11.0</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>UmdFileName</b>

<dd>
<p>[out] A string that contains the name of the OpenGL ICD.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>