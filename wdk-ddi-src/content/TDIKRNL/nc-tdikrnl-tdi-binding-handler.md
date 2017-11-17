---
UID: NC.tdikrnl.TDI_BINDING_HANDLER
title: TDI_BINDING_HANDLER
author: windows-driver-content
description: 
ms.assetid: 227e353e-17de-4333-87aa-6d886b7fcdef
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

# TDI_BINDING_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TDI_BINDING_HANDLER TdiBindingHandler; 

// Definition

VOID TdiBindingHandler 
(
	TDI_PNP_OPCODE PnPOpcode
	PUNICODE_STRING DeviceName
	PWSTR MultiSZBindList
)
{...}

TDI_BINDING_HANDLER 


```

## -parameters

### -param PnPOpcode: 
### -param DeviceName: 
### -param MultiSZBindList: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also