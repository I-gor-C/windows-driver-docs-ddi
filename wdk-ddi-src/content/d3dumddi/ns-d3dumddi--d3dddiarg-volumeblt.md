---
UID: NS.d3dumddi._D3DDDIARG_VOLUMEBLT
title: D3DDDIARG_VOLUMEBLT
author: windows-driver-content
description: The D3DDDIARG_VOLUMEBLT structure describes parameters for a volume bit-block transfer (bitblt) operation.
old-location: display\d3dddiarg_volumeblt.htm
old-project: display
ms.assetid: 564afe6c-7a2e-4657-a481-24015c0be637
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_VOLUMEBLT, D3DDDIARG_VOLUMEBLT
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
req.alt-api: D3DDDIARG_VOLUMEBLT
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

# D3DDDIARG_VOLUMEBLT structure



## -description
<p>The D3DDDIARG_VOLUMEBLT structure describes parameters for a volume bit-block transfer (bitblt) operation. </p>


## -syntax

````
typedef struct _D3DDDIARG_VOLUMEBLT {
  HANDLE    hDstResource;
  HANDLE    hSrcResource;
  UINT      DstX;
  UINT      DstY;
  UINT      DstZ;
  D3DDDIBOX SrcBox;
} D3DDDIARG_VOLUMEBLT;
````


## -struct-fields
<dl>

### -field <b>hDstResource</b>

<dd>
<p>[in] A handle to the destination surface.</p>
</dd>

### -field <b>hSrcResource</b>

<dd>
<p>[in] A handle to the source surface.</p>
</dd>

### -field <b>DstX</b>

<dd>
<p>[in] The width, in screen coordinates, of the destination volume in which the source volume is copied.</p>
</dd>

### -field <b>DstY</b>

<dd>
<p>[in] The height, in screen coordinates, of the destination volume in which the source volume is copied.</p>
</dd>

### -field <b>DstZ</b>

<dd>
<p>[in] The depth, in screen coordinates, of the destination volume in which the source volume is copied.</p>
</dd>

### -field <b>SrcBox</b>

<dd>
<p>[in] A D3DDDIBOX structure that describes the source volume texture to copy to the destination.</p>
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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-volblt.md">VolBlt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_VOLUMEBLT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
