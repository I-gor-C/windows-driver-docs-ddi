---
UID: NF.video.VideoPortReadPortBufferUshort
title: VideoPortReadPortBufferUshort function
author: windows-driver-content
description: The VideoPortReadPortBufferUshort function reads a number of USHORT values from a mapped I/O port and writes them into a buffer.
old-location: display\videoportreadportbufferushort.htm
old-project: display
ms.assetid: 3ad19dc0-f301-4367-b867-6bc714fd3d5e
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: VideoPortReadPortBufferUshort
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
req.alt-api: VideoPortReadPortBufferUshort
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
req.product: Windows 10 or later.
---

# VideoPortReadPortBufferUshort function



## -description
The <b>VideoPortReadPortBufferUshort</b> function reads a number of USHORT values from a mapped I/O port and writes them into a buffer.



## -syntax

````
VOID VideoPortReadPortBufferUshort(
        PUSHORT Port,
  _Out_ PUSHORT Buffer,
        ULONG   Count
);
````


## -parameters

### -param Port 

Pointer to the port. The given <i>Port</i> must be in a mapped I/O-space range returned by <a href="display.videoportgetdevicebase">VideoPortGetDeviceBase</a>.


### -param Buffer [out]

Pointer to a buffer into which an array of USHORT values is written.


### -param Count 

Specifies the number of USHORT values to be written to the buffer.


## -returns
None


## -remarks
The buffer must be large enough to contain at least the specified number of USHORT values.

A miniport driver's <a href="..\video\nc-video-pvideo_hw_interrupt.md">HwVidInterrupt</a> or <a href="..\video\nc-video-pminiport_synchronize_routine.md">HwVidSynchronizeExecutionCallback</a> function can call <b>VideoPortReadPortBufferUshort</b>.

Callers of <b>VideoPortReadPortBufferUshort</b> can be running at any IRQL, provided that the memory pointed to by the <i>Buffer</i> parameter is resident and that pointed to by the <i>Port</i> parameter is resident, mapped device memory.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 2000 and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
See Remarks section.

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nc-video-pvideo_hw_interrupt.md">HwVidInterrupt</a>
</dt>
<dt>
<a href="..\video\nc-video-pminiport_synchronize_routine.md">HwVidSynchronizeExecutionCallback</a>
</dt>
<dt>
<a href="display.videoportgetdevicebase">VideoPortGetDeviceBase</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortReadPortBufferUshort function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

