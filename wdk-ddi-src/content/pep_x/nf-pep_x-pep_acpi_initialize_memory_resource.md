---
UID: NF:pep_x.PEP_ACPI_INITIALIZE_MEMORY_RESOURCE
title: PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_IO_MEMORY_RESOURCE structure.
old-location: kernel\pep_acpi_initialize_memory_resource.htm
old-project: kernel
ms.assetid: 44EC5408-626A-4FDA-A777-C1A733D690F1
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: PEP_ACPI_INITIALIZE_MEMORY_RESOURCE, PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function [Kernel-Mode Driver Architecture], kernel.pep_acpi_initialize_memory_resource, pepfx/PEP_ACPI_INITIALIZE_MEMORY_RESOURCE
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
-	PEP_ACPI_INITIALIZE_MEMORY_RESOURCE
product: Windows
targetos: Windows
req.typenames: PEP_WORK_TYPE, *PPEP_WORK_TYPE, PEP_WORK_TYPE, *PPEP_WORK_TYPE
---


# PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function
The <b>PEP_ACPI_INITIALIZE_MEMORY_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="..\pepfx\ns-pepfx-_pep_acpi_io_memory_resource.md">PEP_ACPI_IO_MEMORY_RESOURCE</a> structure.

## Syntax

````
FORCEINLINE VOID PEP_ACPI_INITIALIZE_MEMORY_RESOURCE(
  _In_  UCHAR              ReadWrite,
  _In_  ULONG              MinimumAddress,
  _In_  ULONG              MaximumAddress,
  _In_  ULONG              Alignment,
  _In_  ULONG              MemorySize,
  _Out_ PPEP_ACPI_RESOURCE Resource
);
````

## Parameters

`ReadWrite`

If true, indicates that the resource is read/write. Otherwise, it's read-only.

`MinimumAddress`

Specifies the minimum acceptable starting address for the IO range.

`MaximumAddress`

Specifies the maximum acceptable starting address for the IO range.

`Alignment`

Specifies the alignment granularity for the memory address assigned.

`MemorySize`

Specifies the number of bytes in the memory range.

`Resource`

A pointer to the resource. The structure behind the pointer is of type <a href="..\pepfx\ns-pepfx-_pep_acpi_io_memory_resource.md">PEP_ACPI_IO_MEMORY_RESOURCE</a>.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10.  |
| **Target Platform** | Windows |
| **Header** | pep_x.h (include Pep_x.h) |

## See Also

<a href="..\pepfx\ns-pepfx-_pep_acpi_io_memory_resource.md">PEP_ACPI_IO_MEMORY_RESOURCE</a>