---
UID: NI:ntddcdvd.IOCTL_DVD_SEND_KEY2
title: IOCTL_DVD_SEND_KEY2
author: windows-driver-content
description: Sends the specified key to a DVD device -to complete the related step in an authentication sequence. The IOCTL_DVD_SEND_KEY2 request has write access to the device and can send a broader range of key types than IOCTL_DVD_SEND_KEY.
old-location: storage\ioctl_dvd_send_key2.htm
old-project: storage
ms.assetid: 58b9c2a5-cd29-4c62-b5ae-39911821e3b7
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IOCTL_DVD_SEND_KEY2, IOCTL_DVD_SEND_KEY2 control code [Storage Devices], k307_f38bdf8b-8bdc-4f28-bf53-d42f8b04a610.xml, ntddcdvd/IOCTL_DVD_SEND_KEY2, storage.ioctl_dvd_send_key2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
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
-	Ntddcdvd.h
api_name:
-	IOCTL_DVD_SEND_KEY2
product: Windows
targetos: Windows
req.typenames: DVD_STRUCTURE_FORMAT, *PDVD_STRUCTURE_FORMAT
---

# IOCTL_DVD_SEND_KEY2 IOCTL
Sends the specified key to a DVD device -to complete the related step in an authentication sequence. The IOCTL_DVD_SEND_KEY2 request has write access to the device and can send a broader range of key types than <a href="..\ntddcdvd\ni-ntddcdvd-ioctl_dvd_send_key.md">IOCTL_DVD_SEND_KEY</a>.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains a <a href="..\ntddcdvd\ns-ntddcdvd-_dvd_copy_protect_key.md">DVD_COPY_PROTECT_KEY</a> structure that indicates the session ID, key type, and key to be sent to the device.

### Input Buffer Length
Length of a <a href="..\ntddcdvd\ns-ntddcdvd-_dvd_copy_protect_key.md">DVD_COPY_PROTECT_KEY</a>.

### Output Buffer
None.

### Output Buffer Length
None.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Information</b> field is set to zero. The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_INSUFFICIENT_RESOURCES.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddcdvd.h (include Ntddcdvd.h) |

## See Also

<a href="..\ntddcdvd\ns-ntddcdvd-_dvd_copy_protect_key.md">DVD_COPY_PROTECT_KEY</a>