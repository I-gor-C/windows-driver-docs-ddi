---
UID: NS.ntddk._KTRAP_FRAME~r1
title: KTRAP_FRAME
author: windows-driver-content
description: 
ms.assetid: 338fcaec-ccad-4d6a-ac6a-f37ca02ab908
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KTRAP_FRAME, KTRAP_FRAME, *PKTRAP_FRAME
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

# KTRAP_FRAME structure

## -description



## -struct-fields

### -field union __unnamed_union_0c2a_62			
 	
### -field union __unnamed_union_0c2a_63			
 	
### -field ULONG Arg3			
 	
### -field ULONG FaultStatus			
 	
### -field ULONG Reserved			
 	
### -field UCHAR ExceptionActive			
 	
### -field UCHAR ContextFromKFramesUnwound			
 	
### -field UCHAR DebugRegistersValid			
 	
### -field PKARM_VFP_STATE VfpState			
 	
### -field ULONG [ARM_MAX_BREAKPOINTS] Bvr			
 	
### -field ULONG [ARM_MAX_BREAKPOINTS] Bcr			
 	
### -field ULONG [ARM_MAX_WATCHPOINTS] Wvr			
 	
### -field ULONG [ARM_MAX_WATCHPOINTS] Wcr			
 	
### -field ULONG R0			
 	
### -field ULONG R1			
 	
### -field ULONG R2			
 	
### -field ULONG R3			
 	
### -field ULONG R12			
 	
### -field ULONG Sp			
 	
### -field ULONG Lr			
 	
### -field ULONG R11			
 	
### -field ULONG Pc			
 	
### -field ULONG Cpsr			
 	
### -field ULONG FaultAddress			
 	
### -field ULONG TrapFrame			
 	
### -field KPROCESSOR_MODE PreviousMode			
 	
### -field KIRQL PreviousIrql			
 	
## -remarks

## -see-also