---
UID: NF:pepfx.PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE
title: PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_EXTENDED_ADDRESS structure.
old-location: kernel\pep_acpi_initialize_extended_memory_resource.htm
old-project: kernel
ms.assetid: F566E078-9446-49E1-9325-AF65F3ABB6B9
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE, PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function [Kernel-Mode Driver Architecture], kernel.pep_acpi_initialize_extended_memory_resource, pepfx/PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE
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
-	PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE
product: Windows
targetos: Windows
req.typenames: PEP_WORK_TYPE, *PPEP_WORK_TYPE
---


# PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function
The <b>PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a> structure.

## Syntax

```
void PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE(
  BOOLEAN            ResourceUsage,
  UCHAR              Decode,
  BOOLEAN            IsMinFixed,
  BOOLEAN            IsMaxFixed,
  UCHAR              Cacheable,
  BOOLEAN            ReadWrite,
  ULONGLONG          AddressGranularity,
  ULONGLONG          AddressMinimum,
  ULONGLONG          AddressMaximum,
  ULONGLONG          AddressTranslation,
  ULONGLONG          RangeLength,
  ULONGLONG          TypeSpecificAttributes,
  PUNICODE_STRING    DescriptorName,
  UCHAR              MemoryRangeType,
  BOOLEAN            TranslationTypeNonStatic,
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

`Cacheable`

The caching flag for the resource.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt>0</dt>
</dl>
</td>
<td width="60%">
Indicates the memory is non-cacheable.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>1</dt>
</dl>
</td>
<td width="60%">
Indicates the memory is cacheable.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>2</dt>
</dl>
</td>
<td width="60%">
Indicates the memory is cacheable and supports write combining.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>3</dt>
</dl>
</td>
<td width="60%">
The memory is cacheable and prefetchable.

</td>
</tr>
</table>

`ReadWrite`

When true, indicates that the resource is available for read/write access. Otherwise, it's read-only.

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

`MemoryRangeType`

This parameter identifies the type of memory range provided by this resource.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt>0</dt>
</dl>
</td>
<td width="60%">
Address range memory: This range is available RAM usable by the operating system.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>1</dt>
</dl>
</td>
<td width="60%">
Address range reserved: This range of addresses is in use or reserved by the system
and is not to be included in the allocatable memory pool of the
operating system's memory manager.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>2</dt>
</dl>
</td>
<td width="60%">
Address range ACPI: ACPI Reclaim Memory. This range is available RAM usable by
the OS after it reads the ACPI tables.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>3</dt>
</dl>
</td>
<td width="60%">
Address Range NVS: ACPI NVS Memory. This range of addresses is in use or
reserved by the system and must not be used by the operating
system. This range is required to be saved and restored across
an NVS sleep.

</td>
</tr>
</table>

`TranslationTypeNonStatic`

TBD

`Resource`

This is cast to *<a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a>.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10.  |
| **Target Platform** | Windows |
| **Header** | pepfx.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a>