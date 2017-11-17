---
UID: NC.mrx.PMRX_CALLDOWN_CTX
title: PMRX_CALLDOWN_CTX
author: windows-driver-content
description: 
ms.assetid: acec8baf-1cb8-41f7-a84f-8effaf1f54c8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mrx.h
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

# PMRX_CALLDOWN_CTX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_CALLDOWN_CTX PmrxCalldownCtx; 

// Definition

NTSTATUS PmrxCalldownCtx 
(
	IN OUT PRX_CONTEXT RxContext
	IN OUT PRDBSS_DEVICE_OBJECT RxDeviceObject
)
{...}

PMRX_CALLDOWN_CTX 


```

## -parameters

### -param RxContext: 
### -param RxDeviceObject: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also