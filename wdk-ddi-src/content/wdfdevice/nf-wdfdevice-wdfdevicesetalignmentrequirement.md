---
UID: NF.wdfdevice.WdfDeviceSetAlignmentRequirement
title: WdfDeviceSetAlignmentRequirement
author: windows-driver-content
description: The WdfDeviceSetAlignmentRequirement method registers the driver's preferred address alignment for the data buffers that the device uses during memory transfer operations.
old-location: wdf\wdfdevicesetalignmentrequirement.htm
old-project: wdf
ms.assetid: 47e857d0-1423-45e5-a5a5-54507b8fa315
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDeviceSetAlignmentRequirement
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceSetAlignmentRequirement
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceSetAlignmentRequirement function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceSetAlignmentRequirement</b> method registers the driver's preferred address alignment for the data buffers that the device uses during memory transfer operations.</p>


## -syntax

````
VOID WdfDeviceSetAlignmentRequirement(
  _In_ WDFDEVICE Device,
  _In_ ULONG     AlignmentRequirement
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>AlignmentRequirement</i> [in]

<dd>
<p>The alignment requirement for a data buffer. This value must be one less than the alignment boundary. For example, you can specify 15 for a 16-byte alignment boundary and 31 for a 32-byte alignment boundary. You can also use one of the FILE_<i>Xxxx</i>_ALIGNMENT constants that are defined in <i>Wdm.h</i>.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>A driver that uses direct I/O can call  <b>WdfDeviceSetAlignmentRequirement</b> to register a preferred alignment requirement.  The alignment applies to I/O requests that go through the I/O Manager, and  not those sent to your driver from another driver that calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>.</p>

<p> Because the I/O manager does not always use the requested alignment, the driver should be prepared for unaligned buffers.</p>

<p>The driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545953">WdfDeviceGetAlignmentRequirement</a> to obtain the current value for the device's alignment requirement.</p>

<p>The I/O manager sets an alignment requirement value for the device when the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>. For more information about a device's alignment requirement value and when a driver must change the value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547807">Initializing a Device Object</a> in the WDM documentation.</p>

<p>If your driver specifies an alignment requirement that is greater that the computer's page size (PAGE_SIZE), the logical addresses that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545814">WdfCommonBufferGetAlignedLogicalAddress</a> method returns are always aligned to the specified alignment requirement, but the virtual addresses that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545820">WdfCommonBufferGetAlignedVirtualAddress</a> method returns might not be aligned to the alignment requirement.</p>

<p>If your driver specifies an alignment requirement that is less than the computer's page size, all logical and virtual addresses are aligned to the specified alignment requirement.</p>

<p>For more information about calling <b>WdfDeviceSetAlignmentRequirement</b>, see <a href="wdf.enabling_dma_transactions">Enabling DMA Transactions</a> and <a href="wdf.using_common_buffers">Using Common Buffers</a>.</p>

<p>The following code example is from the <a href="wdf.sample_kmdf_drivers">AMCC5933</a> sample driver. This example checks a device's current alignment requirement and sets the alignment requirement to a new value, if necessary.</p>

<p>A driver that uses direct I/O can call  <b>WdfDeviceSetAlignmentRequirement</b> to register a preferred alignment requirement.  The alignment applies to I/O requests that go through the I/O Manager, and  not those sent to your driver from another driver that calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>.</p>

<p> Because the I/O manager does not always use the requested alignment, the driver should be prepared for unaligned buffers.</p>

<p>The driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545953">WdfDeviceGetAlignmentRequirement</a> to obtain the current value for the device's alignment requirement.</p>

<p>The I/O manager sets an alignment requirement value for the device when the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>. For more information about a device's alignment requirement value and when a driver must change the value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547807">Initializing a Device Object</a> in the WDM documentation.</p>

<p>If your driver specifies an alignment requirement that is greater that the computer's page size (PAGE_SIZE), the logical addresses that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545814">WdfCommonBufferGetAlignedLogicalAddress</a> method returns are always aligned to the specified alignment requirement, but the virtual addresses that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545820">WdfCommonBufferGetAlignedVirtualAddress</a> method returns might not be aligned to the alignment requirement.</p>

<p>If your driver specifies an alignment requirement that is less than the computer's page size, all logical and virtual addresses are aligned to the specified alignment requirement.</p>

<p>For more information about calling <b>WdfDeviceSetAlignmentRequirement</b>, see <a href="wdf.enabling_dma_transactions">Enabling DMA Transactions</a> and <a href="wdf.using_common_buffers">Using Common Buffers</a>.</p>

<p>The following code example is from the <a href="wdf.sample_kmdf_drivers">AMCC5933</a> sample driver. This example checks a device's current alignment requirement and sets the alignment requirement to a new value, if necessary.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545814">WdfCommonBufferGetAlignedLogicalAddress</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545820">WdfCommonBufferGetAlignedVirtualAddress</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545953">WdfDeviceGetAlignmentRequirement</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceSetAlignmentRequirement method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
