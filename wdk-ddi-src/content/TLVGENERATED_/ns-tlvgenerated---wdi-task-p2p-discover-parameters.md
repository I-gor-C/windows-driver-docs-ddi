---
UID: NS.tlvgenerated_._WDI_TASK_P2P_DISCOVER_PARAMETERS
title: WDI_TASK_P2P_DISCOVER_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: 4cd39899-6082-40f4-b3f8-4228e96612d8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: WDI_TASK_P2P_DISCOVER_PARAMETERS, WDI_TASK_P2P_DISCOVER_PARAMETERS, *PWDI_TASK_P2P_DISCOVER_PARAMETERS
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

# WDI_TASK_P2P_DISCOVER_PARAMETERS structure

## -description



## -struct-fields

### -field struct Optional			
 	
### -field _WDI_TASK_P2P_DISCOVER_PARAMETERS_Optional _WDI_TASK_P2P_DISCOVER_PARAMETERS_Optional			
 	
### -field struct DiscoveryChannelSettings			
 	
### -field ArrayOfElementsOfWDI_P2P_DISCOVERY_CHANNEL_SETTINGS_CONTAINER ArrayOfElementsOfWDI_P2P_DISCOVERY_CHANNEL_SETTINGS_CONTAINER			
 	
### -field struct SSIDList			
 	
### -field ArrayOfElementsOfWDI_SSID ArrayOfElementsOfWDI_SSID			
 	
### -field struct ServiceNameHash			
 	
### -field ArrayOfElementsOfWDI_P2P_SERVICE_NAME_HASH_CONTAINER ArrayOfElementsOfWDI_P2P_SERVICE_NAME_HASH_CONTAINER			
 	
### -field struct ServiceInformationDiscoveryEntry			
 	
### -field ArrayOfElementsOfWDI_P2P_SERVICE_INFORMATION_DISCOVERY_ENTRY_CONTAINER ArrayOfElementsOfWDI_P2P_SERVICE_INFORMATION_DISCOVERY_ENTRY_CONTAINER			
 	
### -field member_function _WDI_TASK_P2P_DISCOVER_PARAMETERS			
 	
### -field WDI_P2P_DISCOVER_MODE_CONTAINER DiscoverMode			
 	
### -field WDI_SCAN_DWELL_TIME_CONTAINER DwellTime			
 	
### -field ArrayOfElements<WDI_P2P_DISCOVERY_CHANNEL_SETTINGS_CONTAINER> DiscoveryChannelSettings			
 	
### -field ArrayOfElements<WDI_SSID> SSIDList			
 	
### -field ArrayOfElements<WDI_P2P_SERVICE_NAME_HASH_CONTAINER> ServiceNameHash			
 	
### -field WDI_BYTE_BLOB VendorIEs			
 	
### -field ArrayOfElements<WDI_P2P_SERVICE_INFORMATION_DISCOVERY_ENTRY_CONTAINER> ServiceInformationDiscoveryEntry			
 	
### -field BOOL_CONTAINER bIncludeListenChannel			
 	
## -remarks

## -see-also