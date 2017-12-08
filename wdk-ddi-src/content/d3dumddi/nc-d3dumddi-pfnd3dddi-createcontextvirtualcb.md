---
UID: NC.d3dumddi.PFND3DDDI_CREATECONTEXTVIRTUALCB
title: PFND3DDDI_CREATECONTEXTVIRTUALCB
author: windows-driver-content
description: pfnCreateContextVirtualCb should be used with contexts that support virtual addressing.
old-location: display\pfncreatecontextvirtualcb.htm
old-project: display
ms.assetid: 7787FEDF-E18C-4120-A073-A13933856F57
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnCreateContextVirtualCb
req.alt-loc: d3dumddi.h
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

# PFND3DDDI_CREATECONTEXTVIRTUALCB callback



## -description
<p><b>pfnCreateContextVirtualCb</b> should be used with contexts that support virtual addressing.</p>


## -prototype

````
PFND3DDDI_CREATECONTEXTVIRTUALCB pfnCreateContextVirtualCb;

HRESULT APIENTRY CALLBACK* pfnCreateContextVirtualCb(
  _In_    HANDLE                 hDevice,
  _Inout_ D3DDDICB_CREATECONTEXT *pData
)
{ ... }
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p>A handle to the display device.</p>
</dd>

### -param pData [in, out]

<dd>
<p>A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-createcontextvirtual.md">D3DDDICB_CREATECONTEXTVIRTUAL</a> structure that describes the context to create.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The context was successfully created.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
        Could not allocate memory that was required for the operation to complete.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other <b>HRESULT</b> values.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>