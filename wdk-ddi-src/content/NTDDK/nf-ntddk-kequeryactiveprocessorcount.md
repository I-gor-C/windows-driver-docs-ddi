---
UID: NF.ntddk.KeQueryActiveProcessorCount
title: KeQueryActiveProcessorCount
author: windows-driver-content
description: The KeQueryActiveProcessorCount routine returns the number of currently active processors.
old-location: kernel\kequeryactiveprocessorcount.htm
ms.assetid: 4369ad33-ba4a-45db-9a41-e77d6c55da53
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeQueryActiveProcessorCount
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
ms.keywords: KeQueryActiveProcessorCount
req.iface: 
---

# KeQueryActiveProcessorCount function



## -description
<p>The <b>KeQueryActiveProcessorCount</b> routine returns the number of currently active processors.</p>


## -syntax

````
ULONG KeQueryActiveProcessorCount(
  _Out_opt_ PKAFFINITY ActiveProcessors
);
````


## -parameters
<dl>

### -param <i>ActiveProcessors</i> [out, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a>-typed variable into which the routine writes a bitmask that represents the set of currently active processors. In a hot-add environment, this mask may change during runtime. This parameter is optional and can be specified as <b>NULL</b> if the caller does not require the mask of active processors. </p>
</dd>
</dl>

## -returns
<p><b>KeQueryActiveProcessorCount</b> returns the number of currently active processors. </p>

## -remarks
<p>A device driver calls the <b>KeQueryActiveProcessorCount</b> routine to retrieve the number of currently active processors. Device drivers that are built for Windows Vista and later versions of the Windows operating system should not use the <b>KeNumberProcessors</b> kernel variable for this purpose.</p>

<p>Callers cannot assume that the <b>KeQueryActiveProcessorCount</b> routine maps processors to bits in the returned <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a> value consecutively, or that the routine will return the same bitmask each time it is called.</p>

<p>Callers must also be aware that the value returned by <b>KeQueryActiveProcessorCount</b> can change at runtime on versions of Windows that support hot-add CPU functionality.</p>

<p>If necessary, register for notification of changes to the number of processors by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553120">KeRegisterProcessorChangeCallback</a> routine.</p>

<p>To query just the affinity mask without getting the number of active processors, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553001">KeQueryActiveProcessors</a>.</p>

<p>Windows 7 and later versions of Windows support processor groups. Drivers that are designed to handle information about processor groups should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552993">KeQueryActiveProcessorCountEx</a> routine, which specifies a processor group, instead of <b>KeQueryActiveProcessorCount</b>, which does not. However, the implementation of <b>KeQueryActiveProcessorCount</b> in Windows 7 and later versions of Windows provides compatibility for drivers that were written for earlier versions of Windows, which do not support processor groups. In this implementation, <b>KeQueryActiveProcessorCount</b> returns the number of active logical processors in group 0, and writes an affinity mask to *<i>ActiveProcessors</i> that specifies the set of active logical processors in group 0. </p>

<p>The KAFFINITY type is an affinity mask that represents a set of logical processors in a group. The KAFFINITY type is 32 bits on a 32-bit version of Windows and is 64 bits on a 64-bit version of Windows.</p>

<p>If a group contains <i>n</i> logical processors, the processors are numbered from 0 to <i>n</i>-1. Processor number <i>i</i> in the group is represented by bit <i>i</i> in the affinity mask, where <i>i</i> is in the range 0 to <i>n</i>-1. Affinity mask bits that do not correspond to logical processors are always zero.</p>

<p>For example, if a KAFFINITY value identifies the active processors in a group, the mask bit for a processor is one if the processor is active, and is zero if the processor is not active.</p>

<p>The number of bits in the affinity mask determines the maximum number of logical processors in a group. For a 64-bit version of Windows, the maximum number of processors per group is 64. For a 32-bit version of Windows, the maximum number of processors per group is 32. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine to obtain the maximum number of processors per group. This number depends on the hardware configuration of the multiprocessor system, but can never exceed the fixed 64-processor and 32-processor limits that are set by the 64-bit and 32-bit versions of Windows, respectively.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a> structure contains an affinity mask and a group number. The group number identifies the group to which the affinity mask applies.</p>

<p>Kernel routines that use the KAFFINITY type include <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>, <b>KeQueryActiveProcessorCount</b>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553001">KeQueryActiveProcessors</a>. </p>

<p>A device driver calls the <b>KeQueryActiveProcessorCount</b> routine to retrieve the number of currently active processors. Device drivers that are built for Windows Vista and later versions of the Windows operating system should not use the <b>KeNumberProcessors</b> kernel variable for this purpose.</p>

<p>Callers cannot assume that the <b>KeQueryActiveProcessorCount</b> routine maps processors to bits in the returned <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a> value consecutively, or that the routine will return the same bitmask each time it is called.</p>

<p>Callers must also be aware that the value returned by <b>KeQueryActiveProcessorCount</b> can change at runtime on versions of Windows that support hot-add CPU functionality.</p>

<p>If necessary, register for notification of changes to the number of processors by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553120">KeRegisterProcessorChangeCallback</a> routine.</p>

<p>To query just the affinity mask without getting the number of active processors, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553001">KeQueryActiveProcessors</a>.</p>

<p>Windows 7 and later versions of Windows support processor groups. Drivers that are designed to handle information about processor groups should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552993">KeQueryActiveProcessorCountEx</a> routine, which specifies a processor group, instead of <b>KeQueryActiveProcessorCount</b>, which does not. However, the implementation of <b>KeQueryActiveProcessorCount</b> in Windows 7 and later versions of Windows provides compatibility for drivers that were written for earlier versions of Windows, which do not support processor groups. In this implementation, <b>KeQueryActiveProcessorCount</b> returns the number of active logical processors in group 0, and writes an affinity mask to *<i>ActiveProcessors</i> that specifies the set of active logical processors in group 0. </p>

<p>The KAFFINITY type is an affinity mask that represents a set of logical processors in a group. The KAFFINITY type is 32 bits on a 32-bit version of Windows and is 64 bits on a 64-bit version of Windows.</p>

<p>If a group contains <i>n</i> logical processors, the processors are numbered from 0 to <i>n</i>-1. Processor number <i>i</i> in the group is represented by bit <i>i</i> in the affinity mask, where <i>i</i> is in the range 0 to <i>n</i>-1. Affinity mask bits that do not correspond to logical processors are always zero.</p>

<p>For example, if a KAFFINITY value identifies the active processors in a group, the mask bit for a processor is one if the processor is active, and is zero if the processor is not active.</p>

<p>The number of bits in the affinity mask determines the maximum number of logical processors in a group. For a 64-bit version of Windows, the maximum number of processors per group is 64. For a 32-bit version of Windows, the maximum number of processors per group is 32. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine to obtain the maximum number of processors per group. This number depends on the hardware configuration of the multiprocessor system, but can never exceed the fixed 64-processor and 32-processor limits that are set by the 64-bit and 32-bit versions of Windows, respectively.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a> structure contains an affinity mask and a group number. The group number identifies the group to which the affinity mask applies.</p>

<p>Kernel routines that use the KAFFINITY type include <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>, <b>KeQueryActiveProcessorCount</b>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553001">KeQueryActiveProcessors</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of Windows. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552993">KeQueryActiveProcessorCountEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553001">KeQueryActiveProcessors</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553120">KeRegisterProcessorChangeCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeQueryActiveProcessorCount routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
