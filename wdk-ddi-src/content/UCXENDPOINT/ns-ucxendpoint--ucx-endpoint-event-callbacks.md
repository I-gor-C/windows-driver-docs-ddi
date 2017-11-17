---
UID: NS.ucxendpoint._UCX_ENDPOINT_EVENT_CALLBACKS
title: UCX_ENDPOINT_EVENT_CALLBACKS
author: windows-driver-content
description: 
ms.assetid: fc9fc6e3-dfc6-4e61-953e-92c117c258ee
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: UCX_ENDPOINT_EVENT_CALLBACKS, UCX_ENDPOINT_EVENT_CALLBACKS, *PUCX_ENDPOINT_EVENT_CALLBACKS
req.header: ucxendpoint.h
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

# UCX_ENDPOINT_EVENT_CALLBACKS structure

## -description



## -struct-fields

### -field ULONG Size			
 	
### -field PFN_UCX_ENDPOINT_PURGE EvtEndpointPurge			
 	
### -field PFN_UCX_ENDPOINT_START EvtEndpointStart			
 	
### -field PFN_UCX_ENDPOINT_ABORT EvtEndpointAbort			
 	
### -field PFN_UCX_ENDPOINT_RESET EvtEndpointReset			
 	
### -field PFN_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS EvtEndpointOkToCancelTransfers			
 	
### -field PFN_UCX_ENDPOINT_STATIC_STREAMS_ADD EvtEndpointStaticStreamsAdd			
 	
### -field PFN_UCX_ENDPOINT_STATIC_STREAMS_ENABLE EvtEndpointStaticStreamsEnable			
 	
### -field PFN_UCX_ENDPOINT_STATIC_STREAMS_DISABLE EvtEndpointStaticStreamsDisable			
 	
### -field HANDLE Reserved1			
 	
### -field PFN_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS EvtEndpointGetIsochTransferPathDelays			
 	
### -field PFN_UCX_ENDPOINT_SET_CHARACTERISTIC EvtEndpointSetCharacteristic			
 	
## -remarks

## -see-also