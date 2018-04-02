---
UID: NS:pep_x._PEP_ACPI_SPB_SPI_RESOURCE
title: "_PEP_ACPI_SPB_SPI_RESOURCE"
author: windows-driver-content
description: The PEP_ACPI_SPB_SPI_RESOURCE structure describes an ACPI SPI serial bus resource.
old-location: kernel\pep_acpi_spb_spi_resource.htm
old-project: kernel
ms.assetid: 75CD5462-8382-4E83-ADC1-3E1B811A0D60
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPEP_ACPI_SPB_SPI_RESOURCE, PEP_ACPI_SPB_SPI_RESOURCE, PEP_ACPI_SPB_SPI_RESOURCE structure [Kernel-Mode Driver Architecture], PPEP_ACPI_SPB_SPI_RESOURCE, PPEP_ACPI_SPB_SPI_RESOURCE structure pointer [Kernel-Mode Driver Architecture], _PEP_ACPI_SPB_SPI_RESOURCE, kernel.pep_acpi_spb_spi_resource, pepfx/PEP_ACPI_SPB_SPI_RESOURCE, pepfx/PPEP_ACPI_SPB_SPI_RESOURCE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	pepfx.h
api_name:
-	PEP_ACPI_SPB_SPI_RESOURCE
product:
- Windows
targetos: Windows
req.typenames: PEP_ACPI_SPB_SPI_RESOURCE, *PPEP_ACPI_SPB_SPI_RESOURCE, PEP_ACPI_SPB_SPI_RESOURCE, *PPEP_ACPI_SPB_SPI_RESOURCE
---

# _PEP_ACPI_SPB_SPI_RESOURCE structure
The <b>PEP_ACPI_SPB_SPI_RESOURCE</b> structure describes an ACPI SPI serial bus resource.

## Syntax
```
typedef struct _PEP_ACPI_SPB_SPI_RESOURCE {
  PEP_ACPI_SPB_RESOURCE SpbCommon;
  ULONG                 ConnectionSpeed;
  UCHAR                 DataBitLength;
  UCHAR                 Phase;
  UCHAR                 Polarity;
  USHORT                DeviceSelection;
} PEP_ACPI_SPB_SPI_RESOURCE, *PPEP_ACPI_SPB_SPI_RESOURCE;
```

## Members


`SpbCommon`

A <a href="https://msdn.microsoft.com/library/windows/hardware/mt186695">PEP_ACPI_SPB_RESOURCE</a> structure describing this resource.

`ConnectionSpeed`

The maximum speed, in hertz, supported by this connection.

`DataBitLength`

The size, in bits, of the smallest unit of transfer.

`Phase`

The phase of the clock pulse on which to capture data.

`Polarity`

The polarity of the clock. If zero, this indicates the
clock is low during the first phase. If 1, this indicates the
clock is high during the first phase.

`DeviceSelection`

The device selection value. This value is
specific to the device and may refer to a chip-select line, GPIO
line, or other line selection mechanism.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pep_x.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt186695">PEP_ACPI_SPB_RESOURCE</a>