---
UID: NC.tdikrnl.TDI_ADD_ADDRESS_HANDLER
title: TDI_ADD_ADDRESS_HANDLER
author: windows-driver-content
description: 
ms.assetid: dac1755a-eb33-4b53-a010-95643c103156
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: tdikrnl.h
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

# TDI_ADD_ADDRESS_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TDI_ADD_ADDRESS_HANDLER TdiAddAddressHandler; 

// Definition

VOID TdiAddAddressHandler 
(
	PTA_ADDRESS Address
)
{...}

TDI_ADD_ADDRESS_HANDLER 


```

## -parameters

### -param Address: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also