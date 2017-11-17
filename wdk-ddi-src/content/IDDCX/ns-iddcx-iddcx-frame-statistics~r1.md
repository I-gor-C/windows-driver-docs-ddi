---
UID: NS.iddcx.IDDCX_FRAME_STATISTICS~r1
title: IDDCX_FRAME_STATISTICS
author: windows-driver-content
description: 
ms.assetid: df49350d-9031-47f4-9e70-83c57c5e6aa7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IDDCX_FRAME_STATISTICS, 
req.header: iddcx.h
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

# IDDCX_FRAME_STATISTICS structure

## -description



## -struct-fields

### -field UINT Size			
 	
### -field UINT PresentationFrameNumber			
 	
### -field IDDCX_FRAME_STATUS FrameStatus			
 	
### -field UINT ReEncodeNumber			
 	
### -field UINT FrameSliceTotal			
 	
### -field UINT CurrentSlice			
 	
### -field UINT64 FrameAcquireQpcTime			
 	
### -field UINT FrameProcessingStepsCount			
 	
### -field IDDCX_FRAME_STATISTICS_STEP * pFrameProcessingStep			
 	
### -field UINT64 SendStartQpcTime			
 	
### -field UINT64 SendStopQpcTime			
 	
### -field UINT64 SendCompleteQpcTime			
 	
### -field IDDCX_FRAME_STATISTICS_FLAGS Flags			
 	
### -field UINT ProcessedPixelCount			
 	
### -field UINT FrameSizeInBytes			
 	
## -remarks

## -see-also