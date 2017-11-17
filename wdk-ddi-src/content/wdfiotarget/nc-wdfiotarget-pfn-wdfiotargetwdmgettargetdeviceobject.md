---
UID: NC.wdfiotarget.PFN_WDFIOTARGETWDMGETTARGETDEVICEOBJECT
title: PFN_WDFIOTARGETWDMGETTARGETDEVICEOBJECT
author: windows-driver-content
description: 
ms.assetid: 40284ff0-ddc7-4792-a27c-898f767268e7
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfiotarget.h
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

# PFN_WDFIOTARGETWDMGETTARGETDEVICEOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETWDMGETTARGETDEVICEOBJECT PfnWdfiotargetwdmgettargetdeviceobject; 

// Definition

WDFAPI PfnWdfiotargetwdmgettargetdeviceobject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
)
{...}

PFN_WDFIOTARGETWDMGETTARGETDEVICEOBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also