---
UID: NC.wdffdo.PFN_WDFFDOLOCKSTATICCHILDLISTFORITERATION
title: PFN_WDFFDOLOCKSTATICCHILDLISTFORITERATION
author: windows-driver-content
description: 
ms.assetid: f855c001-c140-4372-945e-cac92275d09f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdffdo.h
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

# PFN_WDFFDOLOCKSTATICCHILDLISTFORITERATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDOLOCKSTATICCHILDLISTFORITERATION PfnWdffdolockstaticchildlistforiteration; 

// Definition

WDFAPI PfnWdffdolockstaticchildlistforiteration 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Fdo
)
{...}

PFN_WDFFDOLOCKSTATICCHILDLISTFORITERATION 


```

## -parameters

### -param DriverGlobals: 
### -param Fdo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also