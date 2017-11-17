---
UID: NC.wdfusb.PFN_WDFUSBINTERFACEGETDESCRIPTOR
title: PFN_WDFUSBINTERFACEGETDESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: d852ef05-1ec2-495a-b265-68da294e0476
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

# PFN_WDFUSBINTERFACEGETDESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBINTERFACEGETDESCRIPTOR PfnWdfusbinterfacegetdescriptor; 

// Definition

WDFAPI PfnWdfusbinterfacegetdescriptor 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBINTERFACE UsbInterface
	UCHAR SettingIndex
	PUSB_INTERFACE_DESCRIPTOR InterfaceDescriptor
)
{...}

PFN_WDFUSBINTERFACEGETDESCRIPTOR 


```

## -parameters

### -param DriverGlobals: 
### -param UsbInterface: 
### -param SettingIndex: 
### -param InterfaceDescriptor: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also