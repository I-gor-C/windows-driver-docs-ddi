---
UID: NS:acpitabl._LPI_STATE_DESCRIPTOR
title: "_LPI_STATE_DESCRIPTOR"
author: windows-driver-content
description: Defines an LPI state descriptor.
old-location: acpi\lpi_state_descriptor.htm
old-project: acpi
ms.assetid: B52012DB-922A-43A2-A175-7F7887C290F1
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PLPI_STATE_DESCRIPTOR, LPI_STATE_DESCRIPTOR, LPI_STATE_DESCRIPTOR structure [ACPI Devices], PLPI_STATE_DESCRIPTOR, PLPI_STATE_DESCRIPTOR structure pointer [ACPI Devices], _LPI_STATE_DESCRIPTOR, acpi.lpi_state_descriptor, acpitabl/LPI_STATE_DESCRIPTOR, acpitabl/PLPI_STATE_DESCRIPTOR"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: acpitabl.h
req.include-header: Acpitabl.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	acpitabl.h
api_name:
-	LPI_STATE_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: LPI_STATE_DESCRIPTOR, *PLPI_STATE_DESCRIPTOR
---

# _LPI_STATE_DESCRIPTOR structure
Defines an LPI state descriptor.

## Syntax
````
typedef struct _LPI_STATE_DESCRIPTOR {
  ULONG           Type;
  ULONG           Length;
  USHORT          UniqueId;
  UCHAR           Reserved[2];
  LPI_STATE_FLAGS Flags;
  GEN_ADDR        EntryTrigger;
  ULONG           Residency;
  ULONG           Latency;
  GEN_ADDR        ResidencyCounter;
  ULONGLONG       ResidencyCounterFrequency;
} LPI_STATE_DESCRIPTOR, *PLPI_STATE_DESCRIPTOR;
````

## Members


`Type`

The type.

`Length`

The length.

`UniqueId`

A unique ID.

`Reserved`

Reserved.

`Flags`

State flags.

`EntryTrigger`

An entry trigger.

`Residency`

A residency value.

`Latency`

A latency value.

`ResidencyCounter`

Residency counter.

`ResidencyCounterFrequency`

Residency counter frequency.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | acpitabl.h (include Acpitabl.h) |