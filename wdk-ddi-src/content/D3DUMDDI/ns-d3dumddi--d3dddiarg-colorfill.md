---
UID: NS.d3dumddi._D3DDDIARG_COLORFILL
title: D3DDDIARG_COLORFILL
author: windows-driver-content
description: The D3DDDIARG_COLORFILL structure describes the parameters of a color-fill operation.
old-location: display\d3dddiarg_colorfill.htm
ms.assetid: 4d647c59-4e00-46b3-a46f-226e475eb63d
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
req.alt-api: D3DDDIARG_COLORFILL
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
ms.keywords: D3DDDIARG_COLORFILL, D3DDDIARG_COLORFILL
req.iface: 
---

# D3DDDIARG_COLORFILL structure



## -description
<p>The D3DDDIARG_COLORFILL structure describes the parameters of a color-fill operation. </p>


## -syntax

````
typedef struct _D3DDDIARG_COLORFILL {
  HANDLE                hResource;
  UINT                  SubResourceIndex;
  RECT                  DstRect;
  D3DCOLOR              Color;
  D3DDDI_COLORFILLFLAGS Flags;
} D3DDDIARG_COLORFILL;
````


## -struct-fields
<dl>

### -field <b>hResource</b>

<dd>
<p>[in] A handle to the resource.</p>
</dd>

### -field <b>SubResourceIndex</b>

<dd>
<p>[in] The zero-based index into the resource, which is specified by the handle in the <b>hResource</b> member. This index indicates the subresource, or surface, on which a rectangular area is color-filled.</p>
</dd>

### -field <b>DstRect</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569236">RECTL</a> structure that indicates the upper-left and lower-right points of a rectangle on the surface to color fill. </p>
</dd>

### -field <b>Color</b>

<dd>
<p>A D3DCOLOR data type for the A8R8G8B8 fill color. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544394">D3DDDI_COLORFILLFLAGS</a> structure that identifies the type of color-fill operation to perform. </p>
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
<a href="https://msdn.microsoft.com/c120421d-6a10-4d37-b936-98dac75e236b">ColorFill</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544394">D3DDDI_COLORFILLFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569236">RECTL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_COLORFILL structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
