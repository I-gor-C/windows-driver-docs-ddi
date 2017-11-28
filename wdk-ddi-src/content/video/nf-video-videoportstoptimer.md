---
UID: NF.video.VideoPortStopTimer
title: VideoPortStopTimer
author: windows-driver-content
description: The VideoPortStopTimer function disables calls to a miniport driver's HwVidTimer function.
old-location: display\videoportstoptimer.htm
old-project: display
ms.assetid: 8f6927e1-2342-4816-aa43-1849c3a7702b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortStopTimer
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
req.alt-api: VideoPortStopTimer
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortStopTimer function



## -description
<p>The <b>VideoPortStopTimer</b> function disables calls to a miniport driver's <a href="..\video\nc-video-pvideo-hw-timer.md">HwVidTimer</a> function.</p>


## -syntax

````
VOID VideoPortStopTimer(
   PVOID HwDeviceExtension
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> 

<dd>
<p>Pointer to the miniport driver's device extension. This pointer is the input parameter to the <i>HwVidTimer</i> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>After a miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff570370">VideoPortStartTimer</a>, its <i>HwVidTimer</i> function is called at approximately one-second intervals until the miniport driver calls <b>VideoPortStopTimer</b>. A miniport driver's <i>HwVidTimer</i> function <i>must not</i> call <b>VideoPortStopTimer</b>.</p>

<p>A miniport driver cannot call <b>VideoPortStartTimer</b> or <b>VideoPortStopTimer</b> if its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function set the <b>HwTimer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a> structure to <b>NULL</b>. </p>

<p>After a miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff570370">VideoPortStartTimer</a>, its <i>HwVidTimer</i> function is called at approximately one-second intervals until the miniport driver calls <b>VideoPortStopTimer</b>. A miniport driver's <i>HwVidTimer</i> function <i>must not</i> call <b>VideoPortStopTimer</b>.</p>

<p>A miniport driver cannot call <b>VideoPortStartTimer</b> or <b>VideoPortStopTimer</b> if its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function set the <b>HwTimer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a> structure to <b>NULL</b>. </p>

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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556159">DriverEntry of Video Miniport Driver</a>
</dt>
<dt>
<a href="..\video\nc-video-pvideo-hw-timer.md">HwVidTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570370">VideoPortStartTimer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortStopTimer function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
