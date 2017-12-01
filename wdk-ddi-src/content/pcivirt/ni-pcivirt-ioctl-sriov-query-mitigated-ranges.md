---
UID: NI.pcivirt.IOCTL_SRIOV_QUERY_MITIGATED_RANGES
title: IOCTL_SRIOV_QUERY_MITIGATED_RANGES
author: windows-driver-content
description: The request determines the specific ranges on which intercepts must be placed.
old-location: pci\ioctl-sriov-query-mitigated-ranges.htm
old-project: PCI
ms.assetid: 58b6e53d-be7a-4563-a27d-db216a12d60d
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
req.alt-api: IOCTL_SRIOV_QUERY_MITIGATED_RANGES
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

# IOCTL_SRIOV_QUERY_MITIGATED_RANGES IOCTL



## -description
<p>The request determines the specific ranges on which intercepts must be placed. </p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a <a href="buses._sriov_mitigated_ranges_input">SRIOV_MITIGATED_RANGES_INPUT</a> structure that specifies the virtual function (VF) whose ranges are to be mitigated.</p>

<p>A pointer to a <a href="buses._sriov_mitigated_ranges_input">SRIOV_MITIGATED_RANGES_INPUT</a> structure that specifies the virtual function (VF) whose ranges are to be mitigated.</p>

### -input-buffer-length
<p>The size of the <a href="buses._sriov_mitigated_ranges_input">SRIOV_MITIGATED_RANGES_INPUT</a> structure.</p>

<p>The size of the <a href="buses._sriov_mitigated_ranges_input">SRIOV_MITIGATED_RANGES_INPUT</a> structure.</p>

<p>The size of the <a href="buses._sriov_mitigated_ranges_input">SRIOV_MITIGATED_RANGES_INPUT</a> structure.</p>

### -output-buffer
<p>A pointer to a <a href="buses._sriov_mitigated_ranges_output">SRIOV_MITIGATED_RANGES_OUTPUT</a> structure that specifies the virtual function (VF) whose ranges were to mitigated.</p>

<p>A pointer to a <a href="buses._sriov_mitigated_ranges_output">SRIOV_MITIGATED_RANGES_OUTPUT</a> structure that specifies the virtual function (VF) whose ranges were to mitigated.</p>

<p>A pointer to a <a href="buses._sriov_mitigated_ranges_output">SRIOV_MITIGATED_RANGES_OUTPUT</a> structure that specifies the virtual function (VF) whose ranges were to mitigated.</p>

<p>A pointer to a <a href="buses._sriov_mitigated_ranges_output">SRIOV_MITIGATED_RANGES_OUTPUT</a> structure that specifies the virtual function (VF) whose ranges were to mitigated.</p>

### -output-buffer-length
<p>The size of the <a href="buses._sriov_mitigated_ranges_output">SRIOV_MITIGATED_RANGES_OUTPUT</a> structure.</p>

<p>The size of the <a href="buses._sriov_mitigated_ranges_output">SRIOV_MITIGATED_RANGES_OUTPUT</a> structure.</p>

<p>The size of the <a href="buses._sriov_mitigated_ranges_output">SRIOV_MITIGATED_RANGES_OUTPUT</a> structure.</p>

<p>The size of the <a href="buses._sriov_mitigated_ranges_output">SRIOV_MITIGATED_RANGES_OUTPUT</a> structure.</p>

<p>The size of the <a href="buses._sriov_mitigated_ranges_output">SRIOV_MITIGATED_RANGES_OUTPUT</a> structure.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

## -remarks
<p>This IOCTL request is sent by the virtualization stack to the  PCI Express SR-IOV Physical Function (PF) driver that exposes GUID_DEVINTERFACE_VIRTUALIZABLE_DEVICE.</p>

<p>The virtualization stack uses an I/O MMU to differentiate traffic coming from the various interfaces that the device exposes, enforcing policy about which regions of memory a device can access and which interrupts it can generate. </p>

<p>The request  is sent to the physical function (PF) by virtualization stack to get the specific ranges on which intercepts must be placed.</p>

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