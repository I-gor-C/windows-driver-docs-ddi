---
UID: NC.trustedruntimeclx.EVT_TR_PREPARE_HARDWARE_SECURE_ENVIRONMENT
title: EVT_TR_PREPARE_HARDWARE_SECURE_ENVIRONMENT
author: windows-driver-content
description: 
ms.assetid: 7186bbcf-87bf-4d38-89c8-7868d6074c20
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

# EVT_TR_PREPARE_HARDWARE_SECURE_ENVIRONMENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_TR_PREPARE_HARDWARE_SECURE_ENVIRONMENT EvtTrPrepareHardwareSecureEnvironment; 

// Definition

NTSTATUS EvtTrPrepareHardwareSecureEnvironment 
(
	WDFDEVICE MasterDevice
	WDFCMRESLIST RawResources
	WDFCMRESLIST TranslatedResources
)
{...}

EVT_TR_PREPARE_HARDWARE_SECURE_ENVIRONMENT PFN_TR_PREPARE_HARDWARE_SECURE_ENVIRONMENT


```

## -parameters

### -param MasterDevice: 
### -param RawResources: 
### -param TranslatedResources: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also