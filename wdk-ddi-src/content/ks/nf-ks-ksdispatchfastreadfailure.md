---
UID: NF:ks.KsDispatchFastReadFailure
title: KsDispatchFastReadFailure function
author: windows-driver-content
description: The KsDispatchFastReadFailure function is used in a KSDISPATCH_TABLE.FastRead entry when fast I/O read is not handled. The function should always return FALSE.
old-location: stream\ksdispatchfastreadfailure.htm
old-project: stream
ms.assetid: 7e0c72ce-0959-4835-ac1a-3f37869cc81f
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KsDispatchFastReadFailure, KsDispatchFastReadFailure function [Streaming Media Devices], KsDispatchFastWriteFailure, ks/KsDispatchFastReadFailure, ksfunc_fe3ea42f-80ae-4fbd-a2c2-55e957e913cc.xml, stream.ksdispatchfastreadfailure
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
-	KsDispatchFastReadFailure
product: Windows
targetos: Windows
req.typenames: 
---


# KsDispatchFastReadFailure function
The <b>KsDispatchFastReadFailure</b> function is used in a KSDISPATCH_TABLE.FastRead entry when fast I/O read is not handled. The function should always return <b>FALSE</b>.

## Syntax

```
KSDDKAPI BOOLEAN KsDispatchFastReadFailure(
  PFILE_OBJECT     FileObject,
  PLARGE_INTEGER   FileOffset,
  ULONG            Length,
  BOOLEAN          Wait,
  ULONG            LockKey,
  PVOID            Buffer,
  PIO_STATUS_BLOCK IoStatus,
  PDEVICE_OBJECT   DeviceObject
);
```

## Parameters

`FileObject`

Not used.

`FileOffset`

Not used.

`Length`

Not used.

`Wait`

Not used.

`LockKey`

Not used.

`Buffer`

Not used.

`IoStatus`

Not used.

`DeviceObject`

Not used.


## Return Value

The <b>KsDispatchFastReadFailure</b> function returns <b>FALSE</b>.

## Remarks

The <b>KsDispatchFastReadFailure</b> function is needed since the dispatch table for a particular opened instance of a device may not handle a specific major function that another opened instance needs to handle. Therefore, the function pointer in the driver object must always point to a function, such as the <b>KsDispatchFastReadFailure</b> function, that calls a dispatch table entry.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |