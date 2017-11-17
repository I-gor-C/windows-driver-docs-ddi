---
UID: NS.scsi._MODE_CACHING_PAGE_EX
title: MODE_CACHING_PAGE_EX
author: windows-driver-content
description: 
ms.assetid: cad8b3e1-a806-437e-aac9-9aec0de2039a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_CACHING_PAGE_EX, MODE_CACHING_PAGE_EX, *PMODE_CACHING_PAGE_EX
req.header: scsi.h
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

# MODE_CACHING_PAGE_EX structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 SubPageFormat			
 	
### -field UCHAR  : 1 PageSavable			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR  : 1 ReadDisableCache			
 	
### -field UCHAR  : 1 MultiplicationFactor			
 	
### -field UCHAR  : 1 WriteCacheEnable			
 	
### -field UCHAR  : 1 SizeEnable			
 	
### -field UCHAR  : 1 Discontinuity			
 	
### -field UCHAR  : 1 CachingAnalysisPermitted			
 	
### -field UCHAR  : 1 AbortPreFetch			
 	
### -field UCHAR  : 1 InitiatorControl			
 	
### -field UCHAR  : 4 WriteRetensionPriority			
 	
### -field UCHAR  : 4 ReadRetensionPriority			
 	
### -field UCHAR [2] DisablePrefetchTransfer			
 	
### -field UCHAR [2] MinimumPrefetch			
 	
### -field UCHAR [2] MaximumPrefetch			
 	
### -field UCHAR [2] MaximumPrefetchCeiling			
 	
### -field UCHAR  : 1 NvCacheDisable			
 	
### -field UCHAR  : 2 SyncCacheProgress			
 	
### -field UCHAR  : 2 VendorSpecific			
 	
### -field UCHAR  : 1 DisableReadAhead			
 	
### -field UCHAR  : 1 LogicalBlockCacheSegmentSize			
 	
### -field UCHAR  : 1 ForceSequentialWrite			
 	
### -field UCHAR NumberOfCacheSegments			
 	
### -field UCHAR [2] CacheSegmentSize			
 	
### -field UCHAR [4] Reserved			
 	
## -remarks

## -see-also