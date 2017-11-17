---
UID: NS.ntddk._KPCR
title: KPCR
author: windows-driver-content
description: 
ms.assetid: 1275ccb0-7359-4b35-b939-08d65915d3c4
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KPCR, KPCR, *PKPCR
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

# KPCR structure

## -description



## -struct-fields

### -field struct _KPCR			
 	
### -field _KPCR * SelfPcr			
 	
### -field struct _KPRCB			
 	
### -field _KPRCB * Prcb			
 	
### -field struct _KIDTENTRY			
 	
### -field _KIDTENTRY * IDT			
 	
### -field struct _KGDTENTRY			
 	
### -field _KGDTENTRY * GDT			
 	
### -field struct _KTSS			
 	
### -field _KTSS * TSS			
 	
### -field union __unnamed_union_0c2a_48			
 	
### -field KIRQL Irql			
 	
### -field ULONG IRR			
 	
### -field ULONG IrrActive			
 	
### -field ULONG IDR			
 	
### -field PVOID KdVersionBlock			
 	
### -field USHORT MajorVersion			
 	
### -field USHORT MinorVersion			
 	
### -field KAFFINITY SetMember			
 	
### -field ULONG StallScaleFactor			
 	
### -field UCHAR SpareUnused			
 	
### -field UCHAR Number			
 	
### -field UCHAR Spare0			
 	
### -field UCHAR SecondLevelCacheAssociativity			
 	
### -field ULONG VdmAlert			
 	
### -field ULONG [14] KernelReserved			
 	
### -field ULONG SecondLevelCacheSize			
 	
### -field ULONG [16] HalReserved			
 	
### -field struct _EXCEPTION_REGISTRATION_RECORD			
 	
### -field _EXCEPTION_REGISTRATION_RECORD * Used_ExceptionList			
 	
### -field PVOID Used_StackBase			
 	
### -field ULONG MxCsr			
 	
### -field PVOID TssCopy			
 	
### -field ULONG ContextSwitches			
 	
### -field KAFFINITY SetMemberCopy			
 	
### -field PVOID Used_Self			
 	
### -field NT_TIB NtTib			
 	
## -remarks

## -see-also