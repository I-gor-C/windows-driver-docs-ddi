---
UID: NS.ntddk._KTRAP_FRAME~r2
title: KTRAP_FRAME
author: windows-driver-content
description: 
ms.assetid: 564710fa-f6de-4a7d-a2a3-09a218f76533
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

### -field union __unnamed_union_0c2a_68			
 	
### -field union __unnamed_union_0c2a_69			
 	
### -field union __unnamed_union_0c2a_70			
 	
### -field UCHAR ExceptionActive			
 	
### -field UCHAR ContextFromKFramesUnwound			
 	
### -field UCHAR DebugRegistersValid			
 	
### -field ULONG Reserved			
 	
### -field PKARM64_VFP_STATE VfpState			
 	
### -field ULONG [ARM64_MAX_BREAKPOINTS] Bcr			
 	
### -field ULONG64 [ARM64_MAX_BREAKPOINTS] Bvr			
 	
### -field ULONG [ARM64_MAX_WATCHPOINTS] Wcr			
 	
### -field ULONG64 [ARM64_MAX_WATCHPOINTS] Wvr			
 	
### -field ULONG Spsr			
 	
### -field ULONG Esr			
 	
### -field ULONG64 Sp			
 	
### -field ULONG64 Lr			
 	
### -field ULONG64 Fp			
 	
### -field ULONG64 Pc			
 	
### -field KPROCESSOR_MODE PreviousMode			
 	
### -field KIRQL PreviousIrql			
 	
### -field ULONG64 FaultAddress			
 	
### -field ULONG64 TrapFrame			
 	
### -field ULONG64 X0			
 	
### -field ULONG64 X1			
 	
### -field ULONG64 X2			
 	
### -field ULONG64 X3			
 	
### -field ULONG64 X4			
 	
### -field ULONG64 X5			
 	
### -field ULONG64 X6			
 	
### -field ULONG64 X7			
 	
### -field ULONG64 X8			
 	
### -field ULONG64 X9			
 	
### -field ULONG64 X10			
 	
### -field ULONG64 X11			
 	
### -field ULONG64 X12			
 	
### -field ULONG64 X13			
 	
### -field ULONG64 X14			
 	
### -field ULONG64 X15			
 	
### -field ULONG64 X16			
 	
### -field ULONG64 X17			
 	
### -field ULONG64 X18			
 	
### -field ULONG64 [19] X			
 	
## -remarks

## -see-also