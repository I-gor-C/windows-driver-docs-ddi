---
UID: NS.d3d10umddi.D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW
title: D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW
author: windows-driver-content
description: The D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW structure describes cube textures that are used to create a shader resource view in a call to the CreateShaderResourceView(D3D10_1) function.
old-location: display\d3d10_1ddiarg_texcube_shaderresourceview.htm
ms.assetid: 89d0b6fa-b990-43a9-a943-76d270b507cc
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW
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
ms.keywords: D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW, D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW
req.iface: 
---

# D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW structure



## -description
<p>The D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW structure describes cube textures that are used to create a shader resource view in a call to the <a href="https://msdn.microsoft.com/7a0a92d2-a5df-4bee-a950-8a89aeb3dbb8">CreateShaderResourceView(D3D10_1)</a> function. </p>


## -syntax

````
typedef struct D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW {
  UINT MostDetailedMip;
  UINT MipLevels;
  UINT First2DArrayFace;
  UINT NumCubes;
} D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW;
````


## -struct-fields
<dl>

### -field <b>MostDetailedMip</b>

<dd>
<p>[in] The identifier of the most detailed MIP-map. </p>
</dd>

### -field <b>MipLevels</b>

<dd>
<p>[in] The number of MIP-map levels for the texture. </p>
</dd>

### -field <b>First2DArrayFace</b>

<dd>
<p>[in] The identifier of the first 2-D texture that comprises one or more cube textures. </p>
</dd>

### -field <b>NumCubes</b>

<dd>
<p>[in] The number of cube textures for a shader resource view. </p>
</dd>
</dl>

## -remarks
<p>The value in the <b>First2DArrayFace</b> member added with 6 multiplied by the number in the <b>NumCubes</b> member must be less than or equal to the value in the <b>ArraySize</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541697">D3D10DDIARG_CREATERESOURCE</a> structure for the shader resource whose view is created in a call to the driver's <a href="https://msdn.microsoft.com/7a0a92d2-a5df-4bee-a950-8a89aeb3dbb8">CreateShaderResourceView(D3D10_1)</a> function. That is, the following calculation applies:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions. </p>
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
<a href="https://msdn.microsoft.com/310adb3e-1af4-430e-ba50-bd145ffda361">CalcPrivateShaderResourceViewSize(D3D10_1)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7a0a92d2-a5df-4bee-a950-8a89aeb3dbb8">CreateShaderResourceView(D3D10_1)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541861">D3D10_1DDIARG_CREATESHADERRESOURCEVIEW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541697">D3D10DDIARG_CREATERESOURCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
