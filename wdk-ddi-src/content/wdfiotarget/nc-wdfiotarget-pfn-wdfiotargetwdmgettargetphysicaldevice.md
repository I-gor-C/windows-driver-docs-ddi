---
UID: NC.wdfiotarget.PFN_WDFIOTARGETWDMGETTARGETPHYSICALDEVICE
title: PFN_WDFIOTARGETWDMGETTARGETPHYSICALDEVICE
author: windows-driver-content
description: 
ms.assetid: fec080da-6d65-45f8-879c-7e3ee4abe6de
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

# PFN_WDFIOTARGETWDMGETTARGETPHYSICALDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETWDMGETTARGETPHYSICALDEVICE PfnWdfiotargetwdmgettargetphysicaldevice; 

// Definition

WDFAPI PfnWdfiotargetwdmgettargetphysicaldevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
)
{...}

PFN_WDFIOTARGETWDMGETTARGETPHYSICALDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also