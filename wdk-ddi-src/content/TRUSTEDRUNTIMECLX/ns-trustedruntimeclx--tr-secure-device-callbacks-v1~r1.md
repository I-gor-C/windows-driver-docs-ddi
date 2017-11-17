---
UID: NS.trustedruntimeclx._TR_SECURE_DEVICE_CALLBACKS_V1~r1
title: TR_SECURE_DEVICE_CALLBACKS_V1
author: windows-driver-content
description: 
ms.assetid: 0a20c8c2-0de2-4d7f-b4c5-29aa734c2f62
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: TR_SECURE_DEVICE_CALLBACKS_V1, 
req.header: trustedruntimeclx.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
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

# TR_SECURE_DEVICE_CALLBACKS_V1 structure

## -description



## -struct-fields

### -field ULONG Flags			
 	
### -field PFN_TR_CREATE_SECURE_DEVICE_CONTEXT EvtTrCreateSecureDeviceContext			
 	
### -field PFN_TR_DESTROY_SECURE_DEVICE_CONTEXT EvtTrDestroySecureDeviceContext			
 	
### -field PFN_TR_PREPARE_HARDWARE_SECURE_ENVIRONMENT EvtTrPrepareHardwareSecureEnvironment			
 	
### -field PFN_TR_RELEASE_HARDWARE_SECURE_ENVIRONMENT EvtTrReleaseHardwareSecureEnvironment			
 	
### -field PFN_TR_CONNECT_SECURE_ENVIRONMENT EvtTrConnectSecureEnvironment			
 	
### -field PFN_TR_DISCONNECT_SECURE_ENVIRONMENT EvtTrDisconnectSecureEnvironment			
 	
### -field PFN_TR_ENUMERATE_SECURE_SERVICES EvtTrEnumerateSecureServices			
 	
### -field PFN_TR_PROCESS_OTHER_DEVICE_IO EvtTrProcessOtherDeviceIo			
 	
### -field PFN_TR_QUERY_SERVICE_CALLBACKS EvtTrQueryServiceCallbacks			
 	
## -remarks

## -see-also