---
UID: NI:hidclass.IOCTL_GET_PHYSICAL_DESCRIPTOR
title: IOCTL_GET_PHYSICAL_DESCRIPTOR
author: windows-driver-content
description: The IOCTL_GET_PHYSICAL_DESCRIPTOR request obtains the physical descriptor of a top-level collection.
old-location: hid\ioctl_get_physical_descriptor.htm
old-project: hid
ms.assetid: cf15dd7f-4568-40c7-b2e4-7cec8239df0b
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: IOCTL_GET_PHYSICAL_DESCRIPTOR, IOCTL_GET_PHYSICAL_DESCRIPTOR control code [Human Input Devices], hid.ioctl_get_physical_descriptor, hidclass/IOCTL_GET_PHYSICAL_DESCRIPTOR, hidioreq_3a61c6d2-a97a-47d6-86b1-317e22775271.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: hidclass.h
req.include-header: Hidclass.h
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
-	hidclass.h
api_name:
-	IOCTL_GET_PHYSICAL_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: HDAUDIO_STREAM_FORMAT, *PHDAUDIO_STREAM_FORMAT
---

# IOCTL_GET_PHYSICAL_DESCRIPTOR IOCTL
The IOCTL_GET_PHYSICAL_DESCRIPTOR request obtains the physical descriptor of a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a>.

For general information about HIDClass devices, see <a href="https://msdn.microsoft.com/2d3efb38-4eba-43db-8cff-9fac30209952">HID Collections</a>.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer.

### Input Buffer Length
<text></text>

### Output Buffer
<b>Irp-&gt;MdlAddress</b> must point to the buffer that will receive the physical descriptor.

### Output Buffer Length
<text></text>

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The HID class driver sets the <b>Status</b> member of <b>Irp-&gt;IoStatus</b> to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hidclass.h (include Hidclass.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff539677">HidD_GetPhysicalDescriptor</a>