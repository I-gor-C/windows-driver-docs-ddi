---
UID: NF.ntddk.HalAllocateHardwareCounters
title: HalAllocateHardwareCounters
author: windows-driver-content
description: The HalAllocateHardwareCounters routine allocates a set of hardware performance counters.
old-location: kernel\halallocatehardwarecounters.htm
old-project: kernel
ms.assetid: 8a689889-b445-4fda-ae11-090d0d5870b8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: HalAllocateHardwareCounters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HalAllocateHardwareCounters
req.alt-loc: Hal.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hal.lib
req.dll: Hal.dll
req.irql: PASSIVE_LEVEL
req.iface: 
---

# HalAllocateHardwareCounters function



## -description
<p>The <b>HalAllocateHardwareCounters</b> routine allocates a set of hardware performance counters.</p>


## -syntax

````
NTSTATUS HalAllocateHardwareCounters(
  _In_  PGROUP_AFFINITY                 GroupAffinity,
  _In_  ULONG                           GroupCount,
  _In_  PPHYSICAL_COUNTER_RESOURCE_LIST ResourceList,
  _Out_ PHANDLE                         CounterSetHandle
);
````


## -parameters
<dl>

### -param GroupAffinity [in]

<dd>
<p>Reserved for future use. Set this parameter to <b>NULL</b>.</p>
</dd>

### -param GroupCount [in]

<dd>
<p>Reserved for future use. Set this parameter to zero.</p>
</dd>

### -param ResourceList [in]

<dd>
<p>Reserved for future use. Set this parameter to <b>NULL</b>.</p>
</dd>

### -param CounterSetHandle [out]

<dd>
<p>A pointer to a location into which the routine writes a handle to the allocated counter resources. To release these resources later, the caller must pass this handle to the <a href="..\ntddk\nf-ntddk-halfreehardwarecounters.md">HalFreeHardwareCounters</a> routine. If the requested counter resources are unavailable, <b>HalAllocateHardwareCounters</b> sets *<i>CounterSetHandle</i> = <b>NULL</b> and returns STATUS_INSUFFICIENT_RESOURCES.</p>
</dd>
</dl>

## -returns
<p><b>HalAllocateHardwareCounters</b> returns STATUS_SUCCESS if the call was successful. Possible error return values include the following status codes.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The requested counter resources are currently unavailable.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The caller specified an invalid parameter value.</p>

<p> </p>

## -remarks
<p>Most processors have performance monitor units (PMUs) that contain a number of hardware counters. Software tools use these counters to monitor various aspects of system performance. Typically, such a tool consists of a custom kernel-mode driver to program the counters and a user-mode application that communicates with the driver.</p>

<p>If more than one such tool is installed on a computer, the associated drivers must avoid trying to use the same hardware counters simultaneously. To avoid such resource conflicts, all drivers that use counter resources should use the <b>HalAllocateHardwareCounters</b> and <b>HalFreeHardwareCounters</b> routines to coordinate their sharing of these resources.</p>

<p>A counter resource is a single hardware counter, a block of contiguous counters, or a counter overflow interrupt in a PMU.</p>

<p>Before configuring the counters, a driver can call the <b>HalAllocateHardwareCounters</b> routine to acquire exclusive access to a set of counter resources. After the driver no longer needs these resources, it must free the resources by calling the <b>HalFreeHardwareCounters</b> routine.</p>

<p>In Windows 8 and Windows 7, a successful call to <b>HalAllocateHardwareCounters</b> grants the caller exclusive access to all counter resources in the performance monitor unit of a single-processor system. In a multiprocessor system, a successful call grants the caller exclusive access to all counter resources in all processors in the system. Future versions of this routine might provide more fine-grained allocation of counter resources.</p>

<p>Virtualization software typically does not virtualize hardware performance counters. Thus, these counters might not be available in a virtual machine, regardless of whether <b>HalAllocateHardwareCounters</b> returns a status code of STATUS_SUCCESS. For example, hardware performance counters are not available in a Hyper-V virtual machine, but <b>HalAllocateHardwareCounters</b> might still return STATUS_SUCCESS.</p>

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
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hal.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hal.dll</dt>
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
<a href="..\miniport\ns-miniport--group-affinity.md">GROUP_AFFINITY</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-halfreehardwarecounters.md">HalFreeHardwareCounters</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--physical-counter-resource-list.md">PHYSICAL_COUNTER_RESOURCE_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20HalAllocateHardwareCounters routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
