---
UID: NI:pointofservicedriverinterface.IOCTL_POINT_OF_SERVICE_MSR_UPDATE_KEY
title: IOCTL_POINT_OF_SERVICE_MSR_UPDATE_KEY
author: windows-driver-content
description: This I/O control function sets a new encryption key.
old-location: pos\ioctl_point_of_service_msr_update_key.htm
old-project: pos
ms.assetid: 7ac830d3-6a75-4d82-9123-cd7ad9c2cdea
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: pos.ioctl_point_of_service_msr_update_key, IOCTL_POINT_OF_SERVICE_MSR_UPDATE_KEY control code, IOCTL_POINT_OF_SERVICE_MSR_UPDATE_KEY, pointofservicedriverinterface/IOCTL_POINT_OF_SERVICE_MSR_UPDATE_KEY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: pointofservicedriverinterface.h
req.include-header: Pointofservicedriverinterface.h
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
-	pointofservicedriverinterface.h
apiname:
-	IOCTL_POINT_OF_SERVICE_MSR_UPDATE_KEY
product: Windows
targetos: Windows
req.typenames: PosPropertyId
---

# IOCTL_POINT_OF_SERVICE_MSR_UPDATE_KEY IOCTL
This I/O control function sets a new encryption key.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
Pointer to the input buffer, a <a href="..\pointofservicedriverinterface\ns-pointofservicedriverinterface-_msr_update_key.md">MSR_UPDATE_KEY</a> variable.

### Input Buffer Length
Size of the input buffer, in bytes. Set to <b>sizeof(MSR_UPDATE_KEY)</b>.

### Output Buffer
Not used with this operation; set to <b>NULL</b>.

### Output Buffer Length
Not used with this operation; set to <b>0</b> (zero).

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
Returns <b>TRUE</b> if successful; otherwise, returns <b>FALSE</b>.

To get extended error information, call <a href="http://go.microsoft.com/fwlink/p/?LinkId=316871">GetLastError</a>

## Remarks
<h3><a id="Parameters"></a><a id="parameters"></a><a id="PARAMETERS"></a>Parameters</h3>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |