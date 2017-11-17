---
UID: NC.wdfdevice.PFN_WDFDEVICEINITASSIGNWDMIRPPREPROCESSCALLBACK
title: PFN_WDFDEVICEINITASSIGNWDMIRPPREPROCESSCALLBACK
author: windows-driver-content
description: 
ms.assetid: 5b4dc211-5363-4c67-8180-f1b4b7715b02
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdevice.h
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

# PFN_WDFDEVICEINITASSIGNWDMIRPPREPROCESSCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITASSIGNWDMIRPPREPROCESSCALLBACK PfnWdfdeviceinitassignwdmirppreprocesscallback; 

// Definition

WDFAPI PfnWdfdeviceinitassignwdmirppreprocesscallback 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PFN_WDFDEVICE_WDM_IRP_PREPROCESS EvtDeviceWdmIrpPreprocess
	UCHAR MajorFunction
	PUCHAR MinorFunctions
	ULONG NumMinorFunctions
)
{...}

PFN_WDFDEVICEINITASSIGNWDMIRPPREPROCESSCALLBACK 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param EvtDeviceWdmIrpPreprocess: 
### -param MajorFunction: 
### -param MinorFunctions: 
### -param NumMinorFunctions: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also