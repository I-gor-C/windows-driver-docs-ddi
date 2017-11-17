---
UID: NS.ntddk._XSTATE_CONFIGURATION
title: XSTATE_CONFIGURATION
author: windows-driver-content
description: 
ms.assetid: 202d275a-9d5f-4ba2-af0f-7d4530899117
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: XSTATE_CONFIGURATION, XSTATE_CONFIGURATION, *PXSTATE_CONFIGURATION
req.header: ntddk.h
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

# XSTATE_CONFIGURATION structure

## -description



## -struct-fields

### -field union __unnamed_union_0c2a_72			
 	
### -field ULONG64 EnabledFeatures			
 	
### -field ULONG64 EnabledVolatileFeatures			
 	
### -field ULONG Size			
 	
### -field XSTATE_FEATURE [MAXIMUM_XSTATE_FEATURES] Features			
 	
### -field ULONG64 EnabledSupervisorFeatures			
 	
### -field ULONG64 AlignedFeatures			
 	
### -field ULONG AllFeatureSize			
 	
### -field ULONG [MAXIMUM_XSTATE_FEATURES] AllFeatures			
 	
### -field ULONG  : 1 OptimizedSave			
 	
### -field ULONG  : 1 CompactionEnabled			
 	
### -field ULONG ControlFlags			
 	
## -remarks

## -see-also