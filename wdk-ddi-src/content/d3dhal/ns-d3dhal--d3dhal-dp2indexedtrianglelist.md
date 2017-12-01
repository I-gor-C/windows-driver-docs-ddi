---
UID: NS.d3dhal._D3DHAL_DP2INDEXEDTRIANGLELIST
title: D3DHAL_DP2INDEXEDTRIANGLELIST
author: windows-driver-content
description: One or more D3DHAL_DP2INDEXEDTRIANGLELIST structures are parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_INDEXEDTRIANGLELIST, and are used to render a sequence of unconnected triangles using vertex indices.
old-location: display\d3dhal_dp2indexedtrianglelist.htm
old-project: display
ms.assetid: 138d226a-85ca-41d0-a0dd-2772194874e8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2INDEXEDTRIANGLELIST, D3DHAL_DP2INDEXEDTRIANGLELIST, *LPD3DHAL_DP2INDEXEDTRIANGLELIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DHAL_DP2INDEXEDTRIANGLELIST
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
req.iface: 
---

# D3DHAL_DP2INDEXEDTRIANGLELIST structure



## -description
<p>One or more D3DHAL_DP2INDEXEDTRIANGLELIST structures are parsed from the command buffer by the <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> callback when the <a href="..\d3dhal\ns-d3dhal--d3dhal-dp2command.md">D3DHAL_DP2COMMAND</a> structure's <b>bCommand</b> member is set to D3DDP2OP_INDEXEDTRIANGLELIST, and are used to render a sequence of unconnected triangles using vertex indices.</p>


## -syntax

````
typedef struct _D3DHAL_DP2INDEXEDTRIANGLELIST {
  WORD wV1;
  WORD wV2;
  WORD wV3;
  WORD wFlags;
} D3DHAL_DP2INDEXEDTRIANGLELIST, *LPD3DHAL_DP2INDEXEDTRIANGLELIST;
````


## -struct-fields
<dl>

### -field <b>wV1</b>

<dd>
<p>Specifies the index into the vertex buffer location containing coordinate data for the first vertex of the triangle.</p>
</dd>

### -field <b>wV2</b>

<dd>
<p>Specifies the index to the vertex buffer location containing coordinate data for the second vertex of the triangle.</p>
</dd>

### -field <b>wV3</b>

<dd>
<p>Specifies the index to the vertex buffer location containing coordinate data for the third vertex of the triangle.</p>
</dd>

### -field <b>wFlags</b>

<dd>
<p>Specifies the flags that describe how the driver should render the triangle. This member can be a bitwise OR of the following values: </p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DTRIFLAG_EDGEENABLE1</p>
</td>
<td>
<p>The driver should render the triangle edge between <b>wV1</b> and <b>wV2</b> when the fill mode is D3DFILL_WIREFRAME.</p>
</td>
</tr>
<tr>
<td>
<p>D3DTRIFLAG_EDGEENABLE2</p>
</td>
<td>
<p>The driver should render the triangle edge between <b>wV2</b> and <b>wV3</b> when the fill mode is D3DFILL_WIREFRAME.</p>
</td>
</tr>
<tr>
<td>
<p>D3DTRIFLAG_EDGEENABLE3</p>
</td>
<td>
<p>The driver should render the triangle edge between <b>wV3</b> and <b>wV1</b> when the fill mode is D3DFILL_WIREFRAME.</p>
</td>
</tr>
<tr>
<td>
<p>D3DTRIFLAG_EDGEENABLETRIANGLE</p>
</td>
<td>
<p>The driver should render all triangle edges when the fill mode is D3DFILL_WIREFRAME.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> should process <b>wPrimitiveCount</b> * 3 indexes from the command buffer, processing <b>wPrimitiveCount</b> D3DHAL_DP2INDEXEDTRIANGLELIST structures. The value of <b>wPrimitiveCount</b> is specified in the D3DHAL_DP2COMMAND structure.</p>

<p>The driver should process a total of <b>wPrimitiveCount</b>*3 vertices from the vertex buffer, three vertices per triangle, for the current command. The sequence of triangles rendered is (<b>wV1</b>₀, <b>wV2</b>₀, <b>wV3</b>₀), (<b>wV1</b>₁, <b>wV2</b>₁, <b>wV3</b>₁), ..., (<b>wV1</b>ₙ, <b>wV2</b>ₙ, <b>wV3</b>ₙ), where n equals (<b>wPrimitiveCount</b>- 1). The driver should calculate the vertex locations based on the current command as follows:</p>

<p>When the command is D3DDP2OP_INDEXEDTRIANGLELIST, the indexes into the vertex buffer are relative to the vertex buffer offset specified by the <b>dwVertexOffset</b> member of the <a href="..\d3dhal\ns-d3dhal--d3dhal-drawprimitives2data.md">D3DHAL_DRAWPRIMITIVES2DATA</a> structure.</p>

<p>When the command is D3DDP2OP_INDEXEDTRIANGLELIST2, there is a <a href="..\d3dhal\ns-d3dhal--d3dhal-dp2startvertex.md">D3DHAL_DP2STARTVERTEX</a> structure that immediately follows the command in the command buffer. The indexes into the vertex buffer are relative to the vertex buffer offset specified by <b>dwVertexOffset</b> plus the base offset obtained from the <b>wVStart</b> member of the D3DHAL_DP2STARTVERTEX structure.</p>

<p>The following figure shows a portion of a sample command buffer containing a D3DDP2OP_INDEXEDTRIANGLELIST command and two D3DHAL_DP2INDEXEDTRIANGLELIST structures. The driver should draw two triangles âˆ’ with all edges enabled âˆ’ using the following six vertices from the vertex buffer: (v[3], v[4], v[5]), (v[0], v[1], v[2]).</p>

<p>Similarly, the following figure shows a portion of a sample command buffer containing a D3DDP2OP_INDEXEDTRIANGLELIST2 command, a D3DHAL_DP2STARTVERTEX offset, and two D3DHAL_DP2INDEXEDTRIANGLELIST structures. The driver should process six vertices from the vertex buffer, rendering two triangles defined by (v[5], v[6], v[7]), (v[2], v[3], v[4]).</p>

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
<dt>D3DDP2OP_INDEXEDTRIANGLELIST</dt>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-dp2command.md">D3DHAL_DP2COMMAND</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-dp2startvertex.md">D3DHAL_DP2STARTVERTEX</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-drawprimitives2data.md">D3DHAL_DRAWPRIMITIVES2DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2INDEXEDTRIANGLELIST structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
