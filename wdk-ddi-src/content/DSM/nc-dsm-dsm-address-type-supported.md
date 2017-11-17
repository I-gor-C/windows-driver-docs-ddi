---
UID: NC.dsm.DSM_ADDRESS_TYPE_SUPPORTED
title: DSM_ADDRESS_TYPE_SUPPORTED
author: windows-driver-content
description: 
ms.assetid: 76da0be8-a24b-4a6d-a22e-552f28cb40b3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_ADDRESS_TYPE_SUPPORTED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_ADDRESS_TYPE_SUPPORTED DsmAddressTypeSupported; 

// Definition

BOOLEAN DsmAddressTypeSupported 
(
	IN PVOID DsmContext
	IN ULONG AddressType
)
{...}

DSM_ADDRESS_TYPE_SUPPORTED 


```

## -parameters

### -param DsmContext: 
### -param AddressType: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also