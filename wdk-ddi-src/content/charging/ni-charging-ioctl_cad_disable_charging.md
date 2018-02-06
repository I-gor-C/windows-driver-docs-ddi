---
UID: NI:charging.IOCTL_CAD_DISABLE_CHARGING
title: IOCTL_CAD_DISABLE_CHARGING
author: windows-driver-content
description: This IOCTL is for internal use only.
old-location: battery\ioctl_cad_disable_charging.htm
old-project: battery
ms.assetid: 51E91097-7315-489A-8C07-0946481BF573
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: battery.ioctl_cad_disable_charging, IOCTL_CAD_DISABLE_CHARGING control code [Battery Devices], IOCTL_CAD_DISABLE_CHARGING, charging/IOCTL_CAD_DISABLE_CHARGING
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	charging.h
apiname:
-	IOCTL_CAD_DISABLE_CHARGING
product: Windows
targetos: Windows
req.typenames: POWERSOURCEID, *PPOWERSOURCEID
---

# IOCTL_CAD_DISABLE_CHARGING IOCTL
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