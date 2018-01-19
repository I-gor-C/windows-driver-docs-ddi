---
UID : NS:mpiowmi._MPIO_ADAPTER_INFORMATION
title : _MPIO_ADAPTER_INFORMATION
author : windows-driver-content
description : The MPIO_ADAPTER_INFORMATION structure contains information that pertains to MPIO's view of a path.
old-location : storage\mpio_adapter_information.htm
old-project : storage
ms.assetid : bcf159a7-75a5-46aa-897a-2c5eb00f51d8
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _MPIO_ADAPTER_INFORMATION, *PMPIO_ADAPTER_INFORMATION, MPIO_ADAPTER_INFORMATION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : mpiowmi.h
req.include-header : Mpiowmi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : MPIO_ADAPTER_INFORMATION
req.alt-loc : mpiowmi.h
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
req.typenames : "*PMPIO_ADAPTER_INFORMATION, MPIO_ADAPTER_INFORMATION"
---

# _MPIO_ADAPTER_INFORMATION structure
The MPIO_ADAPTER_INFORMATION structure contains information that pertains to MPIO's view of a path.

## Syntax
````
typedef struct _MPIO_ADAPTER_INFORMATION {
  ULONGLONG PathId;
  UCHAR     BusNumber;
  UCHAR     DeviceNumber;
  UCHAR     FunctionNumber;
  UCHAR     Pad;
  WCHAR     AdapterName[63 + 1];
} MPIO_ADAPTER_INFORMATION, *PMPIO_ADAPTER_INFORMATION;
````

## Members

        
            `AdapterName`

            A string field that returns the friendly name of the host bus adapter through which this path is exposed.
        
            `BusNumber`

            An unsigned 8-bitfield that corresponds to the bus number that is assigned by PCI to the host bus adapter through which this path is exposed.
        
            `DeviceNumber`

            An unsigned 8-bitfield that corresponds to the device number that is assigned by PCI to the host bus adapter through which this path is exposed.
        
            `FunctionNumber`

            An unsigned 8-bitfield that corresponds to the function number that is assigned by PCI to the host bus adapter through which this path is exposed.
        
            `Pad`

            Should be zero.
        
            `PathId`

            An unsigned 64-bitfield that represents an identifier that is assigned to a particular path. This field will match the PathIdentifier field in the instance(s) of the PDO_INFORMATION class that represent device(s) exposed via this path.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | mpiowmi.h (include Mpiowmi.h) |