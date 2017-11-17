---
UID: NS.tlvgenerated_._WDI_SET_P2P_START_BACKGROUND_DISCOVERY_PARAMETERS
title: WDI_SET_P2P_START_BACKGROUND_DISCOVERY_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: 8e7feaae-d8cf-4b10-b05f-1d359959849e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: WDI_SET_P2P_START_BACKGROUND_DISCOVERY_PARAMETERS, WDI_SET_P2P_START_BACKGROUND_DISCOVERY_PARAMETERS, *PWDI_SET_P2P_START_BACKGROUND_DISCOVERY_PARAMETERS
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

# WDI_SET_P2P_START_BACKGROUND_DISCOVERY_PARAMETERS structure

## -description



## -struct-fields

### -field struct Optional			
 	
### -field _WDI_SET_P2P_START_BACKGROUND_DISCOVERY_PARAMETERS_Optional _WDI_SET_P2P_START_BACKGROUND_DISCOVERY_PARAMETERS_Optional			
 	
### -field struct DiscoveryChannelSettings			
 	
### -field ArrayOfElementsOfWDI_P2P_DISCOVERY_CHANNEL_SETTINGS_CONTAINER ArrayOfElementsOfWDI_P2P_DISCOVERY_CHANNEL_SETTINGS_CONTAINER			
 	
### -field struct ServiceNameHash			
 	
### -field ArrayOfElementsOfWDI_P2P_SERVICE_NAME_HASH_CONTAINER ArrayOfElementsOfWDI_P2P_SERVICE_NAME_HASH_CONTAINER			
 	
### -field WDI_P2P_BACKGROUND_DISCOVER_MODE_CONTAINER DiscoverMode			
 	
### -field ArrayOfElements<WDI_P2P_DISCOVERY_CHANNEL_SETTINGS_CONTAINER> DiscoveryChannelSettings			
 	
### -field WDI_ADDRESS_LIST_CONTAINER DeviceFilterList			
 	
### -field ArrayOfElements<WDI_P2P_SERVICE_NAME_HASH_CONTAINER> ServiceNameHash			
 	
### -field WDI_BYTE_BLOB VendorIEs			
 	
## -remarks

## -see-also