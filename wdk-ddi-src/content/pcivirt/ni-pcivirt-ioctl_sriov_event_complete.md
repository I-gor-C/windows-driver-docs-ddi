---
UID : NI:pcivirt.IOCTL_SRIOV_EVENT_COMPLETE
title : IOCTL_SRIOV_EVENT_COMPLETE
author : windows-driver-content
description : The request indicates that the virtualization stack or the SR-IOV device received one of the events listed in SRIOV_PF_EVENT.
old-location : pci\ioctl-sriov-event-complete.htm
old-project : PCI
ms.assetid : 5299ec17-1fcb-4449-9ec4-73a4d818df0d
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SRIOV_PF_EVENT, SRIOV_PF_EVENT, *PSRIOV_PF_EVENT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : pcivirt.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_SRIOV_EVENT_COMPLETE
req.alt-loc : Pcivirt.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : SRIOV_PF_EVENT, *PSRIOV_PF_EVENT
---

# IOCTL_SRIOV_EVENT_COMPLETE IOCTL
The  request indicates that the virtualization stack  or the SR-IOV device received one of the events listed in
<a href="https://msdn.microsoft.com/e2b40a9d-57e6-49b1-839a-d34acb108807">SRIOV_PF_EVENT</a>.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
A pointer to an <a href="https://msdn.microsoft.com/3b40d780-8084-4c19-bb8e-9d1ab3dadc95">SRIOV_PNP_EVENT_COMPLETE</a> structure that contains the NTSTATUS code with which <a href="https://msdn.microsoft.com/3f2d67e0-abab-40a1-b4a9-cb65e81884e9">IOCTL_SRIOV_NOTIFICATION</a> request must be completed.

### Input Buffer Length
The size of the <a href="https://msdn.microsoft.com/3b40d780-8084-4c19-bb8e-9d1ab3dadc95">SRIOV_PNP_EVENT_COMPLETE</a> structure.

### Output Buffer
<text></text>

### Output Buffer Length
<text></text>

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.

    ## Remarks
        This IOCTL request is sent by the virtualization stack to the  PCI Express SR-IOV Physical Function (PF) driver that exposes GUID_DEVINTERFACE_VIRTUALIZABLE_DEVICE.

The virtualization stack sends the <b>IOCTL_SRIOV_EVENT_COMPLETE</b> request when the physical function (PF) driver completes the previously sent <a href="https://msdn.microsoft.com/3f2d67e0-abab-40a1-b4a9-cb65e81884e9">IOCTL_SRIOV_NOTIFICATION</a> request. The <b>IOCTL_SRIOV_EVENT_COMPLETE</b> request can be completed
synchronously.  The stack provides the NTSTATUS code to set for the <a href="https://msdn.microsoft.com/3b40d780-8084-4c19-bb8e-9d1ab3dadc95">SRIOV_PNP_EVENT_COMPLETE</a> is the input buffer. The code indicates the status code o use for completion of the event.
</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | pcivirt.h |
| **IRQL** | PASSIVE_LEVEL |