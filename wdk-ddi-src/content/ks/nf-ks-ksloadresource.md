---
UID : NF:ks.KsLoadResource
title : KsLoadResource function
author : windows-driver-content
description : Copies (loads) a resource from the given image.
old-location : stream\ksloadresource.htm
old-project : stream
ms.assetid : a7b9dcca-ce89-4fde-9e58-3c4a675227bc
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KsLoadResource function [Streaming Media Devices], ks/KsLoadResource, ksfunc_d966a58a-b0f0-411f-a19c-1db726efc56e.xml, stream.ksloadresource, KsLoadResource
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ks.h
req.include-header : Ks.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ks.lib
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---


# KsLoadResource function
Copies (loads) a resource from the given image.

## Syntax

````
NTSTATUS KsLoadResource(
  _In_      PVOID     ImageBase,
  _In_      POOL_TYPE PoolType,
  _In_      ULONG_PTR ResourceName,
  _In_      ULONG     ResourceType,
  _Out_     PVOID     *Resource,
  _Out_opt_ PULONG    ResourceSize
);
````

## Parameters

`ImageBase`

Pointer to the image base

`PoolType`

Pool type to use when copying resource

`ResourceName`

Resource name.

`ResourceType`

Resource type

`Resource`

Pointer to resultant resource memory.

`ResourceSize`

Pointer to ULONG value to receive the size of the resource.


## Return Value

STATUS_SUCCESS if successful, STATUS_INSUFFICIENT_RESOURCES if memory cannot be allocated, otherwise an appropriate error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |