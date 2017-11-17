---
UID: NC.wdfpdo.PFN_WDFPDOINITASSIGNCONTAINERID
title: PFN_WDFPDOINITASSIGNCONTAINERID
author: windows-driver-content
description: 
ms.assetid: c3abf930-68db-41f7-bcba-c75aeee5a4ca
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfpdo.h
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

# PFN_WDFPDOINITASSIGNCONTAINERID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOINITASSIGNCONTAINERID PfnWdfpdoinitassigncontainerid; 

// Definition

WDFAPI PfnWdfpdoinitassigncontainerid 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PCUNICODE_STRING ContainerID
)
{...}

PFN_WDFPDOINITASSIGNCONTAINERID 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param ContainerID: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also