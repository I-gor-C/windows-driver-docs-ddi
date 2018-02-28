---
UID: NI:ntddpar.IOCTL_PAR_QUERY_RAW_DEVICE_ID
title: IOCTL_PAR_QUERY_RAW_DEVICE_ID
author: windows-driver-content
description: The IOCTL_PAR_QUERY_RAW_DEVICE_ID request returns a raw device ID, which includes the following:\_a two-byte prefix that specifies the size, in bytes, of the device's IEEE 1284 device ID; the IEEE 1284 device ID; and a NULL terminator.
old-location: parports\ioctl_par_query_raw_device_id.htm
old-project: parports
ms.assetid: 3d7b99ea-eb53-4466-bd98-15c147c00d35
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: IOCTL_PAR_QUERY_RAW_DEVICE_ID, IOCTL_PAR_QUERY_RAW_DEVICE_ID control code [Parallel Ports], cisspd_422dd85c-1d22-4968-9b4c-fd1ef03432e5.xml, ntddpar/IOCTL_PAR_QUERY_RAW_DEVICE_ID, parports.ioctl_par_query_raw_device_id
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddpar.h
req.include-header: Ntddpar.h
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
-	ntddpar.h
api_name:
-	IOCTL_PAR_QUERY_RAW_DEVICE_ID
product: Windows
targetos: Windows
req.typenames: OFFLOAD_SECURITY_ASSOCIATION, *POFFLOAD_SECURITY_ASSOCIATION
---

# IOCTL_PAR_QUERY_RAW_DEVICE_ID IOCTL
The IOCTL_PAR_QUERY_RAW_DEVICE_ID request returns a raw device ID, which includes the following: a two-byte prefix that specifies the size, in bytes, of the device's IEEE 1284 device ID; the IEEE 1284 device ID; and a <b>NULL</b> terminator.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None.

### Input Buffer Length
None.

### Output Buffer
The <b>AssociatedIrp.SystemBuffer</b> member points to a buffer that the client allocates to output a raw device ID. The buffer contains the following contiguous sequence of information: a two-byte prefix that specifies the size, in bytes, of the device's IEEE 1284 device ID; the device ID; and a <b>NULL</b> terminator.

### Output Buffer Length
The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member specifies the size, in bytes, of the output buffer that can hold the following: a two-byte prefix that specifies the size, in bytes, of the device's IEEE 1284 device ID; the device ID; and a <b>NULL</b> terminator. An IEEE 1284 device ID can be up to 64 KB in size.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
If the request is successful, the <b>Information</b> member is set to the size, in bytes, of the information returned in the output buffer. Otherwise, the <b>Information</b> member is set to zero. 

The <b>Status</b> member is set to one of the generic status values returned by device control requests for parallel devices or to one of the following values:


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddpar.h (include Ntddpar.h) |

## See Also

<a href="..\ntddpar\ni-ntddpar-ioctl_par_query_device_id_size.md">IOCTL_PAR_QUERY_DEVICE_ID_SIZE</a>



<a href="..\ntddpar\ni-ntddpar-ioctl_par_query_device_id.md">IOCTL_PAR_QUERY_DEVICE_ID</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20IOCTL_PAR_QUERY_RAW_DEVICE_ID control code%20 RELEASE:%20(2/15/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>