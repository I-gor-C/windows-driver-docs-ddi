---
UID: NC.wdm.TRANSLATE_BUS_ADDRESS
title: TRANSLATE_BUS_ADDRESS
author: windows-driver-content
description: 
ms.assetid: a74bf11c-0b16-4af9-be98-e67b227b6324
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# TRANSLATE_BUS_ADDRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TRANSLATE_BUS_ADDRESS TranslateBusAddress; 

// Definition

_IRQL_requires_same_ BOOLEAN TranslateBusAddress 
(
	PVOID Context
	PHYSICAL_ADDRESS BusAddress
	ULONG Length
	PULONG AddressSpace
	PPHYSICAL_ADDRESS TranslatedAddress
)
{...}

TRANSLATE_BUS_ADDRESS PTRANSLATE_BUS_ADDRESS


```

## -parameters

### -param Context: 
### -param BusAddress: 
### -param Length: 
### -param AddressSpace: 
### -param TranslatedAddress: 



## -returns

Returns _IRQL_requires_same_ BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also