---
UID: NI:pointofservicedriverinterface.IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE
title: IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE
author: windows-driver-content
description: The I/O control function claims the device for exclusive access.
old-location: pos\ioctl_point_of_service_claim_device.htm
old-project: pos
ms.assetid: e9dfa630-d3ac-4228-ae2a-02ff5a0fd558
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE, IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE control code, pointofservicedriverinterface/IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE, pos.ioctl_point_of_service_claim_device
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
-	IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE
product: Windows
targetos: Windows
req.typenames: PosPropertyId
---

# IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE IOCTL
The I/O control function claims the device for exclusive access.

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


This IOCTL is handled by the PosCx library. The driver writer does not need to handle this IOCTL. Instead, call <a href="..\poscx\nf-poscx-poscxclaimdevice.md">PosCxClaimDevice</a>. If the POS device is already claimed by another client, then the POS device driver is responsible for notifying the claim owner using a <a href="https://msdn.microsoft.com/library/windows/hardware/dn790033">ReleaseDeviceRequested</a> event and waiting for the claim owner to retain its claim within 50 milliseconds. If the claim is not reaffirmed, then the current claim owner's claim is automatically revoked and granted to the challenging client.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |