---
UID : NI:pointofservicedriverinterface.IOCTL_POINT_OF_SERVICE_MSR_AUTHENTICATE_DEVICE
title : IOCTL_POINT_OF_SERVICE_MSR_AUTHENTICATE_DEVICE
author : windows-driver-content
description : This IO control function authenticates the magnetic stripe reader (MSR).
old-location : pos\ioctl_point_of_service_msr_authenticate_device.htm
old-project : pos
ms.assetid : fc6b719d-3e05-4ff5-9d81-1e9326ff4ad4
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _PosPropertyId, PosPropertyId
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : pointofservicedriverinterface.h
req.include-header : Pointofservicedriverinterface.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_POINT_OF_SERVICE_MSR_AUTHENTICATE_DEVICE
req.alt-loc : pointofservicedriverinterface.h
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
req.typenames : PosPropertyId
---

# IOCTL_POINT_OF_SERVICE_MSR_AUTHENTICATE_DEVICE IOCTL
This IO control function authenticates the magnetic stripe reader (MSR).

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
Pointer to the input buffer, a <a href="..\pointofservicedriverinterface\ns-pointofservicedriverinterface-_msr_authenticate_device.md">MSR_AUTHENTICATE_DEVICE</a> variable.

### Input Buffer Length
Size of the input buffer, in bytes. Set to sizeof(<b>MSR_AUTHENTICATE_DEVICE</b>).

### Output Buffer
Not used with this operation; set to <b>NULL</b>.

### Output Buffer Length
Not used with this operation; set to <b>0</b> (zero).

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
Returns <b>TRUE</b> if successful; otherwise, returns <b>FALSE</b>.

To get extended error information, call <a href="http://go.microsoft.com/fwlink/p/?LinkId=316871">GetLastError</a>. The following are common error values:



The device is currently claimed by another client.

The device does not support authentication.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |
| **IRQL** |  |