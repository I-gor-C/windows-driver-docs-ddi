---
UID: NS.ntddndis._NDIS_GFT_WILDCARD_MATCH_FLOW_ENTRY
title: NDIS_GFT_WILDCARD_MATCH_FLOW_ENTRY
author: windows-driver-content
description: 
ms.assetid: cae54404-21fe-48a2-815e-ae5fa281363c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_GFT_WILDCARD_MATCH_FLOW_ENTRY, NDIS_GFT_WILDCARD_MATCH_FLOW_ENTRY, *PNDIS_GFT_WILDCARD_MATCH_FLOW_ENTRY
req.header: ntddndis.h
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

# NDIS_GFT_WILDCARD_MATCH_FLOW_ENTRY structure

## -description



## -struct-fields

### -field union CounterValueBuffer			
 	
### -field __unnamed_union_0ae9_63 __unnamed_union_0ae9_63			
 	
### -field NDIS_OBJECT_HEADER Header			
 	
### -field ULONG Flags			
 	
### -field NDIS_GFT_TABLE_ID TableId			
 	
### -field NDIS_NIC_SWITCH_VPORT_ID VPortId			
 	
### -field NDIS_GFP_PROFILE_ID MatchProfileId			
 	
### -field NDIS_STATUS MatchRequestStatus			
 	
### -field NDIS_STATUS ActionRequestStatus			
 	
### -field ULONG CounterFlags			
 	
### -field NDIS_GFT_COUNTER_UPDATE_FREQUENCY CounterUpdateFrequency			
 	
### -field NDIS_GFT_COUNTER_TYPE CounterType			
 	
### -field ULONG UpdatePeriod			
 	
### -field ULONG Priority			
 	
### -field NDIS_GFT_WILDCARD_ACTION Action			
 	
### -field NDIS_NIC_SWITCH_VPORT_ID RedirectionVPortId			
 	
### -field NDIS_NIC_SWITCH_VPORT_ID TtlIsOneRedirectionVPortId			
 	
### -field ULONG NumCounterObjects			
 	
### -field NDIS_GFT_COUNTER_ID [NDIS_GFT_MAX_COUNTER_OBJECTS_PER_FLOW_ENTRY] CounterIdArray			
 	
### -field NDIS_GFT_FLOW_ENTRY_CACHE_HINT CacheHint			
 	
### -field NDIS_GFT_FLOW_ENTRY_ID ClientFlowEntryId			
 	
### -field NDIS_GFT_FLOW_ENTRY_ID ProviderFlowEntryId			
 	
### -field NDIS_GFT_FLOW_ENTRY_STATE FlowState			
 	
### -field ULONG HeaderGroupWildcardMatchArrayOffset			
 	
### -field ULONG HeaderGroupWildcardMatchArrayNumElements			
 	
### -field ULONG HeaderGroupWildcardMatchArrayElementSize			
 	
### -field ULONG CustomActionOffset			
 	
### -field PNDIS_GFT_PACKET_COUNTER_VALUE PacketCounterAddress			
 	
### -field PNDIS_GFT_BYTE_COUNTER_VALUE ByteCounterAddress			
 	
### -field PNDIS_GFT_PACKET_AND_BYTE_COUNTER_VALUE PacketAndByteCounterAddress			
 	
## -remarks

## -see-also