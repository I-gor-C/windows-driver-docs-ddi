---
UID: NF.video.VideoPortMoveMemory
title: VideoPortMoveMemory
author: windows-driver-content
description: The VideoPortMoveMemory function copies data from the source location to the destination location in system memory.
old-location: display\videoportmovememory.htm
ms.assetid: 32b754ef-2a85-4ba7-9d4f-3c2de2501319
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortMoveMemory
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
ms.keywords: VideoPortMoveMemory
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortMoveMemory function



## -description
<p>The <b>VideoPortMoveMemory</b> function copies data from the source location to the destination location in system memory.</p>


## -syntax

````
VOID VideoPortMoveMemory(
  _Inout_ PVOID Destination,
  _Inout_ PVOID Source,
          ULONG Length
);
````


## -parameters
<dl>

### -param <i>Destination</i> [in, out]

<dd>
<p>Pointer to the destination location.</p>
</dd>

### -param <i>Source</i> [in, out]

<dd>
<p>Pointer to the location of the data to copy.</p>
</dd>

### -param <i>Length</i> 

<dd>
<p>Specifies the number of bytes to copy.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>VideoPortMoveMemory</b> moves memory either forward or backward, aligned or unaligned, in 4-byte blocks, followed by any remaining bytes.</p>

<p>The given <i>Destination</i> and <i>Source</i> must be in a mapped logical range returned by <b>VideoPortGetDeviceBase</b> and/or a <a href="wdkgloss.s#wdkgloss.system_space#wdkgloss.system_space"><i>system space</i></a> RAM address, such as an address on the stack.</p>

<p>Callers of <b>VideoPortMoveMemory</b> can be running at any IRQL if both memory blocks are resident. Otherwise, the caller must be running at IRQL &lt; DISPATCH_LEVEL.</p>

<p><b>VideoPortMoveMemory</b> moves memory either forward or backward, aligned or unaligned, in 4-byte blocks, followed by any remaining bytes.</p>

<p>The given <i>Destination</i> and <i>Source</i> must be in a mapped logical range returned by <b>VideoPortGetDeviceBase</b> and/or a <a href="wdkgloss.s#wdkgloss.system_space#wdkgloss.system_space"><i>system space</i></a> RAM address, such as an address on the stack.</p>

<p>Callers of <b>VideoPortMoveMemory</b> can be running at any IRQL if both memory blocks are resident. Otherwise, the caller must be running at IRQL &lt; DISPATCH_LEVEL.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570285">VideoPortCompareMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570310">VideoPortGetDeviceBase</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570492">VideoPortZeroDeviceMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570493">VideoPortZeroMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortMoveMemory function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
