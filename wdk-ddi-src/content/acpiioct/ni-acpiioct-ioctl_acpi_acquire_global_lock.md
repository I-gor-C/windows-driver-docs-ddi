---
UID : NI:acpiioct.IOCTL_ACPI_ACQUIRE_GLOBAL_LOCK
title : IOCTL_ACPI_ACQUIRE_GLOBAL_LOCK
author : windows-driver-content
description : The IOCTL_ACPI_ACQUIRE_GLOBAL_LOCK device control request is reserved for internal use only.
old-location : acpi\ioctl_acpi_acquire_global_lock.htm
old-project : acpi
ms.assetid : 359bd4d4-2557-4755-8904-32162645cdc0
ms.author : windowsdriverdev
ms.date : 12/31/2017
ms.keywords : _UNIT_ISOCH_PARAMS, *PUNIT_ISOCH_PARAMS, UNIT_ISOCH_PARAMS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : acpiioct.h
req.include-header : Acpiioct.h
req.target-type : Windows
req.target-min-winverclnt : Windows Vista and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_ACPI_ACQUIRE_GLOBAL_LOCK
req.alt-loc : Acpiioct.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PUNIT_ISOCH_PARAMS, UNIT_ISOCH_PARAMS"
---

# IOCTL_ACPI_ACQUIRE_GLOBAL_LOCK IOCTL
The IOCTL_ACPI_ACQUIRE_GLOBAL_LOCK device control request is reserved for internal use only.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<text></text>

### Input Buffer Length
<text></text>

### Output Buffer
<text></text>

### Output Buffer Length
<text></text>

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
Irp->IoStatus.Status is set to STATUS_SUCCESS if the request is successful.
Otherwise, Status to the appropriate error condition as a NTSTATUS code. 
For more information, see [XREF-LINK:NTSTATUS Values].


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | acpiioct.h (include Acpiioct.h) |
| **IRQL** |  |