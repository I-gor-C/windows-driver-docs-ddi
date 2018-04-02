---
UID: NF:pep_x.PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE
title: PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_EXTENDED_ADDRESS structure.
old-location: kernel\pep_acpi_initialize_extended_io_resource.htm
old-project: kernel
ms.assetid: 95464DE1-221A-4053-B124-4CFD44557CD3
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE, PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function [Kernel-Mode Driver Architecture], kernel.pep_acpi_initialize_extended_io_resource, pepfx/PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE
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
-	PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE
product: Windows
targetos: Windows
req.typenames: PEP_WORK_TYPE, *PPEP_WORK_TYPE, PEP_WORK_TYPE, *PPEP_WORK_TYPE
---


# PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE function
The <b>PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a> structure.

## Syntax

```
void PEP_ACPI_INITIALIZE_EXTENDED_IO_RESOURCE(
  BOOLEAN            ResourceUsage,
  UCHAR              Decode,
  BOOLEAN            IsMinFixed,
  BOOLEAN            IsMaxFixed,
  UCHAR              ISARanges,
  ULONGLONG          AddressGranularity,
  ULONGLONG          AddressMinimum,
  ULONGLONG          AddressMaximum,
  ULONGLONG          AddressTranslation,
  ULONGLONG          RangeLength,
  ULONGLONG          TypeSpecificAttributes,
  PUNICODE_STRING    DescriptorName,
  BOOLEAN            TranslationTypeNonStatic,
  BOOLEAN            TanslationSparseDensity,
  PPEP_ACPI_RESOURCE Resource
);
```

## Parameters

`ResourceUsage`

This parameter is copied into the <b>GeneralFlags</b> member of the initialized <a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a> structure.

`Decode`

When set, indicates that this bridge subtractively decodes the address. This applies to top level bridges only. 

When not set, indicates that this bridge positively decodes this address.

`IsMinFixed`

When set, indicates that the minimum address is fixed.

`IsMaxFixed`

When set, indicates that the maximum address is fixed.

`ISARanges`

This parameter is copied into the <b>TypeSpecificFlags</b> member of the initialized <a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a> structure.

`AddressGranularity`

A bit mask indicating which bits have been decoded.

`AddressMinimum`

For bridges that translate addresses, this indicates the minimum starting address on the secondary side of the bridge.

`AddressMaximum`

For bridges that translate addresses, this indicates the maximum starting address on the secondary side of the bridge.

`AddressTranslation`

For bridges that translate addresses across the bridge, this is the
address on the primary side.

`RangeLength`

The length of the address range.

`TypeSpecificAttributes`

The type-specific attributes for this resource.

`DescriptorName`

The name of the resource descriptor.

`TranslationTypeNonStatic`

When true, indicates that the resource uses type translation. Otherwise, it uses type-static translation.

`TanslationSparseDensity`

When false, indicates that this is a dense translation. Otherwise, it is sparse.

`Resource`

This is cast to *<a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a>.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10.  |
| **Target Platform** | Windows |
| **Header** | pep_x.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a>