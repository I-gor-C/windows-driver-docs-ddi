---
UID: NF.video.VideoPortInt10
title: VideoPortInt10
author: windows-driver-content
description: The VideoPortInt10 function performs the equivalent of an MS-DOS INT10 operation, such as setting the video mode. VideoPortInt10 runs the BIOS ROM code on the device.
old-location: display\videoportint10.htm
old-project: display
ms.assetid: 5743d84c-6132-4058-b517-250b5de9a6b5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortInt10
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortInt10
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortInt10 function



## -description
<p>The <b>VideoPortInt10</b> function performs the equivalent of an MS-DOS INT10 operation, such as setting the video mode. <b>VideoPortInt10</b> runs the BIOS ROM code on the device.</p>


## -syntax

````
VP_STATUS VideoPortInt10(
   PVOID                     HwDeviceExtension,
   PVIDEO_X86_BIOS_ARGUMENTS BiosArguments
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> 

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>BiosArguments</i> 

<dd>
<p>Pointer to a structure containing values for the x86 registers that should be set before making the BIOS call. The miniport driver should set any unused registers to zero. All values set up in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570553">VIDEO_x86_BIOS_ARGUMENTS</a> structure are interpreted as immediate values.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortInt10</b> returns NO_ERROR if it successfully called the given BIOS INT10 routine; otherwise, it returns an error status.</p>

## -remarks
<p>Generally, VGA-compatible miniport drivers, which support full-screen MS-DOS applications on x86-based machines, call <b>VideoPortInt10</b>. Such a driver's <a href="..\video\nc-video-pvideo-hw-find-adapter.md">HwVidFindAdapter</a> function must have set up the <b>VdmPhysicalVideoMemoryAddress</b> and <b>VdmPhysicalVideoMemoryLength</b> for the range in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570531">VIDEO_PORT_CONFIG_INFO</a> structure.</p>

<p>However, other video miniport drivers also can call this function.</p>

<p>Because <b>VideoPortInt10</b> interprets the <i>BiosArgument</i> parameter values as immediate values, the caller cannot pass in or retrieve data from a memory buffer with this function. </p>

<p>Generally, VGA-compatible miniport drivers, which support full-screen MS-DOS applications on x86-based machines, call <b>VideoPortInt10</b>. Such a driver's <a href="..\video\nc-video-pvideo-hw-find-adapter.md">HwVidFindAdapter</a> function must have set up the <b>VdmPhysicalVideoMemoryAddress</b> and <b>VdmPhysicalVideoMemoryLength</b> for the range in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570531">VIDEO_PORT_CONFIG_INFO</a> structure.</p>

<p>However, other video miniport drivers also can call this function.</p>

<p>Because <b>VideoPortInt10</b> interprets the <i>BiosArgument</i> parameter values as immediate values, the caller cannot pass in or retrieve data from a memory buffer with this function. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nc-video-pvideo-hw-find-adapter.md">HwVidFindAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570531">VIDEO_PORT_CONFIG_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570553">VIDEO_x86_BIOS_ARGUMENTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570310">VideoPortGetDeviceBase</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortInt10 function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
