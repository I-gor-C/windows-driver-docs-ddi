---
UID: NS.d3dkmdt._D3DKMDT_VIDPN_PRESENT_PATH
title: D3DKMDT_VIDPN_PRESENT_PATH
author: windows-driver-content
description: The D3DKMDT_VIDPN_PRESENT_PATH structure contains information about a video present path.
old-location: display\d3dkmdt_vidpn_present_path.htm
old-project: display
ms.assetid: 3676476d-babe-4d68-995b-b7068a587bbc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_VIDPN_PRESENT_PATH,
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
req.alt-api: D3DKMDT_VIDPN_PRESENT_PATH
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

# D3DKMDT_VIDPN_PRESENT_PATH structure



## -description
<p>The D3DKMDT_VIDPN_PRESENT_PATH structure contains information about a video present path.</p>


## -syntax

````
typedef struct _D3DKMDT_VIDPN_PRESENT_PATH {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID            VidPnSourceId;
  D3DDDI_VIDEO_PRESENT_TARGET_ID            VidPnTargetId;
  D3DKMDT_VIDPN_PRESENT_PATH_IMPORTANCE     ImportanceOrdinal;
  D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION ContentTransformation;
  D3DKMDT_2DOFFSET                          VisibleFromActiveTLOffset;
  D3DKMDT_2DOFFSET                          VisibleFromActiveBROffset;
  D3DKMDT_COLOR_BASIS                       VidPnTargetColorBasis;
  D3DKMDT_COLOR_COEFF_DYNAMIC_RANGES        VidPnTargetColorCoeffDynamicRanges;
  D3DKMDT_VIDPN_PRESENT_PATH_CONTENT        Content;
  D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION CopyProtection;
  D3DKMDT_GAMMA_RAMP                        GammaRamp;
} D3DKMDT_VIDPN_PRESENT_PATH;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>The identifier of the path's video present source.</p>
</dd>

### -field <b>VidPnTargetId</b>

<dd>
<p>The identifier of the path's video present target.</p>
</dd>

### -field <b>ImportanceOrdinal</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546697">D3DKMDT_VIDPN_PRESENT_PATH_IMPORTANCE</a> enumerator that specifies the importance of the path relative to other paths. For example, the path presenting the primary view might have higher importance than other paths so that it will be assigned the best source and target mode sets. Path importance ordinal numbers are unique within a given video present network (VidPN) topology. </p>
</dd>

### -field <b>ContentTransformation</b>

<dd>
<p> A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a> enumerator that indicates the transformation applied to the content presented on the video present path.</p>
</dd>

### -field <b>VisibleFromActiveTLOffset</b>

<dd>
<p>A D3DKMDT_2DOFFSET structure that contains the offset, in pixels, from the top-left corner of the video signal's active pixels to the top-left corner of the monitor's visible pixels. The D3DKMDT_2DOFFSET data type is defined in <i>D3dkmdt.h</i> as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545977">D3DKMDT_2DREGION</a> structure.</p>
</dd>

### -field <b>VisibleFromActiveBROffset</b>

<dd>
<p>A D3DKMDT_2DOFFSET structure that contains the offset, in pixels, from the lower-right corner of the video signal's active pixels to the lower-right corner of the monitor's visible pixels.</p>
</dd>

### -field <b>VidPnTargetColorBasis</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545984">D3DKMDT_COLOR_BASIS</a> enumerator that specifies the color basis used by the path's video present target.</p>
</dd>

### -field <b>VidPnTargetColorCoeffDynamicRanges</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545986">D3DKMDT_COLOR_COEFF_DYNAMIC_RANGES</a> structure that specifies a range for each channel in the color basis used by the path's video present target.</p>
</dd>

### -field <b>Content</b>

<dd>
<p>A value from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546652">D3DKMDT_VIDPN_PRESENT_PATH_CONTENT</a> enumeration that indicates the type of content, graphics or video, displayed by the path.</p>
</dd>

### -field <b>CopyProtection</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546656">D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION</a> structure that describes the copy protection supported by, and currently active on, the path.</p>
</dd>

### -field <b>GammaRamp</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546014">D3DKMDT_GAMMA_RAMP</a> structure that contains a description of a gamma lookup table and a pointer to the lookup table.</p>
</dd>
</dl>

## -remarks
<p>A video present path represents a connection between a video present source (view) and a video present target (output) on a display adapter. For more information about video present networks, paths, sources, and targets, see <a href="https://msdn.microsoft.com/62a92f00-b1da-41c2-99af-eef8140b064e">Introduction to Video Present Networks</a>.</p>

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
<a href="display.dxgkddiupdateactivevidpnpresentpath">DxgkDdiUpdateActiveVidPnPresentPath</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_VIDPN_PRESENT_PATH structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
