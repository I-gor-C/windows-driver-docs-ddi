---
UID: NC.wdfusb.PFN_WDFUSBINTERFACEGETNUMCONFIGUREDPIPES
title: PFN_WDFUSBINTERFACEGETNUMCONFIGUREDPIPES
author: windows-driver-content
description: 
ms.assetid: 0acd6955-4041-4665-a662-a68a2835337b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfusb.h
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

# PFN_WDFUSBINTERFACEGETNUMCONFIGUREDPIPES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBINTERFACEGETNUMCONFIGUREDPIPES PfnWdfusbinterfacegetnumconfiguredpipes; 

// Definition

WDFAPI PfnWdfusbinterfacegetnumconfiguredpipes 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBINTERFACE UsbInterface
)
{...}

PFN_WDFUSBINTERFACEGETNUMCONFIGUREDPIPES 


```

## -parameters

### -param DriverGlobals: 
### -param UsbInterface: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also