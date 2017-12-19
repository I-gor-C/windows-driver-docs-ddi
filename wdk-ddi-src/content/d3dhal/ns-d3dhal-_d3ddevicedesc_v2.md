---
UID: NS.D3DHAL._D3DDEVICEDESC_V2
title: _D3DDeviceDesc_V2
author: windows-driver-content
description: The D3DDEVICEDESC_V2 structure contains fields that are already reported in the D3DHAL_D3DEXTENDEDCAPS structure when responding to the GUID_D3DExtendedCaps GUID in DdGetDriverInfo.
old-location: display\d3ddevicedesc_v2.htm
old-project: display
ms.assetid: d8ef093e-81f9-443c-9d85-d0d1b6c03416
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _D3DDeviceDesc_V2, *LPD3DDEVICEDESC_V2, LPD3DDEVICEDESC_V2, D3DDEVICEDESC_V2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDEVICEDESC_V2
req.alt-loc: d3dhal.h
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
---

# _D3DDeviceDesc_V2 structure



## -description
<b>The D3DDEVICEDESC_V2 structure is obsolete; only D3DDEVICEDESC_V1 should be used.</b>

The D3DDEVICEDESC_V2 structure contains fields that are already reported in the 
	 <a href="display.d3dhal_d3dextendedcaps">D3DHAL_D3DEXTENDEDCAPS</a> 
	 structure when responding to the GUID_D3DExtendedCaps GUID in <a href="display.ddgetdriverinfo">DdGetDriverInfo</a>. 
	 


<pre class="syntax" xml:space="preserve"><code>typedef struct _D3DDeviceDesc_V2 {
    DWORD             dwSize;
    DWORD             dwFlags;
    D3DCOLORMODEL     dcmColorModel;
    DWORD             dwDevCaps;
    D3DTRANSFORMCAPS  dtcTransformCaps;
    BOOL              bClipping;
    D3DLIGHTINGCAPS   dlcLightingCaps;
    D3DPRIMCAPS       dpcLineCaps;
    D3DPRIMCAPS       dpcTriCaps;
    DWORD             dwDeviceRenderBitDepth;
    DWORD             dwDeviceZBufferBitDepth;
    DWORD             dwMaxBufferSize;
    DWORD             dwMaxVertexCount;
    DWORD             dwMinTextureWidth;
    DWORD             dwMinTextureHeight;
    DWORD             dwMaxTextureWidth;
    DWORD             dwMaxTextureHeight;
    DWORD             dwMinStippleWidth;
    DWORD             dwMaxStippleWidth;
    DWORD             dwMinStippleHeight;
    DWORD             dwMaxStippleHeight;
} D3DDEVICEDESC_V2, *LPD3DDEVICEDESC_V2;</code></pre>




## -struct-fields


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>