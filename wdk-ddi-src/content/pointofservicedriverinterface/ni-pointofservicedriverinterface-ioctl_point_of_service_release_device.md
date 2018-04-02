---
UID: NI:pointofservicedriverinterface.IOCTL_POINT_OF_SERVICE_RELEASE_DEVICE
title: IOCTL_POINT_OF_SERVICE_RELEASE_DEVICE
author: windows-driver-content
description: This I/O control function is called when a client is ready to relinquish its claim on a device.
old-location: pos\ioctl_point_of_service_release_device.htm
old-project: pos
ms.assetid: 623feb2b-8c49-41e8-9de5-d5955843c6f7
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IOCTL_POINT_OF_SERVICE_RELEASE_DEVICE, IOCTL_POINT_OF_SERVICE_RELEASE_DEVICE control code, pointofservicedriverinterface/IOCTL_POINT_OF_SERVICE_RELEASE_DEVICE, pos.ioctl_point_of_service_release_device
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	pointofservicedriverinterface.h
api_name:
-	IOCTL_POINT_OF_SERVICE_RELEASE_DEVICE
product: Windows
targetos: Windows
req.typenames: PosPropertyId
---

# IOCTL_POINT_OF_SERVICE_RELEASE_DEVICE IOCTL
This I/O control function is called when a client is ready to relinquish its claim on a device.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
Not used with this operation; set to <b>NULL</b>.

### Input Buffer Length
Not used with this operation; set to <b>0</b> (zero).

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

To get extended error information, call <a href="http://go.microsoft.com/fwlink/p/?LinkId=316871">GetLastError</a>. The following list shows common error values:

## Remarks
<h3><a id="Parameters"></a><a id="parameters"></a><a id="PARAMETERS"></a>Parameters</h3>


The driver can handle this IOCTL by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt593132">PosCxReleaseDevice</a>.

To use this IOCTL, the client must have previously called <a href="https://msdn.microsoft.com/library/windows/hardware/dn772093">IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |