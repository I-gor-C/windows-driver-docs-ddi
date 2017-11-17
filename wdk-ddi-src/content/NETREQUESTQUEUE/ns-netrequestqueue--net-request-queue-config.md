---
UID: NS.netrequestqueue._NET_REQUEST_QUEUE_CONFIG
title: NET_REQUEST_QUEUE_CONFIG
author: windows-driver-content
description: 
ms.assetid: 42c1b680-f221-4e73-a33d-354071ae34f3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NET_REQUEST_QUEUE_CONFIG, NET_REQUEST_QUEUE_CONFIG, *PNET_REQUEST_QUEUE_CONFIG
req.header: netrequestqueue.h
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

# NET_REQUEST_QUEUE_CONFIG structure

## -description



## -struct-fields

### -field ULONG Size			
 	
### -field NETADAPTER Adapter			
 	
### -field NET_REQUEST_QUEUE_TYPE Type			
 	
### -field PFN_NET_REQUEST_DEFAULT_SET_DATA EvtRequestDefaultSetData			
 	
### -field PFN_NET_REQUEST_DEFAULT_QUERY_DATA EvtRequestDefaultQueryData			
 	
### -field PFN_NET_REQUEST_DEFAULT_METHOD EvtRequestDefaultMethod			
 	
### -field PFN_NET_REQUEST_DEFAULT EvtRequestDefault			
 	
### -field NET_REQUEST_QUEUE_ADD_HANDLER_ERROR AddHandlerError			
 	
### -field ULONG SizeOfSetDataHandler			
 	
### -field ULONG SizeOfQueryDataHandler			
 	
### -field ULONG SizeOfMethodHandler			
 	
### -field PNET_REQUEST_QUEUE_SET_DATA_HANDLER SetDataHandlers			
 	
### -field PNET_REQUEST_QUEUE_QUERY_DATA_HANDLER QueryDataHandlers			
 	
### -field PNET_REQUEST_QUEUE_METHOD_HANDLER MethodHandlers			
 	
## -remarks

## -see-also