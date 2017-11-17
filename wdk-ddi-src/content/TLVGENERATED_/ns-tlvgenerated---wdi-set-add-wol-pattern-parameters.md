---
UID: NS.tlvgenerated_._WDI_SET_ADD_WOL_PATTERN_PARAMETERS
title: WDI_SET_ADD_WOL_PATTERN_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: 3a2f511e-d3a1-4930-bf7c-91792a211dff
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: WDI_SET_ADD_WOL_PATTERN_PARAMETERS, WDI_SET_ADD_WOL_PATTERN_PARAMETERS, *PWDI_SET_ADD_WOL_PATTERN_PARAMETERS
req.header: tlvgenerated_.hpp
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

# WDI_SET_ADD_WOL_PATTERN_PARAMETERS structure

## -description



## -struct-fields

### -field struct Optional			
 	
### -field _WDI_SET_ADD_WOL_PATTERN_PARAMETERS_Optional _WDI_SET_ADD_WOL_PATTERN_PARAMETERS_Optional			
 	
### -field struct WakePacketPattern			
 	
### -field ArrayOfElementsOfWDI_PACKET_PATTERN_CONTAINER ArrayOfElementsOfWDI_PACKET_PATTERN_CONTAINER			
 	
### -field struct WakePacketIpv4TcpSync			
 	
### -field ArrayOfElementsOfWDI_IPv4_TCP_SYNC_CONTAINER ArrayOfElementsOfWDI_IPv4_TCP_SYNC_CONTAINER			
 	
### -field struct WakePacketIpv6TcpSync			
 	
### -field ArrayOfElementsOfWDI_IPv6TCP_SYNC_CONTAINER ArrayOfElementsOfWDI_IPv6TCP_SYNC_CONTAINER			
 	
### -field member_function _WDI_SET_ADD_WOL_PATTERN_PARAMETERS			
 	
### -field ArrayOfElements<WDI_PACKET_PATTERN_CONTAINER> WakePacketPattern			
 	
### -field UINT32_CONTAINER WakePacketMagicPacketPatternId			
 	
### -field ArrayOfElements<WDI_IPv4_TCP_SYNC_CONTAINER> WakePacketIpv4TcpSync			
 	
### -field ArrayOfElements<WDI_IPv6TCP_SYNC_CONTAINER> WakePacketIpv6TcpSync			
 	
### -field UINT32_CONTAINER WakePacketEapolRequestIdPatternId			
 	
## -remarks

## -see-also