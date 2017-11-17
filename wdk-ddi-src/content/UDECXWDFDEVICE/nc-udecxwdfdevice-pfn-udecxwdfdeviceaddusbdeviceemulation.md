---
UID: NC.udecxwdfdevice.PFN_UDECXWDFDEVICEADDUSBDEVICEEMULATION
title: *PFN_UDECXWDFDEVICEADDUSBDEVICEEMULATION
author: windows-driver-content
description: 
ms.assetid: a0003db3-4591-479c-a513-99b57c18c9db
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxwdfdevice.h
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

# *PFN_UDECXWDFDEVICEADDUSBDEVICEEMULATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXWDFDEVICEADDUSBDEVICEEMULATION *PfnUdecxwdfdeviceaddusbdeviceemulation; 

// Definition

NTSTATUS *PfnUdecxwdfdeviceaddusbdeviceemulation 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE WdfDevice
	PUDECX_WDF_DEVICE_CONFIG Config
)
{...}

*PFN_UDECXWDFDEVICEADDUSBDEVICEEMULATION 


```

## -parameters

### -param DriverGlobals: 
### -param WdfDevice: 
### -param Config: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also