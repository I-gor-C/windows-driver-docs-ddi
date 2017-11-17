---
UID: NS.windot11._DOT11_SEND_GO_NEGOTIATION_RESPONSE_PARAMETERS
title: DOT11_SEND_GO_NEGOTIATION_RESPONSE_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: eb453a7f-80ee-4f9b-90f4-ce9f38de6b38
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_SEND_GO_NEGOTIATION_RESPONSE_PARAMETERS, 
req.header: windot11.h
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

# DOT11_SEND_GO_NEGOTIATION_RESPONSE_PARAMETERS structure

## -description



## -struct-fields

### -field NDIS_OBJECT_HEADER Header			
 	
### -field DOT11_MAC_ADDRESS PeerDeviceAddress			
 	
### -field DOT11_DIALOG_TOKEN DialogToken			
 	
### -field PVOID RequestContext			
 	
### -field ULONG uSendTimeout			
 	
### -field DOT11_WFD_STATUS_CODE Status			
 	
### -field DOT11_WFD_GO_INTENT GroupOwnerIntent			
 	
### -field DOT11_WFD_CONFIGURATION_TIMEOUT MinimumConfigTimeout			
 	
### -field DOT11_MAC_ADDRESS IntendedInterfaceAddress			
 	
### -field DOT11_WFD_GROUP_CAPABILITY GroupCapability			
 	
### -field DOT11_WFD_GROUP_ID GroupID			
 	
### -field BOOLEAN bUseGroupID			
 	
### -field ULONG uIEsOffset			
 	
### -field ULONG uIEsLength			
 	
## -remarks

## -see-also