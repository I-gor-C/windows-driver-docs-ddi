---
UID: NC.video.PI2C_STOP_2
title: PI2C_STOP_2
author: windows-driver-content
description: 
ms.assetid: 580ca2e5-7c13-4907-aca0-101545257250
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: video.h
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

# PI2C_STOP_2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PI2C_STOP_2 Pi2cStop2; 

// Definition

BOOLEAN Pi2cStop2 
(
	IN PVOID HwDeviceExtension
	IN PVIDEO_I2C_CONTROL I2CControl
)
{...}

PI2C_STOP_2 


```

## -parameters

### -param HwDeviceExtension: 
### -param I2CControl: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also