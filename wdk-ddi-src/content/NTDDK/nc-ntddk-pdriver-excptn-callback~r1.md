---
UID: NC.ntddk.PDRIVER_EXCPTN_CALLBACK~r1
title: PDRIVER_EXCPTN_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 568e2f81-e1c2-43f7-b5ad-d4d66023bb4e
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

# PDRIVER_EXCPTN_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDRIVER_EXCPTN_CALLBACK PdriverExcptnCallback; 

// Definition

VOID PdriverExcptnCallback 
(
	PVOID Context
	_KTRAP_FRAME *TrapFrame
	_KEXCEPTION_FRAME *ExceptionFrame
	PVOID Exception
)
{...}

PDRIVER_EXCPTN_CALLBACK 


```

## -parameters

### -param Context: 
### -param *TrapFrame: 
### -param *ExceptionFrame: 
### -param Exception: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also