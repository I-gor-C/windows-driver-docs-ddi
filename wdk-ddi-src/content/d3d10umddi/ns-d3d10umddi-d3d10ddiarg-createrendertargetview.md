---
UID: NS.d3d10umddi.D3D10DDIARG_CREATERENDERTARGETVIEW
title: D3D10DDIARG_CREATERENDERTARGETVIEW
author: windows-driver-content
description: The D3D10DDIARG_CREATERENDERTARGETVIEW structure describes the render target view to create.
old-location: display\d3d10ddiarg_createrendertargetview.htm
old-project: display
ms.assetid: 2d21aacb-3b2b-4c33-ac35-9f15c1fa8171
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D10DDIARG_CREATERENDERTARGETVIEW, D3D10DDIARG_CREATERENDERTARGETVIEW
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10DDIARG_CREATERENDERTARGETVIEW
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

# D3D10DDIARG_CREATERENDERTARGETVIEW structure



## -description
<p>The D3D10DDIARG_CREATERENDERTARGETVIEW structure describes the render target view to create.</p>


## -syntax

````
typedef struct D3D10DDIARG_CREATERENDERTARGETVIEW {
  D3D10DDI_HRESOURCE    hDrvResource;
  DXGI_FORMAT           Format;
  D3D10DDIRESOURCE_TYPE ResourceDimension;
  union {
    D3D10DDIARG_BUFFER_RENDERTARGETVIEW  Buffer;
    D3D10DDIARG_TEX1D_RENDERTARGETVIEW   Tex1D;
    D3D10DDIARG_TEX2D_RENDERTARGETVIEW   Tex2D;
    D3D10DDIARG_TEX3D_RENDERTARGETVIEW   Tex3D;
    D3D10DDIARG_TEXCUBE_RENDERTARGETVIEW TexCube;
  };
} D3D10DDIARG_CREATERENDERTARGETVIEW;
````


## -struct-fields
<dl>

### -field <b>hDrvResource</b>

<dd>
<p>[in] A handle to the render target. </p>
</dd>

### -field <b>Format</b>

<dd>
<p>[in] A DXGI_FORMAT-typed value that indicates the pixel format of the render target.</p>
</dd>

### -field <b>ResourceDimension</b>

<dd>
<p>[in] A <a href="display.d3d10ddiresource_type">D3D10DDIRESOURCE_TYPE</a>-typed value that indicates the resource type and dimensionality of the render target. </p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_BUFFER, a member in the union that is contained in D3D10DDIARG_CREATERENDERTARGETVIEW that can hold a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-buffer-rendertargetview.md">D3D10DDIARG_BUFFER_RENDERTARGETVIEW</a> structure for a buffer. </p>
</dd>

### -field <b>Tex1D</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURE1D, a member in the union that is contained in D3D10DDIARG_CREATERENDERTARGETVIEW that can hold a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-tex1d-rendertargetview.md">D3D10DDIARG_TEX1D_RENDERTARGETVIEW</a> structure for a one-dimensional texture. </p>
</dd>

### -field <b>Tex2D</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURE2D, a member in the union that is contained in D3D10DDIARG_CREATERENDERTARGETVIEW that can hold a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-tex2d-rendertargetview.md">D3D10DDIARG_TEX2D_RENDERTARGETVIEW</a> structure for a two-dimensional texture. </p>
</dd>

### -field <b>Tex3D</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURE3D, a member in the union that is contained in D3D10DDIARG_CREATERENDERTARGETVIEW that can hold a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-tex3d-rendertargetview.md">D3D10DDIARG_TEX3D_RENDERTARGETVIEW</a> structure for a three-dimensional texture. </p>
</dd>

### -field <b>TexCube</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURECUBE, a member in the union that is contained in D3D10DDIARG_CREATERENDERTARGETVIEW that can hold a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-texcube-rendertargetview.md">D3D10DDIARG_TEXCUBE_RENDERTARGETVIEW</a> structure for a cube texture. </p>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivaterendertargetviewsize.md">CalcPrivateRenderTargetViewSize</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createrendertargetview.md">CreateRenderTargetView</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-buffer-rendertargetview.md">D3D10DDIARG_BUFFER_RENDERTARGETVIEW</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-tex1d-rendertargetview.md">D3D10DDIARG_TEX1D_RENDERTARGETVIEW</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-tex2d-rendertargetview.md">D3D10DDIARG_TEX2D_RENDERTARGETVIEW</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-tex3d-rendertargetview.md">D3D10DDIARG_TEX3D_RENDERTARGETVIEW</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-texcube-rendertargetview.md">D3D10DDIARG_TEXCUBE_RENDERTARGETVIEW</a>
</dt>
<dt>
<a href="display.d3d10ddiresource_type">D3D10DDIRESOURCE_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10DDIARG_CREATERENDERTARGETVIEW structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
