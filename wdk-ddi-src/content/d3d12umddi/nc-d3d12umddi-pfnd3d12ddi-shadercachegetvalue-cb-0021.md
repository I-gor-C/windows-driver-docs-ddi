---
UID: NC.d3d12umddi.PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021
title: PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021
author: windows-driver-content
description: The pfnShaderCacheGetValueCb callback function gets a shader cache value.
old-location: display\pfnd3d12ddi_shadercachegetvalue_cb_0021.htm
old-project: display
ms.assetid: EFC9E2D0-1995-4FE9-840C-7B33081AEF2F
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
req.alt-api: pfnShaderCacheGetValueCb
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

# PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021 callback



## -description
<p>The <i>pfnShaderCacheGetValueCb</i> callback function gets a shader cache value. </p>


## -prototype

````
PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021 pfnShaderCacheGetValueCb;

HRESULT APIENTRY CALLBACK * pfnShaderCacheGetValueCb(
                  D3D12DDI_HRTDEVICE              hRTDevice,
                  D3D12DDI_HRTPIPELINESTATE       hRTPSO,
  _In_            D3D12DDI_SHADERCACHE_HASH       *pPrecomputedHash,
  _In_      const _reads_bytes_(KeyLen) void      *pKey,
                  SIZE_T                          KeyLen,
  _Out_opt_       _writes_bytes_(*pValueLen) void *pValue,
  _Inout_         SIZE_T                          *pValueLen
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

### -param <i>pValue</i> [out, optional]

<dd>
<p>A pointer to an output value. </p>
</dd>

### -param <i>pValueLen</i> [in, out]

<dd>
<p>The length of the output value.</p>
</dd>
</dl>

## -returns
<p>If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks
<p>Access this callback by using the <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi-shadercache-callbacks-0021.md">D3D12DDI_SHADERCACHE_CALLBACKS_0021</a> structure.</p>

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

## -see-also
<dl>
<dt>
<a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi-shadercache-callbacks-0021.md">D3D12DDI_SHADERCACHE_CALLBACKS_0021</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021 callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
