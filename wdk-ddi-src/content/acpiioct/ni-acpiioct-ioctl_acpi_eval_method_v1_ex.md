---
UID: NI:acpiioct.IOCTL_ACPI_EVAL_METHOD_V1_EX
title: IOCTL_ACPI_EVAL_METHOD_V1_EX
author: windows-driver-content
description: The IOCTL_ACPI_EVAL_METHOD_V1_EX control code synchronously evaluates an ACPI control method that is supported by the device.
old-location: acpi\ioctl_acpi_eval_method_v1_ex.htm
old-project: acpi
ms.assetid: 2EACDAE2-C6B4-4906-AB1E-3A8FA781D528
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: IOCTL_ACPI_EVAL_METHOD_V1_EX, IOCTL_ACPI_EVAL_METHOD_V1_EX control code [ACPI Devices], acpi.ioctl_acpi_eval_method_v1_ex, acpiioct/IOCTL_ACPI_EVAL_METHOD_V1_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: acpiioct.h
req.include-header: Acpiioct.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709 and later versions.
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
-	Acpiioct.h
api_name:
-	IOCTL_ACPI_EVAL_METHOD_V1_EX
product: Windows
targetos: Windows
req.typenames: UNIT_ISOCH_PARAMS, *PUNIT_ISOCH_PARAMS
---

# IOCTL_ACPI_EVAL_METHOD_V1_EX IOCTL
The <b>IOCTL_ACPI_EVAL_METHOD_V1_EX</b> control code synchronously evaluates an ACPI control method that is supported by the device.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
An input buffer structure that depends on the type of input arguments to be passed to the control method.

### Input Buffer Length
The size, in bytes, of the input buffer.

### Output Buffer
An output buffer structure that contains the output arguments from the control method.

### Output Buffer Length
The size, in bytes, of the output buffer.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 and later versions. Windows 10, version 1709 and later versions. |
| **Header** | acpiioct.h (include Acpiioct.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548651">WdfIoTargetSendInternalIoctlOthersSynchronously</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548656">WdfIoTargetSendInternalIoctlSynchronously</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548660">WdfIoTargetSendIoctlSynchronously</a>