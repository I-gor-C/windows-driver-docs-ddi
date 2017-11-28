---
UID: NE.d3dkmddi._DXGK_RENDERKM_OPERATION
title: DXGK_RENDERKM_OPERATION
author: windows-driver-content
description: The DXGK_RENDERKM_OPERATION enumeration indicates the type of GDI hardware-accelerated rendering operation to perform when the DxgkDdiRenderKm function is called.
old-location: display\dxgk_renderkm_operation.htm
old-project: display
ms.assetid: bde22894-97a1-42a8-97c1-ba9738c087b9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_RENDERKM_OPERATION
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_RENDERKM_OPERATION enumeration



## -description
<p>The DXGK_RENDERKM_OPERATION enumeration indicates the type of GDI hardware-accelerated rendering operation to perform when the <a href="display.dxgkddirenderkm">DxgkDdiRenderKm</a> function is called.</p>


## -syntax

````
typedef enum _DXGK_RENDERKM_OPERATION { 
  DXGK_GDIOP_BITBLT          = 1,
  DXGK_GDIOP_COLORFILL       = 2,
  DXGK_GDIOP_ALPHABLEND      = 3,
  DXGK_GDIOP_STRETCHBLT      = 4,
  DXGK_GDIOP_ESCAPE          = 5,
  DXGK_GDIOP_TRANSPARENTBLT  = 6,
  DXGK_GDIOP_CLEARTYPEBLEND  = 7
} DXGK_RENDERKM_OPERATION;
````


## -enum-fields
<dl>

### -field <a id="DXGK_GDIOP_BITBLT"></a><a id="dxgk_gdiop_bitblt"></a><b>DXGK_GDIOP_BITBLT</b>

<dd>
<p>Indicates a bit-block transfer (bitblt).</p>
</dd>

### -field <a id="DXGK_GDIOP_COLORFILL"></a><a id="dxgk_gdiop_colorfill"></a><b>DXGK_GDIOP_COLORFILL</b>

<dd>
<p>Indicates a color fill.</p>
</dd>

### -field <a id="DXGK_GDIOP_ALPHABLEND"></a><a id="dxgk_gdiop_alphablend"></a><b>DXGK_GDIOP_ALPHABLEND</b>

<dd>
<p>Indicates an alpha blend.</p>
</dd>

### -field <a id="DXGK_GDIOP_STRETCHBLT"></a><a id="dxgk_gdiop_stretchblt"></a><b>DXGK_GDIOP_STRETCHBLT</b>

<dd>
<p>Indicates a stretch blt.</p>
</dd>

### -field <a id="DXGK_GDIOP_ESCAPE"></a><a id="dxgk_gdiop_escape"></a><b>DXGK_GDIOP_ESCAPE</b>

<dd>
<p>Reserved for future use. The driver should skip this command when setting the value of the <b>CommandSize</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562026">DXGK_RENDERKM_COMMAND</a> structure.</p>
</dd>

### -field <a id="DXGK_GDIOP_TRANSPARENTBLT"></a><a id="dxgk_gdiop_transparentblt"></a><b>DXGK_GDIOP_TRANSPARENTBLT</b>

<dd>
<p>Indicates a blt with transparency.</p>
</dd>

### -field <a id="DXGK_GDIOP_CLEARTYPEBLEND"></a><a id="dxgk_gdiop_cleartypeblend"></a><b>DXGK_GDIOP_CLEARTYPEBLEND</b>

<dd>
<p>Indicates a ClearType blend.</p>
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
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562026">DXGK_RENDERKM_COMMAND</a>
</dt>
<dt>
<a href="display.dxgkddirenderkm">DxgkDdiRenderKm</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_RENDERKM_OPERATION enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
