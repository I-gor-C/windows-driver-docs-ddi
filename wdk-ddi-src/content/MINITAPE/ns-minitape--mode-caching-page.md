---
UID: NS.minitape._MODE_CACHING_PAGE
title: MODE_CACHING_PAGE
author: windows-driver-content
description: 
ms.assetid: 2ce89b2d-19c4-4e54-958a-174468f841b5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_CACHING_PAGE, MODE_CACHING_PAGE, *PMODE_CACHING_PAGE
req.header: minitape.h
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

# MODE_CACHING_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved			
 	
### -field UCHAR  : 1 PageSavable			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR  : 1 ReadDisableCache			
 	
### -field UCHAR  : 1 MultiplicationFactor			
 	
### -field UCHAR  : 1 WriteCacheEnable			
 	
### -field UCHAR  : 5 Reserved2			
 	
### -field UCHAR  : 4 WriteRetensionPriority			
 	
### -field UCHAR  : 4 ReadRetensionPriority			
 	
### -field UCHAR [2] DisablePrefetchTransfer			
 	
### -field UCHAR [2] MinimumPrefetch			
 	
### -field UCHAR [2] MaximumPrefetch			
 	
### -field UCHAR [2] MaximumPrefetchCeiling			
 	
## -remarks

## -see-also