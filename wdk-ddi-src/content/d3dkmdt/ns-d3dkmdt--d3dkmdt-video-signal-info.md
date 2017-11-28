---
UID: NS.d3dkmdt._D3DKMDT_VIDEO_SIGNAL_INFO
title: D3DKMDT_VIDEO_SIGNAL_INFO
author: windows-driver-content
description: The D3DKMDT_VIDEO_SIGNAL_INFO structure contains information about a video signal driven by a video output on a display adapter.
old-location: display\d3dkmdt_video_signal_info.htm
old-project: display
ms.assetid: 38d0a655-265b-46e0-8af3-de6757025588
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_VIDEO_SIGNAL_INFO,
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
req.alt-api: D3DKMDT_VIDEO_SIGNAL_INFO
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

# D3DKMDT_VIDEO_SIGNAL_INFO structure



## -description
<p>The D3DKMDT_VIDEO_SIGNAL_INFO structure contains information about a video signal driven by a video output on a display adapter.</p>


## -syntax

````
typedef struct _D3DKMDT_VIDEO_SIGNAL_INFO {
  D3DKMDT_VIDEO_SIGNAL_STANDARD VideoStandard;
  D3DKMDT_2DREGION              TotalSize;
  D3DKMDT_2DREGION              ActiveSize;
  D3DDDI_RATIONAL               VSyncFreq;
  D3DDDI_RATIONAL               HSyncFreq;
  SIZE_T                        PixelRate;
  union {
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3_M1)
    struct {
      D3DDDI_VIDEO_SIGNAL_SCANLINE_ORDERING ScanLineOrdering  :3;
      UINT                                  VSyncFreqDivider  :6;
      UINT                                  Reserved  :23;
    } AdditionalSignalInfo;
#endif 
    D3DDDI_VIDEO_SIGNAL_SCANLINE_ORDERING ScanLineOrdering;
  };
} D3DKMDT_VIDEO_SIGNAL_INFO;
````


## -struct-fields
<dl>

### -field <b>VideoStandard</b>

<dd>
<p>A constant from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546632">D3DKMDT_VIDEO_SIGNAL_STANDARD</a> enumeration that indicates the video standard (if any) that defines the video signal.</p>
</dd>

### -field <b>TotalSize</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545977">D3DKMDT_2DREGION</a> structure that specifies the width and height (in pixels) of the entire video signal.</p>
</dd>

### -field <b>ActiveSize</b>

<dd>
<p>A D3DKMDT_2DREGION structure that specifies the width and height (in pixels) of the active portion of the video signal.</p>
</dd>

### -field <b>VSyncFreq</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544641">D3DDDI_RATIONAL</a> structure that specifies the vertical refresh rate in Hz.</p>
</dd>

### -field <b>HSyncFreq</b>

<dd>
<p>A D3DDDI_RATIONAL structure that specifies the horizontal refresh rate in Hz.</p>
</dd>

### -field <b>PixelRate</b>

<dd>
<p>The pixel clock rate.</p>
</dd>

### -field <b>AdditionalSignalInfo</b>

<dd>
<p>Supported by WDDM 1.3 and later display miniport drivers running on Windows 8.1 and later.</p>
<dl>

### -field <b>ScanLineOrdering</b>

<dd>
<p>A constant from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544682">D3DDDI_VIDEO_SIGNAL_SCANLINE_ORDERING</a> enumeration that indicates the scanline ordering (for example, progressive or interlaced) of the video signal.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>VSyncFreqDivider</b>

<dd>
<p>The ratio of the VSync rate of a monitor that displays through a Miracast connected session to the VSync rate of the Miracast sink.</p>
<p>To avoid visual artifacts, the VSync rate of the display monitor that's connected to the Miracast sink must be an integer multiple of the VSync rate of the Miracast sink. The display miniport driver reports the latter rate to the operating system as the refresh rate of the desktop present path.</p>
<div class="alert"><b>Note</b>  The operating system fails any attempt by the driver to add a target mode that results in a Miracast target having a VSync rate below 23.9 Hz.</div>
<div> </div>
<p>For a non-Miracast target, the driver should set <b>VSyncFreqDivider</b> to zero.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>
</dl>
</dd>

### -field <b>ScanLineOrdering</b>

<dd>
<p>A constant from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544682">D3DDDI_VIDEO_SIGNAL_SCANLINE_ORDERING</a> enumeration that indicates the scanline ordering (for example, progressive or interlaced) of the video signal.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546729">D3DKMDT_VIDPN_TARGET_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546617">D3DKMDT_VIDEO_PRESENT_TARGET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_VIDEO_SIGNAL_INFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
