---
UID : NI:pointofservicedriverinterface.IOCTL_POINT_OF_SERVICE_SET_PROPERTY
title : IOCTL_POINT_OF_SERVICE_SET_PROPERTY
author : windows-driver-content
description : This I/O control function sets the specified property on the device.
old-location : pos\ioctl_point_of_service_set_property.htm
old-project : pos
ms.assetid : 8907a99f-37b0-4c09-b92a-ac720328020e
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
req.alt-api : IOCTL_POINT_OF_SERVICE_SET_PROPERTY
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

# IOCTL_POINT_OF_SERVICE_SET_PROPERTY IOCTL
This I/O control function sets the specified property on the device.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<a href="..\pointofservicedriverinterface\ne-pointofservicedriverinterface-_pospropertyid.md">PosPropertyId</a> of the property to set followed by the value of the property. The encoding for the type follows the property ID in the byte stream.

### Input Buffer Length
Set to sizeof(<i>PosPropertyId</i>) + the size of the property value.

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

To get extended error information, call <a href="http://go.microsoft.com/fwlink/p/?LinkId=316871">GetLastError</a>. The following list shows common error values (other return values may be returned as defined by your property callback implementation):



The device is currently claimed by another client.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |
| **IRQL** |  |