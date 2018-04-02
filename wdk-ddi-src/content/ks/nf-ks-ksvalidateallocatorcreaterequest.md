---
UID: NF:ks.KsValidateAllocatorCreateRequest
title: KsValidateAllocatorCreateRequest function
author: windows-driver-content
description: The KsValidateAllocatorCreateRequest function validates an IRP_MJ_CREATE request as an allocator request and returns the create structure associated with the request on success.
old-location: stream\ksvalidateallocatorcreaterequest.htm
old-project: stream
ms.assetid: 9275257b-50d8-4272-b340-4344644b3e15
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KsValidateAllocatorCreateRequest, KsValidateAllocatorCreateRequest function [Streaming Media Devices], ks/KsValidateAllocatorCreateRequest, ksfunc_2d988d7a-d39f-4c77-8c18-06d01a8d75e9.xml, stream.ksvalidateallocatorcreaterequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Ks.lib
-	Ks.dll
api_name:
-	KsValidateAllocatorCreateRequest
product: Windows
targetos: Windows
req.typenames: 
---


# KsValidateAllocatorCreateRequest function
The <b>KsValidateAllocatorCreateRequest</b> function validates an IRP_MJ_CREATE request as an allocator request and returns the create structure associated with the request on success.

## Syntax

```
KSDDKAPI NTSTATUS KsValidateAllocatorCreateRequest(
  PIRP                 Irp,
  PKSALLOCATOR_FRAMING *AllocatorFraming
);
```

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
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |