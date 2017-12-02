---
UID: NF.video.VideoPortGetDeviceBase
title: VideoPortGetDeviceBase
author: windows-driver-content
description: The VideoPortGetDeviceBase function maps a range of bus-relative device memory or I/O addresses into system space.
old-location: display\videoportgetdevicebase.htm
old-project: display
ms.assetid: 53665c1d-8c0b-45c7-8d23-13c0964eda39
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortGetDeviceBase
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
req.alt-api: VideoPortGetDeviceBase
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

# VideoPortGetDeviceBase function



## -description
<p>The <b>VideoPortGetDeviceBase</b> function maps a range of bus-relative device memory or I/O addresses into system space.</p>


## -syntax

````
PVOID VideoPortGetDeviceBase(
   PVOID            HwDeviceExtension,
   PHYSICAL_ADDRESS IoAddress,
   ULONG            NumberOfUchars,
   UCHAR            InIoSpace
);
````


## -parameters
<dl>

### -param HwDeviceExtension 

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param IoAddress 

<dd>
<p>The base physical address of the range to map. You get this bus-relative value by calling <a href="..\video\nf-video-videoportgetdevicedata.md">VideoPortGetDeviceData</a>, <a href="..\video\nf-video-videoportgetregistryparameters.md">VideoPortGetRegistryParameters</a>, or <a href="..\video\nf-video-videoportgetaccessranges.md">VideoPortGetAccessRanges</a>. Otherwise, this value is a driver-supplied, default base address for the device memory or I/O ports.</p>
<p>You must have successfully claimed the range described by <i>IoAddress</i> and <i>NumberOfUchars</i> in the registry through a preceding call to <a href="..\video\nf-video-videoportverifyaccessranges.md">VideoPortVerifyAccessRanges</a> or <b>VideoPortGetAccessRanges</b>.</p>
</dd>

### -param NumberOfUchars 

<dd>
<p>The number of bytes, starting at <i>IoAddress</i>, to map.</p>
</dd>

### -param InIoSpace 

<dd>
<p>The location of the <i>IoAddress</i> range. This parameter can be one of the following flags or an ORed, compatible combination of these flags.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_DENSE</p>
</td>
<td>
<p>Obsolete.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_IO</p>
</td>
<td>
<p>The address range is in I/O space, not in memory space.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_MEMORY</p>
</td>
<td>
<p>The address range is in memory space, not in I/O space.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_P6CACHE</p>
</td>
<td>
<p>The processor aggregates a sequence of write operations, sends them to a cache line, and later flushes the cache. This flag is meaningful only when VIDEO_MEMORY_SPACE_IO is not set.</p>
<p>Designates the video memory as write-combined (WC). For information about WC caching, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=204787">Write-Combining Memory in Video Miniport Drivers</a> website article.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>If successful, <b>VideoPortGetDeviceBase</b> returns the base virtual address of the mapping. If the specified bus-relative range cannot be mapped, <b>VideoPortGetDeviceBase</b> returns <b>NULL</b>.</p>

## -remarks
<p>You can pass the mapped virtual addresses to the <b>VideoPortRead</b><i>Xxx</i>, <b>VideoPortWrite</b><i>Xxx</i>, and <b>VideoPort</b><i>Xxx</i><b>Memory</b> functions, except for <a href="..\video\nf-video-videoportmapmemory.md">VideoPortMapMemory</a> and <a href="..\video\nf-video-videoportunmapmemory.md">VideoPortUnmapMemory</a>.</p>

<p>You must call <b>VideoPortGetDeviceBase</b> from the miniport driver's <a href="..\video\nc-video-pvideo-hw-find-adapter.md">HwVidFindAdapter</a>, <a href="..\video\nc-video-pminiport-query-device-routine.md">HwVidQueryDeviceCallback</a>, or <a href="..\video\nc-video-pminiport-get-registry-routine.md">HwVidQueryNamedValueCallback</a> function.</p>

<p>Before <i>HwVidFindAdapter</i> returns control, you should store both the mapped base address returned by <b>VideoPortGetDeviceBase</b> and the length of the mapped access range in the adapter's device extension (pointed to by <i>HwDeviceExtension</i>) for later use.</p>

<p>Access to the mapped address space must follow these rules:</p>

<p>If <i>InIoSpace</i> is VIDEO_MEMORY_SPACE_IO, which indicates that the address is in I/O space, the virtual address that this function returns should be passed to the <b>VideoPortReadPort</b><i>Xxx</i>, <b>VideoPortWritePort</b><i>Xxx</i>, <b>VideoPortReadPortBuffer</b><i>Xxx</i>, and <b>VideoPortWritePortBuffer</b><i>Xxx</i> functions, where <i>Xxx</i> is <b>Uchar</b>, <b>Ushort</b>, or <b>Ulong</b>.</p>

<p>If <i>InIoSpace</i> is VIDEO_MEMORY_SPACE_MEMORY, which indicates that the address is not in I/O space but in memory space, the virtual address that this function returns should be passed to the <b>VideoPortReadRegister</b><i>Xxx</i>, <b>VideoPortWriteRegister</b><i>Xxx</i>, <b>VideoPortReadRegisterBuffer</b><i>Xxx</i>, and <b>VideoPortWriteRegisterBuffer</b><i>Xxx</i> functions, where <i>Xxx</i> is <b>Uchar</b>, <b>Ushort</b>, or <b>Ulong</b>.</p>

<p>The driver must not access addresses that are outside the range delimited by <i>NumberOfUchars</i>.</p>

<p><b>VideoPortGetDeviceBase</b> and <a href="..\video\nf-video-videoportmapmemory.md">VideoPortMapMemory</a> can both be called by the video miniport driver to map video memory into a virtual address space. If you call both of these functions to map the same physical addresses, or if you call one of the functions more than once to map the same physical addresses, you might have more than one virtual-address range that maps to the same physical-address range. In that case, you must set the VIDEO_MEMORY_SPACE_P6CACHE flag of the <i>InIoSpace</i> parameter to the same value in all of those calls.</p>

<p>Every universal memory architecture (UMA) display device uses a frame buffer that is located in main memory rather than on a PCI bus. In this case, do not call <b>VideoPortMapMemory</b> to map the frame buffer. To map a UMA frame buffer into system space, call <a href="..\wdm\nf-wdm-mmmapiospace.md">MmMapIoSpace</a>.</p>

<p>If a miniport driver does not support an adapter that it has mapped a logical range for, it must perform two steps before it returns control to the <a href="display.driverentry_of_video_miniport_driver">DriverEntry</a> function: call <a href="..\video\nf-video-videoportfreedevicebase.md">VideoPortFreeDeviceBase</a> to unmap the previously mapped range from system space, and call <a href="..\video\nf-video-videoportgetaccessranges.md">VideoPortGetAccessRanges</a> or <a href="..\video\nf-video-videoportverifyaccessranges.md">VideoPortVerifyAccessRanges</a> to release its claims on the range in the registry. </p>

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
<a href="..\video\nc-video-pminiport-query-device-routine.md">HwVidQueryDeviceCallback</a>
</dt>
<dt>
<a href="..\video\nc-video-pminiport-get-registry-routine.md">HwVidQueryNamedValueCallback</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportcomparememory.md">VideoPortCompareMemory</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportfreedevicebase.md">VideoPortFreeDeviceBase</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportgetaccessranges.md">VideoPortGetAccessRanges</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportgetdevicedata.md">VideoPortGetDeviceData</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportgetregistryparameters.md">VideoPortGetRegistryParameters</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportmovememory.md">VideoPortMoveMemory</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportverifyaccessranges.md">VideoPortVerifyAccessRanges</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportzerodevicememory.md">VideoPortZeroDeviceMemory</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportzeromemory.md">VideoPortZeroMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortGetDeviceBase function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
