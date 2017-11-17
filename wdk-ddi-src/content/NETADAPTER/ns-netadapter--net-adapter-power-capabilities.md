---
UID: NS.netadapter._NET_ADAPTER_POWER_CAPABILITIES
title: NET_ADAPTER_POWER_CAPABILITIES
author: windows-driver-content
description: 
ms.assetid: c6abc696-9249-43f7-b500-cc553b08d671
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NET_ADAPTER_POWER_CAPABILITIES, NET_ADAPTER_POWER_CAPABILITIES, *PNET_ADAPTER_POWER_CAPABILITIES
req.header: netadapter.h
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

# NET_ADAPTER_POWER_CAPABILITIES structure

## -description



## -struct-fields

### -field ULONG Size			
 	
### -field NET_ADAPTER_POWER_FLAGS Flags			
 	
### -field NET_ADAPTER_WAKE_PATTERN_FLAGS SupportedWakePatterns			
 	
### -field ULONG NumTotalWakePatterns			
 	
### -field ULONG MaxWakePatternSize			
 	
### -field ULONG MaxWakePatternOffset			
 	
### -field ULONG MaxWakePacketSaveBuffer			
 	
### -field NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS SupportedProtocolOffloads			
 	
### -field ULONG NumArpOffloadIPv4Addresses			
 	
### -field ULONG NumNSOffloadIPv6Addresses			
 	
### -field NET_ADAPTER_WAKEUP_EVENTS_FLAGS SupportedWakeUpEvents			
 	
### -field NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS SupportedMediaSpecificWakeUpEvents			
 	
### -field PFN_NET_ADAPTER_PREVIEW_WAKE_PATTERN EvtAdapterPreviewWakePattern			
 	
### -field PFN_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD EvtAdapterPreviewProtocolOffload			
 	
### -field WDF_TRI_STATE ManageS0IdlePowerReferences			
 	
## -remarks

## -see-also