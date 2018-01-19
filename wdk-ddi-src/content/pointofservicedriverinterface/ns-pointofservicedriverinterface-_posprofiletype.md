---
UID : NS:pointofservicedriverinterface._PosProfileType
title : _PosProfileType
author : windows-driver-content
description : This structure describes the number of profile strings in a buffer.
old-location : pos\posprofiletype.htm
old-project : pos
ms.assetid : b0ef1592-f3f3-4ca1-83f8-dc7cb76cda36
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _PosProfileType, PosProfileType
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : pointofservicedriverinterface.h
req.include-header : PointOfServiceDriverInterface.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PosProfileType
req.alt-loc : PointOfServiceDriverInterface.h
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
req.typenames : PosProfileType
---

# _PosProfileType structure
This structure describes the number of profile strings in a buffer.

## Syntax
````
typedef struct _PosProfileType {
  UINT32 EntryCount;
  UINT32 DataLength;
} PosProfileType;
````

## Members


    ## Remarks
        The buffer of profile <i>PosStringType</i> strings follows this structure in memory.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | pointofservicedriverinterface.h (include PointOfServiceDriverInterface.h) |