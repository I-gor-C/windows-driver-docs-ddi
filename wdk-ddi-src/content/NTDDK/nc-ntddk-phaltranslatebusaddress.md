---
UID: NC.ntddk.pHalTranslateBusAddress
title: pHalTranslateBusAddress
author: windows-driver-content
description: 
ms.assetid: 06731c8d-b710-4b8b-9ac9-bf0dd55a4e9b
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

# pHalTranslateBusAddress callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalTranslateBusAddress Phaltranslatebusaddress; 

// Definition

BOOLEAN Phaltranslatebusaddress 
(
	INTERFACE_TYPE InterfaceType
	ULONG BusNumber
	PHYSICAL_ADDRESS BusAddress
	PULONG AddressSpace
	PPHYSICAL_ADDRESS TranslatedAddress
)
{...}

pHalTranslateBusAddress 


```

## -parameters

### -param InterfaceType: 
### -param BusNumber: 
### -param BusAddress: 
### -param AddressSpace: 
### -param TranslatedAddress: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also