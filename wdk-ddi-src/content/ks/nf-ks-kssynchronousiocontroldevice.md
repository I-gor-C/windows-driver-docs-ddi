---
UID: NF:ks.KsSynchronousIoControlDevice
title: KsSynchronousIoControlDevice function
author: windows-driver-content
description: The KsSynchronousIoControlDevice function performs a synchronous device I/O control on the target device object. It waits in a nonalertable state until the I/O completes. This function can only be called at PASSIVE_LEVEL.
old-location: stream\kssynchronousiocontroldevice.htm
old-project: stream
ms.assetid: 7e4ca8ea-52c1-462e-bf02-cc82e9ab2be2
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KsSynchronousIoControlDevice, KsSynchronousIoControlDevice function [Streaming Media Devices], ks/KsSynchronousIoControlDevice, ksfunc_b3bba8f7-d9fb-4372-bfff-f39b4d925561.xml, stream.kssynchronousiocontroldevice
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
-	KsSynchronousIoControlDevice
product: Windows
targetos: Windows
req.typenames: 
---


# KsSynchronousIoControlDevice function
The <b>KsSynchronousIoControlDevice</b> function performs a synchronous device I/O control on the target device object. It waits in a nonalertable state until the I/O completes. This function can only be called at PASSIVE_LEVEL.

## Syntax

```
KSDDKAPI NTSTATUS KsSynchronousIoControlDevice(
  PFILE_OBJECT    FileObject,
  KPROCESSOR_MODE RequestorMode,
  ULONG           IoControl,
  PVOID           InBuffer,
  ULONG           InSize,
  PVOID           OutBuffer,
  ULONG           OutSize,
  PULONG          BytesReturned
);
```

## Parameters

`FileObject`

Indicates the file object to fill in the first stack location with.

`RequestorMode`

TBD

`IoControl`

Specifies the I/O control to send.

`InBuffer`

Points to the device input buffer.

`InSize`

Specifies the size in bytes of the device input buffer.

`OutBuffer`

Points to the device output buffer.

`OutSize`

Specifies the size in bytes of the device output buffer.

`BytesReturned`

Points to the place in which to put the number of bytes returned.


## Return Value

<b>KsSynchronousIoControlDevice </b>returns the result of the device I/O control.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |