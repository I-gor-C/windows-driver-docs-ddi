---
UID: NC.wdm.PGPE_CONNECT_VECTOR
title: PGPE_CONNECT_VECTOR
author: windows-driver-content
description: 
ms.assetid: ed8f9476-4f57-4b9f-aa10-d35551759574
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

# PGPE_CONNECT_VECTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGPE_CONNECT_VECTOR PgpeConnectVector; 

// Definition

NTSTATUS PgpeConnectVector 
(
)
{...}

PGPE_CONNECT_VECTOR 


```

## -parameters




## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also