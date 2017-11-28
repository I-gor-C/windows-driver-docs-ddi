---
UID: NF.video.VideoPortStallExecution
title: VideoPortStallExecution
author: windows-driver-content
description: The VideoPortStallExecution function retains control of the processor for the specified number of microseconds and returns to the caller.
old-location: display\videoportstallexecution.htm
old-project: display
ms.assetid: 70b406f8-d9ac-4882-89bc-e257cbe06921
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortStallExecution
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
req.alt-api: VideoPortStallExecution
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
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortStallExecution function



## -description
<p>The <b>VideoPortStallExecution</b> function retains control of the processor for the specified number of microseconds and returns to the caller.</p>


## -syntax

````
VOID VideoPortStallExecution(
   ULONG Microseconds
);
````


## -parameters
<dl>

### -param <i>Microseconds</i> 

<dd>
<p>Specifies the delay interval, in microseconds.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Maximum acceptable values for <i>Microseconds</i> are thousands of microseconds during miniport driver initialization. Otherwise, the given delay interval must be no more than 50 microseconds. In general, <b>VideoPortStallExecution</b> can be called only if the miniport driver must wait for a very few microseconds for its adapter to update state.</p>

<p>While a miniport driver's <a href="..\video\nc-video-pvideo-hw-interrupt.md">HwVidInterrupt</a> or <a href="..\video\nc-video-pminiport-synchronize-routine.md">HwVidSynchronizeExecutionCallback</a> function can call <b>VideoPortStallExecution</b>, the miniport driver should be designed to avoid such a call if at all possible. Delays while running at high hardware priorities adversely affect the overall I/O throughput of the system and can freeze the machine.</p>

<p>If a miniport driver has work to be done at regular intervals of more than 50 microseconds, it should implement the <a href="..\video\nc-video-pvideo-hw-timer.md">HwVidTimer</a> function. Calls to a miniport driver-supplied <i>HwVidTimer</i> function at approximately one-second intervals can be enabled with <a href="https://msdn.microsoft.com/library/windows/hardware/ff570370">VideoPortStartTimer</a> and disabled with <a href="https://msdn.microsoft.com/library/windows/hardware/ff570371">VideoPortStopTimer</a>. </p>

<p>Maximum acceptable values for <i>Microseconds</i> are thousands of microseconds during miniport driver initialization. Otherwise, the given delay interval must be no more than 50 microseconds. In general, <b>VideoPortStallExecution</b> can be called only if the miniport driver must wait for a very few microseconds for its adapter to update state.</p>

<p>While a miniport driver's <a href="..\video\nc-video-pvideo-hw-interrupt.md">HwVidInterrupt</a> or <a href="..\video\nc-video-pminiport-synchronize-routine.md">HwVidSynchronizeExecutionCallback</a> function can call <b>VideoPortStallExecution</b>, the miniport driver should be designed to avoid such a call if at all possible. Delays while running at high hardware priorities adversely affect the overall I/O throughput of the system and can freeze the machine.</p>

<p>If a miniport driver has work to be done at regular intervals of more than 50 microseconds, it should implement the <a href="..\video\nc-video-pvideo-hw-timer.md">HwVidTimer</a> function. Calls to a miniport driver-supplied <i>HwVidTimer</i> function at approximately one-second intervals can be enabled with <a href="https://msdn.microsoft.com/library/windows/hardware/ff570370">VideoPortStartTimer</a> and disabled with <a href="https://msdn.microsoft.com/library/windows/hardware/ff570371">VideoPortStopTimer</a>. </p>

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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nc-video-pvideo-hw-interrupt.md">HwVidInterrupt</a>
</dt>
<dt>
<a href="..\video\nc-video-pminiport-synchronize-routine.md">HwVidSynchronizeExecutionCallback</a>
</dt>
<dt>
<a href="..\video\nc-video-pvideo-hw-timer.md">HwVidTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570370">VideoPortStartTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570371">VideoPortStopTimer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortStallExecution function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
