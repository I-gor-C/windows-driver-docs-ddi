---
UID: NC.wdm.PGPE_DISCONNECT_VECTOR2
title: PGPE_DISCONNECT_VECTOR2
author: windows-driver-content
description: 
ms.assetid: 1bb2b048-5f43-4d61-af99-221a84552dd1
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

# PGPE_DISCONNECT_VECTOR2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGPE_DISCONNECT_VECTOR2 PgpeDisconnectVector2; 

// Definition

NTSTATUS PgpeDisconnectVector2 
(
	PVOID Context
	PVOID ObjectContext
)
{...}

PGPE_DISCONNECT_VECTOR2 


```

## -parameters

### -param Context: 
### -param ObjectContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also