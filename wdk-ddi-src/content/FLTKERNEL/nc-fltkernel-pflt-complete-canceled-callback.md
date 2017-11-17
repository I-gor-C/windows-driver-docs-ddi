---
UID: NC.fltkernel.PFLT_COMPLETE_CANCELED_CALLBACK
title: PFLT_COMPLETE_CANCELED_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 4de70f6b-06b5-4f7f-9714-eb13b7f7df58
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: fltkernel.h
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

# PFLT_COMPLETE_CANCELED_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLT_COMPLETE_CANCELED_CALLBACK PfltCompleteCanceledCallback; 

// Definition

VOID PfltCompleteCanceledCallback 
(
	PFLT_CALLBACK_DATA CallbackData
)
{...}

PFLT_COMPLETE_CANCELED_CALLBACK 


```

## -parameters

### -param CallbackData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also