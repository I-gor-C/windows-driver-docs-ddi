---
UID: NS.wdm._DISPATCHER_HEADER
title: DISPATCHER_HEADER
author: windows-driver-content
description: 
ms.assetid: 020a7246-e217-4773-acf5-6fea2f9bfe86
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DISPATCHER_HEADER, DISPATCHER_HEADER, *PDISPATCHER_HEADER
req.header: wdm.h
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

# DISPATCHER_HEADER structure

## -description



## -struct-fields

### -field union DUMMYUNIONNAME			
 	
### -field __unnamed_union_0cb3_56 __unnamed_union_0cb3_56			
 	
### -field LONG SignalState			
 	
### -field LIST_ENTRY WaitListHead			
 	
### -field UCHAR Type			
 	
### -field UCHAR Signalling			
 	
### -field UCHAR Size			
 	
### -field UCHAR Reserved1			
 	
### -field union __unnamed_union_0cb3_60			
 	
### -field union DUMMYUNIONNAME			
 	
### -field __unnamed_union_0cb3_62 __unnamed_union_0cb3_62			
 	
### -field UCHAR TimerType			
 	
### -field UCHAR Hand			
 	
### -field UCHAR  : 1 Absolute			
 	
### -field UCHAR  : 1 Wake			
 	
### -field UCHAR  : TIMER_TOLERABLE_DELAY_BITS EncodedTolerableDelay			
 	
### -field UCHAR TimerControlFlags			
 	
### -field UCHAR  : TIMER_EXPIRED_INDEX_BITS Index			
 	
### -field UCHAR  : 1 Index			
 	
### -field UCHAR  : TIMER_PROCESSOR_INDEX_BITS Processor			
 	
### -field UCHAR  : 1 Inserted			
 	
### -field UCHAR  : 1 Expired			
 	
### -field UCHAR TimerMiscFlags			
 	
### -field union DUMMYUNIONNAME			
 	
### -field __unnamed_union_0cb3_65 __unnamed_union_0cb3_65			
 	
### -field UCHAR Timer2Type			
 	
### -field UCHAR Timer2ComponentId			
 	
### -field UCHAR Timer2RelativeId			
 	
### -field UCHAR  : 1 Timer2Inserted			
 	
### -field UCHAR  : 1 Timer2Expiring			
 	
### -field UCHAR  : 1 Timer2CancelPending			
 	
### -field UCHAR  : 1 Timer2SetPending			
 	
### -field UCHAR  : 1 Timer2Running			
 	
### -field UCHAR  : 1 Timer2Disabled			
 	
### -field UCHAR  : 2 Timer2ReservedFlags			
 	
### -field UCHAR Timer2Flags			
 	
### -field union DUMMYUNIONNAME			
 	
### -field __unnamed_union_0cb3_68 __unnamed_union_0cb3_68			
 	
### -field UCHAR QueueType			
 	
### -field UCHAR QueueSize			
 	
### -field UCHAR QueueReserved			
 	
### -field UCHAR  : 1 Abandoned			
 	
### -field UCHAR  : 1 DisableIncrement			
 	
### -field UCHAR  : 6 QueueReservedControlFlags			
 	
### -field UCHAR QueueControlFlags			
 	
### -field union DUMMYUNIONNAME			
 	
### -field __unnamed_union_0cb3_71 __unnamed_union_0cb3_71			
 	
### -field union DUMMYUNIONNAME2			
 	
### -field __unnamed_union_0cb3_73 __unnamed_union_0cb3_73			
 	
### -field UCHAR ThreadType			
 	
### -field UCHAR ThreadReserved			
 	
### -field UCHAR  : 1 CycleProfiling			
 	
### -field UCHAR  : 1 CounterProfiling			
 	
### -field UCHAR  : 1 GroupScheduling			
 	
### -field UCHAR  : 1 AffinitySet			
 	
### -field UCHAR  : 1 Tagged			
 	
### -field UCHAR  : 1 EnergyProfiling			
 	
### -field UCHAR  : 2 ThreadReservedControlFlags			
 	
### -field UCHAR  : 1 Instrumented			
 	
### -field UCHAR  : 1 ThreadReservedControlFlags			
 	
### -field UCHAR ThreadControlFlags			
 	
### -field BOOLEAN  : 1 ActiveDR7			
 	
### -field BOOLEAN  : 1 Instrumented			
 	
### -field BOOLEAN  : 1 Minimal			
 	
### -field BOOLEAN  : 3 Reserved4			
 	
### -field BOOLEAN  : 1 UmsScheduled			
 	
### -field BOOLEAN  : 1 UmsPrimary			
 	
### -field UCHAR DebugActive			
 	
### -field UCHAR MutantType			
 	
### -field UCHAR MutantSize			
 	
### -field BOOLEAN DpcActive			
 	
### -field UCHAR MutantReserved			
 	
### -field LONG Lock			
 	
### -field LONG LockNV			
 	
## -remarks

## -see-also