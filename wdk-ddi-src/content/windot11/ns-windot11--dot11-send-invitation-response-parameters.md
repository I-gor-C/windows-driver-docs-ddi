---
UID: NS.windot11._DOT11_SEND_INVITATION_RESPONSE_PARAMETERS
title: DOT11_SEND_INVITATION_RESPONSE_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: fcd63d4b-7dcd-4a98-8f1e-2eb59563804c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_SEND_INVITATION_RESPONSE_PARAMETERS, 
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

# DOT11_SEND_INVITATION_RESPONSE_PARAMETERS structure

## -description



## -struct-fields

### -field NDIS_OBJECT_HEADER Header			
 	
### -field DOT11_MAC_ADDRESS ReceiverDeviceAddress			
 	
### -field DOT11_DIALOG_TOKEN DialogToken			
 	
### -field PVOID RequestContext			
 	
### -field ULONG uSendTimeout			
 	
### -field DOT11_WFD_STATUS_CODE Status			
 	
### -field DOT11_WFD_CONFIGURATION_TIMEOUT MinimumConfigTimeout			
 	
### -field DOT11_MAC_ADDRESS GroupBSSID			
 	
### -field BOOLEAN bUseGroupBSSID			
 	
### -field DOT11_WFD_CHANNEL OperatingChannel			
 	
### -field BOOLEAN bUseSpecifiedOperatingChannel			
 	
### -field ULONG uIEsOffset			
 	
### -field ULONG uIEsLength			
 	
## -remarks

## -see-also