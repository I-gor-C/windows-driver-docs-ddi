---
UID: NS.d3dumddi._D3DDDIARG_BUFFERBLT1
title: D3DDDIARG_BUFFERBLT1
author: windows-driver-content
description: Describes the parameters of a buffer bit-block transfer (bitblt) operation.
old-location: display\d3dddiarg_bufferblt1.htm
old-project: display
ms.assetid: 1dd2bf12-741b-4f3a-9c80-367b5d5036b5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_BUFFERBLT1, D3DDDIARG_BUFFERBLT1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_BUFFERBLT1
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
req.iface: 
---

# D3DDDIARG_BUFFERBLT1 structure



## -description
<p>Describes the parameters of a buffer bit-block transfer (bitblt) operation.</p>


## -syntax

````
typedef struct _D3DDDIARG_BUFFERBLT1 {
  HANDLE      hDstResource;
  HANDLE      hSrcResource;
  UINT        Offset;
  D3DDDIRANGE SrcRange;
  UINT        CopyFlags;
} D3DDDIARG_BUFFERBLT1;
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

### -field <b>Offset</b>

<dd>
<p>The offset in the destination surface, in bytes.</p>
</dd>

### -field <b>SrcRange</b>

<dd>
<p>The source range.</p>
</dd>

### -field <b>CopyFlags</b>

<dd>
<p>A value that specifies characteristics of a copy operation as a bitwise OR of the values in the <a href="..\d3dumddi\ne-d3dumddi-d3dddi-copy-flags.md">D3DDDI_COPY_FLAGS</a> enumeration type.</p>
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
<dt>D3dumddi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\ne-d3dumddi-d3dddi-copy-flags.md">D3DDDI_COPY_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_BUFFERBLT1 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
