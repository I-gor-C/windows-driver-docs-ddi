---
UID: NC.wdm.PGPE_CONNECT_VECTOR2
title: PGPE_CONNECT_VECTOR2
author: windows-driver-content
description: 
ms.assetid: 729cb6da-687a-4988-ba7b-8120f9a03251
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

# PGPE_CONNECT_VECTOR2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGPE_CONNECT_VECTOR2 PgpeConnectVector2; 

// Definition

NTSTATUS PgpeConnectVector2 
(
	PVOID Context
	ULONG GpeNumber
	KINTERRUPT_MODE Mode
	BOOLEAN Shareable
	PGPE_SERVICE_ROUTINE ServiceRoutine
	PVOID ServiceContext
	PVOID *ObjectContext
)
{...}

PGPE_CONNECT_VECTOR2 


```

## -parameters

### -param Context: 
### -param GpeNumber: 
### -param Mode: 
### -param Shareable: 
### -param ServiceRoutine: 
### -param ServiceContext: 
### -param *ObjectContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also