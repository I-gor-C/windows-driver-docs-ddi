---
UID: NC.ntddk.PDRIVER_CPE_EXCEPTION_CALLBACK
title: PDRIVER_CPE_EXCEPTION_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 13da9e23-0021-4884-be0d-bb0a086a9395
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

# PDRIVER_CPE_EXCEPTION_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDRIVER_CPE_EXCEPTION_CALLBACK PdriverCpeExceptionCallback; 

// Definition

VOID PdriverCpeExceptionCallback 
(
	PVOID Context
	PCPE_EXCEPTION CmcLog
)
{...}

PDRIVER_CPE_EXCEPTION_CALLBACK 


```

## -parameters

### -param Context: 
### -param CmcLog: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also