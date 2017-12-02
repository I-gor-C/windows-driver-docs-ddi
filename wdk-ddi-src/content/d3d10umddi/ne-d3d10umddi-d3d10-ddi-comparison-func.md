---
UID: NE.d3d10umddi.D3D10_DDI_COMPARISON_FUNC
title: D3D10_DDI_COMPARISON_FUNC
author: windows-driver-content
description: The D3D10_DDI_COMPARISON_FUNC enumeration type contains values that identify the comparison function to perform.
old-location: display\d3d10_ddi_comparison_func.htm
old-project: display
ms.assetid: 32a823e2-324a-45f3-82ad-e9f99749dc85
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_DDI_COMPARISON_FUNC
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

# D3D10_DDI_COMPARISON_FUNC enumeration



## -description
<p>The D3D10_DDI_COMPARISON_FUNC enumeration type contains values that identify the comparison function to perform.</p>


## -syntax

````
typedef enum D3D10_DDI_COMPARISON_FUNC { 
  D3D10_DDI_COMPARISON_NEVER          = 1,
  D3D10_DDI_COMPARISON_LESS           = 2,
  D3D10_DDI_COMPARISON_EQUAL          = 3,
  D3D10_DDI_COMPARISON_LESS_EQUAL     = 4,
  D3D10_DDI_COMPARISON_GREATER        = 5,
  D3D10_DDI_COMPARISON_NOT_EQUAL      = 6,
  D3D10_DDI_COMPARISON_GREATER_EQUAL  = 7,
  D3D10_DDI_COMPARISON_ALWAYS         = 8
} D3D10_DDI_COMPARISON_FUNC;
````


## -enum-fields
<dl>

### -field D3D10_DDI_COMPARISON_NEVER

<dd>
<p>The comparison never succeeds.</p>
</dd>

### -field D3D10_DDI_COMPARISON_LESS

<dd>
<p>The comparison is a less-than operation.</p>
</dd>

### -field D3D10_DDI_COMPARISON_EQUAL

<dd>
<p>The comparison is an equal-to operation.</p>
</dd>

### -field D3D10_DDI_COMPARISON_LESS_EQUAL

<dd>
<p>The comparison is a less-than or equal-to operation.</p>
</dd>

### -field D3D10_DDI_COMPARISON_GREATER

<dd>
<p>The comparison is a greater-than operation.</p>
</dd>

### -field D3D10_DDI_COMPARISON_NOT_EQUAL

<dd>
<p>The comparison is a not-equal-to operation.</p>
</dd>

### -field D3D10_DDI_COMPARISON_GREATER_EQUAL

<dd>
<p>The comparison is a greater-than or equal-to operation.</p>
</dd>

### -field D3D10_DDI_COMPARISON_ALWAYS

<dd>
<p>The comparison always succeeds.</p>
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
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10-ddi-depth-stencil-desc.md">D3D10_DDI_DEPTH_STENCIL_DESC</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10-ddi-depth-stencilop-desc.md">D3D10_DDI_DEPTH_STENCILOP_DESC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_DDI_COMPARISON_FUNC enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
