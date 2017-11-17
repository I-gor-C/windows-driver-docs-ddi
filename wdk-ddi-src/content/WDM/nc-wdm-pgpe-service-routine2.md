---
UID: NC.wdm.PGPE_SERVICE_ROUTINE2
title: PGPE_SERVICE_ROUTINE2
author: windows-driver-content
description: 
ms.assetid: 89bda86d-2fa5-49a4-b660-298e48ddfd2e
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

# PGPE_SERVICE_ROUTINE2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGPE_SERVICE_ROUTINE2 PgpeServiceRoutine2; 

// Definition

BOOLEAN PgpeServiceRoutine2 
(
	PVOID ObjectContext
	PVOID ServiceContext
)
{...}

PGPE_SERVICE_ROUTINE2 


```

## -parameters

### -param ObjectContext: 
### -param ServiceContext: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also