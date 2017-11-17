---
UID: NC.srb.PHW_STARTIO
title: PHW_STARTIO
author: windows-driver-content
description: 
ms.assetid: 0b17dded-488a-4eeb-8d7e-9a7a30b60b78
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: srb.h
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

# PHW_STARTIO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_STARTIO PhwStartio; 

// Definition

BOOLEAN PhwStartio 
(
	PVOID DeviceExtension
	PSCSI_REQUEST_BLOCK Srb
)
{...}

PHW_STARTIO 


```

## -parameters

### -param DeviceExtension: 
### -param Srb: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also