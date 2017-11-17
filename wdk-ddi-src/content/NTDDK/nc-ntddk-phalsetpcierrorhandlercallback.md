---
UID: NC.ntddk.pHalSetPciErrorHandlerCallback
title: pHalSetPciErrorHandlerCallback
author: windows-driver-content
description: 
ms.assetid: de90e7a0-40a5-4b3a-afc4-908d9ec2a39c
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

# pHalSetPciErrorHandlerCallback callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalSetPciErrorHandlerCallback Phalsetpcierrorhandlercallback; 

// Definition

VOID Phalsetpcierrorhandlercallback 
(
	PCI_ERROR_HANDLER_CALLBACK Callback
)
{...}

pHalSetPciErrorHandlerCallback 


```

## -parameters

### -param Callback: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also