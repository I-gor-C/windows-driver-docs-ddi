---
UID: NC.wdfcontrol.PFN_WDFCONTROLDEVICEINITSETSHUTDOWNNOTIFICATION
title: PFN_WDFCONTROLDEVICEINITSETSHUTDOWNNOTIFICATION
author: windows-driver-content
description: 
ms.assetid: 74fbac88-57ae-48f5-abc9-6d76dbf583fc
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcontrol.h
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

# PFN_WDFCONTROLDEVICEINITSETSHUTDOWNNOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCONTROLDEVICEINITSETSHUTDOWNNOTIFICATION PfnWdfcontroldeviceinitsetshutdownnotification; 

// Definition

WDFAPI PfnWdfcontroldeviceinitsetshutdownnotification 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PFN_WDF_DEVICE_SHUTDOWN_NOTIFICATION Notification
	UCHAR Flags
)
{...}

PFN_WDFCONTROLDEVICEINITSETSHUTDOWNNOTIFICATION 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param Notification: 
### -param Flags: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also