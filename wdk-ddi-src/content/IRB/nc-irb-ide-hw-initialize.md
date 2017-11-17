---
UID: NC.irb.IDE_HW_INITIALIZE
title: IDE_HW_INITIALIZE
author: windows-driver-content
description: 
ms.assetid: e51ae075-81d6-4789-a7c6-27366cc4fb81
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

# IDE_HW_INITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IDE_HW_INITIALIZE IdeHwInitialize; 

// Definition

BOOLEAN IdeHwInitialize 
(
	PVOID ChannelExtension
	PIDE_DEVICE_PARAMETERS DeviceParameters
	PIDENTIFY_DEVICE_DATA IdentifyData
)
{...}

IDE_HW_INITIALIZE 


```

## -parameters

### -param ChannelExtension: 
### -param DeviceParameters: 
### -param IdentifyData: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also