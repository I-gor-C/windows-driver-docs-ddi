---
UID: NC.hwnclx.HWN_CLX_UNREGISTER_CLIENT
title: HWN_CLX_UNREGISTER_CLIENT
author: windows-driver-content
description: 
ms.assetid: 17915b03-e624-4fda-8c31-eb79a71c68e3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hwnclx.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# HWN_CLX_UNREGISTER_CLIENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

HWN_CLX_UNREGISTER_CLIENT HwnClxUnregisterClient; 

// Definition

NTSTATUS HwnClxUnregisterClient 
(
	WDFDRIVER Driver
)
{...}

HWN_CLX_UNREGISTER_CLIENT PHWN_CLX_UNREGISTER_CLIENT


```

## -parameters

### -param Driver: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also