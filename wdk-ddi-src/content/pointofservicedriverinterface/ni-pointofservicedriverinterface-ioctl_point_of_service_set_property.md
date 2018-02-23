---
UID: NI:pointofservicedriverinterface.IOCTL_POINT_OF_SERVICE_SET_PROPERTY
title: IOCTL_POINT_OF_SERVICE_SET_PROPERTY
author: windows-driver-content
description: This I/O control function sets the specified property on the device.
old-location: pos\ioctl_point_of_service_set_property.htm
old-project: pos
ms.assetid: 8907a99f-37b0-4c09-b92a-ac720328020e
ms.author: windowsdriverdev
ms.date: 2/19/2018
ms.keywords: pos.ioctl_point_of_service_set_property, IOCTL_POINT_OF_SERVICE_SET_PROPERTY control code, IOCTL_POINT_OF_SERVICE_SET_PROPERTY, pointofservicedriverinterface/IOCTL_POINT_OF_SERVICE_SET_PROPERTY
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
-	IOCTL_POINT_OF_SERVICE_SET_PROPERTY
product: Windows
targetos: Windows
req.typenames: PosPropertyId
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
Returns <b>TRUE</b> if successful; otherwise, returns <b>FALSE</b>.

To get extended error information, call <a href="http://go.microsoft.com/fwlink/p/?LinkId=316871">GetLastError</a>. The following list shows common error values (other return values may be returned as defined by your property callback implementation):

## Remarks
<h3><a id="Parameters"></a><a id="parameters"></a><a id="PARAMETERS"></a>Parameters</h3>


The client must successfully call <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_claim_device.md">IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE</a> before using this IOCTL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |