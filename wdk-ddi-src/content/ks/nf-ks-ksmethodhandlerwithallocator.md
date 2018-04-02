---
UID: NF:ks.KsMethodHandlerWithAllocator
title: KsMethodHandlerWithAllocator function
author: windows-driver-content
description: The KsMethodHandlerWithAllocator functions performs the same handling as KsMethodHandler, with the same restrictions, but allows an optional allocator callback to be used to provide a buffer for the parameters.
old-location: stream\ksmethodhandlerwithallocator.htm
old-project: stream
ms.assetid: 3a4c2eaa-167a-406a-a792-612c3e624f89
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KsMethodHandlerWithAllocator, KsMethodHandlerWithAllocator function [Streaming Media Devices], ks/KsMethodHandlerWithAllocator, ksfunc_b8089a49-086b-4695-bebd-6fc3817ed7e0.xml, stream.ksmethodhandlerwithallocator
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
-	KsMethodHandlerWithAllocator
product: Windows
targetos: Windows
req.typenames: 
---


# KsMethodHandlerWithAllocator function
The <b>KsMethodHandlerWithAllocator</b> functions performs the same handling as <b>KsMethodHandler</b>, with the same restrictions, but allows an optional allocator callback to be used to provide a buffer for the parameters. If used, the filter may need to free the buffer in some nonconventional manner. Note that the IRP_BUFFERED_IO and IRP_DEALLOCATE_BUFFER flags are not set when using a custom allocator.

## Syntax

```
KSDDKAPI NTSTATUS KsMethodHandlerWithAllocator(
  PIRP                 Irp,
  ULONG                MethodSetsCount,
  const KSMETHOD_SET   *MethodSet,
  PFNKSALLOCATOR       Allocator,
  ULONG MethodItemSize OPTIONAL
);
```

## Parameters

`Irp`

Specifies the IRP with the method request being handled.

`MethodSetsCount`

Indicates the number of method set structures being passed.

`MethodSet`

Specifies the pointer to the list of method set information.

`Allocator`

Optionally points to an allocation function that will be used to allocate memory to store the method parameters.

`OPTIONAL`

TBD


## Return Value

The <b>KsMethodHandler</b> function returns STATUS_SUCCESS if successful, or an error specific to the method being handled if unsuccessful. The function always sets the IO_STATUS_BLOCK.Information field of the PIRP.IoStatus element within the IRP to zero because of an internal error, or the element is set by a method handler. The function does not set the IO_STATUS_BLOCK.Status field nor complete the IRP.

On 64-bit platforms, if the <i>PropertyItemSize</i> parameter is not a multiple of 8, STATUS_INVALID_PARAMETER is returned, and the call fails.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |