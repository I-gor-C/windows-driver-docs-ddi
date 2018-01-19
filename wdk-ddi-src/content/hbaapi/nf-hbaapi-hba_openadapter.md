---
UID : NF:hbaapi.HBA_OpenAdapter
title : HBA_OpenAdapter function
author : windows-driver-content
description : The HBA_OpenAdapter routine opens an HBA and returns a handle.
old-location : storage\hba_openadapter.htm
old-project : storage
ms.assetid : 78c37e2c-171b-483c-967d-1b80bde24338
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : HBA_OpenAdapter
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : hbaapi.h
req.include-header : Hbaapi.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : HBA_OpenAdapter
req.alt-loc : Hbaapi.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Hbaapi.lib
req.dll : Hbaapi.dll
req.irql : 
req.typenames : HBA_WWNTYPE
---


# HBA_OpenAdapter function
The <b>HBA_OpenAdapter</b> routine opens an HBA and returns a handle.

## Syntax

````
HBA_HANDLE HBA_API HBA_OpenAdapter(
  _In_ PSTR SniaAdapterName
);
````

## Parameters

`AdapterName`




## Return Value

The <b>HBA_OpenAdapter</b> routine returns a handle to the open HBA.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | hbaapi.h (include Hbaapi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |