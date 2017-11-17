---
UID: NC.wdm.PGPE_DISABLE_EVENT2
title: PGPE_DISABLE_EVENT2
author: windows-driver-content
description: 
ms.assetid: 889c807b-5c7f-4617-bc2e-450eb10c72e7
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

# PGPE_DISABLE_EVENT2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGPE_DISABLE_EVENT2 PgpeDisableEvent2; 

// Definition

NTSTATUS PgpeDisableEvent2 
(
	PVOID Context
	PVOID ObjectContext
)
{...}

PGPE_DISABLE_EVENT2 


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