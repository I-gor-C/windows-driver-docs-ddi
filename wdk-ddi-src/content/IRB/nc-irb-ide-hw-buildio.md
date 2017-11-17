---
UID: NC.irb.IDE_HW_BUILDIO
title: IDE_HW_BUILDIO
author: windows-driver-content
description: 
ms.assetid: 30396e12-8bef-44f9-8193-cec3e0fa67a0
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

# IDE_HW_BUILDIO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IDE_HW_BUILDIO IdeHwBuildio; 

// Definition

BOOLEAN IdeHwBuildio 
(
	PVOID ChannelExtension
	PIDE_REQUEST_BLOCK Irb
)
{...}

IDE_HW_BUILDIO 


```

## -parameters

### -param ChannelExtension: 
### -param Irb: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also