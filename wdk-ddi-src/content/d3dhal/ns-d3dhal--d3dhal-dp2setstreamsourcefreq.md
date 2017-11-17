---
UID: NS.d3dhal._D3DHAL_DP2SETSTREAMSOURCEFREQ
title: D3DHAL_DP2SETSTREAMSOURCEFREQ
author: windows-driver-content
description: DirectX 9.0 and later versions only. The D3DHAL_DP2SETSTREAMSOURCEFREQ structure is used to set the frequency divisor of a stream source that is bound to a vertex buffer for D3dDrawPrimitives2.
old-location: display\d3dhal_dp2setstreamsourcefreq.htm
ms.assetid: c7f9cfc5-5698-404b-9b67-51ad8e351519
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
req.alt-api: D3DHAL_DP2SETSTREAMSOURCEFREQ
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
ms.keywords: D3DHAL_DP2SETSTREAMSOURCEFREQ, D3DHAL_DP2SETSTREAMSOURCEFREQ
req.iface: 
---

# D3DHAL_DP2SETSTREAMSOURCEFREQ structure



## -description
<p>
   DirectX 9.0 and later versions only.
   </p>
<p>The D3DHAL_DP2SETSTREAMSOURCEFREQ structure is used to set the frequency divisor of a stream source that is bound to a vertex buffer for <a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>.</p>


## -syntax

````
typedef struct _D3DHAL_DP2SETSTREAMSOURCEFREQ {
  DWORD dwStream;
  DWORD dwDivider;
} D3DHAL_DP2SETSTREAMSOURCEFREQ, *LPD3DHAL_DP2SETSTREAMSOURCEFREQ;
````


## -struct-fields
<dl>

### -field <b>dwStream</b>

<dd>
<p>Specifies the data stream, in the range from 0 to the maximum number of streams -1, whose frequency is being modified.</p>
</dd>

### -field <b>dwDivider</b>

<dd>
<p>Specifies the frequency divisor, which is the number of vertices after which data from the given stream is fetched into the vertex shader. This number can be greater than zero and at most 2^16-1 (WORD).</p>
</dd>
</dl>

## -remarks
<p>A driver is requested to set a stream's frequency divisor through the D3DDP2OP_SETSTREAMSOURCEFREQ operation code. </p>

<p>A driver for a device that supports vertex shader version 3.0 and later can implement stream frequency division. For more information, see <a href="https://msdn.microsoft.com/81bbced4-7331-4e54-9617-1ef29b02f162">Modifying Vertex Stream Frequency</a>.</p>

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
<dt>D3DDP2OP_SETSTREAMSOURCEFREQ</dt>
<dt>
<a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2SETSTREAMSOURCEFREQ structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
