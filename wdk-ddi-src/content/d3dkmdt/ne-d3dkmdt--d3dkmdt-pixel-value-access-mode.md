---
UID: NE.d3dkmdt._D3DKMDT_PIXEL_VALUE_ACCESS_MODE
title: D3DKMDT_PIXEL_VALUE_ACCESS_MODE
author: windows-driver-content
description: The D3DKMDT_PIXEL_VALUE_ACCESS_MODE enumeration is used to indicate the way color values or palette indices are stored in the primary surface of a video present source.
old-location: display\d3dkmdt_pixel_value_access_mode.htm
old-project: display
ms.assetid: da4074ac-309d-46b9-b630-79d73ed73f36
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_PIXEL_VALUE_ACCESS_MODE
req.alt-loc: d3dkmdt.h
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

# D3DKMDT_PIXEL_VALUE_ACCESS_MODE enumeration



## -description
<p>The D3DKMDT_PIXEL_VALUE_ACCESS_MODE enumeration is used to indicate the way color values or palette indices are stored in the primary surface of a video present source.</p>


## -syntax

````
typedef enum _D3DKMDT_PIXEL_VALUE_ACCESS_MODE { 
  D3DKMDT_PVAM_UNINITIALIZED    = 0,
  D3DKMDT_PVAM_DIRECT           = 1,
  D3DKMDT_PVAM_PRESETPALETTE    = 2,
  D3DKMDT_PVAM_SETTABLEPALETTE  = 3
} D3DKMDT_PIXEL_VALUE_ACCESS_MODE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_PVAM_UNINITIALIZED"></a><a id="d3dkmdt_pvam_uninitialized"></a><b>D3DKMDT_PVAM_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_PIXEL_VALUE_ACCESS_MODE has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_PVAM_DIRECT"></a><a id="d3dkmdt_pvam_direct"></a><b>D3DKMDT_PVAM_DIRECT</b>

<dd>
<p>Indicates that colors are stored directly in the primary surface.</p>
</dd>

### -field <a id="D3DKMDT_PVAM_PRESETPALETTE"></a><a id="d3dkmdt_pvam_presetpalette"></a><b>D3DKMDT_PVAM_PRESETPALETTE</b>

<dd>
<p>Indicates that palette indices are stored in the primary surface. Colors are stored in a palette that is specific to the display adapter. The operating system can query the display miniport driver for the palette.</p>
</dd>

### -field <a id="D3DKMDT_PVAM_SETTABLEPALETTE"></a><a id="d3dkmdt_pvam_settablepalette"></a><b>D3DKMDT_PVAM_SETTABLEPALETTE</b>

<dd>
<p>Indicates that palette indices are stored in the primary surface. Colors are stored in a palette that the operating system can set dynamically by calling the display miniport driver.</p>
</dd>
</dl>

## -remarks
<p>The <b>Format.Graphics</b> member of the <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-source-mode.md">D3DKMDT_VIDPN_SOURCE_MODE</a> structure is a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-graphics-rendering-format.md">D3DKMDT_GRAPHICS_RENDERING_FORMAT</a> structure. The <b>PixelValueAccessMode</b> member of the D3DKMDT_GRAPHICS_RENDERING_FORMAT structure is a D3DKMDT_PIXEL_VALUE_ACCESS_MODE value.</p>

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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.vidpn_source_mode_set_interface">VidPn Source Mode Set Interface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_PIXEL_VALUE_ACCESS_MODE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
