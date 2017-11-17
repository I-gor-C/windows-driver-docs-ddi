---
UID: NS.ntifs._TXFS_QUERY_RM_INFORMATION
title: TXFS_QUERY_RM_INFORMATION
author: windows-driver-content
description: 
ms.assetid: 53d8a955-2fa4-4b32-b7d4-dcde839cdce4
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: TXFS_QUERY_RM_INFORMATION, 
req.header: ntifs.h
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

# TXFS_QUERY_RM_INFORMATION structure

## -description



## -struct-fields

### -field ULONG BytesRequired			
 	
### -field ULONGLONG TailLsn			
 	
### -field ULONGLONG CurrentLsn			
 	
### -field ULONGLONG ArchiveTailLsn			
 	
### -field ULONGLONG LogContainerSize			
 	
### -field LARGE_INTEGER HighestVirtualClock			
 	
### -field ULONG LogContainerCount			
 	
### -field ULONG LogContainerCountMax			
 	
### -field ULONG LogContainerCountMin			
 	
### -field ULONG LogGrowthIncrement			
 	
### -field ULONG LogAutoShrinkPercentage			
 	
### -field ULONG Flags			
 	
### -field USHORT LoggingMode			
 	
### -field USHORT Reserved			
 	
### -field ULONG RmState			
 	
### -field ULONGLONG LogCapacity			
 	
### -field ULONGLONG LogFree			
 	
### -field ULONGLONG TopsSize			
 	
### -field ULONGLONG TopsUsed			
 	
### -field ULONGLONG TransactionCount			
 	
### -field ULONGLONG OnePCCount			
 	
### -field ULONGLONG TwoPCCount			
 	
### -field ULONGLONG NumberLogFileFull			
 	
### -field ULONGLONG OldestTransactionAge			
 	
### -field GUID RMName			
 	
### -field ULONG TmLogPathOffset			
 	
## -remarks

## -see-also