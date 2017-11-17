---
UID: NS.ntddk._KUMS_CONTEXT_HEADER
title: KUMS_CONTEXT_HEADER
author: windows-driver-content
description: 
ms.assetid: 1781277c-244d-4bb1-980c-87ce5299ba1c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KUMS_CONTEXT_HEADER, KUMS_CONTEXT_HEADER, *PKUMS_CONTEXT_HEADER
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

# KUMS_CONTEXT_HEADER structure

## -description



## -struct-fields

### -field struct _KTHREAD			
 	
### -field _KTHREAD * SourceThread			
 	
### -field union __unnamed_union_0c2a_56			
 	
### -field ULONG64 P1Home			
 	
### -field ULONG64 P2Home			
 	
### -field ULONG64 P3Home			
 	
### -field ULONG64 P4Home			
 	
### -field PVOID StackTop			
 	
### -field ULONG64 StackSize			
 	
### -field ULONG64 RspOffset			
 	
### -field ULONG64 Rip			
 	
### -field PXMM_SAVE_AREA32 FltSave			
 	
### -field PKTRAP_FRAME TrapFrame			
 	
### -field PKEXCEPTION_FRAME ExceptionFrame			
 	
### -field ULONG64 Return			
 	
### -field ULONG64  : 1 Volatile			
 	
### -field ULONG64  : 63 Reserved			
 	
### -field ULONG64 Flags			
 	
## -remarks

## -see-also