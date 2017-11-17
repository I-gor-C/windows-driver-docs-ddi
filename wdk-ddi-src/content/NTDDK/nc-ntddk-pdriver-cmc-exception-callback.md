---
UID: NC.ntddk.PDRIVER_CMC_EXCEPTION_CALLBACK
title: PDRIVER_CMC_EXCEPTION_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 6372286f-82ef-4cd2-aca5-d8bfa6967445
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# PDRIVER_CMC_EXCEPTION_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDRIVER_CMC_EXCEPTION_CALLBACK PdriverCmcExceptionCallback; 

// Definition

VOID PdriverCmcExceptionCallback 
(
	PVOID Context
	PCMC_EXCEPTION CmcLog
)
{...}

PDRIVER_CMC_EXCEPTION_CALLBACK 


```

## -parameters

### -param Context: 
### -param CmcLog: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also