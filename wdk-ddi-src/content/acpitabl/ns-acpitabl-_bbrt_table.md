---
UID : NS:acpitabl._BBRT_TABLE
title : _BBRT_TABLE
author : windows-driver-content
description : Defines a Boot Background Resource Table.
old-location : acpi\bbrt_table.htm
old-project : acpi
ms.assetid : 0FC4D7BA-4292-4D87-8982-D20D267D6FA5
ms.author : windowsdriverdev
ms.date : 12/31/2017
ms.keywords : _BBRT_TABLE, *PBBRT_TABLE, BBRT_TABLE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : acpitabl.h
req.include-header : Acpitabl.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : BBRT_TABLE
req.alt-loc : acpitabl.h
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
req.typenames : "*PBBRT_TABLE, BBRT_TABLE"
---

# _BBRT_TABLE structure
Defines a Boot Background Resource Table.

## Syntax
````
typedef struct _BBRT_TABLE {
  DESCRIPTION_HEADER Header;
  ULONG              Background;
  ULONG              Foreground;
} BBRT_TABLE, *PBBRT_TABLE;
````

## Members

        
            `Background`

            A background value.
        
            `Foreground`

            A foreground value.
        
            `Header`

            A header.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | acpitabl.h (include Acpitabl.h) |