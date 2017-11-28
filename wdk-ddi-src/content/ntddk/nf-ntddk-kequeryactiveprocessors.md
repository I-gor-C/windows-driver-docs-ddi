---
UID: NF.ntddk.KeQueryActiveProcessors
title: KeQueryActiveProcessors
author: windows-driver-content
description: The KeQueryActiveProcessors routine returns a bitmask of the currently active processors.
old-location: kernel\kequeryactiveprocessors.htm
old-project: kernel
ms.assetid: 3a7e50e9-0aeb-46e8-a1d2-7267df4921ad
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeQueryActiveProcessors
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeQueryActiveProcessors
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlKeApcLte1, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: See Remarks section.
req.iface: 
---

# KeQueryActiveProcessors function



## -description
<p>The <b>KeQueryActiveProcessors</b> routine returns a bitmask of the currently active processors.</p>


## -syntax

````
KAFFINITY KeQueryActiveProcessors(void);
````


## -parameters


## -returns
<p><b>KeQueryActiveProcessors</b> returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a> value that represents the set of currently active processors.</p>

<p><b>KeQueryActiveProcessors</b> returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a> value that represents the set of currently active processors.</p>

<p><b>KeQueryActiveProcessors</b> returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a> value that represents the set of currently active processors.</p>

## -remarks
<p>Callers cannot assume that <b>KeQueryActiveProcessors</b> maps processors to bits consecutively, or that the routine consistently uses the same mapping each time it is called. The only valid use for the return value is to determine the number of active processors by counting the number of bits that are set.</p>

<p>Callers must also be aware that the value returned by <b>KeQueryActiveProcessors</b> can change during runtime on versions of Windows that support hot-add CPU functionality.</p>

<p>Windows 7 and later versions of Windows support processor groups. Drivers that are designed to handle information about processor groups should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553007">KeQueryGroupAffinity</a> routine, which specifies a processor group, instead of <b>KeQueryActiveProcessors</b>, which does not. However, the implementation of <b>KeQueryActiveProcessors</b> in Windows 7 and later versions of Windows provides compatibility for drivers that were written for earlier versions of Windows, which do not support processor groups. In this implementation, <b>KeQueryActiveProcessors</b> returns an affinity mask that specifies the set of active logical processors in group 0.</p>

<p>In Windows Vista and later versions of Windows, this routine can be called at any IRQL. However, in Windows Server 2003 and earlier versions of Windows, this routine must be called at IRQL &lt;= APC_LEVEL.</p>

<p>The KAFFINITY type is an affinity mask that represents a set of logical processors in a group. The KAFFINITY type is 32 bits on a 32-bit version of Windows and is 64 bits on a 64-bit version of Windows.</p>

<p>If a group contains <i>n</i> logical processors, the processors are numbered from 0 to <i>n</i>-1. Processor number <i>i</i> in the group is represented by bit <i>i</i> in the affinity mask, where <i>i</i> is in the range 0 to <i>n</i>-1. Affinity mask bits that do not correspond to logical processors are always zero.</p>

<p>For example, if a KAFFINITY value identifies the active processors in a group, the mask bit for a processor is one if the processor is active, and is zero if the processor is not active.</p>

<p>The number of bits in the affinity mask determines the maximum number of logical processors in a group. For a 64-bit version of Windows, the maximum number of processors per group is 64. For a 32-bit version of Windows, the maximum number of processors per group is 32. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine to obtain the maximum number of processors per group. This number depends on the hardware configuration of the multiprocessor system, but can never exceed the fixed 64-processor and 32-processor limits that are set by the 64-bit and 32-bit versions of Windows, respectively.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a> structure contains an affinity mask and a group number. The group number identifies the group to which the affinity mask applies.</p>

<p>Kernel routines that use the KAFFINITY type include <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>, and <b>KeQueryActiveProcessors</b>. </p>

<p>The <b>KeNumberProcessors</b> kernel variable is obsolete in Windows Vista with Service Pack 1 (SP1), Windows Server 2008, and later versions of Windows. <b>KeNumberProcessors</b> does not appear in WDK headers for WDK releases starting with Windows Vista SP1; however, the variable is still exported from the kernel, so drivers built for earlier platforms will not break</p>

<p>Windows Server 2008 includes support for <a href="https://msdn.microsoft.com/1b6a1dc5-ec32-4bb9-acaf-14db284b4a0e">Dynamic Hardware Partitioning</a> (DHP) in the Windows Datacenter and Enterprise Edition SKUs. As part of DHP, Windows Server 2008 supports hot adding CPUs at runtime. In a hot-add CPU environment, the number of processors may not remain constant during runtime.</p>

<p>Accordingly, in Windows Server 2008, code that can determine the number of processors must use <b>KeQueryActiveProcessors</b> instead of direct references to the kernel variable, <b>KeNumberProcessors</b>.</p>

<p>Review any code that currently references <b>KeNumberProcessors</b> to make sure that it accommodates changes to CPU count in hot-add CPU environments.</p>

<p>You can use the <a href="NULL">PNPCPU</a> tool to simulate hot adding a CPU for testing purposes.</p>

<p>Starting with Windows XP, <b>KeNumberProcessors</b> is an 8-bit integer value that indicates the number of processors in the platform. In earlier versions of Windows, <b>KeNumberProcessors</b> is a pointer to an 8-bit integer value that indicates the number of processors in the platform.</p>

<p>Callers cannot assume that <b>KeQueryActiveProcessors</b> maps processors to bits consecutively, or that the routine consistently uses the same mapping each time it is called. The only valid use for the return value is to determine the number of active processors by counting the number of bits that are set.</p>

<p>Callers must also be aware that the value returned by <b>KeQueryActiveProcessors</b> can change during runtime on versions of Windows that support hot-add CPU functionality.</p>

<p>Windows 7 and later versions of Windows support processor groups. Drivers that are designed to handle information about processor groups should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553007">KeQueryGroupAffinity</a> routine, which specifies a processor group, instead of <b>KeQueryActiveProcessors</b>, which does not. However, the implementation of <b>KeQueryActiveProcessors</b> in Windows 7 and later versions of Windows provides compatibility for drivers that were written for earlier versions of Windows, which do not support processor groups. In this implementation, <b>KeQueryActiveProcessors</b> returns an affinity mask that specifies the set of active logical processors in group 0.</p>

<p>In Windows Vista and later versions of Windows, this routine can be called at any IRQL. However, in Windows Server 2003 and earlier versions of Windows, this routine must be called at IRQL &lt;= APC_LEVEL.</p>

<p>The KAFFINITY type is an affinity mask that represents a set of logical processors in a group. The KAFFINITY type is 32 bits on a 32-bit version of Windows and is 64 bits on a 64-bit version of Windows.</p>

<p>If a group contains <i>n</i> logical processors, the processors are numbered from 0 to <i>n</i>-1. Processor number <i>i</i> in the group is represented by bit <i>i</i> in the affinity mask, where <i>i</i> is in the range 0 to <i>n</i>-1. Affinity mask bits that do not correspond to logical processors are always zero.</p>

<p>For example, if a KAFFINITY value identifies the active processors in a group, the mask bit for a processor is one if the processor is active, and is zero if the processor is not active.</p>

<p>The number of bits in the affinity mask determines the maximum number of logical processors in a group. For a 64-bit version of Windows, the maximum number of processors per group is 64. For a 32-bit version of Windows, the maximum number of processors per group is 32. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine to obtain the maximum number of processors per group. This number depends on the hardware configuration of the multiprocessor system, but can never exceed the fixed 64-processor and 32-processor limits that are set by the 64-bit and 32-bit versions of Windows, respectively.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a> structure contains an affinity mask and a group number. The group number identifies the group to which the affinity mask applies.</p>

<p>Kernel routines that use the KAFFINITY type include <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>, and <b>KeQueryActiveProcessors</b>. </p>

<p>The <b>KeNumberProcessors</b> kernel variable is obsolete in Windows Vista with Service Pack 1 (SP1), Windows Server 2008, and later versions of Windows. <b>KeNumberProcessors</b> does not appear in WDK headers for WDK releases starting with Windows Vista SP1; however, the variable is still exported from the kernel, so drivers built for earlier platforms will not break</p>

<p>Windows Server 2008 includes support for <a href="https://msdn.microsoft.com/1b6a1dc5-ec32-4bb9-acaf-14db284b4a0e">Dynamic Hardware Partitioning</a> (DHP) in the Windows Datacenter and Enterprise Edition SKUs. As part of DHP, Windows Server 2008 supports hot adding CPUs at runtime. In a hot-add CPU environment, the number of processors may not remain constant during runtime.</p>

<p>Accordingly, in Windows Server 2008, code that can determine the number of processors must use <b>KeQueryActiveProcessors</b> instead of direct references to the kernel variable, <b>KeNumberProcessors</b>.</p>

<p>Review any code that currently references <b>KeNumberProcessors</b> to make sure that it accommodates changes to CPU count in hot-add CPU environments.</p>

<p>You can use the <a href="NULL">PNPCPU</a> tool to simulate hot adding a CPU for testing purposes.</p>

<p>Starting with Windows XP, <b>KeNumberProcessors</b> is an 8-bit integer value that indicates the number of processors in the platform. In earlier versions of Windows, <b>KeNumberProcessors</b> is a pointer to an 8-bit integer value that indicates the number of processors in the platform.</p>

<p>Callers cannot assume that <b>KeQueryActiveProcessors</b> maps processors to bits consecutively, or that the routine consistently uses the same mapping each time it is called. The only valid use for the return value is to determine the number of active processors by counting the number of bits that are set.</p>

<p>Callers must also be aware that the value returned by <b>KeQueryActiveProcessors</b> can change during runtime on versions of Windows that support hot-add CPU functionality.</p>

<p>Windows 7 and later versions of Windows support processor groups. Drivers that are designed to handle information about processor groups should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553007">KeQueryGroupAffinity</a> routine, which specifies a processor group, instead of <b>KeQueryActiveProcessors</b>, which does not. However, the implementation of <b>KeQueryActiveProcessors</b> in Windows 7 and later versions of Windows provides compatibility for drivers that were written for earlier versions of Windows, which do not support processor groups. In this implementation, <b>KeQueryActiveProcessors</b> returns an affinity mask that specifies the set of active logical processors in group 0.</p>

<p>In Windows Vista and later versions of Windows, this routine can be called at any IRQL. However, in Windows Server 2003 and earlier versions of Windows, this routine must be called at IRQL &lt;= APC_LEVEL.</p>

<p>The KAFFINITY type is an affinity mask that represents a set of logical processors in a group. The KAFFINITY type is 32 bits on a 32-bit version of Windows and is 64 bits on a 64-bit version of Windows.</p>

<p>If a group contains <i>n</i> logical processors, the processors are numbered from 0 to <i>n</i>-1. Processor number <i>i</i> in the group is represented by bit <i>i</i> in the affinity mask, where <i>i</i> is in the range 0 to <i>n</i>-1. Affinity mask bits that do not correspond to logical processors are always zero.</p>

<p>For example, if a KAFFINITY value identifies the active processors in a group, the mask bit for a processor is one if the processor is active, and is zero if the processor is not active.</p>

<p>The number of bits in the affinity mask determines the maximum number of logical processors in a group. For a 64-bit version of Windows, the maximum number of processors per group is 64. For a 32-bit version of Windows, the maximum number of processors per group is 32. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine to obtain the maximum number of processors per group. This number depends on the hardware configuration of the multiprocessor system, but can never exceed the fixed 64-processor and 32-processor limits that are set by the 64-bit and 32-bit versions of Windows, respectively.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a> structure contains an affinity mask and a group number. The group number identifies the group to which the affinity mask applies.</p>

<p>Kernel routines that use the KAFFINITY type include <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>, and <b>KeQueryActiveProcessors</b>. </p>

<p>The <b>KeNumberProcessors</b> kernel variable is obsolete in Windows Vista with Service Pack 1 (SP1), Windows Server 2008, and later versions of Windows. <b>KeNumberProcessors</b> does not appear in WDK headers for WDK releases starting with Windows Vista SP1; however, the variable is still exported from the kernel, so drivers built for earlier platforms will not break</p>

<p>Windows Server 2008 includes support for <a href="https://msdn.microsoft.com/1b6a1dc5-ec32-4bb9-acaf-14db284b4a0e">Dynamic Hardware Partitioning</a> (DHP) in the Windows Datacenter and Enterprise Edition SKUs. As part of DHP, Windows Server 2008 supports hot adding CPUs at runtime. In a hot-add CPU environment, the number of processors may not remain constant during runtime.</p>

<p>Accordingly, in Windows Server 2008, code that can determine the number of processors must use <b>KeQueryActiveProcessors</b> instead of direct references to the kernel variable, <b>KeNumberProcessors</b>.</p>

<p>Review any code that currently references <b>KeNumberProcessors</b> to make sure that it accommodates changes to CPU count in hot-add CPU environments.</p>

<p>You can use the <a href="NULL">PNPCPU</a> tool to simulate hot adding a CPU for testing purposes.</p>

<p>Starting with Windows XP, <b>KeNumberProcessors</b> is an 8-bit integer value that indicates the number of processors in the platform. In earlier versions of Windows, <b>KeNumberProcessors</b> is a pointer to an 8-bit integer value that indicates the number of processors in the platform.</p>

<p>Callers cannot assume that <b>KeQueryActiveProcessors</b> maps processors to bits consecutively, or that the routine consistently uses the same mapping each time it is called. The only valid use for the return value is to determine the number of active processors by counting the number of bits that are set.</p>

<p>Callers must also be aware that the value returned by <b>KeQueryActiveProcessors</b> can change during runtime on versions of Windows that support hot-add CPU functionality.</p>

<p>Windows 7 and later versions of Windows support processor groups. Drivers that are designed to handle information about processor groups should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553007">KeQueryGroupAffinity</a> routine, which specifies a processor group, instead of <b>KeQueryActiveProcessors</b>, which does not. However, the implementation of <b>KeQueryActiveProcessors</b> in Windows 7 and later versions of Windows provides compatibility for drivers that were written for earlier versions of Windows, which do not support processor groups. In this implementation, <b>KeQueryActiveProcessors</b> returns an affinity mask that specifies the set of active logical processors in group 0.</p>

<p>In Windows Vista and later versions of Windows, this routine can be called at any IRQL. However, in Windows Server 2003 and earlier versions of Windows, this routine must be called at IRQL &lt;= APC_LEVEL.</p>

<p>The KAFFINITY type is an affinity mask that represents a set of logical processors in a group. The KAFFINITY type is 32 bits on a 32-bit version of Windows and is 64 bits on a 64-bit version of Windows.</p>

<p>If a group contains <i>n</i> logical processors, the processors are numbered from 0 to <i>n</i>-1. Processor number <i>i</i> in the group is represented by bit <i>i</i> in the affinity mask, where <i>i</i> is in the range 0 to <i>n</i>-1. Affinity mask bits that do not correspond to logical processors are always zero.</p>

<p>For example, if a KAFFINITY value identifies the active processors in a group, the mask bit for a processor is one if the processor is active, and is zero if the processor is not active.</p>

<p>The number of bits in the affinity mask determines the maximum number of logical processors in a group. For a 64-bit version of Windows, the maximum number of processors per group is 64. For a 32-bit version of Windows, the maximum number of processors per group is 32. Call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine to obtain the maximum number of processors per group. This number depends on the hardware configuration of the multiprocessor system, but can never exceed the fixed 64-processor and 32-processor limits that are set by the 64-bit and 32-bit versions of Windows, respectively.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a> structure contains an affinity mask and a group number. The group number identifies the group to which the affinity mask applies.</p>

<p>Kernel routines that use the KAFFINITY type include <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>, and <b>KeQueryActiveProcessors</b>. </p>

<p>The <b>KeNumberProcessors</b> kernel variable is obsolete in Windows Vista with Service Pack 1 (SP1), Windows Server 2008, and later versions of Windows. <b>KeNumberProcessors</b> does not appear in WDK headers for WDK releases starting with Windows Vista SP1; however, the variable is still exported from the kernel, so drivers built for earlier platforms will not break</p>

<p>Windows Server 2008 includes support for <a href="https://msdn.microsoft.com/1b6a1dc5-ec32-4bb9-acaf-14db284b4a0e">Dynamic Hardware Partitioning</a> (DHP) in the Windows Datacenter and Enterprise Edition SKUs. As part of DHP, Windows Server 2008 supports hot adding CPUs at runtime. In a hot-add CPU environment, the number of processors may not remain constant during runtime.</p>

<p>Accordingly, in Windows Server 2008, code that can determine the number of processors must use <b>KeQueryActiveProcessors</b> instead of direct references to the kernel variable, <b>KeNumberProcessors</b>.</p>

<p>Review any code that currently references <b>KeNumberProcessors</b> to make sure that it accommodates changes to CPU count in hot-add CPU environments.</p>

<p>You can use the <a href="NULL">PNPCPU</a> tool to simulate hot adding a CPU for testing purposes.</p>

<p>Starting with Windows XP, <b>KeNumberProcessors</b> is an 8-bit integer value that indicates the number of processors in the platform. In earlier versions of Windows, <b>KeNumberProcessors</b> is a pointer to an 8-bit integer value that indicates the number of processors in the platform.</p>

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
<p>Available starting with Windows 2000.</p>
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
<p>See Remarks section.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547803">IrqlKeApcLte1</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553007">KeQueryGroupAffinity</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeQueryActiveProcessors routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
