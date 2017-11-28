---
UID: NS.d3dukmdt._D3DDDI_OPENALLOCATIONINFO
title: D3DDDI_OPENALLOCATIONINFO
author: windows-driver-content
description: The D3DDDI_OPENALLOCATIONINFO structure describes an allocation to be opened.
old-location: display\d3dddi_openallocationinfo.htm
old-project: display
ms.assetid: cd50602a-c4aa-410b-9ed6-56d7237571cd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_OPENALLOCATIONINFO, D3DDDI_OPENALLOCATIONINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_OPENALLOCATIONINFO
req.alt-loc: d3dukmdt.h
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

# D3DDDI_OPENALLOCATIONINFO structure



## -description
<p>The D3DDDI_OPENALLOCATIONINFO structure describes an allocation to be opened.</p>


## -syntax

````
typedef struct _D3DDDI_OPENALLOCATIONINFO {
  D3DKMT_HANDLE hAllocation;
  const VOID    *pPrivateDriverData;
  UINT          PrivateDriverDataSize;
} D3DDDI_OPENALLOCATIONINFO;
````


## -struct-fields
<dl>

### -field <b>hAllocation</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the allocation. The user-mode display driver should use this handle to reference the allocation in the command buffer.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>[in] A pointer to a block of private data, which was passed to the display miniport driver when the resource was created. </p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>[in] The size, in bytes, of the block of private data that is pointed to by <b>pPrivateDriverData</b>.</p>
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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>