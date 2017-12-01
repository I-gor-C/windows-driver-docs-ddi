---
UID: NF.ntddk.KeSetHardwareCounterConfiguration
title: KeSetHardwareCounterConfiguration
author: windows-driver-content
description: The KeSetHardwareCounterConfiguration routine specifies a list of hardware counters to use for thread profiling.
old-location: kernel\kesethardwarecounterconfiguration.htm
old-project: kernel
ms.assetid: 9677dbd7-4b6f-49a9-ac38-fdcbaeb3a6f8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeSetHardwareCounterConfiguration
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeSetHardwareCounterConfiguration
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
req.irql: <= APC_LEVEL
req.iface: 
---

# KeSetHardwareCounterConfiguration function



## -description
<p>The <b>KeSetHardwareCounterConfiguration</b> routine specifies a list of hardware counters to use for thread profiling.</p>


## -syntax

````
NTSTATUS KeSetHardwareCounterConfiguration(
  _In_ PHARDWARE_COUNTER CounterArray,
  _In_ ULONG             Count
);
````


## -parameters
<dl>

### -param <i>CounterArray</i> [in]

<dd>
<p>A pointer to a <a href="..\ntddk\ns-ntddk--hardware-counter.md">HARDWARE_COUNTER</a> array that describes the hardware counter configuration to use for thread profiling. Each array element is a structure that describes a hardware counter. Before the routine returns, it copies the contents of this array into its internal data structures.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the number of elements in the array that is pointed to by the <i>CounterArray</i> parameter.</p>
</dd>
</dl>

## -returns
<p><b>KeSetHardwareCounterConfiguration</b> returns STATUS_SUCCESS if the call is successful. Possible error return values include the following:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The value of the <i>Count</i> parameter exceeds the maximum number of counters that is specified by the MAX_HW_COUNTERS constant, which is defined in the Ntddk.h header file.</p><dl>
<dt><b>STATUS_WMI_ALREADY_ENABLED</b></dt>
</dl><p>One or more of the counters that are specified in the <i>CounterArray</i> array are already enabled.</p><dl>
<dt><b>STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This routine is not implemented for the processor architecture that the caller is running on.</p>

<p> </p>

## -remarks
<p>In Windows 7, this routine is implemented only for the x86-based, x64-based, and Itanium-based architectures. If a caller is running on a processor architecture that is not supported, the routine returns STATUS_NOT_IMPLEMENTED.</p>

<p>This routine tells the operating system which hardware counters to use for thread profiling. Call this routine only when thread profiling is disabled. If the <i>CounterArray</i> array specifies any hardware counters that are currently being used, the routine fails and returns STATUS_WMI_ALREADY_ENABLED.</p>

<p>An application thread can enable thread profiling to obtain a set of performance measurements from the hardware counters in the performance monitoring unit (PMU) of the local processor. The operating system supports only one profiling application at a time. Concurrent instances of a thread-profiling application are not supported. A thread can enable thread profiling for itself but not for other threads.</p>

<p>When thread profiling is enabled, the operating system uses the hardware counters that were specified in the last call to <b>KeSetHardwareCounterConfiguration</b>. Each successful <b>KeSetHardwareCounterConfiguration</b> call replaces any hardware counter configuration that might have been set in a previous <b>KeSetHardwareCounterConfiguration</b> call.</p>

<p>Set <i>Count</i> = 0 to specify an empty hardware counter configuration. This configuration effectively prevents the use of hardware counters for thread profiling. The default hardware counter configuration that exists after system startup and before the initial <b>KeSetHardwareCounterConfiguration</b> call is an empty configuration.</p>

<p>The effect of a successful <b>KeSetHardwareCounterConfiguration</b> call is global. If a thread in any process is profiled, the profiler uses the hardware counter configuration that was set by the last call to <b>KeSetHardwareCounterConfiguration</b>. In a multiprocessor system, a <b>KeSetHardwareCounterConfiguration</b> call sets the hardware counter configuration to use for thread profiling across all processors in the system, although each processor uses its own set of hardware counters.</p>

<p>To avoid resource conflicts, all drivers that use counter resources should use the <a href="..\ntddk\nf-ntddk-halallocatehardwarecounters.md">HalAllocateHardwareCounters</a> and <a href="..\ntddk\nf-ntddk-halfreehardwarecounters.md">HalFreeHardwareCounters</a> routines to coordinate their sharing of these resources.</p>

<p>To query the operating system for the hardware counter configuration that is currently in effect for thread profiling, call the <a href="..\ntddk\nf-ntddk-kequeryhardwarecounterconfiguration.md">KeQueryHardwareCounterConfiguration</a> routine.</p>

<p>Virtualization software typically does not virtualize hardware performance counters. Thus, hardware performance counters are unlikely to be available in a virtual machine.</p>

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
<p>Available starting with Windows 7.</p>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-halallocatehardwarecounters.md">HalAllocateHardwareCounters</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-halfreehardwarecounters.md">HalFreeHardwareCounters</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--hardware-counter.md">HARDWARE_COUNTER</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-kequeryhardwarecounterconfiguration.md">KeQueryHardwareCounterConfiguration</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeSetHardwareCounterConfiguration routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
