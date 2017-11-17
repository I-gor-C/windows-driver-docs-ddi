---
UID: NC.scsiwmi.PSCSIWMI_FUNCTION_CONTROL
title: PSCSIWMI_FUNCTION_CONTROL
author: windows-driver-content
description: 
ms.assetid: 8444fe70-3554-4ceb-99e5-0f1d7ba0a502
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: scsiwmi.h
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

# PSCSIWMI_FUNCTION_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSCSIWMI_FUNCTION_CONTROL PscsiwmiFunctionControl; 

// Definition

BOOLEAN PscsiwmiFunctionControl 
(
	PVOID DeviceContext
	PSCSIWMI_REQUEST_CONTEXT RequestContext
	ULONG GuidIndex
	SCSIWMI_ENABLE_DISABLE_CONTROL Function
	BOOLEAN Enable
)
{...}

PSCSIWMI_FUNCTION_CONTROL 


```

## -parameters

### -param DeviceContext: 
### -param RequestContext: 
### -param GuidIndex: 
### -param Function: 
### -param Enable: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also