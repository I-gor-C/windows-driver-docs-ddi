---
UID: NI:lamp.IOCTL_LAMP_GET_CAPABILITIES_WHITE
title: IOCTL_LAMP_GET_CAPABILITIES_WHITE
author: windows-driver-content
description: The IOCTL_LAMP_GET_CAPABILITIES_WHITE control code queries the capabilities of the lamp when the device is configured to emit white light.
old-location: stream\ioctl_lamp_get_capabilities_white.htm
old-project: stream
ms.assetid: F4A7CF9A-023F-42FC-A40C-E95964EC5392
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: stream.ioctl_lamp_get_capabilities_white, IOCTL_LAMP_GET_CAPABILITIES_WHITE control code [Streaming Media Devices], IOCTL_LAMP_GET_CAPABILITIES_WHITE, lamp/IOCTL_LAMP_GET_CAPABILITIES_WHITE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: lamp.h
req.include-header: 
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
-	lamp.h
apiname:
-	IOCTL_LAMP_GET_CAPABILITIES_WHITE
product: Windows
targetos: Windows
req.typenames: LAMP_MODE
---

# IOCTL_LAMP_GET_CAPABILITIES_WHITE IOCTL
The <b>IOCTL_LAMP_GET_CAPABILITIES_WHITE</b> 
   control code queries the capabilities of the lamp when the device is configured to emit white light.
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>#define IOCTL_LAMP_GET_CAPABILITIES_WHITE \
    CTL_CODE(IOCTL_LAMP_BASE, 0x0000, METHOD_BUFFERED, FILE_ANY_ACCESS)</pre>
</td>
</tr>
</table></span></div>

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<code>Irp-&gt;AssociatedIrp.SystemBuffer</code> points to a buffer of type <a href="..\lamp\ns-lamp-lamp_capabilities_white.md">LAMP_CAPABILITIES_WHITE</a>.

### Input Buffer Length
Length of the buffer.

### Output Buffer
<code>Irp-&gt;AssociatedIrp.SystemBuffer</code> is filled with all capabilities supported by the lamp hardware.

### Output Buffer Length
<code>IO_STACK_LOCATION.Parameters.DeviceIoControl.OutputBufferLength</code> is the length of the buffer (in bytes) passed in the <code>Irp-&gt;AssociatedIrp.SystemBuffer</code> field.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The driver sets <code>Irp-&gt;IoStatus.Status</code> to <b>STATUS_SUCCESS</b> or the appropriate error status. It will set <code>Irp-&gt;IoStatus.Information</code> to the number of bytes required to hold the buffer.

## Remarks
By requirement, a lamp whose driver supports the <b>GUID_DEVINTERFACE_LAMP</b> interface is required to support emitting white light.

The payload of this IOCTL is a <a href="..\lamp\ns-lamp-lamp_capabilities_white.md">LAMP_CAPABILITIES_WHITE</a> structure.

The <b>IsLightIntensityAdjustable</b> field indicates whether the luminance level can be programmed. If this field evaluates to <b>FALSE</b>, it means that the underlying device only supports the on/off switch and the light intensity cannot be adjusted.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | lamp.h |