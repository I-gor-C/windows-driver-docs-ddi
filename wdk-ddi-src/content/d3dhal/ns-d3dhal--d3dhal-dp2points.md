---
UID: NS.d3dhal._D3DHAL_DP2POINTS
title: D3DHAL_DP2POINTS
author: windows-driver-content
description: One or more D3DHAL_DP2POINTS structures are parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_POINTS, and are used to render the specified points.
old-location: display\d3dhal_dp2points.htm
old-project: display
ms.assetid: 9987ed83-7aa1-4e07-a85b-26607000ecba
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2POINTS, D3DHAL_DP2POINTS, *LPD3DHAL_DP2POINTS
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
req.alt-api: D3DHAL_DP2POINTS
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

# D3DHAL_DP2POINTS structure



## -description
<p>One or more D3DHAL_DP2POINTS structures are parsed from the command buffer by the <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> callback when the <a href="..\d3dhal\ns-d3dhal--d3dhal-dp2command.md">D3DHAL_DP2COMMAND</a> structure's <b>bCommand</b> member is set to D3DDP2OP_POINTS, and are used to render the specified points.</p>


## -syntax

````
typedef struct _D3DHAL_DP2POINTS {
  WORD wCount;
  WORD wVStart;
} D3DHAL_DP2POINTS, *LPD3DHAL_DP2POINTS;
````


## -struct-fields
<dl>

### -field <b>wCount</b>

<dd>
<p>Specifies the number of points to render.</p>
</dd>

### -field <b>wVStart</b>

<dd>
<p>Specifies the index into the vertex buffer containing coordinate data for the initial point.</p>
</dd>
</dl>

## -remarks
<p>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> should process <b>wPrimitiveCount</b> D3DHAL_DP2POINTS structures from the command buffer. The value of <b>wPrimitiveCount</b> is specified in the D3DHAL_DP2COMMAND structure.</p>

<p>For each D3DHAL_DP2POINTS structure, <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> should sequentially process <b>wCount</b> vertices from the vertex buffer. Starting from the vertex buffer offset, the sequence of points rendered is <b>wVStart</b>, (<b>wVStart</b>+1), ..., (<b>wVStart</b>+(<b>wCount</b>-1)).</p>

<p>The following figure shows a portion of a sample command buffer containing a D3DDP2OP_POINTS command and two D3DHAL_DP2POINTS structures. The driver should draw a total of seven points using the following vertices from the vertex buffer: v[2], v[3], v[4], v[7], v[8], v[9], v[10].</p>

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
<dt>D3DDP2OP_POINTS</dt>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-dp2command.md">D3DHAL_DP2COMMAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2POINTS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
