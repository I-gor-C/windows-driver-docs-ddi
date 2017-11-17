---
UID: NS.ntddk._KPCR~r3
title: KPCR
author: windows-driver-content
description: 
ms.assetid: 16da6cec-95b7-48fb-8db2-d4a8d960fc8b
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

### -field union __unnamed_union_0c2a_64			
 	
### -field union __unnamed_union_0c2a_66			
 	
### -field KIRQL CurrentIrql			
 	
### -field UCHAR SecondLevelCacheAssociativity			
 	
### -field UCHAR [2] Pad1			
 	
### -field USHORT MajorVersion			
 	
### -field USHORT MinorVersion			
 	
### -field ULONG StallScaleFactor			
 	
### -field ULONG SecondLevelCacheSize			
 	
### -field USHORT InterruptPad			
 	
### -field ULONG64 [6] PanicStorage			
 	
### -field PVOID KdVersionBlock			
 	
### -field PVOID [15] HalReserved			
 	
### -field struct _KPCR			
 	
### -field _KPCR * Self			
 	
### -field PVOID [2] TibPad0			
 	
### -field PVOID Spare1			
 	
### -field PVOID PcrReserved0			
 	
### -field PKSPIN_LOCK_QUEUE LockArray			
 	
### -field PVOID Used_Self			
 	
### -field NT_TIB NtTib			
 	
### -field UCHAR ApcInterrupt			
 	
### -field UCHAR DispatchInterrupt			
 	
### -field USHORT SoftwareInterruptPending			
 	
## -remarks

## -see-also