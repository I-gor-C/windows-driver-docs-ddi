---
UID: NS.d3d10umddi.D3D11DDIARG_CREATEDEPTHSTENCILVIEW
title: D3D11DDIARG_CREATEDEPTHSTENCILVIEW
author: windows-driver-content
description: The D3D11DDIARG_CREATEDEPTHSTENCILVIEW structure describes the depth-stencil view to create.
old-location: display\d3d11ddiarg_createdepthstencilview.htm
old-project: display
ms.assetid: 563a443b-f460-4fb2-b179-454466c2291b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11DDIARG_CREATEDEPTHSTENCILVIEW, D3D11DDIARG_CREATEDEPTHSTENCILVIEW
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11DDIARG_CREATEDEPTHSTENCILVIEW is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11DDIARG_CREATEDEPTHSTENCILVIEW
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

# D3D11DDIARG_CREATEDEPTHSTENCILVIEW structure



## -description
<p>The D3D11DDIARG_CREATEDEPTHSTENCILVIEW structure describes the depth-stencil view to create.</p>


## -syntax

````
typedef struct D3D11DDIARG_CREATEDEPTHSTENCILVIEW {
  D3D10DDI_HRESOURCE    hDrvResource;
  DXGI_FORMAT           Format;
  D3D10DDIRESOURCE_TYPE ResourceDimension;
  UINT                  Flags;
  union {
    D3D10DDIARG_TEX1D_DEPTHSTENCILVIEW   Tex1D;
    D3D10DDIARG_TEX2D_DEPTHSTENCILVIEW   Tex2D;
    D3D10DDIARG_TEXCUBE_DEPTHSTENCILVIEW TexCube;
  };
} D3D11DDIARG_CREATEDEPTHSTENCILVIEW;
````


## -struct-fields
<dl>

### -field <b>hDrvResource</b>

<dd>
<p>[in] A handle to the base depth stencil resource. </p>
</dd>

### -field <b>Format</b>

<dd>
<p>[in] A DXGI_FORMAT-typed value that indicates the pixel format of the depth-stencil view.</p>
</dd>

### -field <b>ResourceDimension</b>

<dd>
<p>[in] A <a href="display.d3d10ddiresource_type">D3D10DDIRESOURCE_TYPE</a>-typed value that indicates the resource type and dimensionality of the base resource. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A valid bitwise OR of <a href="..\d3d10umddi\ne-d3d10umddi-d3d11-ddi-createdepthstencilview-flag.md">D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG</a>-typed values that indicates the type of depth-stencil view to create. </p>
</dd>

### -field <b>Tex1D</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURE1D, a member in the union that is contained in D3D10DDIARG_CREATEDEPTHSTENCILVIEW that can hold a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-tex1d-depthstencilview.md">D3D10DDIARG_TEX1D_DEPTHSTENCILVIEW</a> structure for a one-dimensional texture. </p>
</dd>

### -field <b>Tex2D</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURE2D, a member in the union that is contained in D3D10DDIARG_CREATEDEPTHSTENCILVIEW that can hold a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-tex2d-depthstencilview.md">D3D10DDIARG_TEX2D_DEPTHSTENCILVIEW</a> structure for a two-dimensional texture. </p>
</dd>

### -field <b>TexCube</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURECUBE, a member in the union that is contained in D3D10DDIARG_CREATEDEPTHSTENCILVIEW that can hold a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-texcube-depthstencilview.md">D3D10DDIARG_TEXCUBE_DEPTHSTENCILVIEW</a> structure for a cube texture. </p>
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
<p>D3D11DDIARG_CREATEDEPTHSTENCILVIEW is supported beginning with the Windows 7 operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivatedepthstencilviewsize.md">CalcPrivateDepthStencilViewSize(D3D11)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createdepthstencilview.md">CreateDepthStencilView(D3D11)</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-tex1d-depthstencilview.md">D3D10DDIARG_TEX1D_DEPTHSTENCILVIEW</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-tex2d-depthstencilview.md">D3D10DDIARG_TEX2D_DEPTHSTENCILVIEW</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-texcube-depthstencilview.md">D3D10DDIARG_TEXCUBE_DEPTHSTENCILVIEW</a>
</dt>
<dt>
<a href="display.d3d10ddiresource_type">D3D10DDIRESOURCE_TYPE</a>
</dt>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3d11-ddi-createdepthstencilview-flag.md">D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11DDIARG_CREATEDEPTHSTENCILVIEW structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
