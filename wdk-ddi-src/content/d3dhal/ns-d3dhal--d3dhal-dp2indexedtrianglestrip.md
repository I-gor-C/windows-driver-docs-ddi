---
UID: NS.d3dhal._D3DHAL_DP2INDEXEDTRIANGLESTRIP
title: D3DHAL_DP2INDEXEDTRIANGLESTRIP
author: windows-driver-content
description: One or more D3DHAL_DP2INDEXEDTRIANGLESTRIP structures are parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_INDEXEDTRIANGLESTRIP, and are used to render strips of connected triangles using vertex indices.
old-location: display\d3dhal_dp2indexedtrianglestrip.htm
ms.assetid: 542f89f1-f562-4293-9ca1-96e7a0512772
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DHAL_DP2INDEXEDTRIANGLESTRIP
req.alt-loc: d3dhal.h
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
ms.keywords: D3DHAL_DP2INDEXEDTRIANGLESTRIP, D3DHAL_DP2INDEXEDTRIANGLESTRIP, *LPD3DHAL_DP2INDEXEDTRIANGLESTRIP
req.iface: 
---

# D3DHAL_DP2INDEXEDTRIANGLESTRIP structure



## -description
<p>One or more D3DHAL_DP2INDEXEDTRIANGLESTRIP structures are parsed from the command buffer by the <a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a> callback when the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a> structure's <b>bCommand</b> member is set to D3DDP2OP_INDEXEDTRIANGLESTRIP, and are used to render strips of connected triangles using vertex indices.</p>


## -syntax

````
typedef struct _D3DHAL_DP2INDEXEDTRIANGLESTRIP {
  WORD wV[3];
} D3DHAL_DP2INDEXEDTRIANGLESTRIP, *LPD3DHAL_DP2INDEXEDTRIANGLESTRIP;
````


## -struct-fields
<dl>

### -field <b>wV</b>

<dd>
<p>Specifies the index into the vertex buffer containing coordinate data for the first vertex of the triangle strip.</p>
<p>Although this member has only enough space to contain three indexes, this array of indexes should be treated as a variable-sized array with (<b>wPrimitiveCount</b> + 2) elements. (<b>wPrimitiveCount</b> is a member of the D3DHAL_DP2COMMAND structure.)</p>
</dd>
</dl>

## -remarks
<p>
<a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a> should process (<b>wPrimitiveCount</b>+2) indexes from the command buffer, in effect, processing <b>wPrimitiveCount</b> D3DHAL_DP2INDEXEDTRIANGLESTRIP structures.</p>

<p>The triangle edges in a triangle strip are rendered in this order: (<b>wV[</b>0<b>]</b>, <b>wV[</b>1<b>]</b>, <b>wV[</b>2<b>]</b>), (<b>wV[</b>1<b>]</b>, <b>wV[</b>3<b>]</b>, <b>wV[</b>2<b>]</b>), (<b>wV[</b>2<b>]</b>, <b>wV[</b>3<b>]</b>, <b>wV[</b>4<b>]</b>), (<b>wV[</b>3<b>]</b>, <b>wV[</b>5<b>]</b>, <b>wV[</b>4<b>]</b>),...</p>

<p>For the last triangle in the triangle strip, however, the edges are rendered in different orders when <b>wPrimitiveCount</b>t is odd and when it is even.</p>

<p>When <b>wPrimitiveCount</b> is an odd number, the last triangle's edges are rendered in this order: (<b>wV[wPrimitiveCount </b>- 1<b>]</b>, <b>wV[wPrimitiveCount]</b>, <b>wV[wPrimitiveCount</b>+ 1<b>]</b>).</p>

<p>When <b>wPrimitiveCount</b> is an even number, the last triangle's edges are rendered in this order: (<b>wV[wPrimitiveCount</b>- 1<b>]</b>, <b>wV[wPrimitiveCount</b>+1<b>]</b>, <b>wV[wPrimitiveCount</b>).</p>

<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545832">D3DHAL_DP2STARTVERTEX</a> structure immediately follows the command in the command buffer. The vertex buffer indexes are relative to the vertex buffer offset specified by the <b>dwVertexOffset</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545957">D3DHAL_DRAWPRIMITIVES2DATA</a> structure plus the base offset obtained from the <b>wVStart</b> member of the D3DHAL_DP2STARTVERTEX structure.</p>

<p>The following figure shows a portion of a sample command buffer containing a D3DDP2OP_INDEXEDTRIANGLESTRIP command, a D3DHAL_DP2STARTVERTEX offset of zero, and a logical list of D3DHAL_DP2INDEXEDTRIANGLESTRIP structures. The driver should process five vertices from the vertex buffer, rendering a strip of three triangles defined by (v[1], v[3], v[6]), (v[3], v[4], v[6]), (v[6], v[4], v[5]).</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>D3DDP2OP_INDEXEDTRIANGLESTRIP</dt>
<dt>
<a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545832">D3DHAL_DP2STARTVERTEX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545957">D3DHAL_DRAWPRIMITIVES2DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2INDEXEDTRIANGLESTRIP structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
