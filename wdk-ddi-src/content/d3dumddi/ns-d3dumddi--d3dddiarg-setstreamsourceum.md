---
UID: NS.d3dumddi._D3DDDIARG_SETSTREAMSOURCEUM
title: D3DDDIARG_SETSTREAMSOURCEUM
author: windows-driver-content
description: The D3DDDIARG_SETSTREAMSOURCEUM structure describes the vertex stream to bind to a user-memory buffer.
old-location: display\d3dddiarg_setstreamsourceum.htm
old-project: display
ms.assetid: 1406f6d7-7da9-4c1a-93c5-384b13fa5e81
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_SETSTREAMSOURCEUM, D3DDDIARG_SETSTREAMSOURCEUM
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
req.alt-api: D3DDDIARG_SETSTREAMSOURCEUM
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

# D3DDDIARG_SETSTREAMSOURCEUM structure



## -description
<p>The D3DDDIARG_SETSTREAMSOURCEUM structure describes the vertex stream to bind to a user-memory buffer. </p>


## -syntax

````
typedef struct _D3DDDIARG_SETSTREAMSOURCEUM {
  UINT Stream;
  UINT Stride;
} D3DDDIARG_SETSTREAMSOURCEUM;
````


## -struct-fields
<dl>

### -field <b>Stream</b>

<dd>
<p>[in] The index, starting from zero, for the vertex stream to bind to a user-memory buffer.</p>
</dd>

### -field <b>Stride</b>

<dd>
<p>[in] The size, in bytes, from one vertex to the next vertex in the stream. In contrast to the call to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setstreamsource.md">SetStreamSource</a> function, <b>Stride</b> cannot be set to zero. Because only one stream can be bound to a user memory buffer, each vertex in the stream must receive different data for processing.</p>
<p>The <b>Stride</b> value must be DWORD-aligned. </p>
</dd>
</dl>

## -remarks
<p>In a call to the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setstreamsourceum.md">SetStreamSourceUM</a> function, a pointer to a D3DDDIARG_SETSTREAMSOURCEUM structure is passed in the <i>pData</i> parameter. The Microsoft Direct3D runtime supplies vertex data for the vertex stream through the <i>pUMBuffer</i> parameter in a call to the user-mode display driver's <b>SetStreamSourceUM</b> function. </p>

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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setstreamsourceum.md">SetStreamSourceUM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_SETSTREAMSOURCEUM structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
