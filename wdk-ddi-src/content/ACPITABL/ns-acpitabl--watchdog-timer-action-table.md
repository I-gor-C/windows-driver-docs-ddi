---
UID: NS.acpitabl._WATCHDOG_TIMER_ACTION_TABLE
title: WATCHDOG_TIMER_ACTION_TABLE
author: windows-driver-content
description: 
ms.assetid: 68ef0fad-94d6-42a0-a009-d52ae0001e4b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: WATCHDOG_TIMER_ACTION_TABLE, WATCHDOG_TIMER_ACTION_TABLE, *PWATCHDOG_TIMER_ACTION_TABLE
req.header: acpitabl.h
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

# WATCHDOG_TIMER_ACTION_TABLE structure

## -description



## -struct-fields

### -field DESCRIPTION_HEADER Header			
 	
### -field ULONG WatchdogHeaderLength			
 	
### -field USHORT PciSegment			
 	
### -field UCHAR PciBusNumber			
 	
### -field UCHAR PciDeviceNumber			
 	
### -field UCHAR PciFunctionNumber			
 	
### -field UCHAR [3] Reserved1			
 	
### -field ULONG TimerPeriod			
 	
### -field ULONG MaximumCount			
 	
### -field ULONG MinimumCount			
 	
### -field UCHAR WatchdogFlags			
 	
### -field UCHAR [3] Reserved2			
 	
### -field ULONG InstructionCount			
 	
### -field WATCHDOG_TIMER_INSTRUCTION_ENTRY [ANYSIZE_ARRAY] InstructionEntry			
 	
## -remarks

## -see-also