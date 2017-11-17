---
UID: NC.wdfusb.PFN_WDFUSBINTERFACEGETENDPOINTINFORMATION
title: PFN_WDFUSBINTERFACEGETENDPOINTINFORMATION
author: windows-driver-content
description: 
ms.assetid: 79edd733-fffc-4548-908b-0e3b67b854f1
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

# PFN_WDFUSBINTERFACEGETENDPOINTINFORMATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBINTERFACEGETENDPOINTINFORMATION PfnWdfusbinterfacegetendpointinformation; 

// Definition

WDFAPI PfnWdfusbinterfacegetendpointinformation 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBINTERFACE UsbInterface
	UCHAR SettingIndex
	UCHAR EndpointIndex
	PWDF_USB_PIPE_INFORMATION EndpointInfo
)
{...}

PFN_WDFUSBINTERFACEGETENDPOINTINFORMATION 


```

## -parameters

### -param DriverGlobals: 
### -param UsbInterface: 
### -param SettingIndex: 
### -param EndpointIndex: 
### -param EndpointInfo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also