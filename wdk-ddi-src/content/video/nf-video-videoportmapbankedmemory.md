---
UID: NF.video.VideoPortMapBankedMemory
title: VideoPortMapBankedMemory
author: windows-driver-content
description: The VideoPortMapBankedMemory function is obsolete, and is supported only for Windows NT 4.0 and previous drivers.
old-location: display\videoportmapbankedmemory.htm
old-project: display
ms.assetid: ee94d883-b4c4-4cd5-9b61-2e51810f8fc8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortMapBankedMemory
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
req.alt-api: VideoPortMapBankedMemory
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

# VideoPortMapBankedMemory function



## -description
<p>The <b>VideoPortMapBankedMemory</b> function is <b>obsolete</b>, and is supported only for Windows NT 4.0 and previous drivers. Windows 2000 and later drivers must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff570331">VideoPortMapMemory</a>.</p>
<p><b>VideoPortMapBankedMemory</b> remaps a bus-relative physical range of video memory into the corresponding display driver's virtual address space in response to a VRP with the <b>IoControlCode</b> member set to <a href="https://msdn.microsoft.com/library/windows/hardware/ff568149">IOCTL_VIDEO_SHARE_VIDEO_MEMORY</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567812">IOCTL_VIDEO_MAP_VIDEO_MEMORY</a>. </p>


## -syntax

````
VP_STATUS VideoPortMapBankedMemory(
   PVOID                   HwDeviceExtension,
   PHYSICAL_ADDRESS        PhysicalAddress,
   PULONG                  Length,
   PULONG                  InIoSpace,
   PVOID                   *VirtualAddress,
   ULONG                   BankLength,
   UCHAR                   ReadWriteBank,
   PBANKED_SECTION_ROUTINE BankRoutine,
   PVOID                   Context
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> 

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>PhysicalAddress</i> 

<dd>
<p>Specifies the bus-relative base address of the range to be mapped.</p>
</dd>

### -param <i>Length</i> 

<dd>
<p>Pointer to a variable specifying the total number of bytes of device memory to be mapped (regardless of bank size). <b>VideoPortMapBankedMemory</b> returns the actual size of the memory mapped, which can be rounded to a system-determined alignment boundary, in this parameter. However, the miniport and display drivers cannot access memory outside the range delimited by the input value at <i>Length</i>.</p>
</dd>

### -param <i>InIoSpace</i> 

<dd>
<p>Indicates the location of the range. This parameter can be one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_DENSE</p>
</td>
<td>
<p>Obsolete</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_IO</p>
</td>
<td>
<p>The range is in system I/O space rather than in memory space.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_MEMORY</p>
</td>
<td>
<p>The range is in memory space rather than in system I/O space.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_P6CACHE</p>
</td>
<td>
<p>The processor aggregates a sequence of write operations and sends them to a given cache line. The processor then flushes the cache. This flag is meaningful only when VIDEO_MEMORY_SPACE_IO is <i>not</i> set.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_USER_MODE</p>
</td>
<td>
<p>Indicates that the address range specified should be mapped into user mode rather than kernel mode. This flag is meaningful only when VIDEO_MEMORY_SPACE_IO is <i>not</i> set.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>VirtualAddress</i> 

<dd>
<p>Is a handle to the process into which the memory must be mapped, or <b>NULL</b>. <b>NULL</b> specifies that the port driver should map the logical memory range at any location in the address space of the current process. Otherwise, this handle can be a value passed in a <a href="wdkgloss.v#wdkgloss.video_request_packet__vrp_#wdkgloss.video_request_packet__vrp_"><i>VRP</i></a> by the miniport driver's corresponding display driver. On return from a successful call, <b>VideoPortMapBankedMemory</b> resets the variable to the base virtual address to which it has mapped the given <i>PhysicalAddress</i>.</p>
</dd>

### -param <i>BankLength</i> 

<dd>
<p>Specifies the size of a bank, in bytes.</p>
</dd>

### -param <i>ReadWriteBank</i> 

<dd>
<p>If set to <b>TRUE</b> the bank is Read\Write; if set to <b>FALSE</b> there are two independent read and write banks. </p>
</dd>

### -param <i>BankRoutine</i> 

<dd>
<p>Pointer to a driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff567322">HwVidBankedMemoryCallback</a> function to be called by the Memory Manager when a new bank is accessed by the display driver.</p>
</dd>

### -param <i>Context</i> 

<dd>
<p>Pointer to a miniport driver-supplied context that is passed back to the driver when the <i>BankRoutine</i> is called.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortMapBankedMemory</b> returns NO_ERROR if the given logical range was successfully mapped to a user-space virtual range. Otherwise, it can return ERROR_INVALID_PARAMETER.</p>

## -remarks
<p><b>VideoPortMapBankedMemory</b> runs in kernel mode within the same context as the user-mode thread that initiated the call.</p>

<p><b>VideoPortMapBankedMemory</b> is called by miniport drivers to efficiently manage x86 type devices that are limited to mapping a frame buffer in banks. When this routine returns to the caller, the frame buffer managed by the miniport driver is mapped as a linear frame buffer into the address space of the requesting process (see <i>VirtualAddress</i> parameter). When an access is made to an address in that mapped space, the Memory Manager calls the miniport driver to update the Bank Index Register to point to a new bank that contains the currently referenced address. The Bank Index Register is maintained by the miniport driver in <i>BankRoutine</i>. The correct Bank Index is calculated by the Memory Manager transparently to a display driver and passed to the miniport driver in the callback to <i>BankRoutine</i>. </p>

<p><b>VideoPortMapBankedMemory</b> runs in kernel mode within the same context as the user-mode thread that initiated the call.</p>

<p><b>VideoPortMapBankedMemory</b> is called by miniport drivers to efficiently manage x86 type devices that are limited to mapping a frame buffer in banks. When this routine returns to the caller, the frame buffer managed by the miniport driver is mapped as a linear frame buffer into the address space of the requesting process (see <i>VirtualAddress</i> parameter). When an access is made to an address in that mapped space, the Memory Manager calls the miniport driver to update the Bank Index Register to point to a new bank that contains the currently referenced address. The Bank Index Register is maintained by the miniport driver in <i>BankRoutine</i>. The correct Bank Index is calculated by the Memory Manager transparently to a display driver and passed to the miniport driver in the callback to <i>BankRoutine</i>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567322">HwVidBankedMemoryCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567812">IOCTL_VIDEO_MAP_VIDEO_MEMORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568149">IOCTL_VIDEO_SHARE_VIDEO_MEMORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568155">IOCTL_VIDEO_UNSHARE_VIDEO_MEMORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570547">VIDEO_REQUEST_PACKET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570331">VideoPortMapMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570376">VideoPortUnmapMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortMapBankedMemory function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
