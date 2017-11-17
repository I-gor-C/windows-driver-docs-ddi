---
UID: NS.d3dumddi._D3DDDIARG_TEXBLT1
title: D3DDDIARG_TEXBLT1
author: windows-driver-content
description: Describes parameters for a texture bit-block transfer (bitblt) operation.
old-location: display\d3dddiarg_texblt1.htm
ms.assetid: e11fd9b5-c3ad-4f8f-890c-30ca5ce4a57f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_TEXBLT1
req.alt-loc: D3dumddi.h
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
ms.keywords: D3DDDIARG_TEXBLT1, D3DDDIARG_TEXBLT1
req.iface: 
---

# D3DDDIARG_TEXBLT1 structure



## -description
<p>Describes parameters for a texture bit-block transfer (bitblt) operation.</p>


## -syntax

````
typedef struct _D3DDDIARG_TEXBLT1 {
  HANDLE hDstResource;
  HANDLE hSrcResource;
  UINT   CubeMapFace;
  POINT  DstPoint;
  RECT   SrcRect;
  UINT   CopyFlags;
} D3DDDIARG_TEXBLT1;
````


## -struct-fields
<dl>

### -field <b>hDstResource</b>

<dd>
<p>A handle to the destination resource.</p>
</dd>

### -field <b>hSrcResource</b>

<dd>
<p>A handle to the source resource.</p>
</dd>

### -field <b>CubeMapFace</b>

<dd>
<p>The face of a cube map.</p>
</dd>

### -field <b>DstPoint</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569161">POINT</a> structure that describes the destination point where the source texture is copied.</p>
</dd>

### -field <b>SrcRect</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that describes the source texture to copy to the destination point.</p>
</dd>

### -field <b>CopyFlags</b>

<dd>
<p>A value that specifies characteristics of a copy operation as a bitwise OR of the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451175">D3DDDI_COPY_FLAGS</a> enumeration type.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451175">D3DDDI_COPY_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569161">POINT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_TEXBLT1 structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
