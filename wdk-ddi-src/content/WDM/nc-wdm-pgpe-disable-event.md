---
UID: NC.wdm.PGPE_DISABLE_EVENT
title: PGPE_DISABLE_EVENT
author: windows-driver-content
description: 
ms.assetid: 2e4d762d-1077-44c2-9267-9563ab998d26
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PGPE_DISABLE_EVENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGPE_DISABLE_EVENT PgpeDisableEvent; 

// Definition

NTSTATUS PgpeDisableEvent 
(
)
{...}

PGPE_DISABLE_EVENT 


```

## -parameters




## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also