---
UID: NI.pcivirt.IOCTL_SRIOV_QUERY_MITIGATED_RANGE_COUNT
title: IOCTL_SRIOV_QUERY_MITIGATED_RANGE_COUNT
author: windows-driver-content
description: The request determines the ranges of memory-mapped I/O space that must mitigated.
old-location: pci\ioctl-sriov-query-mitigated-range-count.htm
old-project: PCI
ms.assetid: 68fd97a5-b7ea-43c0-96ed-b64445fd21dd
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PARCLASS_INFORMATION, PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_SRIOV_QUERY_MITIGATED_RANGE_COUNT
req.alt-loc: Pcivirt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# IOCTL_SRIOV_QUERY_MITIGATED_RANGE_COUNT IOCTL



## -description
<p> The request determines the ranges of memory-mapped I/O space that must mitigated. </p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a <a href="buses._sriov_mitigated_range_count_input">SRIOV_MITIGATED_RANGE_COUNT_INPUT</a> structure. Set the <b>VfIndex</b> member to 0. </p>

<p>A pointer to a <a href="buses._sriov_mitigated_range_count_input">SRIOV_MITIGATED_RANGE_COUNT_INPUT</a> structure. Set the <b>VfIndex</b> member to 0. </p>

### -input-buffer-length
<p>The size of the <a href="buses._sriov_mitigated_range_count_input">SRIOV_MITIGATED_RANGE_COUNT_INPUT</a> structure.</p>

<p>The size of the <a href="buses._sriov_mitigated_range_count_input">SRIOV_MITIGATED_RANGE_COUNT_INPUT</a> structure.</p>

<p>The size of the <a href="buses._sriov_mitigated_range_count_input">SRIOV_MITIGATED_RANGE_COUNT_INPUT</a> structure.</p>

### -output-buffer
<p>A pointer to a <a href="buses._sriov_mitigated_range_count_output">SRIOV_MITIGATED_RANGE_COUNT_OUTPUT</a> structure that is filled by the physical function (PF) driver with  ranges of memory-mapped I/O space. </p>

<p>A pointer to a <a href="buses._sriov_mitigated_range_count_output">SRIOV_MITIGATED_RANGE_COUNT_OUTPUT</a> structure that is filled by the physical function (PF) driver with  ranges of memory-mapped I/O space. </p>

<p>A pointer to a <a href="buses._sriov_mitigated_range_count_output">SRIOV_MITIGATED_RANGE_COUNT_OUTPUT</a> structure that is filled by the physical function (PF) driver with  ranges of memory-mapped I/O space. </p>

<p>A pointer to a <a href="buses._sriov_mitigated_range_count_output">SRIOV_MITIGATED_RANGE_COUNT_OUTPUT</a> structure that is filled by the physical function (PF) driver with  ranges of memory-mapped I/O space. </p>

### -output-buffer-length
<p>The size of the <a href="buses._sriov_mitigated_range_count_output">SRIOV_MITIGATED_RANGE_COUNT_OUTPUT</a> structure. </p>

<p>The size of the <a href="buses._sriov_mitigated_range_count_output">SRIOV_MITIGATED_RANGE_COUNT_OUTPUT</a> structure. </p>

<p>The size of the <a href="buses._sriov_mitigated_range_count_output">SRIOV_MITIGATED_RANGE_COUNT_OUTPUT</a> structure. </p>

<p>The size of the <a href="buses._sriov_mitigated_range_count_output">SRIOV_MITIGATED_RANGE_COUNT_OUTPUT</a> structure. </p>

<p>The size of the <a href="buses._sriov_mitigated_range_count_output">SRIOV_MITIGATED_RANGE_COUNT_OUTPUT</a> structure. </p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>TBD</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p>TBD</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p>TBD</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p>TBD</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p>TBD</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p>TBD</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

## -remarks
<p>This IOCTL request is sent by the virtualization stack to the  PCI Express SR-IOV Physical Function (PF) driver that exposes GUID_DEVINTERFACE_VIRTUALIZABLE_DEVICE.</p>

<p>The virtualization stack uses an I/O MMU to differentiate traffic coming from the various interfaces that the device exposes, enforcing policy about which regions of memory a device can access and which interrupts it can generate. </p>

<p>The request is sent to the physical function (PF) driver by the virtualization stack to find out the ranges of memory-mapped I/O space
in which the stack must place
intercepts  on those pages and send the requests to read and write values
within those pages to the PF driver.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pcivirt.h</dt>
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