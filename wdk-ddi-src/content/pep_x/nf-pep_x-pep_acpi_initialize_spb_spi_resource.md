---
UID: NF:pep_x.PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE
title: PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE function
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_SPI_RESOURCE structure.
old-location: kernel\pep_acpi_initialize_spb_spi_resource.htm
old-project: kernel
ms.assetid: 76568167-283C-4966-B7FC-0E8CDCD19B60
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE, PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE function [Kernel-Mode Driver Architecture], kernel.pep_acpi_initialize_spb_spi_resource, pepfx/PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE
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
-	PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE
product:
- Windows
targetos: Windows
req.typenames: PEP_WORK_TYPE, *PPEP_WORK_TYPE, PEP_WORK_TYPE, *PPEP_WORK_TYPE
---


# PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE function
The <b>PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="https://msdn.microsoft.com/library/windows/hardware/mt186696">PEP_ACPI_SPB_SPI_RESOURCE</a> structure.

## Syntax

```
void PEP_ACPI_INITIALIZE_SPB_SPI_RESOURCE(
  USHORT             DeviceSelection,
  UCHAR              DeviceSelectionPolarity,
  UCHAR              WireMode,
  UCHAR              DataBitLength,
  BOOLEAN            SlaveMode,
  ULONG              ConnectionSpeed,
  UCHAR              ClockPolarity,
  UCHAR              ClockPhase,
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

`DeviceSelection`

The device selection value. This value is
specific to the device and may refer to a chip-select line, GPIO
line, or other line selection mechanism.

`DeviceSelectionPolarity`

The polarity of the clock. If zero, this indicates the
clock is low during the first phase. If 1, this indicates the
clock is high during the first phase.

`WireMode`

When zero, indicates that this device produces and consumes this resource. Otherwise, this device only consumes this resource.

`DataBitLength`

The size, in bits, of the smallest unit of transfer.

`SlaveMode`

Indicates if the resource is operating in slave mode.

`ConnectionSpeed`

The maximum speed, in hertz, supported by this connection.

`ClockPolarity`

The polarity of the clock. If zero, this indicates the
clock is low during the first phase. If 1, this indicates the
clock is high during the first phase.

`ClockPhase`

The phase of the clock pulse on which to capture data.

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

A pointer to the resource. The structure behind the pointer is of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt186696">PEP_ACPI_SPB_SPI_RESOURCE</a>.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10.  |
| **Target Platform** | Windows |
| **Header** | pep_x.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt186696">PEP_ACPI_SPB_SPI_RESOURCE</a>