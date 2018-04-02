---
UID: NF:d3dkmthk.D3DKMTDestroyProtectedSession
title: D3DKMTDestroyProtectedSession function
author: windows-driver-content
description: Used to destroy a protected session.
old-location: display\d3dkmtdestroyprotectedsession.htm
old-project: display
ms.assetid: e27ab1db-647d-447c-b79d-2553aa088398
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMTDestroyProtectedSession, D3DKMTDestroyProtectedSession method [Display Devices], d3dkmthk/D3DKMTDestroyProtectedSession, display.d3dkmtdestroyprotectedsession
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
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
-	D3DKMTDestroyProtectedSession
product: Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
---


# D3DKMTDestroyProtectedSession function
Used to destroy a protected session.

## Syntax

```
NTSTATUS D3DKMTDestroyProtectedSession(

);
```

## Parameters

This function has no parameters.

## Return Value

Returns STATUS_SUCCESS if completed successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | d3dkmthk.h |