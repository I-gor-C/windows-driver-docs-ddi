---
UID: NS.ntddk._KTRAP_FRAME
title: KTRAP_FRAME
author: windows-driver-content
description: 
ms.assetid: 856398c2-5270-4a09-b0f5-44f3091c49ac
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

### -field struct __unnamed_struct_0c2a_54			
 	
### -field union __unnamed_union_0c2a_52			
 	
### -field union __unnamed_union_0c2a_53			
 	
### -field union __unnamed_union_0c2a_55			
 	
### -field ULONG64 P1Home			
 	
### -field ULONG64 P2Home			
 	
### -field ULONG64 P3Home			
 	
### -field ULONG64 P4Home			
 	
### -field ULONG64 P5			
 	
### -field KPROCESSOR_MODE PreviousMode			
 	
### -field KIRQL PreviousIrql			
 	
### -field UCHAR FaultIndicator			
 	
### -field UCHAR ExceptionActive			
 	
### -field ULONG MxCsr			
 	
### -field ULONG64 Rax			
 	
### -field ULONG64 Rcx			
 	
### -field ULONG64 Rdx			
 	
### -field ULONG64 R8			
 	
### -field ULONG64 R9			
 	
### -field ULONG64 R10			
 	
### -field ULONG64 R11			
 	
### -field M128A Xmm0			
 	
### -field M128A Xmm1			
 	
### -field M128A Xmm2			
 	
### -field M128A Xmm3			
 	
### -field M128A Xmm4			
 	
### -field M128A Xmm5			
 	
### -field ULONG64 Dr0			
 	
### -field ULONG64 Dr1			
 	
### -field ULONG64 Dr2			
 	
### -field ULONG64 Dr3			
 	
### -field ULONG64 Dr6			
 	
### -field ULONG64 Dr7			
 	
### -field USHORT SegDs			
 	
### -field USHORT SegEs			
 	
### -field USHORT SegFs			
 	
### -field USHORT SegGs			
 	
### -field ULONG64 TrapFrame			
 	
### -field ULONG64 Rbx			
 	
### -field ULONG64 Rdi			
 	
### -field ULONG64 Rsi			
 	
### -field ULONG64 Rbp			
 	
### -field ULONG64 Rip			
 	
### -field USHORT SegCs			
 	
### -field UCHAR Fill0			
 	
### -field UCHAR Logging			
 	
### -field USHORT [2] Fill1			
 	
### -field ULONG EFlags			
 	
### -field ULONG Fill2			
 	
### -field ULONG64 Rsp			
 	
### -field USHORT SegSs			
 	
### -field USHORT Fill3			
 	
### -field ULONG Fill4			
 	
### -field ULONG64 GsBase			
 	
### -field ULONG64 GsSwap			
 	
### -field ULONG64 FaultAddress			
 	
### -field ULONG64 ContextRecord			
 	
### -field ULONG64 ErrorCode			
 	
### -field ULONG64 ExceptionFrame			
 	
## -remarks

## -see-also