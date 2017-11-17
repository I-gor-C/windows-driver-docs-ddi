---
UID: NC.ucxcontroller.PFN_UCXCONTROLLERRESETCOMPLETE
title: PFN_UCXCONTROLLERRESETCOMPLETE
author: windows-driver-content
description: 
ms.assetid: bfeef0ec-5d54-4094-aac1-926ca244af7c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxcontroller.h
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

# PFN_UCXCONTROLLERRESETCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXCONTROLLERRESETCOMPLETE PfnUcxcontrollerresetcomplete; 

// Definition

WDFAPI PfnUcxcontrollerresetcomplete 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXCONTROLLER Controller
	PUCX_CONTROLLER_RESET_COMPLETE_INFO UcxControllerResetCompleteInfo
)
{...}

PFN_UCXCONTROLLERRESETCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param Controller: 
### -param UcxControllerResetCompleteInfo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also