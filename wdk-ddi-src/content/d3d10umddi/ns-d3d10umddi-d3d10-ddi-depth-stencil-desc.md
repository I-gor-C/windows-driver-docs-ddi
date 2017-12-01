---
UID: NS.d3d10umddi.D3D10_DDI_DEPTH_STENCIL_DESC
title: D3D10_DDI_DEPTH_STENCIL_DESC
author: windows-driver-content
description: The D3D10_DDI_DEPTH_STENCIL_DESC structure describes a depth stencil state.
old-location: display\d3d10_ddi_depth_stencil_desc.htm
old-project: display
ms.assetid: d1043d5b-6f2c-4c2f-894a-ae6870865257
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D10_DDI_DEPTH_STENCIL_DESC, D3D10_DDI_DEPTH_STENCIL_DESC
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
req.alt-api: D3D10_DDI_DEPTH_STENCIL_DESC
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

# D3D10_DDI_DEPTH_STENCIL_DESC structure



## -description
<p>The D3D10_DDI_DEPTH_STENCIL_DESC structure describes a depth stencil state.</p>


## -syntax

````
typedef struct D3D10_DDI_DEPTH_STENCIL_DESC {
  BOOL                           DepthEnable;
  D3D10_DDI_DEPTH_WRITE_MASK     DepthWriteMask;
  D3D10_DDI_COMPARISON_FUNC      DepthFunc;
  BOOL                           StencilEnable;
  BOOL                           FrontEnable;
  BOOL                           BackEnable;
  UINT8                          StencilReadMask;
  UINT8                          StencilWriteMask;
  D3D10_DDI_DEPTH_STENCILOP_DESC FrontFace;
  D3D10_DDI_DEPTH_STENCILOP_DESC BackFace;
} D3D10_DDI_DEPTH_STENCIL_DESC;
````


## -struct-fields
<dl>

### -field <b>DepthEnable</b>

<dd>
<p>[in] A Boolean value that specifies whether depth is enabled. <b>TRUE</b> indicates depth is enabled; <b>FALSE</b> indicates depth is disabled. </p>
</dd>

### -field <b>DepthWriteMask</b>

<dd>
<p>[in] A bitwise value that indicates the write properties for a depth stencil state. This member is a valid bitwise OR of the following values from the D3D10_DDI_DEPTH_WRITE_MASK enumeration.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3D10_DDI_DEPTH_WRITE_MASK_ZERO (0)</p>
</td>
<td>
<p>No properties</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_DDI_DEPTH_WRITE_MASK_ALL (1)</p>
</td>
<td>
<p>All properties</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DepthFunc</b>

<dd>
<p>[in] A <a href="..\d3d10umddi\ne-d3d10umddi-d3d10-ddi-comparison-func.md">D3D10_DDI_COMPARISON_FUNC</a>-typed value that indicates the depth-comparison function to perform.</p>
</dd>

### -field <b>StencilEnable</b>

<dd>
<p>[in] A Boolean value that specifies whether stencil is enabled. <b>TRUE</b> indicates stencil is enabled; <b>FALSE</b> indicates stencil is disabled. </p>
</dd>

### -field <b>FrontEnable</b>

<dd>
<p>[in] A Boolean value that specifies whether the performance of stencil operations on forward-facing polygons is enabled. <b>TRUE</b> indicates that the performance on forward-facing polygons is enabled; <b>FALSE</b> indicates that it is disabled. </p>
</dd>

### -field <b>BackEnable</b>

<dd>
<p>[in] A Boolean value that specifies whether the performance of stencil operations on back-facing polygons is enabled. <b>TRUE</b> indicates that the performance on back-facing polygons is enabled; <b>FALSE</b> indicates that it is disabled. </p>
</dd>

### -field <b>StencilReadMask</b>

<dd>
<p>[in] An 8-bit bitwise value that the driver uses in a bitwise AND operation with the stencil value in the stencil buffer immediately after reading the stencil value out of the stencil buffer. </p>
</dd>

### -field <b>StencilWriteMask</b>

<dd>
<p>[in] An 8-bit bitwise value that the driver uses in a bitwise AND operation with the current stencil value before writing the result back out to the stencil buffer. </p>
</dd>

### -field <b>FrontFace</b>

<dd>
<p>[in] A <a href="..\d3d10umddi\ns-d3d10umddi-d3d10-ddi-depth-stencilop-desc.md">D3D10_DDI_DEPTH_STENCILOP_DESC</a> structure that describes the stencil operation to perform on forward-facing polygons.</p>
</dd>

### -field <b>BackFace</b>

<dd>
<p>[in] A <a href="..\d3d10umddi\ns-d3d10umddi-d3d10-ddi-depth-stencilop-desc.md">D3D10_DDI_DEPTH_STENCILOP_DESC</a> structure that describes the stencil operation to perform on back-facing polygons.</p>
</dd>
</dl>

## -remarks
<p>If the <b>StencilEnable</b> member is set to <b>TRUE</b>, the <b>FrontEnable</b> member, <b>BackEnable</b> member, or both must also be set to <b>TRUE</b>. </p>

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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatedepthstencilstatesize.md">CalcPrivateDepthStencilStateSize</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdepthstencilstate.md">CreateDepthStencilState</a>
</dt>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3d10-ddi-comparison-func.md">D3D10_DDI_COMPARISON_FUNC</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10-ddi-depth-stencilop-desc.md">D3D10_DDI_DEPTH_STENCILOP_DESC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_DDI_DEPTH_STENCIL_DESC structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
