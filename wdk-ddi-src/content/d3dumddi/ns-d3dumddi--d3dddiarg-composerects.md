---
UID: NS.d3dumddi._D3DDDIARG_COMPOSERECTS
title: D3DDDIARG_COMPOSERECTS
author: windows-driver-content
description: The D3DDDIARG_COMPOSERECTS structure describes the parameters that are used to compose rectangular areas.
old-location: display\d3dddiarg_composerects.htm
old-project: display
ms.assetid: 9360f9c4-e30e-4fc0-ade7-1d98ff8b1d1b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_COMPOSERECTS, D3DDDIARG_COMPOSERECTS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_COMPOSERECTS
req.alt-loc: d3dumddi.h
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

# D3DDDIARG_COMPOSERECTS structure



## -description
<p>The D3DDDIARG_COMPOSERECTS structure describes the parameters that are used to compose rectangular areas. </p>


## -syntax

````
typedef struct _D3DDDIARG_COMPOSERECTS {
  HANDLE                hSrcResource;
  UINT                  SrcSubResourceIndex;
  HANDLE                hDstResource;
  UINT                  DstSubResourceIndex;
  HANDLE                hSrcRectDescsVB;
  UINT                  NumRects;
  HANDLE                hDstRectDescsVB;
  D3DDDI_COMPOSERECTSOP Operation;
  INT                   XOffset;
  INT                   YOffset;
} D3DDDIARG_COMPOSERECTS;
````


## -struct-fields
<dl>

### -field <b>hSrcResource</b>

<dd>
<p>[in] A handle to the source resource that contains the source surface. When the surface is created, the user-mode display driver receives the D3DDDIFMT_A1 (one bit per pixel) value in the <b>Format</b> member and the <b>TextApi</b> bit-field flag in the <b>Flags</b> member of the <a href="..\d3dukmdt\ns-d3dukmdt--d3dddiarg-createresource.md">D3DDDIARG_CREATERESOURCE</a> structure in a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a> function. The surface must be created as part of a texture.</p>
</dd>

### -field <b>SrcSubResourceIndex</b>

<dd>
<p>[in] The index to the source surface within the source resource. </p>
</dd>

### -field <b>hDstResource</b>

<dd>
<p>[in] A handle to the destination resource that contains the destination surface. When the surface is created, the user-mode display driver receives the D3DDDIFMT_A1 (one bit per pixel) value in the <b>Format</b> member of <a href="..\d3dukmdt\ns-d3dukmdt--d3dddiarg-createresource.md">D3DDDIARG_CREATERESOURCE</a> in a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a>. The surface must be created as part of a texture. The surface might have been created with the <b>TextApi</b> bit-field flag. </p>
</dd>

### -field <b>DstSubResourceIndex</b>

<dd>
<p>[in] The index to the destination surface within the destination resource. </p>
</dd>

### -field <b>hSrcRectDescsVB</b>

<dd>
<p>[in] A handle to a vertex buffer that contains an array of D3DCOMPOSERECTSRCDESC structures. Each element in the array defines a rectangle on the source surface. When the vertex buffer is created, the user-mode display driver receives the <b>TextApi</b> bit-field flag in the <b>Flags</b> member of the <a href="..\d3dukmdt\ns-d3dukmdt--d3dddiarg-createresource.md">D3DDDIARG_CREATERESOURCE</a> structure in a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a> function. </p>
</dd>

### -field <b>NumRects</b>

<dd>
<p>[in] The number of rectangular areas to copy, which is the number of D3DCOMPOSERECTDSTDESC structures in the vertex buffer that is identified by the <b>hDstRectDescsVB</b> member. Drivers should ignore calls to <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-composerects.md">ComposeRects</a> with <b>NumRects</b> set to greater than 0xFFFF.</p>
</dd>

### -field <b>hDstRectDescsVB</b>

<dd>
<p>[in] A handle to a vertex buffer that contains an array of D3DCOMPOSERECTDSTDESC structures. Each element in the array defines where to copy a source rectangle on the destination surface. For more information, see the following Remarks section. When the vertex buffer is created, the user-mode display driver receives the <b>TextApi</b> bit-field flag in the <b>Flags</b> member of the <a href="..\d3dukmdt\ns-d3dukmdt--d3dddiarg-createresource.md">D3DDDIARG_CREATERESOURCE</a> structure in a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a> function. </p>
</dd>

### -field <b>Operation</b>

<dd>
<p>[in] A D3DDDI_COMPOSERECTSOP value that describes how to compose the rectangular areas. This member can be one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DDDICOMPOSERECTS_COPY</p>
</td>
<td>
<p>Copy each source bit to the destination.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDICOMPOSERECTS_OR</p>
</td>
<td>
<p>Combine source and destination bits in an OR operation and copy to the destination. </p>
</td>
</tr>
<tr>
<td>
<p>D3DDDICOMPOSERECTS_AND</p>
</td>
<td>
<p>Combine source and destination bits in an AND operation and copy to the destination. </p>
</td>
</tr>
<tr>
<td>
<p>D3DDDICOMPOSERECTS_NEG</p>
</td>
<td>
<p>Combine the negative of the source bits with the destination bits and copy to the destination. [Dest bit &amp; (~ Src bit)]</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>XOffset</b>

<dd>
<p>[in] An offset to add to the <i>x</i>-coordinates of all of the destination rectangular areas. The offset can be negative, which might cause the resultant rectangles to be rejected or clipped. </p>
</dd>

### -field <b>YOffset</b>

<dd>
<p>[in] An offset to add to the <i>y</i>-coordinates of all of the destination rectangular areas. The offset can be negative, which might cause the resultant rectangles to be rejected or clipped. </p>
</dd>
</dl>

## -remarks
<p>The vertex buffers that contain the composing instructions are created with D3DUSAGE_TEXTAPI usage. The following code defines the structures that are contained in the vertex buffer arrays. For more information about these structures, see the DirectX SDK documentation.</p>

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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-composerects.md">ComposeRects</a>
</dt>
<dt>
<a href="display.rect">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_COMPOSERECTS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
