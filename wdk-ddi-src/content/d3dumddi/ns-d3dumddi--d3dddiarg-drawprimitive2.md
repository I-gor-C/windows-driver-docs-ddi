---
UID: NS.d3dumddi._D3DDDIARG_DRAWPRIMITIVE2
title: D3DDDIARG_DRAWPRIMITIVE2
author: windows-driver-content
description: The D3DDDIARG_DRAWPRIMITIVE2 structure describes a nonindexed primitive to draw.
old-location: display\d3dddiarg_drawprimitive2.htm
old-project: display
ms.assetid: fb9668a8-54b5-4d07-8682-af2b593308a5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_DRAWPRIMITIVE2, D3DDDIARG_DRAWPRIMITIVE2
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
req.alt-api: D3DDDIARG_DRAWPRIMITIVE2
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

# D3DDDIARG_DRAWPRIMITIVE2 structure



## -description
<p>The D3DDDIARG_DRAWPRIMITIVE2 structure describes a nonindexed primitive to draw. </p>


## -syntax

````
typedef struct _D3DDDIARG_DRAWPRIMITIVE2 {
  D3DPRIMITIVETYPE PrimitiveType;
  UINT             FirstVertexOffset;
  UINT             PrimitiveCount;
} D3DDDIARG_DRAWPRIMITIVE2;
````


## -struct-fields
<dl>

### -field <b>PrimitiveType</b>

<dd>
<p>[in] A D3DPRIMITIVETYPE-typed value that indicates the type of primitive to draw. This member can be one of the following values: D3DPT_POINTLIST, D3DPT_LINELIST, D3DPT_LINESTRIP, D3DPT_TRIANGLELIST, D3DPT_TRIANGLESTRIP, or D3DPT_TRIANGLEFAN. For more information about D3DPRIMITIVETYPE, see the Microsoft Windows SDK documentation.</p>
</dd>

### -field <b>FirstVertexOffset</b>

<dd>
<p>[in] The offset, in bytes, in stream zero of the vertex data. This member differs from the <b>VStart</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543057">D3DDDIARG_DRAWPRIMITIVE</a> structure that is used with the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawprimitive.md">DrawPrimitive</a> function. In <b>VStart</b>, the start of the vertex data in the vertex stream is specified by a vertex index rather than an actual byte offset.</p>
</dd>

### -field <b>PrimitiveCount</b>

<dd>
<p>[in] The number of triangles, lines, or points to draw for the given primitive. </p>
</dd>
</dl>

## -remarks
<p>The Microsoft Direct3D runtime transforms the vertex data before passing a pointer to the description of the vertex data in the <i>pData</i> parameter in a call to the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawprimitive2.md">DrawPrimitive2</a> function. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543057">D3DDDIARG_DRAWPRIMITIVE</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawprimitive2.md">DrawPrimitive2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_DRAWPRIMITIVE2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
