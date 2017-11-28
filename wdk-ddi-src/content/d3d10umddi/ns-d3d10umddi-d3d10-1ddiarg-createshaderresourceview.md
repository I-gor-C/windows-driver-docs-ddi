---
UID: NS.d3d10umddi.D3D10_1DDIARG_CREATESHADERRESOURCEVIEW
title: D3D10_1DDIARG_CREATESHADERRESOURCEVIEW
author: windows-driver-content
description: The D3D10_1DDIARG_CREATESHADERRESOURCEVIEW structure describes the shader resource view to create.
old-location: display\d3d10_1ddiarg_createshaderresourceview.htm
old-project: display
ms.assetid: d899ae74-9ee6-43c9-a8a9-44deb9eaa368
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D10_1DDIARG_CREATESHADERRESOURCEVIEW, D3D10_1DDIARG_CREATESHADERRESOURCEVIEW
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D10_1DDIARG_CREATESHADERRESOURCEVIEW is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_1DDIARG_CREATESHADERRESOURCEVIEW
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

# D3D10_1DDIARG_CREATESHADERRESOURCEVIEW structure



## -description
<p>The D3D10_1DDIARG_CREATESHADERRESOURCEVIEW structure describes the shader resource view to create.</p>


## -syntax

````
typedef struct D3D10_1DDIARG_CREATESHADERRESOURCEVIEW {
  D3D10DDI_HRESOURCE    hDrvResource;
  DXGI_FORMAT           Format;
  D3D10DDIRESOURCE_TYPE ResourceDimension;
  union {
    D3D10DDIARG_BUFFER_SHADERRESOURCEVIEW    Buffer;
    D3D10DDIARG_TEX1D_SHADERRESOURCEVIEW     Tex1D;
    D3D10DDIARG_TEX2D_SHADERRESOURCEVIEW     Tex2D;
    D3D10DDIARG_TEX3D_SHADERRESOURCEVIEW     Tex3D;
    D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW TexCube;
  };
} D3D10_1DDIARG_CREATESHADERRESOURCEVIEW;
````


## -struct-fields
<dl>

### -field <b>hDrvResource</b>

<dd>
<p>[in] A handle to the shader resource. </p>
</dd>

### -field <b>Format</b>

<dd>
<p>[in] A DXGI_FORMAT-typed value that indicates the pixel format of the view.</p>
</dd>

### -field <b>ResourceDimension</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>-typed value that indicates the resource type and dimensionality. </p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_BUFFER, a member in the union that is contained in D3D10_1DDIARG_CREATESHADERRESOURCEVIEW that can hold a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541645">D3D10DDIARG_BUFFER_SHADERRESOURCEVIEW</a> structure for a buffer. </p>
</dd>

### -field <b>Tex1D</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURE1D, a member in the union that is contained in D3D10_1DDIARG_CREATESHADERRESOURCEVIEW that can hold a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541760">D3D10DDIARG_TEX1D_SHADERRESOURCEVIEW</a> structure for a one-dimensional texture. </p>
</dd>

### -field <b>Tex2D</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURE2D, a member in the union that is contained in D3D10_1DDIARG_CREATESHADERRESOURCEVIEW that can hold a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541773">D3D10DDIARG_TEX2D_SHADERRESOURCEVIEW</a> structure for a two-dimensional texture. </p>
</dd>

### -field <b>Tex3D</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURE3D, a member in the union that is contained in D3D10_1DDIARG_CREATESHADERRESOURCEVIEW that can hold a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541789">D3D10DDIARG_TEX3D_SHADERRESOURCEVIEW</a> structure for a three-dimensional texture. </p>
</dd>

### -field <b>TexCube</b>

<dd>
<p>[in] If the value in the <b>ResourceDimension</b> member is set to D3D10DDIRESOURCE_TEXTURECUBE, a member in the union that is contained in D3D10_1DDIARG_CREATESHADERRESOURCEVIEW that can hold a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541865">D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW</a> structure for a cube texture. </p>
</dd>
</dl>

## -remarks
<p>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-1ddi-createshaderresourceview.md">CreateShaderResourceView(D3D10_1)</a> has a major functionality difference from the Direct3D 10.0 version (that is,<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createshaderresourceview.md">CreateShaderResourceView</a>) in regard to the <b>ResourceDimension</b> member of D3D10_1DDIARG_CREATESHADERRESOURCEVIEW. If the Direct3D runtime attempts to create a view on a shader resource, <b>CreateShaderResourceView</b> requires that the <b>ResourceDimension</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff541708">D3D10DDIARG_CREATESHADERRESOURCEVIEW</a> match the <b>ResourceDimension</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff541697">D3D10DDIARG_CREATERESOURCE</a> for the shader resource that was created in a call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a> function. If the Direct3D 10.1 runtime attempts to create a view on a shader resource, <b>CreateShaderResourceView(D3D10_1)</b> allows a slight relaxation for its <b>ResourceDimension</b> member. <b>CreateShaderResourceView(D3D10_1)</b> allows the creation of Tex2D views on TexCube resources. In addition, the distinction between TexCube at the resource level is gone in Direct3D version 10.1. <b>CreateShaderResourceView(D3D10_1)</b> only represents whether it can create a TexCube view. In Direct3D version 10.0, copying a resource, validation of a multiple render target, and so on (that is, various operations that required the resource type to be identical) all included the distinction of TexCube to factor into the resource type. In Direct3D version 10.1, the runtime can determine only Tex2D.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3D10_1DDIARG_CREATESHADERRESOURCEVIEW is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions. </p>
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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-1ddi-calcprivateshaderresourceviewsize.md">CalcPrivateShaderResourceViewSize(D3D10_1)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-1ddi-createshaderresourceview.md">CreateShaderResourceView(D3D10_1)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541865">D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541645">D3D10DDIARG_BUFFER_SHADERRESOURCEVIEW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541760">D3D10DDIARG_TEX1D_SHADERRESOURCEVIEW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541773">D3D10DDIARG_TEX2D_SHADERRESOURCEVIEW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541789">D3D10DDIARG_TEX3D_SHADERRESOURCEVIEW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_1DDIARG_CREATESHADERRESOURCEVIEW structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
