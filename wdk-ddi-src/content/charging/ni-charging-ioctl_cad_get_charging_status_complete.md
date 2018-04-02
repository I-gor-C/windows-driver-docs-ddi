---
UID: NI:charging.IOCTL_CAD_GET_CHARGING_STATUS_COMPLETE
title: IOCTL_CAD_GET_CHARGING_STATUS_COMPLETE
author: windows-driver-content
description: This IOCTL is for internal use only.
old-location: battery\ioctl_cad_get_charging_status_complete.htm
old-project: battery
ms.assetid: 715F1DF3-C3CF-4662-8095-22ECA0E45796
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: IOCTL_CAD_GET_CHARGING_STATUS_COMPLETE, IOCTL_CAD_GET_CHARGING_STATUS_COMPLETE control code [Battery Devices], battery.ioctl_cad_get_charging_status_complete, charging/IOCTL_CAD_GET_CHARGING_STATUS_COMPLETE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: charging.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	charging.h
api_name:
-	IOCTL_CAD_GET_CHARGING_STATUS_COMPLETE
product:
- Windows
targetos: Windows
req.typenames: POWERSOURCEID, *PPOWERSOURCEID
---

# IOCTL_CAD_GET_CHARGING_STATUS_COMPLETE IOCTL
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

For more information, see [NTSTATUS Values](https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/ntstatus-values).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | charging.h |