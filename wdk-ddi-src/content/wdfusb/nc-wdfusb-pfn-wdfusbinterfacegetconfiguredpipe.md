---
UID: NC.wdfusb.PFN_WDFUSBINTERFACEGETCONFIGUREDPIPE
title: PFN_WDFUSBINTERFACEGETCONFIGUREDPIPE
author: windows-driver-content
description: 
ms.assetid: 3fa53253-fbdd-40b9-9070-cc6f93a69463
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

# PFN_WDFUSBINTERFACEGETCONFIGUREDPIPE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBINTERFACEGETCONFIGUREDPIPE PfnWdfusbinterfacegetconfiguredpipe; 

// Definition

WDFAPI PfnWdfusbinterfacegetconfiguredpipe 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBINTERFACE UsbInterface
	UCHAR PipeIndex
	PWDF_USB_PIPE_INFORMATION PipeInfo
)
{...}

PFN_WDFUSBINTERFACEGETCONFIGUREDPIPE 


```

## -parameters

### -param DriverGlobals: 
### -param UsbInterface: 
### -param PipeIndex: 
### -param PipeInfo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also