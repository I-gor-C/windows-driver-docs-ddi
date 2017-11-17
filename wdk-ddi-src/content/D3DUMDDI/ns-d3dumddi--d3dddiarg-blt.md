---
UID: NS.d3dumddi._D3DDDIARG_BLT
title: D3DDDIARG_BLT
author: windows-driver-content
description: The D3DDDIARG_BLT structure describes the parameters of a bit-block transfer (bitblt).
old-location: display\d3dddiarg_blt.htm
ms.assetid: 9663d0fe-7397-49d7-b860-e466a9311aca
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_BLT
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
ms.keywords: D3DDDIARG_BLT, D3DDDIARG_BLT
req.iface: 
---

# D3DDDIARG_BLT structure



## -description
<p>The D3DDDIARG_BLT structure describes the parameters of a bit-block transfer (bitblt). </p>


## -syntax

````
typedef struct _D3DDDIARG_BLT {
  HANDLE          hSrcResource;
  UINT            SrcSubResourceIndex;
  RECT            SrcRect;
  HANDLE          hDstResource;
  UINT            DstSubResourceIndex;
  RECT            DstRect;
  UINT            ColorKey;
  D3DDDI_BLTFLAGS Flags;
} D3DDDIARG_BLT;
````


## -struct-fields
<dl>

### -field <b>hSrcResource</b>

<dd>
<p>[in] A handle to the source resource.</p>
</dd>

### -field <b>SrcSubResourceIndex</b>

<dd>
<p>[in] The index to the source surface within the resource. </p>
</dd>

### -field <b>SrcRect</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure for the source rectangle. </p>
</dd>

### -field <b>hDstResource</b>

<dd>
<p>[in] A handle to the destination resource.</p>
</dd>

### -field <b>DstSubResourceIndex</b>

<dd>
<p>[in] The index to the destination surface within the resource. </p>
</dd>

### -field <b>DstRect</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure for the destination rectangle. </p>
</dd>

### -field <b>ColorKey</b>

<dd>
<p>[in] A value for the color key. Note that the <b>SrcColorKey</b> and <b>DstColorKey</b> bit-field flags are never set simultaneously in the <b>Flags</b> member.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544379">D3DDDI_BLTFLAGS</a> structure that identifies the type of bitblt to perform. Note that some bit-field flags in this structure are mutually exclusive with other flags. For more information about these flags, see the following Remarks section.</p>
</dd>
</dl>

## -remarks
<p>If a filtering option (for example, the <b>Point</b> or <b>Linear</b> bit-field flag) is not specified in the <b>Flags</b> member, the driver can use its own filtering technique.</p>

<p>The <b>SrcColorKey</b> and <b>DstColorKey</b> bit-field flags are never set simultaneously. Similarly, the <b>Point</b> bit-field flag is not simultaneously set with the <b>Linear</b> bit-field flag. </p>

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
<a href="https://msdn.microsoft.com/e87576c6-0173-4d8e-bbaf-b82e2907140a">Blt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544379">D3DDDI_BLTFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_BLT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
