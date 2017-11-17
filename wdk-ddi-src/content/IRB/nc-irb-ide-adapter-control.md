---
UID: NC.irb.IDE_ADAPTER_CONTROL
title: IDE_ADAPTER_CONTROL
author: windows-driver-content
description: 
ms.assetid: a2059437-2b4e-422b-b4e6-53956e38694f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: irb.h
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

# IDE_ADAPTER_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IDE_ADAPTER_CONTROL IdeAdapterControl; 

// Definition

BOOLEAN IdeAdapterControl 
(
	PVOID ControllerExtension
	IDE_CONTROL_ACTION ControlAction
	PVOID Parameters
)
{...}

IDE_ADAPTER_CONTROL 


```

## -parameters

### -param ControllerExtension: 
### -param ControlAction: 
### -param Parameters: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also