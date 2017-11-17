---
UID: NC.wdfusb.PFN_WDFUSBINTERFACEGETNUMENDPOINTS
title: PFN_WDFUSBINTERFACEGETNUMENDPOINTS
author: windows-driver-content
description: 
ms.assetid: ea236dca-8944-445f-a01c-1c92b60f0cbc
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

# PFN_WDFUSBINTERFACEGETNUMENDPOINTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBINTERFACEGETNUMENDPOINTS PfnWdfusbinterfacegetnumendpoints; 

// Definition

WDFAPI PfnWdfusbinterfacegetnumendpoints 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBINTERFACE UsbInterface
	UCHAR SettingIndex
)
{...}

PFN_WDFUSBINTERFACEGETNUMENDPOINTS 


```

## -parameters

### -param DriverGlobals: 
### -param UsbInterface: 
### -param SettingIndex: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also