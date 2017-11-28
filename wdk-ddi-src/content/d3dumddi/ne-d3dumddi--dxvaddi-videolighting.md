---
UID: NE.d3dumddi._DXVADDI_VIDEOLIGHTING
title: DXVADDI_VIDEOLIGHTING
author: windows-driver-content
description: The DXVADDI_VIDEOLIGHTING enumeration type contains values that identify lighting conditions for viewing video.
old-location: display\dxvaddi_videolighting.htm
old-project: display
ms.assetid: 2ae1c84e-119a-4649-b3f0-eafbb044dd91
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_VIDEOLIGHTING
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

# DXVADDI_VIDEOLIGHTING enumeration



## -description
<p>The DXVADDI_VIDEOLIGHTING enumeration type contains values that identify lighting conditions for viewing video.</p>


## -syntax

````
typedef enum _DXVADDI_VIDEOLIGHTING { 
  DXVADDI_VideoLightingMask      = 0x0F,
  DXVADDI_VideoLighting_Unknown  = 0,
  DXVADDI_VideoLighting_bright   = 1,
  DXVADDI_VideoLighting_office   = 2,
  DXVADDI_VideoLighting_dim      = 3,
  DXVADDI_VideoLighting_dark     = 4
} DXVADDI_VIDEOLIGHTING;
````


## -enum-fields
<dl>

### -field <a id="DXVADDI_VideoLightingMask"></a><a id="dxvaddi_videolightingmask"></a><a id="DXVADDI_VIDEOLIGHTINGMASK"></a><b>DXVADDI_VideoLightingMask</b>

<dd>
<p>The video lighting mask. The first 4 (0x0F) bits of a DWORD can be used to specify video lighting.</p>
</dd>

### -field <a id="DXVADDI_VideoLighting_Unknown"></a><a id="dxvaddi_videolighting_unknown"></a><a id="DXVADDI_VIDEOLIGHTING_UNKNOWN"></a><b>DXVADDI_VideoLighting_Unknown</b>

<dd>
<p>The video lighting condition is not specified. The default is dim.</p>
</dd>

### -field <a id="DXVADDI_VideoLighting_bright"></a><a id="dxvaddi_videolighting_bright"></a><a id="DXVADDI_VIDEOLIGHTING_BRIGHT"></a><b>DXVADDI_VideoLighting_bright</b>

<dd>
<p>A bright light for viewing video (for example, outside lighting conditions).</p>
</dd>

### -field <a id="DXVADDI_VideoLighting_office"></a><a id="dxvaddi_videolighting_office"></a><a id="DXVADDI_VIDEOLIGHTING_OFFICE"></a><b>DXVADDI_VideoLighting_office</b>

<dd>
<p>A medium brightness light for viewing video (for example, lighting conditions in home offices).</p>
</dd>

### -field <a id="DXVADDI_VideoLighting_dim"></a><a id="dxvaddi_videolighting_dim"></a><a id="DXVADDI_VIDEOLIGHTING_DIM"></a><b>DXVADDI_VideoLighting_dim</b>

<dd>
<p>A dim light for viewing video (for example, low-level lighting in a living room while watching television). </p>
</dd>

### -field <a id="DXVADDI_VideoLighting_dark"></a><a id="dxvaddi_videolighting_dark"></a><a id="DXVADDI_VIDEOLIGHTING_DARK"></a><b>DXVADDI_VideoLighting_dark</b>

<dd>
<p>Near-darkness for viewing video (for example, movie-theatre lighting).</p>
</dd>
</dl>

## -remarks
<p>One of the values of DXVADDI_VIDEOLIGHTING can be specified in the <b>VideoLighting</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a>.</p>

<p>The video lighting values can be used to alter the gamma to generate a comparable experience in a different lighting condition. </p>

<p>One of the values of DXVADDI_VIDEOLIGHTING can be specified in the <b>VideoLighting</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a>.</p>

<p>The video lighting values can be used to alter the gamma to generate a comparable experience in a different lighting condition. </p>

<p>One of the values of DXVADDI_VIDEOLIGHTING can be specified in the <b>VideoLighting</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a>.</p>

<p>The video lighting values can be used to alter the gamma to generate a comparable experience in a different lighting condition. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_VIDEOLIGHTING enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
