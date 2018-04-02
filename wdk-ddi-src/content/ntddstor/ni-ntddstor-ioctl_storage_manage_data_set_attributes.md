---
UID: NI:ntddstor.IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES
title: IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES
author: windows-driver-content
description: This IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES request is used to send a manage data set attributes request to a storage device.
old-location: storage\ioctl_storage_manage_data_set_attributes.htm
old-project: storage
ms.assetid: 678bbca6-f21f-480a-897d-a30e922d01e3
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES, IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES control code [Storage Devices], k307_99edaea9-af25-4aba-ba16-0758c63252b6.xml, ntddstor/IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES, storage.ioctl_storage_manage_data_set_attributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddstor.h
req.include-header: Ntddstor.h
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
req.irql: IRQL < DISPATCH_LEVEL (See Remarks section.)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddstor.h
api_name:
-	IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES
product: Windows
targetos: Windows
req.typenames: STORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION
---

# IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES IOCTL
This <b>IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</b> request is used to send a manage data set attributes request to a storage device.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The buffer at <i>Irp-&gt;AssociatedIrp.SystemBuffer</i> contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552527">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a> structure. Note that the buffer may include parameter and data set range blocks. Also, the <b>Action</b> member of this structure defines the action to be performed through a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552520">DEVICE_DATA_MANAGEMENT_SET_ACTION</a> enumeration value.

### Input Buffer Length
<i>Parameters.DeviceIoControl.InputBufferLength</i> in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be at least <b>sizeof</b>(<a href="https://msdn.microsoft.com/library/windows/hardware/ff552527">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a>).

### Output Buffer
Depending on the value set in the <b>Action</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff552527">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a>, the request may return data in the buffer at <i>Irp-&gt;AssociatedIrp.SystemBuffer</i>. The system buffer will contain valid data if the manage data set action operation returns output and <i>Parameters.DeviceIoControl.InputBufferLength</i> &gt; 0.

### Output Buffer Length
The length of <a href="https://msdn.microsoft.com/library/windows/hardware/ff552527">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a>.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Status</b> field can be set to STATUS_SUCCESS, or possibly to STATUS_INVALID_DEVICE_REQUEST, STATUS_BUFFER_TOO_SMALL, STATUS_BUFFER_OVERFLOW, or some other error status.

## Remarks
Due to memory pool requirements by the storage driver stack, completion of the IRP containing this IOCTL must be at IRQL &lt; DISPATCH_LEVEL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddstor.h (include Ntddstor.h) |
| **IRQL** | IRQL < DISPATCH_LEVEL (See Remarks section.) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552520">DEVICE_DATA_MANAGEMENT_SET_ACTION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552527">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a>