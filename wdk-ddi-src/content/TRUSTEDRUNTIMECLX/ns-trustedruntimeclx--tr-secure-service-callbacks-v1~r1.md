---
UID: NS.trustedruntimeclx._TR_SECURE_SERVICE_CALLBACKS_V1~r1
title: TR_SECURE_SERVICE_CALLBACKS_V1
author: windows-driver-content
description: 
ms.assetid: 61aee53a-1753-45cf-a489-62b5085b5a5f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: TR_SECURE_SERVICE_CALLBACKS_V1, 
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

# TR_SECURE_SERVICE_CALLBACKS_V1 structure

## -description



## -struct-fields

### -field ULONG Flags			
 	
### -field PFN_TR_CREATE_SECURE_SERVICE_CONTEXT EvtTrCreateSecureServiceContext			
 	
### -field PFN_TR_DESTROY_SECURE_SERVICE_CONTEXT EvtTrDestroySecureServiceContext			
 	
### -field PFN_TR_CONNECT_SECURE_SERVICE EvtTrConnectSecureService			
 	
### -field PFN_TR_DISCONNECT_SECURE_SERVICE EvtTrDisconnectSecureService			
 	
### -field PFN_TR_CREATE_SECURE_SERVICE_SESSION_CONTEXT EvtTrCreateSecureSessionContext			
 	
### -field PFN_TR_DESTROY_SECURE_SERVICE_SESSION_CONTEXT EvtTrDestroySecureSessionContext			
 	
### -field PFN_TR_PROCESS_SECURE_SERVICE_REQUEST EvtTrProcessSecureServiceRequest			
 	
### -field PFN_TR_CANCEL_SECURE_SERVICE_REQUEST EvtTrCancelSecureServiceRequest			
 	
### -field PFN_TR_PROCESS_OTHER_SECURE_SERVICE_IO EvtTrProcessOtherSecureServiceIo			
 	
## -remarks

## -see-also