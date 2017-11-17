---
UID: NC.wdfdevice.PFN_WDFWDMDEVICEGETWDFDEVICEHANDLE
title: PFN_WDFWDMDEVICEGETWDFDEVICEHANDLE
author: windows-driver-content
description: 
ms.assetid: e5bc611e-7ca8-4463-bee7-fbe236786e89
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

# PFN_WDFWDMDEVICEGETWDFDEVICEHANDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWDMDEVICEGETWDFDEVICEHANDLE PfnWdfwdmdevicegetwdfdevicehandle; 

// Definition

WDFAPI PfnWdfwdmdevicegetwdfdevicehandle 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PDEVICE_OBJECT DeviceObject
)
{...}

PFN_WDFWDMDEVICEGETWDFDEVICEHANDLE 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceObject: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also