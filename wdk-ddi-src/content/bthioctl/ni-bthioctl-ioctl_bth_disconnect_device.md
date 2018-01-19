---
UID : NI:bthioctl.IOCTL_BTH_DISCONNECT_DEVICE
title : IOCTL_BTH_DISCONNECT_DEVICE
author : windows-driver-content
description : Profile drivers use IOCTL_BTH_DISCONNECT_DEVICE to request the operating system to disconnect the specified remote device.
old-location : bltooth\ioctl_bth_disconnect_device.htm
old-project : bltooth
ms.assetid : 03c7f389-60a4-4c98-881d-a58926644275
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : _HFP_BYPASS_CODEC_ID_V1, *PHFP_BYPASS_CODEC_ID_V1, HFP_BYPASS_CODEC_ID_V1
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : bthioctl.h
req.include-header : Bthioctl.h
req.target-type : Windows
req.target-min-winverclnt : Versions: Supported in Windows Vista, and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_BTH_DISCONNECT_DEVICE
req.alt-loc : Bthioctl.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= PASSIVE_LEVEL
req.typenames : "*PHFP_BYPASS_CODEC_ID_V1, HFP_BYPASS_CODEC_ID_V1"
---

# IOCTL_BTH_DISCONNECT_DEVICE IOCTL
Profile drivers use IOCTL_BTH_DISCONNECT_DEVICE to request the operating system to disconnect the
     specified remote device.



Profile drivers use IOCTL_BTH_DISCONNECT_DEVICE to request the operating system to disconnect the
     specified remote device.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The 
      <b>AssociatedIrp.SystemBuffer</b> member contains the address of the remote device to disconnect
      from.

### Input Buffer Length
The length of the address in the buffer.

### Output Buffer
None.

### Output Buffer Length
None.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to zero because the Bluetooth driver
      stack returns no data with this IOCTL.

The 
      <b>Status</b> member is set to one of the values in the following table.

STATUS_SUCCESS

The IOCTL completed successfully.

STATUS_DEVICE_NOT_CONNECTED

The specified remote device is not connected.

    ## Remarks
        Calling IOCTL_BTH_DISCONNECT_DEVICE forces a disconnect from the remote device without regard to the
    state of any L2CAP and SCO connections. All active SCO connections will be disconnected before the ACL
    connection is disconnected. Pending data transfers might fail.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | bthioctl.h (include Bthioctl.h) |
| **IRQL** | <= PASSIVE_LEVEL |