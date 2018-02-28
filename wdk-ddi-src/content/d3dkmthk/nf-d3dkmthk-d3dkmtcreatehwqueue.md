---
UID: NF:d3dkmthk.D3DKMTCreateHwQueue
title: D3DKMTCreateHwQueue function
author: windows-driver-content
description: Used to create a new hardware queue.
old-location: display\d3dkmtcreatehwqueue.htm
old-project: display
ms.assetid: FD4E892F-DDC6-449A-B77F-6C7F8240E467
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: D3DKMTCreateHwQueue, D3DKMTCreateHwQueue method [Display Devices], d3dkmthk/D3DKMTCreateHwQueue, display.d3dkmtcreatehwqueue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
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
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmthk.h
api_name:
-	D3DKMTCreateHwQueue
product: Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
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
| **Target Platform** | Windows |
| **Header** | d3dkmthk.h |
| **Library** | NtosKrnl.exe |