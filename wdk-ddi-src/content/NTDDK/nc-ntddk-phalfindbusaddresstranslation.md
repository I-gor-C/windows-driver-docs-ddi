---
UID: NC.ntddk.pHalFindBusAddressTranslation
title: pHalFindBusAddressTranslation
author: windows-driver-content
description: 
ms.assetid: 58789b41-6b92-4db8-9b31-f421bf73f290
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

# pHalFindBusAddressTranslation callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalFindBusAddressTranslation Phalfindbusaddresstranslation; 

// Definition

BOOLEAN Phalfindbusaddresstranslation 
(
	PHYSICAL_ADDRESS BusAddress
	PULONG AddressSpace
	PPHYSICAL_ADDRESS TranslatedAddress
	PULONG_PTR Context
	BOOLEAN NextBus
)
{...}

pHalFindBusAddressTranslation 


```

## -parameters

### -param BusAddress: 
### -param AddressSpace: 
### -param TranslatedAddress: 
### -param Context: 
### -param NextBus: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also