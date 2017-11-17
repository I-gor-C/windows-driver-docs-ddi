---
UID: NC.d3d12umddi.PFND3D12DDI_OPENCRYPTOSESSIONPOLICY_0030
title: PFND3D12DDI_OPENCRYPTOSESSIONPOLICY_0030
author: windows-driver-content
description: Used to open a crypto session policy.
old-location: display\pfnd3d12ddi_opencryptosessionpolicy_0030.htm
ms.assetid: 24B30BE0-9B7E-4946-8677-E3E727A63498
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
req.alt-api: PFND3D12DDI_OPENCRYPTOSESSIONPOLICY_0030
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

# PFND3D12DDI_OPENCRYPTOSESSIONPOLICY_0030 callback



## -description
<p>Used to open a crypto session policy.</p>


## -prototype

````
HRESULT APIENTRY* PFND3D12DDI_OPENCRYPTOSESSIONPOLICY_0030(
             D3D12DDI_HDEVICE                            hDrvDevice,
  _In_ const D3D12DDIARG_OPEN_CRYPTO_SESSION_POLICY_0030 *pArgs,
             D3D12DDI_HCRYPTOSESSIONPOLICY_0030           hDrvCryptoSessionPolicy
);
````


## -parameters
<dl>

### -param <i>hDrvDevice</i> 

<dd>
<p>The hardware device being processed.</p>
</dd>

### -param <i>pArgs</i> [in]

<dd>
<p>The arguments used to open a crypto session policy.</p>
</dd>

### -param <i> hDrvCryptoSessionPolicy</i> 

<dd>
<p>The crypto session policy.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if completed successfully.</p>

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