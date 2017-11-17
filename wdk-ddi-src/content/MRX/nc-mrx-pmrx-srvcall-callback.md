---
UID: NC.mrx.PMRX_SRVCALL_CALLBACK
title: PMRX_SRVCALL_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 8153f9a0-5e25-40dc-801c-19facc8072b4
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

# PMRX_SRVCALL_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_SRVCALL_CALLBACK PmrxSrvcallCallback; 

// Definition

VOID PmrxSrvcallCallback 
(
	IN OUT PMRX_SRVCALL_CALLBACK_CONTEXT Context
)
{...}

PMRX_SRVCALL_CALLBACK 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also