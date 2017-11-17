---
UID: NS.ndis._NDIS_CLIENT_CHARACTERISTICS
title: NDIS_CLIENT_CHARACTERISTICS
author: windows-driver-content
description: 
ms.assetid: 2921dd9d-e124-4520-8ece-ea0a1a94b5d1
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_CLIENT_CHARACTERISTICS, NDIS_CLIENT_CHARACTERISTICS, *PNDIS_CLIENT_CHARACTERISTICS
req.header: ndis.h
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

# NDIS_CLIENT_CHARACTERISTICS structure

## -description



## -struct-fields

### -field UCHAR MajorVersion			
 	
### -field UCHAR MinorVersion			
 	
### -field USHORT Filler			
 	
### -field UINT Reserved			
 	
### -field CO_CREATE_VC_HANDLER ClCreateVcHandler			
 	
### -field CO_DELETE_VC_HANDLER ClDeleteVcHandler			
 	
### -field CO_REQUEST_HANDLER ClRequestHandler			
 	
### -field CO_REQUEST_COMPLETE_HANDLER ClRequestCompleteHandler			
 	
### -field CL_OPEN_AF_COMPLETE_HANDLER ClOpenAfCompleteHandler			
 	
### -field CL_CLOSE_AF_COMPLETE_HANDLER ClCloseAfCompleteHandler			
 	
### -field CL_REG_SAP_COMPLETE_HANDLER ClRegisterSapCompleteHandler			
 	
### -field CL_DEREG_SAP_COMPLETE_HANDLER ClDeregisterSapCompleteHandler			
 	
### -field CL_MAKE_CALL_COMPLETE_HANDLER ClMakeCallCompleteHandler			
 	
### -field CL_MODIFY_CALL_QOS_COMPLETE_HANDLER ClModifyCallQoSCompleteHandler			
 	
### -field CL_CLOSE_CALL_COMPLETE_HANDLER ClCloseCallCompleteHandler			
 	
### -field CL_ADD_PARTY_COMPLETE_HANDLER ClAddPartyCompleteHandler			
 	
### -field CL_DROP_PARTY_COMPLETE_HANDLER ClDropPartyCompleteHandler			
 	
### -field CL_INCOMING_CALL_HANDLER ClIncomingCallHandler			
 	
### -field CL_INCOMING_CALL_QOS_CHANGE_HANDLER ClIncomingCallQoSChangeHandler			
 	
### -field CL_INCOMING_CLOSE_CALL_HANDLER ClIncomingCloseCallHandler			
 	
### -field CL_INCOMING_DROP_PARTY_HANDLER ClIncomingDropPartyHandler			
 	
### -field CL_CALL_CONNECTED_HANDLER ClCallConnectedHandler			
 	
## -remarks

## -see-also