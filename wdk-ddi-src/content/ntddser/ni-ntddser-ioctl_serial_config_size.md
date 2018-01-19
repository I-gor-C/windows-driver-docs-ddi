---
UID : NI:ntddser.IOCTL_SERIAL_CONFIG_SIZE
title : IOCTL_SERIAL_CONFIG_SIZE
author : windows-driver-content
description : The IOCTL_SERIAL_CONFIG_SIZE request returns information about configuration size.
old-location : serports\ioctl_serial_config_size.htm
old-project : serports
ms.assetid : 13229dcc-e698-4743-9ca2-303bef69304c
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : SdBusSubmitRequestAsync
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : ntddser.h
req.include-header : Ntddser.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_SERIAL_CONFIG_SIZE
req.alt-loc : Ntddser.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : SD_REQUEST_FUNCTION
---

# IOCTL_SERIAL_CONFIG_SIZE IOCTL
The <b>IOCTL_SERIAL_CONFIG_SIZE</b> request returns information about configuration size.

Serial.sys always returns a configuration size of zero.

This request is obsolete and should not be used by new drivers for Microsoft Windows 2000 and later.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None.

### Input Buffer Length
None.

### Output Buffer
The <b>AssociatedIrp.SystemBuffer</b> member points to a client-allocated ULONG buffer that Serial.sys uses to output configuration size information.

### Output Buffer Length
The <b>Parameters.DeviceIoControl.OutputBufferLength</b> is set to the size in bytes of a ULONG.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
The <b>Information</b> member is set to the size in bytes of a ULONG.

The <b>Status</b> member is set to one of the <a href="serial_device_control_requests.htm#generic_status_values_for_serial_device_control_requests">Generic Status Values for Serial Device Control Requests</a>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | ntddser.h (include Ntddser.h) |
| **IRQL** |  |