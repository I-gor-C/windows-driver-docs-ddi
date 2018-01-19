---
UID : NS:ntddstor._STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR
title : _STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR
author : windows-driver-content
description : The STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure is used to retrieve the attributes information for a device.
old-location : storage\storage_device_attributes_descriptor.htm
old-project : storage
ms.assetid : DA8434EF-6163-4D07-A81D-D1AC2D55BFB4
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR, STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR, PSTORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddstor.h
req.include-header : Ntddstor.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR
req.alt-loc : ntddstor.h
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
req.typenames : STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR, PSTORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR
---

# _STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure
The STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure is used to retrieve the attributes information for a  device.

## Syntax
````
typedef struct _STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR {
  ULONG   Version;
  ULONG   Size;
  ULONG64 Attributes;
} STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR, *PSTORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR;
````

## Members

        
            `Attributes`

            <table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `Size`

            Indicates the quantity of data reported, in bytes. This is the <code>sizeof(STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR)</code>.
        
            `Version`

            Contains the version of the data reported.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddstor.h (include Ntddstor.h) |