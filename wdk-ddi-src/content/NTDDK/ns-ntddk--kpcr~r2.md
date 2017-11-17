---
UID: NS.ntddk._KPCR~r2
title: KPCR
author: windows-driver-content
description: 
ms.assetid: 491561ef-9442-4d69-96d4-6749037fdd8f
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

### -field union __unnamed_union_0c2a_58			
 	
### -field union __unnamed_union_0c2a_60			
 	
### -field KIRQL CurrentIrql			
 	
### -field UCHAR SecondLevelCacheAssociativity			
 	
### -field ULONG [3] Unused0			
 	
### -field USHORT MajorVersion			
 	
### -field USHORT MinorVersion			
 	
### -field ULONG StallScaleFactor			
 	
### -field PVOID [3] Unused1			
 	
### -field ULONG [15] KernelReserved			
 	
### -field ULONG SecondLevelCacheSize			
 	
### -field USHORT InterruptPad			
 	
### -field ULONG [32] HalReserved			
 	
### -field PVOID KdVersionBlock			
 	
### -field PVOID Unused3			
 	
### -field ULONG [8] PcrAlign1			
 	
### -field struct _KPCR			
 	
### -field _KPCR * Self			
 	
### -field struct _KPRCB			
 	
### -field _KPRCB * CurrentPrcb			
 	
### -field ULONG [2] TibPad0			
 	
### -field PVOID Spare1			
 	
### -field PKSPIN_LOCK_QUEUE LockArray			
 	
### -field PVOID Used_Self			
 	
### -field NT_TIB NtTib			
 	
### -field UCHAR ApcInterrupt			
 	
### -field UCHAR DispatchInterrupt			
 	
### -field USHORT SoftwareInterruptPending			
 	
## -remarks

## -see-also