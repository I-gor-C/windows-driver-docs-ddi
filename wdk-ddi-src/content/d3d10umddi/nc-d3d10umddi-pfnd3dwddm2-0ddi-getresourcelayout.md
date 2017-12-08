---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_GETRESOURCELAYOUT
title: PFND3DWDDM2_0DDI_GETRESOURCELAYOUT
author: windows-driver-content
description: The pfnGetResourceLayout callback function supports getting resource layout information.
old-location: display\pfnd3dwddm2_0ddi_getresourcelayout.htm
old-project: display
ms.assetid: 0158F1B4-AA6E-41F9-BAEF-A3C688758205
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnGetResourceLayout
req.alt-loc: d3d10umddi.h
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

# PFND3DWDDM2_0DDI_GETRESOURCELAYOUT callback



## -description
<p>The <i>pfnGetResourceLayout</i> callback function supports getting resource layout information. </p>


## -prototype

````
PFND3DWDDM2_0DDI_GETRESOURCELAYOUT pfnGetResourceLayout;

VOID APIENTRY* pfnGetResourceLayout(
            D3D10DDI_HDEVICE                                            hDevice,
            D3D10DDI_HRESOURCE                                          hResource,
            UINT                                                        SubresourceCount,
  _Out_     D3DKMT_HANDLE                                               *Handle,
  _Out_     D3DWDDM2_0DDI_TEXTURE_LAYOUT                                *TextureLayout,
  _Out_     UINT                                                        *pMipLevelSwizzleTransition,
  _Out_opt_ _writes_(SubresourceCount) D3DWDDM2_0DDI_SUBRESOURCE_LAYOUT *SubresourceLayout
)
{ ... }
````


## -parameters
<dl>

### -param hDevice 

<dd>
<p>A device handle.</p>
</dd>

### -param hResource 

<dd>
<p>A resource handle. </p>
</dd>

### -param SubresourceCount 

<dd>
<p>The subresource count.</p>
</dd>

### -param Handle [out]

<dd>
<p>A kernel handle.</p>
</dd>

### -param TextureLayout [out]

<dd>
<p>A pointer to a texture layout.</p>
</dd>

### -param pMipLevelSwizzleTransition [out]

<dd>
<p>A pointer to a MIP level swizzle transition. </p>
</dd>

### -param SubresourceLayout [out, optional]

<dd>
<p>A pointer to the subresource layout.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>