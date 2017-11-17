---
UID: NS.wudfwdm._PO_FX_DEVICE_V2
title: PO_FX_DEVICE_V2
author: windows-driver-content
description: 
ms.assetid: a1020295-c081-4578-81f4-eb9051c64b23
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PO_FX_DEVICE_V2, PO_FX_DEVICE_V2, *PPO_FX_DEVICE_V2
req.header: wudfwdm.h
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

# PO_FX_DEVICE_V2 structure

## -description



## -struct-fields

### -field ULONG Version			
 	
### -field ULONGLONG Flags			
 	
### -field PPO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK ComponentActiveConditionCallback			
 	
### -field PPO_FX_COMPONENT_IDLE_CONDITION_CALLBACK ComponentIdleConditionCallback			
 	
### -field PPO_FX_COMPONENT_IDLE_STATE_CALLBACK ComponentIdleStateCallback			
 	
### -field PPO_FX_DEVICE_POWER_REQUIRED_CALLBACK DevicePowerRequiredCallback			
 	
### -field PPO_FX_DEVICE_POWER_NOT_REQUIRED_CALLBACK DevicePowerNotRequiredCallback			
 	
### -field PPO_FX_POWER_CONTROL_CALLBACK PowerControlCallback			
 	
### -field PVOID DeviceContext			
 	
### -field ULONG ComponentCount			
 	
### -field PO_FX_COMPONENT_V2 [ANYSIZE_ARRAY] Components			
 	
## -remarks

## -see-also