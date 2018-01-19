---
UID : NF:winspool.SetJobNamedProperty
title : SetJobNamedProperty function
author : windows-driver-content
description : .
old-location : print\setjobnamedproperty.htm
old-project : print
ms.assetid : 6A03B009-21D4-4CD2-9BB5-36F402118270
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : SetJobNamedProperty
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : winspool.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SetJobNamedProperty
req.alt-loc : Winspool.h
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
req.typenames : BIDI_TYPE
req.product : Windows 10 or later.
---


# SetJobNamedProperty function


## Syntax

````
DWORD WINAPI SetJobNamedProperty(
  _In_       HANDLE                    hPrinter,
  _In_       DWORD                     JobId,
  _In_ const PrintNamedProperty        *pProperty
);
````

## Parameters

`hPrinter`



`JobId`

TD

`pProperty`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | winspool.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |