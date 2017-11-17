---
UID: NS.ntddnlb._SEND_RECEIVE_HOOK_INFO
title: SEND_RECEIVE_HOOK_INFO
author: windows-driver-content
description: 
ms.assetid: f817a102-fe73-408d-8b54-fc37efe28276
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SEND_RECEIVE_HOOK_INFO, SEND_RECEIVE_HOOK_INFO, *PSEND_RECEIVE_HOOK_INFO
req.header: ntddnlb.h
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

# SEND_RECEIVE_HOOK_INFO structure

## -description



## -struct-fields

### -field NLB_HOOK_API_VERSION Version			
 	
### -field const WCHAR * pAdapter			
 	
### -field IF_INDEX IFIndex			
 	
### -field const NET_BUFFER * pPacket			
 	
### -field const UCHAR * pMediaHeader			
 	
### -field ULONG cMediaHeaderLength			
 	
### -field const UCHAR * pPayload			
 	
### -field ULONG cPayloadLength			
 	
### -field ULONG Flags			
 	
### -field VOID * Reserved			
 	
### -field NLB_HOOK_IP_TUPLE NewTuple			
 	
## -remarks

## -see-also