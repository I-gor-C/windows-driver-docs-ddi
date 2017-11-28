---
UID: NS.d3dhal._D3DHAL_CLIPPEDTRIANGLEFAN
title: D3DHAL_CLIPPEDTRIANGLEFAN
author: windows-driver-content
description: DirectX 8.0 and later versions only.
old-location: display\d3dhal_clippedtrianglefan.htm
old-project: display
ms.assetid: c169c483-ffad-470c-9adb-397e275341e3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_CLIPPEDTRIANGLEFAN, D3DHAL_CLIPPEDTRIANGLEFAN
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
req.alt-api: D3DHAL_CLIPPEDTRIANGLEFAN
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

# D3DHAL_CLIPPEDTRIANGLEFAN structure



## -description
<p>
   DirectX 8.0 and later versions only.
   </p>
<p>One or more D3DHAL_CLIPPEDTRIANGLEFAN structures are parsed from the command buffer by the <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> callback when the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a> structure's <b>bCommand</b> member is set to D3DDP2OP_CLIPPEDTRIANGLEFAN, and are used to render clipped triangle fans.</p>


## -syntax

````
typedef struct _D3DHAL_CLIPPEDTRIANGLEFAN {
  DWORD FirstVertexOffset;
  DWORD dwEdgeFlags;
  DWORD PrimitiveCount;
} D3DHAL_CLIPPEDTRIANGLEFAN, *LPD3DHAL_CLIPPEDTRIANGLEFAN;
````


## -struct-fields
<dl>

### -field <b>FirstVertexOffset</b>

<dd>
<p>Specifies the byte offset into stream 0 of the start of the vertex data (not the index of the vertex).</p>
</dd>

### -field <b>dwEdgeFlags</b>

<dd>
<p>Specifies a bitmask that identifies what edges are to be drawn when rendering wire frame (to prevent the drawing of edges introduced by clipping). For more information about this bitmask, see the Remarks section of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545906">D3DHAL_DP2TRIANGLEFAN_IMM</a> structure.</p>
</dd>

### -field <b>PrimitiveCount</b>

<dd>
<p>Specifies the number of triangles in the given triangle fan.</p>
</dd>
</dl>

## -remarks


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
<dt>D3DDP2OP_CLIPPEDTRIANGLEFAN</dt>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_CLIPPEDTRIANGLEFAN structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
