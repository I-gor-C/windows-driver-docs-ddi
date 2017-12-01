---
UID: NS.d3dkmddi._DXGKARG_SETPOINTERSHAPE
title: DXGKARG_SETPOINTERSHAPE
author: windows-driver-content
description: The DXGKARG_SETPOINTERSHAPE structure describes the appearance of the mouse pointer and the location that it should be displayed in.
old-location: display\dxgkarg_setpointershape.htm
old-project: display
ms.assetid: fcb06620-8a30-4980-8733-35d7aabcc872
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_SETPOINTERSHAPE, DXGKARG_SETPOINTERSHAPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_SETPOINTERSHAPE
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

# DXGKARG_SETPOINTERSHAPE structure



## -description
<p>The DXGKARG_SETPOINTERSHAPE structure describes the appearance of the mouse pointer and the location that it should be displayed in. </p>


## -syntax

````
typedef struct _DXGKARG_SETPOINTERSHAPE {
  DXGK_POINTERFLAGS              Flags;
  UINT                           Width;
  UINT                           Height;
  UINT                           Pitch;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  const VOID                     *pPixels;
  UINT                           XHot;
  UINT                           YHot;
} DXGKARG_SETPOINTERSHAPE;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-pointerflags.md">DXGK_POINTERFLAGS</a> structure that identifies, in bit-field flags, how to display the mouse pointer.</p>
</dd>

### -field <b>Width</b>

<dd>
<p>[in] The width of the mouse pointer, in pixels.</p>
</dd>

### -field <b>Height</b>

<dd>
<p>[in] The height of the mouse pointer, in scan lines.</p>
</dd>

### -field <b>Pitch</b>

<dd>
<p>[in] The width of the mouse pointer, in bytes.</p>
</dd>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology that the mouse pointer is located in. </p>
</dd>

### -field <b>pPixels</b>

<dd>
<p>[in] A pointer to the start of the following bitmap depending on the bit-field flag that is set in the <b>Flags</b> member:</p>
<table>
<tr>
<th>Bit-field flag</th>
<th>Bitmap</th>
</tr>
<tr>
<td>
<p><b>Monochrome</b></p>
</td>
<td>
<p>
<dl>

### -field For monochrome mouse pointers:


### -field A monochrome bitmap whose size is specified by <b>Width</b> and <b>Height</b> in a 1 bits per pixel (bpp) DIB format AND mask that is followed by another 1 bpp DIB format XOR mask of the same size.

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p><b>Color</b></p>
</td>
<td>
<p>
<dl>

### -field For color mouse pointers:


### -field A color bitmap whose size is specified by <b>Width</b> and <b>Height</b> in a 32 bpp ARGB device independent bitmap (DIB) format.

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p><b>MaskedColor</b></p>
</td>
<td>
<p>
<dl>

### -field For masked color mouse pointers:


### -field A 32-bpp ARGB format bitmap with the mask value in the alpha bits. The only allowed mask values are 0 and 0xFF. When the mask value is 0, the RGB value should replace the screen pixel. When the mask value is 0xFF, an XOR operation is performed on the RGB value and the screen pixel; the result should replace the screen pixel.

</dl>
</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>XHot</b>

<dd>
<p>[in] The column, in pixels, that the mouse pointer is located on from the top left of the bitmap that <b>pPixels</b> points to. </p>
</dd>

### -field <b>YHot</b>

<dd>
<p>[in] The row, in pixels, that the mouse pointer is located on from the top left of the bitmap that <b>pPixels</b> points to.</p>
</dd>
</dl>

## -remarks
<p>The <b>XHot</b> and <b>YHot</b> members are used by display miniport drivers that are not associated with hardware, and these members can be ignored by drivers that control hardware. </p>

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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-pointerflags.md">DXGK_POINTERFLAGS</a>
</dt>
<dt>
<a href="display.dxgkddisetpointershape">DxgkDdiSetPointerShape</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_SETPOINTERSHAPE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
