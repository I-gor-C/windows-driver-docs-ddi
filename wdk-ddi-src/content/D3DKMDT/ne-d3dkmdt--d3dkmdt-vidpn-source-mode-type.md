---
UID: NE.d3dkmdt._D3DKMDT_VIDPN_SOURCE_MODE_TYPE
title: D3DKMDT_VIDPN_SOURCE_MODE_TYPE
author: windows-driver-content
description: The D3DKMDT_VIDPN_SOURCE_MODE_TYPE enumeration is used to indicate whether a video present network (VidPN) source mode is a graphics mode, a text mode, or a stereo mode.
old-location: display\d3dkmdt_vidpn_source_mode_type.htm
ms.assetid: c2a48cf2-f595-4f78-b779-416d324e90d7
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_VIDPN_SOURCE_MODE_TYPE
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
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# D3DKMDT_VIDPN_SOURCE_MODE_TYPE enumeration



## -description
<p>The D3DKMDT_VIDPN_SOURCE_MODE_TYPE enumeration is used to indicate whether a video present network (VidPN) source mode is a graphics mode, a text mode, or a stereo mode.</p>


## -syntax

````
typedef enum _D3DKMDT_VIDPN_SOURCE_MODE_TYPE { 
  D3DKMDT_RMT_UNINITIALIZED                  = 0,
  D3DKMDT_RMT_GRAPHICS                       = 1,
  D3DKMDT_RMT_TEXT                           = 2,
  D3DKMDT_RMT_GRAPHICS_STEREO                = 3,
  D3DKMDT_RMT_GRAPHICS_STEREO_ADVANCED_SCAN  = 4
} D3DKMDT_VIDPN_SOURCE_MODE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_RMT_UNINITIALIZED"></a><a id="d3dkmdt_rmt_uninitialized"></a><b>D3DKMDT_RMT_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_VIDPN_SOURCE_MODE_TYPE has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_RMT_GRAPHICS"></a><a id="d3dkmdt_rmt_graphics"></a><b>D3DKMDT_RMT_GRAPHICS</b>

<dd>
<p>Indicates that the VidPN source mode is a graphics mode.</p>
</dd>

### -field <a id="D3DKMDT_RMT_TEXT"></a><a id="d3dkmdt_rmt_text"></a><b>D3DKMDT_RMT_TEXT</b>

<dd>
<p>Indicates that the VidPN source mode is a text mode.</p>
</dd>

### -field <a id="D3DKMDT_RMT_GRAPHICS_STEREO"></a><a id="d3dkmdt_rmt_graphics_stereo"></a><b>D3DKMDT_RMT_GRAPHICS_STEREO</b>

<dd>
<p>Available beginning with Windows 8.</p>
<p>Indicates that the VidPN source mode is stereo, and the allocation can only be scanned by the display miniport driver as both left and right channels.</p>
</dd>

### -field <a id="D3DKMDT_RMT_GRAPHICS_STEREO_ADVANCED_SCAN"></a><a id="d3dkmdt_rmt_graphics_stereo_advanced_scan"></a><b>D3DKMDT_RMT_GRAPHICS_STEREO_ADVANCED_SCAN</b>

<dd>
<p>Available beginning with Windows 8.</p>
<p>Indicates that the VidPN source mode is stereo, and the allocation can only be scanned by the display miniport driver as both left and right channels, or as only the left channel, or as only  the right channel.</p>
<p>If mono content needs to be displayed in a stereo mode, the operating system can better manage resources if <b>D3DKMDT_RMT_GRAPHICS_STEREO_ADVANCED_SCAN</b> is set instead of <b>D3DKMDT_RMT_GRAPHICS_STEREO</b>.</p>
</dd>
</dl>

## -remarks
<p>The <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a> structure is a D3DKMDT_VIDPN_SOURCE_MODE_TYPE value.</p>

<p>The <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a> structure is a D3DKMDT_VIDPN_SOURCE_MODE_TYPE value.</p>

<p>The <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a> structure is a D3DKMDT_VIDPN_SOURCE_MODE_TYPE value.</p>

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