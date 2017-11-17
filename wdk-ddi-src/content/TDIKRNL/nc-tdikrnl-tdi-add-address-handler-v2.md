---
UID: NC.tdikrnl.TDI_ADD_ADDRESS_HANDLER_V2
title: TDI_ADD_ADDRESS_HANDLER_V2
author: windows-driver-content
description: 
ms.assetid: bf826a6a-865c-4991-99fc-a6d0c66b09e1
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

# TDI_ADD_ADDRESS_HANDLER_V2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TDI_ADD_ADDRESS_HANDLER_V2 TdiAddAddressHandlerV2; 

// Definition

VOID TdiAddAddressHandlerV2 
(
	PTA_ADDRESS Address
	PUNICODE_STRING DeviceName
	PTDI_PNP_CONTEXT Context
)
{...}

TDI_ADD_ADDRESS_HANDLER_V2 


```

## -parameters

### -param Address: 
### -param DeviceName: 
### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also