---
UID: NF:pep_x.PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE
title: PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE function
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_I2C_RESOURCE structure.
old-location: kernel\pep_acpi_initialize_spb_i2c_resource.htm
old-project: kernel
ms.assetid: 5F1606D8-1E6F-494F-AE70-07A1EC1FEA47
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE, PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE function [Kernel-Mode Driver Architecture], kernel.pep_acpi_initialize_spb_i2c_resource, pepfx/PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: pep_x.h
req.include-header: Pep_x.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
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
-	pepfx.h
api_name:
-	PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE
product:
- Windows
targetos: Windows
req.typenames: PEP_WORK_TYPE, *PPEP_WORK_TYPE, PEP_WORK_TYPE, *PPEP_WORK_TYPE
---


# PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE function
The <b>PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="https://msdn.microsoft.com/library/windows/hardware/mt186694">PEP_ACPI_SPB_I2C_RESOURCE</a> structure.

## Syntax

```
void PEP_ACPI_INITIALIZE_SPB_I2C_RESOURCE(
  USHORT             SlaveAddress,
  BOOLEAN            DeviceInitiated,
  ULONG              ConnectionSpeed,
  BOOLEAN            AddressingMode,
  PUNICODE_STRING    ResourceSource,
  UCHAR              ResourceSourceIndex,
  BOOLEAN            ResourceUsage,
  BOOLEAN            SharedMode,
  PCHAR              VendorData,
  USHORT             VendorDataLength,
  PPEP_ACPI_RESOURCE Resource
);
```

## Parameters

`SlaveAddress`

The I2C bus address for this connection.

`DeviceInitiated`

If true, indicates that communication over this connection is initiated by the device.

`ConnectionSpeed`

The maximum speed, in hertz, supported by this connection.

`AddressingMode`

Indicates that this device is in addressing mode.

`ResourceSource`

The name of the serial bus controller device to which this
connection descriptor applies. The name can be a fully
qualified path, a relative path, or a simple name segment
that utilizes the namespace search rules.

`ResourceSourceIndex`

This parameter should always be set to zero.

`ResourceUsage`

Indicates if the resource is in use.

`SharedMode`

Indicates if the resource is shared.

`VendorData`

A pointer to optional data that is specific to the serial bus connection type.

`VendorDataLength`

The length of the buffer pointed to by the <i>VendorData</i> parameter.

`Resource`

A pointer to the resource. The structure behind the pointer is of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt186694">PEP_ACPI_SPB_I2C_RESOURCE</a>.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10.  |
| **Target Platform** | Windows |
| **Header** | pep_x.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt186694">PEP_ACPI_SPB_I2C_RESOURCE</a>