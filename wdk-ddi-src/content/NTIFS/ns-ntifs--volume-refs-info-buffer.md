---
UID: NS.ntifs._VOLUME_REFS_INFO_BUFFER
title: VOLUME_REFS_INFO_BUFFER
author: windows-driver-content
description: 
ms.assetid: 6f3830ad-d817-4302-a0d4-db98b546ee99
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: VOLUME_REFS_INFO_BUFFER, VOLUME_REFS_INFO_BUFFER, *PVOLUME_REFS_INFO_BUFFER
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

# VOLUME_REFS_INFO_BUFFER structure

## -description



## -struct-fields

### -field LARGE_INTEGER CacheSizeInBytes			
 	
### -field LARGE_INTEGER AllocatedCacheInBytes			
 	
### -field LARGE_INTEGER PopulatedCacheInBytes			
 	
### -field LARGE_INTEGER InErrorCacheInBytes			
 	
### -field LARGE_INTEGER MemoryUsedForCacheMetadata			
 	
### -field ULONG CacheLineSize			
 	
### -field LONG CacheTransactionsOutstanding			
 	
### -field LONG CacheLinesFree			
 	
### -field LONG CacheLinesInError			
 	
### -field LARGE_INTEGER CacheHitsInBytes			
 	
### -field LARGE_INTEGER CacheMissesInBytes			
 	
### -field LARGE_INTEGER CachePopulationUpdatesInBytes			
 	
### -field LARGE_INTEGER CacheWriteThroughUpdatesInBytes			
 	
### -field LARGE_INTEGER CacheInvalidationsInBytes			
 	
### -field LARGE_INTEGER CacheOverReadsInBytes			
 	
### -field LARGE_INTEGER MetadataWrittenBytes			
 	
### -field LONG CacheHitCounter			
 	
### -field LONG CacheMissCounter			
 	
### -field LONG CacheLineAllocationCounter			
 	
### -field LONG CacheInvalidationsCounter			
 	
### -field LONG CachePopulationUpdatesCounter			
 	
### -field LONG CacheWriteThroughUpdatesCounter			
 	
### -field LONG MaxCacheTransactionsOutstanding			
 	
### -field LONG DataWritesReallocationCount			
 	
### -field LONG DataInPlaceWriteCount			
 	
### -field LONG MetadataAllocationsFastTierCount			
 	
### -field LONG MetadataAllocationsSlowTierCount			
 	
### -field LONG DataAllocationsFastTierCount			
 	
### -field LONG DataAllocationsSlowTierCount			
 	
### -field LONG DestagesSlowTierToFastTier			
 	
### -field LONG DestagesFastTierToSlowTier			
 	
### -field LONG SlowTierDataFillRatio			
 	
### -field LONG FastTierDataFillRatio			
 	
### -field LONG SlowTierMetadataFillRatio			
 	
### -field LONG FastTierMetadataFillRatio			
 	
### -field LONG SlowToFastDestageReadLatency			
 	
### -field LONG SlowToFastDestageReadLatencyBase			
 	
### -field LONG SlowToFastDestageWriteLatency			
 	
### -field LONG SlowToFastDestageWriteLatencyBase			
 	
### -field LONG FastToSlowDestageReadLatency			
 	
### -field LONG FastToSlowDestageReadLatencyBase			
 	
### -field LONG FastToSlowDestageWriteLatency			
 	
### -field LONG FastToSlowDestageWriteLatencyBase			
 	
### -field LONG SlowTierContainerFillRatio			
 	
### -field LONG SlowTierContainerFillRatioBase			
 	
### -field LONG FastTierContainerFillRatio			
 	
### -field LONG FastTierContainerFillRatioBase			
 	
### -field LONG TreeUpdateLatency			
 	
### -field LONG TreeUpdateLatencyBase			
 	
### -field LONG CheckpointLatency			
 	
### -field LONG CheckpointLatencyBase			
 	
### -field LONG TreeUpdateCount			
 	
### -field LONG CheckpointCount			
 	
### -field LONG LogWriteCount			
 	
### -field LONG LogFillRatio			
 	
### -field LONG ReadCacheInvalidationsForOverwrite			
 	
### -field LONG ReadCacheInvalidationsForReuse			
 	
### -field LONG ReadCacheInvalidationsGeneral			
 	
### -field LONG ReadCacheChecksOnMount			
 	
### -field LONG ReadCacheIssuesOnMount			
 	
### -field LONG TrimLatency			
 	
### -field LONG TrimLatencyBase			
 	
### -field LONG DataCompactionCount			
 	
### -field LONG CompactionReadLatency			
 	
### -field LONG CompactionReadLatencyBase			
 	
### -field LONG CompactionWriteLatency			
 	
### -field LONG CompactionWriteLatencyBase			
 	
## -remarks

## -see-also