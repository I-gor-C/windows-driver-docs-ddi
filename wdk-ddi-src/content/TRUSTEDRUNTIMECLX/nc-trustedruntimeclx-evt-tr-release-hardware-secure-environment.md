---
UID: NC.trustedruntimeclx.EVT_TR_RELEASE_HARDWARE_SECURE_ENVIRONMENT
title: EVT_TR_RELEASE_HARDWARE_SECURE_ENVIRONMENT
author: windows-driver-content
description: 
ms.assetid: cb5316d0-50b0-4383-a6fa-ede8ec02d87f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: trustedruntimeclx.h
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

# EVT_TR_RELEASE_HARDWARE_SECURE_ENVIRONMENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_TR_RELEASE_HARDWARE_SECURE_ENVIRONMENT EvtTrReleaseHardwareSecureEnvironment; 

// Definition

NTSTATUS EvtTrReleaseHardwareSecureEnvironment 
(
	WDFDEVICE MasterDevice
	WDFCMRESLIST TranslatedResources
)
{...}

EVT_TR_RELEASE_HARDWARE_SECURE_ENVIRONMENT PFN_TR_RELEASE_HARDWARE_SECURE_ENVIRONMENT


```

## -parameters

### -param MasterDevice: 
### -param TranslatedResources: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also