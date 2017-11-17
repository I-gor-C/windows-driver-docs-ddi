---
UID: NS.windot11._DOT11_SEND_INVITATION_REQUEST_PARAMETERS
title: DOT11_SEND_INVITATION_REQUEST_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: 55ff2791-a4c9-43ba-82c2-c43425c44ea2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_SEND_INVITATION_REQUEST_PARAMETERS, 
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

# DOT11_SEND_INVITATION_REQUEST_PARAMETERS structure

## -description



## -struct-fields

### -field NDIS_OBJECT_HEADER Header			
 	
### -field DOT11_DIALOG_TOKEN DialogToken			
 	
### -field DOT11_MAC_ADDRESS PeerDeviceAddress			
 	
### -field ULONG uSendTimeout			
 	
### -field DOT11_WFD_CONFIGURATION_TIMEOUT MinimumConfigTimeout			
 	
### -field DOT11_WFD_INVITATION_FLAGS InvitationFlags			
 	
### -field DOT11_MAC_ADDRESS GroupBSSID			
 	
### -field BOOLEAN bUseGroupBSSID			
 	
### -field DOT11_WFD_CHANNEL OperatingChannel			
 	
### -field BOOLEAN bUseSpecifiedOperatingChannel			
 	
### -field DOT11_WFD_GROUP_ID GroupID			
 	
### -field BOOLEAN bLocalGO			
 	
### -field ULONG uIEsOffset			
 	
### -field ULONG uIEsLength			
 	
## -remarks

## -see-also