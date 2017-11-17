---
UID: NC.ntddk.pHalHandlerForBus
title: pHalHandlerForBus
author: windows-driver-content
description: 
ms.assetid: b68dce0c-0fe3-4c60-b7ac-15403ed25776
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

# pHalHandlerForBus callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalHandlerForBus Phalhandlerforbus; 

// Definition

PBUS_HANDLER Phalhandlerforbus 
(
	INTERFACE_TYPE InterfaceType
	ULONG BusNumber
)
{...}

pHalHandlerForBus 


```

## -parameters

### -param InterfaceType: 
### -param BusNumber: 



## -returns

Returns PBUS_HANDLER that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also