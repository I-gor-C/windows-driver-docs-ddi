---
UID: NC.wdm.PGPE_ENABLE_EVENT2
title: PGPE_ENABLE_EVENT2
author: windows-driver-content
description: 
ms.assetid: 7f8ffbd2-b6ee-4220-ac9b-34a70a6ed105
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

# PGPE_ENABLE_EVENT2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGPE_ENABLE_EVENT2 PgpeEnableEvent2; 

// Definition

NTSTATUS PgpeEnableEvent2 
(
	PVOID Context
	PVOID ObjectContext
)
{...}

PGPE_ENABLE_EVENT2 


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