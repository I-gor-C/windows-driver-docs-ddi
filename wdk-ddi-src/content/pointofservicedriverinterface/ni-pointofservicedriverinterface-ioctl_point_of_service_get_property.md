---
UID : NI:pointofservicedriverinterface.IOCTL_POINT_OF_SERVICE_GET_PROPERTY
title : IOCTL_POINT_OF_SERVICE_GET_PROPERTY
author : windows-driver-content
description : This I/O control function returns the value of the specified property from the device driver.
old-location : pos\ioctl_point_of_service_get_property.htm
old-project : pos
ms.assetid : 7d0231b3-4db7-47b3-8208-70d2cd337005
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
req.alt-api : IOCTL_POINT_OF_SERVICE_GET_PROPERTY
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

# IOCTL_POINT_OF_SERVICE_GET_PROPERTY IOCTL
This I/O control function returns the value of the specified property from the device driver.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
Pointer to a buffer that contains the <a href="..\pointofservicedriverinterface\ne-pointofservicedriverinterface-_pospropertyid.md">PosPropertyId</a> for the property you want to get.

### Input Buffer Length
Size, in bytes, of the buffer pointed to by <i>lpInBuffer</i>. Set to sizeof(<i>PosPropertyId</i>).

### Output Buffer
Pointer to a buffer that receives the property value.

### Output Buffer Length
Size, in bytes, of the buffer pointed to by <i>lpOutBuffer</i>.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
Returns <b>TRUE</b> if successful; otherwise, returns <b>FALSE</b>.

To get extended error information, call <a href="http://go.microsoft.com/fwlink/p/?LinkId=316871">GetLastError</a>. The following list shows common error values (other status values may be returned as defined by your GET property callback implementation):



The calling thread does not have a claim on the device.

The output buffer is not large enough to contain the output value. The driver will copy as much data into the output buffer as possible.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |
| **IRQL** |  |