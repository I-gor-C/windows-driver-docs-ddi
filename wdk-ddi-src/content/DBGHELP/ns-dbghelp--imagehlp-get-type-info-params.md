---
UID: NS.dbghelp._IMAGEHLP_GET_TYPE_INFO_PARAMS
title: IMAGEHLP_GET_TYPE_INFO_PARAMS
author: windows-driver-content
description: 
ms.assetid: 8a43a164-a820-4d3a-a786-f4bb6e3d98f4
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMAGEHLP_GET_TYPE_INFO_PARAMS, IMAGEHLP_GET_TYPE_INFO_PARAMS, *PIMAGEHLP_GET_TYPE_INFO_PARAMS
req.header: dbghelp.h
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

# IMAGEHLP_GET_TYPE_INFO_PARAMS structure

## -description



## -struct-fields

### -field IN ULONG SizeOfStruct			
 	
### -field IN ULONG Flags			
 	
### -field IN ULONG NumIds			
 	
### -field IN PULONG TypeIds			
 	
### -field IN ULONG64 TagFilter			
 	
### -field IN ULONG NumReqs			
 	
### -field IN IMAGEHLP_SYMBOL_TYPE_INFO * ReqKinds			
 	
### -field IN PULONG_PTR ReqOffsets			
 	
### -field IN PULONG ReqSizes			
 	
### -field IN ULONG_PTR ReqStride			
 	
### -field IN ULONG_PTR BufferSize			
 	
### -field OUT PVOID Buffer			
 	
### -field OUT ULONG EntriesMatched			
 	
### -field OUT ULONG EntriesFilled			
 	
### -field OUT ULONG64 TagsFound			
 	
### -field OUT ULONG64 AllReqsValid			
 	
### -field IN ULONG NumReqsValid			
 	
### -field OUT PULONG64 ReqsValid OPTIONAL			
 	
## -remarks

## -see-also