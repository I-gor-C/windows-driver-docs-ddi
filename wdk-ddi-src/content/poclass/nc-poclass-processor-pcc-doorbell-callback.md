---
UID: NC.poclass.PROCESSOR_PCC_DOORBELL_CALLBACK
title: PROCESSOR_PCC_DOORBELL_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 16c8913c-75e9-4caa-955b-33b3518f0525
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: poclass.h
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

# PROCESSOR_PCC_DOORBELL_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PROCESSOR_PCC_DOORBELL_CALLBACK ProcessorPccDoorbellCallback; 

// Definition

VOID ProcessorPccDoorbellCallback 
(
	ULONG Status
	ULONG_PTR Context
)
{...}

PROCESSOR_PCC_DOORBELL_CALLBACK 


```

## -parameters

### -param Status: 
### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also