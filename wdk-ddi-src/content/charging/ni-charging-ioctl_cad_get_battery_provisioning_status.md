---
UID : NI:charging.IOCTL_CAD_GET_BATTERY_PROVISIONING_STATUS
title : IOCTL_CAD_GET_BATTERY_PROVISIONING_STATUS
author : windows-driver-content
description : This IOCTL is for internal use only.
old-location : battery\ioctl_cad_get_battery_provisioning_status.htm
old-project : battery
ms.assetid : 4E92A629-C080-4C32-8768-D0615F35B161
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : battery.ioctl_cad_get_battery_provisioning_status, IOCTL_CAD_GET_BATTERY_PROVISIONING_STATUS control code [Battery Devices], IOCTL_CAD_GET_BATTERY_PROVISIONING_STATUS, charging/IOCTL_CAD_GET_BATTERY_PROVISIONING_STATUS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : charging.h
req.include-header : 
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
req.typenames : POWERSOURCEID, *PPOWERSOURCEID
---

# IOCTL_CAD_GET_BATTERY_PROVISIONING_STATUS IOCTL
This IOCTL is for internal use only.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<text></text>

### Input Buffer Length
<text></text>

### Output Buffer
<text></text>

### Output Buffer Length
<text></text>

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
Irp->IoStatus.Status is set to STATUS_SUCCESS if the request is successful.
Otherwise, Status to the appropriate error condition as a NTSTATUS code. 
For more information, see [XREF-LINK:NTSTATUS Values].


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | charging.h |