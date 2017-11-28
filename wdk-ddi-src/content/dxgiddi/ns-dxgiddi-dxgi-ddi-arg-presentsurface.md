---
UID: NS.dxgiddi.DXGI_DDI_ARG_PRESENTSURFACE
title: DXGI_DDI_ARG_PRESENTSURFACE
author: windows-driver-content
description: Describes a surface to display.
old-location: display\dxgi_ddi_arg_presentsurface.htm
old-project: display
ms.assetid: 1A1E2644-7411-4D69-8D45-B19D707221AB
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_DDI_ARG_PRESENTSURFACE, DXGI_DDI_ARG_PRESENTSURFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_ARG_PRESENTSURFACE
req.alt-loc: Dxgiddi.h
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

# DXGI_DDI_ARG_PRESENTSURFACE structure



## -description
<p>Describes a surface to display.</p>


## -syntax

````
typedef struct DXGI_DDI_ARG_PRESENTSURFACE {
  DXGI_DDI_HRESOURCE hSurface;
  UINT               SubResourceIndex;
} DXGI_DDI_ARG_PRESENTSURFACE;
````


## -struct-fields
<dl>

### -field <b>hSurface</b>

<dd>
<p>[in] A handle to the resource that contains the surface. </p>
</dd>

### -field <b>SubResourceIndex</b>

<dd>
<p>The zero-based index into the resource, which the handle in the <b>hSurface</b> member specifies. The <b>SubResourceIndex</b> index indicates the surface.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>WDDM 1.3 and later</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>