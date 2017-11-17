---
UID: NC.sensorscx.PFN_SENSORSCXDEVICEGETSENSORLIST
title: *PFN_SENSORSCXDEVICEGETSENSORLIST
author: windows-driver-content
description: 
ms.assetid: 6e2fcb66-87ef-4eec-9c94-02d02ceb8f53
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sensorscx.h
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

# *PFN_SENSORSCXDEVICEGETSENSORLIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_SENSORSCXDEVICEGETSENSORLIST *PfnSensorscxdevicegetsensorlist; 

// Definition

NTSTATUS *PfnSensorscxdevicegetsensorlist 
(
	PSENSORSCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE FxDevice
	SENSOROBJECT *pSensorList
	PULONG pListCount
)
{...}

*PFN_SENSORSCXDEVICEGETSENSORLIST 


```

## -parameters

### -param DriverGlobals: 
### -param FxDevice: 
### -param *pSensorList: 
### -param pListCount: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also