---
UID : NF:ks.KsValidateAllocatorCreateRequest
title : KsValidateAllocatorCreateRequest function
author : windows-driver-content
description : The KsValidateAllocatorCreateRequest function validates an IRP_MJ_CREATE request as an allocator request and returns the create structure associated with the request on success.
old-location : stream\ksvalidateallocatorcreaterequest.htm
old-project : stream
ms.assetid : 9275257b-50d8-4272-b340-4344644b3e15
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KsValidateAllocatorCreateRequest
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
req.alt-api : KsValidateAllocatorCreateRequest
req.alt-loc : Ks.lib,Ks.dll
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
req.typenames : 
---


# KsValidateAllocatorCreateRequest function
The <b>KsValidateAllocatorCreateRequest</b> function validates an IRP_MJ_CREATE request as an allocator request and returns the create structure associated with the request on success.

## Syntax

````
NTSTATUS KsValidateAllocatorCreateRequest(
  _In_  PIRP                 Irp,
  _Out_ PKSALLOCATOR_FRAMING *AllocatorFraming
);
````

## Parameters

`Irp`

Specifies the IRP with the IRP_MJ_CREATE request being validated.

`AllocatorFraming`

Caller-defined pointer that on successful completion contains an address to the framing structure supplied with the request.


## Return Value

The <b>KsValidateAllocatorCreateRequest</b> function returns STATUS_SUCCESS if successful, or an error if the allocator request is not valid.


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