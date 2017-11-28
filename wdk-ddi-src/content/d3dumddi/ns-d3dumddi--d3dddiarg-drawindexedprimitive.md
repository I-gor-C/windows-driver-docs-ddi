---
UID: NS.d3dumddi._D3DDDIARG_DRAWINDEXEDPRIMITIVE
title: D3DDDIARG_DRAWINDEXEDPRIMITIVE
author: windows-driver-content
description: The D3DDDIARG_DRAWINDEXEDPRIMITIVE structure describes an indexed primitive to draw.
old-location: display\d3dddiarg_drawindexedprimitive.htm
old-project: display
ms.assetid: 3f8cc918-9819-4c32-93f3-dbc2c1023016
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_DRAWINDEXEDPRIMITIVE, D3DDDIARG_DRAWINDEXEDPRIMITIVE
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
req.alt-api: D3DDDIARG_DRAWINDEXEDPRIMITIVE
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

# D3DDDIARG_DRAWINDEXEDPRIMITIVE structure



## -description
<p>The D3DDDIARG_DRAWINDEXEDPRIMITIVE structure describes an indexed primitive to draw.</p>


## -syntax

````
typedef struct _D3DDDIARG_DRAWINDEXEDPRIMITIVE {
  D3DPRIMITIVETYPE PrimitiveType;
  INT              BaseVertexIndex;
  UINT             MinIndex;
  UINT             NumVertices;
  UINT             StartIndex;
  UINT             PrimitiveCount;
} D3DDDIARG_DRAWINDEXEDPRIMITIVE;
````


## -struct-fields
<dl>

### -field <b>PrimitiveType</b>

<dd>
<p>[in] A D3DPRIMITIVETYPE-typed value that indicates the type of primitive to draw. This member can be one of the following values: D3DPT_POINTLIST, D3DPT_LINELIST, D3DPT_LINESTRIP, D3DPT_TRIANGLELIST, D3DPT_TRIANGLESTRIP, or D3DPT_TRIANGLEFAN. For more information about D3DPRIMITIVETYPE, see the Microsoft Windows SDK documentation.</p>
</dd>

### -field <b>BaseVertexIndex</b>

<dd>
<p>[in] The number that should be added to each index that is referenced by the various primitives to determine the actual index of the vertex elements in each vertex stream.</p>
</dd>

### -field <b>MinIndex</b>

<dd>
<p>[in] The minimum index of a range of vertices that are potentially accessed by the primitives to be drawn and, therefore, which vertices should be processed.</p>
</dd>

### -field <b>NumVertices</b>

<dd>
<p>[in] The number of vertices in a range that are potentially accessed by the primitives to be drawn and, therefore, which vertices should be processed.</p>
</dd>

### -field <b>StartIndex</b>

<dd>
<p>[in] The first index in the index buffer from which indices are read to draw the primitives.</p>
</dd>

### -field <b>PrimitiveCount</b>

<dd>
<p>[in] The number of triangles, lines, or points to draw for the given primitive. </p>
</dd>
</dl>

## -remarks
<p>The Microsoft Direct3D runtime does not transform the index data before passing a pointer to the description of the index data in the <i>pData</i> parameter in a call to the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawindexedprimitive.md">DrawIndexedPrimitive</a> function. </p>

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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawindexedprimitive.md">DrawIndexedPrimitive</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_DRAWINDEXEDPRIMITIVE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
