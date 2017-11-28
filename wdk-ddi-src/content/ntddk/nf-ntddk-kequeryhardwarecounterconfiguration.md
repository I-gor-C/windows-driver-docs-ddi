---
UID: NF.ntddk.KeQueryHardwareCounterConfiguration
title: KeQueryHardwareCounterConfiguration
author: windows-driver-content
description: The KeQueryHardwareCounterConfiguration routine queries the operating system for the list of hardware counters to use for thread profiling.
old-location: kernel\kequeryhardwarecounterconfiguration.htm
old-project: kernel
ms.assetid: 5ac33177-38fc-4027-95c9-c2cf9ccdaa52
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeQueryHardwareCounterConfiguration
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeQueryHardwareCounterConfiguration
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

# KeQueryHardwareCounterConfiguration function



## -description
<p>The <b>KeQueryHardwareCounterConfiguration</b> routine queries the operating system for the list of hardware counters to use for thread profiling. </p>


## -syntax

````
NTSTATUS KeQueryHardwareCounterConfiguration(
  _Out_ PHARDWARE_COUNTER CounterArray,
  _In_  ULONG             MaximumCount,
  _Out_ PULONG            Count
);
````


## -parameters
<dl>

### -param <i>CounterArray</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer into which the routine writes an array of elements of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff546980">HARDWARE_COUNTER</a>. Each array element is a structure that contains information about a hardware counter. The array contains one element for each hardware counter that is assigned to thread profiling. If the routine fails, it writes nothing to this buffer. </p>
</dd>

### -param <i>MaximumCount</i> [in]

<dd>
<p>Specifies the maximum number of elements that the routine can write to the buffer that is pointed to by the <i>CounterArray</i> parameter. The size of the caller-allocated buffer must be at least <i>MaximumCount</i> * <b>sizeof</b>(<b>HARDWARE_COUNTER</b>) bytes. </p>
</dd>

### -param <i>Count</i> [out]

<dd>
<p>A pointer to a location into which the routine writes the number of array elements that it has written to the buffer that is pointed to by the <i>CounterArray</i> parameter. If the buffer length that is specified by <i>MaximumCount</i> is not large enough to contain the entire array, the routine writes the required length to *<i>Count</i> and returns STATUS_BUFFER_TOO_SMALL. </p>
</dd>
</dl>

## -returns
<p><b>KeQueryHardwareCounterConfiguration</b> returns STATUS_SUCCESS if the call is successful. Possible error return values include the following:</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The <i>MaximumCount</i> parameter specifies a buffer length that is not large enough to contain the counter configuration information. </p><dl>
<dt><b>STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This routine is not implemented for the processor architecture that the caller is running on. </p>

<p> </p>

## -remarks
<p>In Windows 7, this routine is implemented only for the x86-based, x64-based, and Itanium-based architectures. If the caller is running on a processor architecture that is not supported, the routine returns STATUS_NOT_IMPLEMENTED. </p>

<p>To set the hardware counter configuration to use for thread profiling, call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553257">KeSetHardwareCounterConfiguration</a> routine. </p>

<p>In Windows 7, this routine is implemented only for the x86-based, x64-based, and Itanium-based architectures. If the caller is running on a processor architecture that is not supported, the routine returns STATUS_NOT_IMPLEMENTED. </p>

<p>To set the hardware counter configuration to use for thread profiling, call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553257">KeSetHardwareCounterConfiguration</a> routine. </p>

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
<p>Available in Windows 7 and later versions of Windows. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546980">HARDWARE_COUNTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553257">KeSetHardwareCounterConfiguration</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeQueryHardwareCounterConfiguration routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
