---
UID: NI:ntddstor.IOCTL_STORAGE_DEVICE_POWER_CAP
title: IOCTL_STORAGE_DEVICE_POWER_CAP
author: windows-driver-content
description: A driver can use IOCTL_STORAGE_DEVICE_POWER_CAP to specify a maximum operational power consumption level for a storage device.
old-location: storage\ioctl_storage_device_power_cap.htm
old-project: storage
ms.assetid: 88DEC1F2-F0E7-4E95-9A46-D9E8EF72B1BB
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IOCTL_STORAGE_DEVICE_POWER_CAP, IOCTL_STORAGE_DEVICE_POWER_CAP control code [Storage Devices], ntddstor/IOCTL_STORAGE_DEVICE_POWER_CAP, storage.ioctl_storage_device_power_cap
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	Ntddstor.h
api_name:
-	IOCTL_STORAGE_DEVICE_POWER_CAP
product:
- Windows
targetos: Windows
req.typenames: STORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION
---

# IOCTL_STORAGE_DEVICE_POWER_CAP IOCTL
A driver can use <b>IOCTL_STORAGE_DEVICE_POWER_CAP</b> to specify a maximum operational power  consumption level for a storage device. The OS will do it's best to transition the device to a power state that will not exceed the given maximum. However, this depends on what the device supports. The actual maximum may be less than or greater than the desired maximum.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<b>
       Parameters.DeviceIoControl.InputBufferLength</b> indicates the size, in bytes, of the parameter buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>, which must be &gt;= <b>sizeof</b>(<a href="https://msdn.microsoft.com/library/windows/hardware/dn931805">STORAGE_DEVICE_POWER_CAP</a>).

<b>
       Irp-&gt;AssociatedIrp.SystemBuffer</b> contains <a href="https://msdn.microsoft.com/library/windows/hardware/dn931805">STORAGE_DEVICE_POWER_CAP</a> data that specifies the maximum power. 

<b>
       Parameters.DeviceIoControl.OutputBufferLength</b> indicates the number of bytes that can be written to <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>. <b>OutputBufferLength</b> must be <b>sizeof</b>(<a href="https://msdn.microsoft.com/library/windows/hardware/dn931805">STORAGE_DEVICE_POWER_CAP</a>).

### Input Buffer Length
The length of .

### Output Buffer
If the operation is successful, the output buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> will contain a <a href="https://msdn.microsoft.com/library/windows/hardware/dn931805">STORAGE_DEVICE_POWER_CAP</a> structure.

### Output Buffer Length
<b>
       Parameters.DeviceIoControl.InputBufferLength</b> indicates the size, in bytes, of the parameter buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>, which must be &gt;= <b>sizeof</b>(<a href="https://msdn.microsoft.com/library/windows/hardware/dn931805">STORAGE_DEVICE_POWER_CAP</a>).

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Information</b> field is set to the number of bytes returned. The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_INVALID_DEVICE_REQUEST, STATUS_INVALID_PARAMETER, or STATUS_NOT_SUPPORTED.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | ntddstor.h (include Ntddstor.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn931805">STORAGE_DEVICE_POWER_CAP</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn931806">STORAGE_DEVICE_POWER_CAP_UNITS</a>