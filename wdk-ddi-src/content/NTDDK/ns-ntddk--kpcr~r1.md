---
UID: NS.ntddk._KPCR~r1
title: KPCR
author: windows-driver-content
description: 
ms.assetid: c1e1acad-56a3-45eb-b581-f60bb6f0e96c
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

### -field union __unnamed_union_0c2a_50			
 	
### -field union _KIDTENTRY64			
 	
### -field _KIDTENTRY64 * IdtBase			
 	
### -field ULONG64 [2] Unused			
 	
### -field KIRQL Irql			
 	
### -field UCHAR SecondLevelCacheAssociativity			
 	
### -field UCHAR ObsoleteNumber			
 	
### -field UCHAR Fill0			
 	
### -field ULONG [3] Unused0			
 	
### -field USHORT MajorVersion			
 	
### -field USHORT MinorVersion			
 	
### -field ULONG StallScaleFactor			
 	
### -field PVOID [3] Unused1			
 	
### -field ULONG [15] KernelReserved			
 	
### -field ULONG SecondLevelCacheSize			
 	
### -field ULONG [16] HalReserved			
 	
### -field ULONG Unused2			
 	
### -field PVOID KdVersionBlock			
 	
### -field PVOID Unused3			
 	
### -field ULONG [24] PcrAlign1			
 	
### -field struct _KTSS64			
 	
### -field _KTSS64 * TssBase			
 	
### -field struct _KPCR			
 	
### -field _KPCR * Self			
 	
### -field struct _KPRCB			
 	
### -field _KPRCB * CurrentPrcb			
 	
### -field union _KGDTENTRY64			
 	
### -field _KGDTENTRY64 * GdtBase			
 	
### -field ULONG64 UserRsp			
 	
### -field PKSPIN_LOCK_QUEUE LockArray			
 	
### -field PVOID Used_Self			
 	
### -field NT_TIB NtTib			
 	
## -remarks

## -see-also