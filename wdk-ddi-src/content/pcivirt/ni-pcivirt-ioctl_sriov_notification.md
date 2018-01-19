---
UID : NI:pcivirt.IOCTL_SRIOV_NOTIFICATION
title : IOCTL_SRIOV_NOTIFICATION
author : windows-driver-content
description : The request indicates that the virtualization stack wants to be notified when one of the events listed in SRIOV_PF_EVENT occurs.
old-location : pci\ioctl-sriov-notification.htm
old-project : PCI
ms.assetid : 3f2d67e0-abab-40a1-b4a9-cb65e81884e9
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
req.alt-api : IOCTL_SRIOV_NOTIFICATION
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

# IOCTL_SRIOV_NOTIFICATION IOCTL
The  request indicates that the virtualization stack wants to be notified when one of the events listed in
<a href="https://msdn.microsoft.com/e2b40a9d-57e6-49b1-839a-d34acb108807">SRIOV_PF_EVENT</a> occurs.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<text></text>

### Input Buffer Length
<text></text>

### Output Buffer
A buffer that contains an <a href="https://msdn.microsoft.com/e2b40a9d-57e6-49b1-839a-d34acb108807">SRIOV_PF_EVENT</a>-type value that is filled by the  physical function (PF) driver when it completes the request.

### Output Buffer Length
A pointer to the variable, which is assigned the number of
    written bytes to the output buffer when the request is completed.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.

    ## Remarks
        This IOCTL request is sent by the virtualization stack to the  PCI Express SR-IOV Physical Function (PF) driver that exposes GUID_DEVINTERFACE_VIRTUALIZABLE_DEVICE.

The <b>IOCTL_SRIOV_NOTIFICATION</b> request is held in a queue by the PF driver until the request is either cancelled by sender or the device experiences one of the events listed in
<a href="https://msdn.microsoft.com/e2b40a9d-57e6-49b1-839a-d34acb108807">SRIOV_PF_EVENT</a>. The driver then completes the pending request.


If the PF driver receives this IOCTL request while processing a Plug and Play event  for which the driver has not 
yet completed a notification, it should complete the IOCTL request immediately with the 
event details in the output buffer.  Otherwise, the driver should queue the request until either it is cancelled
or a Plug and Play event that requires notification occurs.


The virtualization stack can send the <b>IOCTL_SRIOV_NOTIFICATION</b> request immediately after the previous <b>IOCTL_SRIOV_NOTIFICATION</b> request completes.   The PF driver must keep track of the fact 
that an event notification has been delivered and must not complete two IOCTL requests for the same event twice.

  It is pended by the PF driver until it is canceled by the sender or until the PF driver experiences one of several PnP events, at which point it is completed. </p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | pcivirt.h |
| **IRQL** | PASSIVE_LEVEL |