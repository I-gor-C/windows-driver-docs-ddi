---
UID: NC.sensorscx.PSENSORSCX_EXPORTED_INTERFACES
title: PSENSORSCX_EXPORTED_INTERFACES
author: windows-driver-content
description: 
ms.assetid: 56233b5c-c37f-4f5d-958e-1d948cd66964
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sensorscx.h
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

# PSENSORSCX_EXPORTED_INTERFACES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSENSORSCX_EXPORTED_INTERFACES PsensorscxExportedInterfaces; 

// Definition

VOID PsensorscxExportedInterfaces 
(
	 VOID
)
{...}

PSENSORSCX_EXPORTED_INTERFACES 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also