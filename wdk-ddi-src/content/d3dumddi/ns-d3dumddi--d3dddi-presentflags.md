---
UID: NS.d3dumddi._D3DDDI_PRESENTFLAGS
title: D3DDDI_PRESENTFLAGS
author: windows-driver-content
description: The D3DDDI_PRESENTFLAGS structure identifies how to perform a present operation.
old-location: display\d3dddi_presentflags.htm
old-project: display
ms.assetid: adab4c0f-b879-409c-97a3-f161a50514f5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_PRESENTFLAGS, D3DDDI_PRESENTFLAGS
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
req.alt-api: D3DDDI_PRESENTFLAGS
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

# D3DDDI_PRESENTFLAGS structure



## -description
<p>The D3DDDI_PRESENTFLAGS structure identifies how to perform a present operation.</p>


## -syntax

````
typedef struct _D3DDDI_PRESENTFLAGS {
  union {
    struct {
      UINT Blt  :1;
      UINT ColorFill  :1;
      UINT Flip  :1;
      UINT Reserved  :29;
    };
    UINT   Value;
  };
} D3DDDI_PRESENTFLAGS;
````


## -struct-fields
<dl>

### -field <b>Blt</b>

<dd>
<p>A UINT value that specifies whether to perform a bit-block transfer (bitblt) data to the primary surface. </p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>ColorFill</b>

<dd>
<p>A UINT value that specifies whether to perform a colorfill bitblt to the primary surface . </p>
<p>Setting this member is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
</dd>

### -field <b>Flip</b>

<dd>
<p>A UINT value that specifies whether to flip to a new surface. </p>
<p>Setting this member is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 29 bits (0xFFFFFFF8) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that is contained in D3DDDI_PRESENTFLAGS that can hold one 32-bit value that identifies how to perform a present operation.</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543240">D3DDDIARG_PRESENT</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-present.md">Present</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_PRESENTFLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
