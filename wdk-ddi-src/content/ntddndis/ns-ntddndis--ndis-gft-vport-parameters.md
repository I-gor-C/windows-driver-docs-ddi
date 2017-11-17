---
UID: NS.ntddndis._NDIS_GFT_VPORT_PARAMETERS
title: NDIS_GFT_VPORT_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: c723b2c0-235b-4e3e-9afb-b28468ddd0dc
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_GFT_VPORT_PARAMETERS, NDIS_GFT_VPORT_PARAMETERS, *PNDIS_GFT_VPORT_PARAMETERS
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

# NDIS_GFT_VPORT_PARAMETERS structure

## -description



## -struct-fields

### -field NDIS_OBJECT_HEADER Header			
 	
### -field ULONG Flags			
 	
### -field NDIS_NIC_SWITCH_VPORT_ID VPortId			
 	
### -field NDIS_NIC_SWITCH_VPORT_ID ExceptionVPortId			
 	
### -field ULONG SamplingRate			
 	
### -field ULONG64 DscpMask			
 	
### -field ULONG NumDscpMaskCounterObjects			
 	
### -field NDIS_GFT_COUNTER_ID [NDIS_GFT_VPORT_MAX_DSCP_MASK_COUNTER_OBJECTS] DscpMaskCounterIdArray			
 	
### -field ULONG64 PriorityMask			
 	
### -field ULONG NumPriorityMaskCounterObjects			
 	
### -field NDIS_GFT_COUNTER_ID [NDIS_GFT_VPORT_MAX_PRIORITY_MASK_COUNTER_OBJECTS] PriorityMaskCounterIdArray			
 	
### -field USHORT VxLanSrcPortBase			
 	
### -field USHORT VxLanSrcPortRange			
 	
### -field ULONG DscpFlags			
 	
## -remarks

## -see-also