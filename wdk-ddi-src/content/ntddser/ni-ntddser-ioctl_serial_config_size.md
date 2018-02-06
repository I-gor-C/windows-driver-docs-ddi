---
UID: NI:ntddser.IOCTL_SERIAL_CONFIG_SIZE
title: IOCTL_SERIAL_CONFIG_SIZE
author: windows-driver-content
description: The IOCTL_SERIAL_CONFIG_SIZE request returns information about configuration size.
old-location: serports\ioctl_serial_config_size.htm
old-project: serports
ms.assetid: 13229dcc-e698-4743-9ca2-303bef69304c
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: serports.ioctl_serial_config_size, IOCTL_SERIAL_CONFIG_SIZE control code [Serial Ports], IOCTL_SERIAL_CONFIG_SIZE, ntddser/IOCTL_SERIAL_CONFIG_SIZE, serref_c851a6c5-27c1-4690-bb2f-36bd458b6629.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddser.h
req.include-header: Ntddser.h
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
-	Ntddser.h
apiname:
-	IOCTL_SERIAL_CONFIG_SIZE
product: Windows
targetos: Windows
req.typenames: SD_REQUEST_FUNCTION
---

# IOCTL_SERIAL_CONFIG_SIZE IOCTL
The <b>IOCTL_SERIAL_CONFIG_SIZE</b> request returns information about configuration size.

Serial.sys always returns a configuration size of zero.

This request is obsolete and should not be used by new drivers for Microsoft Windows 2000 and later.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None.

### Input Buffer Length
None.

### Output Buffer
The <b>AssociatedIrp.SystemBuffer</b> member points to a client-allocated ULONG buffer that Serial.sys uses to output configuration size information.

### Output Buffer Length
The <b>Parameters.DeviceIoControl.OutputBufferLength</b> is set to the size in bytes of a ULONG.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Information</b> member is set to the size in bytes of a ULONG.

The <b>Status</b> member is set to one of the <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/serports/serial-device-control-requests2">Generic Status Values for Serial Device Control Requests</a>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddser.h (include Ntddser.h) |