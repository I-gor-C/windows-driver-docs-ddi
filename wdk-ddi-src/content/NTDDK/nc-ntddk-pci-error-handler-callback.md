---
UID: NC.ntddk.PCI_ERROR_HANDLER_CALLBACK
title: PCI_ERROR_HANDLER_CALLBACK
author: windows-driver-content
description: 
ms.assetid: d5913b9e-da3b-4932-82d3-405d1ab08b8a
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

# PCI_ERROR_HANDLER_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCI_ERROR_HANDLER_CALLBACK PciErrorHandlerCallback; 

// Definition

VOID PciErrorHandlerCallback 
(
	 VOID
)
{...}

PCI_ERROR_HANDLER_CALLBACK 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also