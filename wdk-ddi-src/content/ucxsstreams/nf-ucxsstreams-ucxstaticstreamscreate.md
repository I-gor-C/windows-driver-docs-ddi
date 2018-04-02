---
UID: NF:ucxsstreams.UcxStaticStreamsCreate
title: UcxStaticStreamsCreate function
author: windows-driver-content
description: Creates a static streams object.
old-location: buses\_ucxstaticstreamscreate.htm
old-project: usbref
ms.assetid: F7AA10E3-5F56-4751-A603-54A0BFB00927
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UcxStaticStreamsCreate, UcxStaticStreamsCreate method [Buses], buses._ucxstaticstreamscreate, ucxsstreams/UcxStaticStreamsCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucxsstreams.h
req.include-header: Ucxclass.h, Ucxstreams.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	ucxsstreams.h
api_name:
-	UcxStaticStreamsCreate
product: Windows
targetos: Windows
req.typenames: UCX_ROOTHUB_CONFIG, *PUCX_ROOTHUB_CONFIG
req.product: Windows 10 or later.
---


# UcxStaticStreamsCreate function
Creates a static streams object.

## Syntax

```
NTSTATUS UcxStaticStreamsCreate(
  UCXENDPOINT            Endpoint,
  PUCXSSTREAMS_INIT      *StaticStreamsInit,
  PWDF_OBJECT_ATTRIBUTES Attributes,
  UCXSSTREAMS            *StaticStreams
);
```

## Parameters

`Endpoint`

A handle to the endpoint object that supports static streams. The client driver retrieved the handle in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt188039">UcxEndpointCreate</a>.

`StaticStreamsInit`

TBD

`Attributes`

A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that specifies attributes for the stream object.

`StaticStreams`

TBD


## Return Value

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.

## Remarks

The client driver for the host controller must call this method after the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> call. The parent of the new endpoint object is the endpoint object. 

Typically, the client driver calls this method in its implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187843">EVT_UCX_USBDEVICE_ENDPOINT_ADD</a> event callback.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10  |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxsstreams.h (include Ucxclass.h, Ucxstreams.h) |
| **IRQL** | PASSIVE_LEVEL |