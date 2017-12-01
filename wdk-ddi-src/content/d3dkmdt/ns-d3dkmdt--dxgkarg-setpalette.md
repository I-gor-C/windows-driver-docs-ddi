---
UID: NS.d3dkmdt._DXGKARG_SETPALETTE
title: DXGKARG_SETPALETTE
author: windows-driver-content
description: The DXGKARG_SETPALETTE structure describes the palette to set for a display.
old-location: display\dxgkarg_setpalette.htm
old-project: display
ms.assetid: a76d9549-d182-437f-a570-7d24fd6a5488
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_SETPALETTE, DXGKARG_SETPALETTE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_SETPALETTE
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
req.irql: 
req.iface: 
---

# DXGKARG_SETPALETTE structure



## -description
<p>The DXGKARG_SETPALETTE structure describes the palette to set for a display. </p>


## -syntax

````
typedef struct _DXGKARG_SETPALETTE {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           FirstEntry;
  UINT                           NumEntries;
  D3DKMDT_PALETTEDATA            *pLookupTable;
} DXGKARG_SETPALETTE;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology that the palette is set on. </p>
</dd>

### -field <b>FirstEntry</b>

<dd>
<p>[in] The location in the device palette that the first entry in the array of color entries that <b>pLookupTable</b> specifies is copied to. The remaining entries that <b>pLookupTable</b> specifies are copied sequentially, from this starting point into the device's palette.</p>
</dd>

### -field <b>NumEntries</b>

<dd>
<p>[in] The number of color entries in the array that <b>pLookupTable</b> specifies.</p>
</dd>

### -field <b>pLookupTable</b>

<dd>
<p>[in] An array of color entries to copy into the device's color palette (that is, the device's color registers). Each color entry is accessed as a generic 32-bit value or as the <b>Red</b>, <b>Green</b>, <b>Blue</b>, and <b>Unused</b> members of a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-palettedata.md">D3DKMDT_PALETTEDATA</a> structure.</p>
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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-palettedata.md">D3DKMDT_PALETTEDATA</a>
</dt>
<dt>
<a href="display.dxgkddisetpalette">DxgkDdiSetPalette</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_SETPALETTE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
