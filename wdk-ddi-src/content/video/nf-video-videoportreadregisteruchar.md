---
UID: NF.video.VideoPortReadRegisterUchar
title: VideoPortReadRegisterUchar
author: windows-driver-content
description: The VideoPortReadRegisterUchar function reads a byte from a mapped register.
old-location: display\videoportreadregisteruchar.htm
old-project: display
ms.assetid: 53270599-7e8e-491a-8d7b-05f550f100d3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortReadRegisterUchar
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
req.alt-api: VideoPortReadRegisterUchar
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
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortReadRegisterUchar function



## -description
<p>The <b>VideoPortReadRegisterUchar</b> function reads a byte from a mapped register.</p>


## -syntax

````
UCHAR VideoPortReadRegisterUchar(
   PUCHAR Register
);
````


## -parameters
<dl>

### -param <i>Register</i> 

<dd>
<p>Pointer to the register. The given <i>Register</i> must be in a mapped memory-space range returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff570310">VideoPortGetDeviceBase</a>.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortReadRegisterUchar</b> returns the byte read from the adapter.</p>

## -remarks
<p>A miniport driver's <a href="..\video\nc-video-pvideo-hw-interrupt.md">HwVidInterrupt</a> or <a href="..\video\nc-video-pminiport-synchronize-routine.md">HwVidSynchronizeExecutionCallback</a> function can call <b>VideoPortReadRegisterUchar</b>.</p>

<p>Callers of <b>VideoPortReadRegisterUchar</b> can be running at any IRQL, provided that the memory pointed to by the <i>Register</i> parameter is resident, mapped device memory.</p>

<p>A miniport driver's <a href="..\video\nc-video-pvideo-hw-interrupt.md">HwVidInterrupt</a> or <a href="..\video\nc-video-pminiport-synchronize-routine.md">HwVidSynchronizeExecutionCallback</a> function can call <b>VideoPortReadRegisterUchar</b>.</p>

<p>Callers of <b>VideoPortReadRegisterUchar</b> can be running at any IRQL, provided that the memory pointed to by the <i>Register</i> parameter is resident, mapped device memory.</p>

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
<p>See Remarks section.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570310">VideoPortGetDeviceBase</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortReadRegisterUchar function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
