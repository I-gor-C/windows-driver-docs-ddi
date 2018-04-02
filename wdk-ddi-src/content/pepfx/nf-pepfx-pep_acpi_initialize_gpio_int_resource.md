---
UID: NF:pepfx.PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE
title: PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE function
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_GPIO_RESOURCE structure.
old-location: kernel\pep_acpi_initialize_gpio_int_resource.htm
old-project: kernel
ms.assetid: EF8E3D1D-9C87-4083-A022-FD888D370B20
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE, PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE function [Kernel-Mode Driver Architecture], kernel.pep_acpi_initialize_gpio_int_resource, pepfx/PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: pepfx.h
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
-	PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE
product: Windows
targetos: Windows
req.typenames: PEP_WORK_TYPE, *PPEP_WORK_TYPE
---


# PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE function
The <b>PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="https://msdn.microsoft.com/library/windows/hardware/mt186671">PEP_ACPI_GPIO_RESOURCE</a> structure.

## Syntax

```
void PEP_ACPI_INITIALIZE_GPIO_INT_RESOURCE(
  KINTERRUPT_MODE      InterruptType,
  KINTERRUPT_POLARITY  LevelType,
  BOOLEAN              Shareable,
  BOOLEAN              CanWake,
  GPIO_PIN_CONFIG_TYPE PinConfig,
  USHORT               DebounceTimeout,
  UCHAR                ResourceSourceIndex,
  PUNICODE_STRING      ResourceSourceName,
  BOOLEAN              ResourceUsage,
  PUCHAR               VendorData,
  USHORT               VendorDataLength,
  PUSHORT              PinTable,
  UCHAR                PinCount,
  PPEP_ACPI_RESOURCE   Resource
);
```

## Parameters

`InterruptType`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff554239">KINTERRUPT_MODE</a> enumeration value that identifies the interrupt type.

`LevelType`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff554243">KINTERRUPT_POLARITY</a> enumeration value that identifies how a device signals an interrupt request on an interrupt line.

`Shareable`

Indicates if the device can be shared.

`CanWake`

Indicates if the device can be woken from a low-power state.

`PinConfig`

A <a href="https://msdn.microsoft.com/library/windows/hardware/mt186634">GPIO_PIN_CONFIG_TYPE</a> enumeration value that identifies the GPIO pin configuration type.

`DebounceTimeout`

Specifies the hardware debounce wait time, in hundredths of milliseconds.

`ResourceSourceIndex`

This parameter should always be zero.

`ResourceSourceName`

This parameter should always be "ResourceConsumer."

`ResourceUsage`

Indicates if this device is in use.

`VendorData`

A pointer to a raw data buffer containing vendor-defined byte data to be decoded by the OS driver.

`VendorDataLength`

The size of the buffer in the <i>VendorData</i> partameter.

`PinTable`

A list of pin numbers on the resource.

`PinCount`

The number of pins described by the <i>PinTable</i> parameter.

`Resource`

A pointer to the resource. The structure behind the pointer is of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt186671">PEP_ACPI_GPIO_RESOURCE</a>.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10.  |
| **Target Platform** | Windows |
| **Header** | pepfx.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt186634">GPIO_PIN_CONFIG_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554239">KINTERRUPT_MODE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554243">KINTERRUPT_POLARITY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt186671">PEP_ACPI_GPIO_RESOURCE</a>