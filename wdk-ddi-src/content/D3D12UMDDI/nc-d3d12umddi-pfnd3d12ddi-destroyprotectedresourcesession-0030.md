---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYPROTECTEDRESOURCESESSION_0030
title: PFND3D12DDI_DESTROYPROTECTEDRESOURCESESSION_0030
author: windows-driver-content
description: Used to destroy a protected resource session.
old-location: display\pfnd3d12ddi_destroyprotectedresourcesession_0030.htm
ms.assetid: B247AB7B-D133-43FE-A208-CF5E3C7F7DBE
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFND3D12DDI_DESTROYPROTECTEDRESOURCESESSION_0030
req.alt-loc: d3d12umddi.h
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
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
req.iface: 
---

# PFND3D12DDI_DESTROYPROTECTEDRESOURCESESSION_0030 callback



## -description
<p>Used to destroy a protected resource session.</p>


## -prototype

````
VOID APIENTRY* PFND3D12DDI_DESTROYPROTECTEDRESOURCESESSION_0030(
   D3D12DDI_HDEVICE                        hDrvDevice,
   D3D12DDI_HPROTECTEDRESOURCESESSION_0030 hDrvProtectedResourceSession
);
````


## -parameters
<dl>

### -param <i>hDrvDevice</i> 

<dd>
<p>The hardware device being processed.</p>
</dd>

### -param <i>hDrvProtectedResourceSession</i> 

<dd>
<p>The protected resource session.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>