---
UID: NS.d3dhal._D3DHAL_DP2SETRENDERTARGET
title: D3DHAL_DP2SETRENDERTARGET
author: windows-driver-content
description: The D3DHAL_DP2SETRENDERTARGET structure is used with the D3DDP2OP_SETRENDERTARGET opcode to map a new rendering target surface and depth buffer in the current context.
old-location: display\d3dhal_dp2setrendertarget.htm
old-project: display
ms.assetid: 0ececf46-23a4-456b-8305-b9cd0ffba4b6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2SETRENDERTARGET, D3DHAL_DP2SETRENDERTARGET
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
req.alt-api: D3DHAL_DP2SETRENDERTARGET
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

# D3DHAL_DP2SETRENDERTARGET structure



## -description
<p>The D3DHAL_DP2SETRENDERTARGET structure is used with the D3DDP2OP_SETRENDERTARGET opcode to map a new rendering target surface and depth buffer in the current context.</p>


## -syntax

````
typedef struct _D3DHAL_DP2SETRENDERTARGET {
  DWORD hRenderTarget;
  DWORD hZBuffer;
} D3DHAL_DP2SETRENDERTARGET, *LPD3DHAL_DP2SETRENDERTARGET;
````


## -struct-fields
<dl>

### -field hRenderTarget

<dd>
<p>Specifies a handle to the rendering target.</p>
</dd>

### -field hZBuffer

<dd>
<p>Specifies a handle to the depth buffer.</p>
</dd>
</dl>

## -remarks
<p>The driver should carry out the following tasks in response to a D3DDP2OP_SETRENDERTARGET opcode in the <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> command stream:</p>

<p>Store the rendering target identified by <b>hRenderTarget</b> in the driver's context. </p>

<p>Store the depth buffer identified by <b>hZBuffer</b> in the driver's context. </p>

<p>See the <i>p3samp</i> sample driver that ships with the Microsoft Windows Driver Development Kit (DDK) for more implementation details.</p>

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
<dt>D3DDP2OP_SETRENDERTARGET</dt>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2SETRENDERTARGET structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
