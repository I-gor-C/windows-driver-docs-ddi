---
UID: NC.wdfrequest.PFN_WDFREQUESTWDMFORMATUSINGSTACKLOCATION
title: PFN_WDFREQUESTWDMFORMATUSINGSTACKLOCATION
author: windows-driver-content
description: 
ms.assetid: e5734926-7b2a-485c-b7ce-545851579339
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfrequest.h
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

# PFN_WDFREQUESTWDMFORMATUSINGSTACKLOCATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTWDMFORMATUSINGSTACKLOCATION PfnWdfrequestwdmformatusingstacklocation; 

// Definition

WDFAPI PfnWdfrequestwdmformatusingstacklocation 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PIO_STACK_LOCATION Stack
)
{...}

PFN_WDFREQUESTWDMFORMATUSINGSTACKLOCATION 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param Stack: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also