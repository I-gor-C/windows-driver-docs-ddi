---
UID : NI:ntddser.IOCTL_SERENUM_GET_PORT_NAME
title : IOCTL_SERENUM_GET_PORT_NAME
author : windows-driver-content
description : The IOCTL_SERENUM_GET_PORT_NAME request returns the value of the PortName (or Identifier) entry value for the RS-232 port -- see Registry Settings for a Plug and Play Serial Device.
old-location : serports\ioctl_serenum_get_port_name.htm
old-project : serports
ms.assetid : c61bc594-91be-418f-9e40-ebe99e31304f
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : serports.ioctl_serenum_get_port_name, IOCTL_SERENUM_GET_PORT_NAME control code [Serial Ports], IOCTL_SERENUM_GET_PORT_NAME, ntddser/IOCTL_SERENUM_GET_PORT_NAME, senumref_448bb4bf-eda4-4fbc-abb6-5f470d07861e.xml
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : SD_REQUEST_FUNCTION
---

# IOCTL_SERENUM_GET_PORT_NAME IOCTL
The IOCTL_SERENUM_GET_PORT_NAME request returns the value of the <b>PortName</b> (or <b>Identifier</b>) entry value for the RS-232 port -- see <a href="https://msdn.microsoft.com/57bd090a-20fe-41c6-b730-0479f6ae0982">Registry Settings for a Plug and Play Serial Device</a>.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None.

### Input Buffer Length
None.

### Output Buffer
The <b>AssociatedIrp.SystemBuffer</b> member points to a client-allocated buffer that Serenum uses to output the port name. The port name is a null-terminated Unicode string.

### Output Buffer Length
The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is set to the size in bytes of a client-allocated output buffer.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
If the request is successful, the <b>Information</b> member is set to the size in bytes of the null-terminated Unicode string that is returned in the client's output buffer.

The <b>Status</b> member is set to one of the following values:


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddser.h (include Ntddser.h) |