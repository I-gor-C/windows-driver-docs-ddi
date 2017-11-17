---
UID: NC.wdfusb.PFN_WDFUSBINTERFACESELECTSETTING
title: PFN_WDFUSBINTERFACESELECTSETTING
author: windows-driver-content
description: 
ms.assetid: 5bc0a332-6b16-4d4e-8bf6-f1db1a62ed92
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

# PFN_WDFUSBINTERFACESELECTSETTING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBINTERFACESELECTSETTING PfnWdfusbinterfaceselectsetting; 

// Definition

WDFAPI PfnWdfusbinterfaceselectsetting 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBINTERFACE UsbInterface
	PWDF_OBJECT_ATTRIBUTES PipesAttributes
	PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS Params
)
{...}

PFN_WDFUSBINTERFACESELECTSETTING 


```

## -parameters

### -param DriverGlobals: 
### -param UsbInterface: 
### -param PipesAttributes: 
### -param Params: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also