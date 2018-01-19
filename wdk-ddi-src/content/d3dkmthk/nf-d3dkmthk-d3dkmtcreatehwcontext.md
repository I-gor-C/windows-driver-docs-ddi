---
UID : NF:d3dkmthk.D3DKMTCreateHwContext
title : D3DKMTCreateHwContext function
author : windows-driver-content
description : Used to create a new hardware context.
old-location : display\d3dkmtcreatehwcontext.htm
old-project : display
ms.assetid : 147F46A9-1182-4480-8886-7C39F940EA7D
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMTCreateHwContext
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : d3dkmthk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMTCreateHwContext
req.alt-loc : d3dkmthk.h
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
req.typenames : D3DKMT_DRIVERVERSION
---


# D3DKMTCreateHwContext function
Used to create a new hardware context.

## Syntax

````
NTSTATUS D3DKMTCreateHwContext(
  _Inout_ D3DKMT_CREATEHWCONTEXT *createHwContext
);
````

## Parameters

This function has no parameters.

## Return Value

Returns STATUS_SUCCESS if called successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |