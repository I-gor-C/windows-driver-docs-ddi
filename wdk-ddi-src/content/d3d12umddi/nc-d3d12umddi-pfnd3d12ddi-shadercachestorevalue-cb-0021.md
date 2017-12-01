---
UID: NC.d3d12umddi.PFND3D12DDI_SHADERCACHESTOREVALUE_CB_0021
title: PFND3D12DDI_SHADERCACHESTOREVALUE_CB_0021
author: windows-driver-content
description: The pfnShaderCacheStoreValueCb callback function stores a shader cache value.
old-location: display\pfnd3d12ddi_shadercachestorevalue_cb_0021.htm
old-project: display
ms.assetid: F47C4E6E-4B09-4461-85F6-2E850CE2A2F6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnShaderCacheStoreValueCb
req.alt-loc: D3d12umddi.h
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

# PFND3D12DDI_SHADERCACHESTOREVALUE_CB_0021 callback



## -description
<p>The <i>pfnShaderCacheStoreValueCb</i> callback function stores a shader cache value. </p>


## -prototype

````
PFND3D12DDI_SHADERCACHESTOREVALUE_CB_0021 pfnShaderCacheStoreValueCb;

HRESULT APIENTRY CALLBACK * pfnShaderCacheStoreValueCb(
             D3D12DDI_HRTDEVICE           hRTDevice,
             D3D12DDI_HRTPIPELINESTATE    hRTPSO,
  _In_       D3D12DDI_SHADERCACHE_HASH    *pPrecomputedHash,
  _In_ const _reads_bytes_(KeyLen) void   *pKey,
             SIZE_T                       KeyLen,
  _In_ const _reads_bytes_(ValueLen) void *pValue,
             SIZE_T                       ValueLen
)
{ ... }
````


## -parameters
<dl>

### -param <i>hRTDevice</i> 

<dd>
<p>The handle of the device for the driver to use when it calls back into the runtime.</p>
</dd>

### -param <i>hRTPSO</i> 

<dd>
<p>The handle of a PSO.</p>
</dd>

### -param <i>pPrecomputedHash</i> [in]

<dd>
<p>A hash value.</p>
</dd>

### -param <i>pKey</i> [in]

<dd>
<p>A pointer to a key.</p>
</dd>

### -param <i>KeyLen</i> 

<dd>
<p>The length of the key.</p>
</dd>

### -param <i>pValue</i> [in]

<dd>
<p>A pointer to an output value. </p>
</dd>

### -param <i>ValueLen</i> 

<dd>
<p>The length of the output value.</p>
</dd>
</dl>

## -returns
<p>If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks
<p>Access this callback by using the <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi-shadercache-callbacks-0021.md">D3D12DDI_SHADERCACHE_CALLBACKS_0021</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>