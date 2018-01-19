---
UID : NF:d3dkmthk.D3DKMTCreateHwQueue
title : D3DKMTCreateHwQueue function
author : windows-driver-content
description : Used to create a new hardware queue.
old-location : display\d3dkmtcreatehwqueue.htm
old-project : display
ms.assetid : FD4E892F-DDC6-449A-B77F-6C7F8240E467
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMTCreateHwQueue
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
req.alt-api : D3DKMTCreateHwQueue
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


# D3DKMTCreateHwQueue function
Used to create a new hardware queue.

## Syntax

````
NTSTATUS D3DKMTCreateHwQueue(
  _Inout_ D3DKMT_CREATEHWQUEUE *createHwQueue
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