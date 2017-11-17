---
UID: NS.ksproxy._ALLOCATOR_PROPERTIES_EX
title: ALLOCATOR_PROPERTIES_EX
author: windows-driver-content
description: 
ms.assetid: 6f107b4b-cece-4322-8396-a19aac816086
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ALLOCATOR_PROPERTIES_EX, ALLOCATOR_PROPERTIES_EX
req.header: ksproxy.h
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

# ALLOCATOR_PROPERTIES_EX structure

## -description



## -struct-fields

### -field long cBuffers			
 	
### -field long cbBuffer			
 	
### -field long cbAlign			
 	
### -field long cbPrefix			
 	
### -field GUID MemoryType			
 	
### -field GUID BusType			
 	
### -field PIPE_STATE State			
 	
### -field PIPE_TERMINATION Input			
 	
### -field PIPE_TERMINATION Output			
 	
### -field ULONG Strategy			
 	
### -field ULONG Flags			
 	
### -field ULONG Weight			
 	
### -field KS_LogicalMemoryType LogicalMemoryType			
 	
### -field PIPE_ALLOCATOR_PLACE AllocatorPlace			
 	
### -field PIPE_DIMENSIONS Dimensions			
 	
### -field KS_FRAMING_RANGE PhysicalRange			
 	
### -field IKsAllocatorEx * PrevSegment			
 	
### -field ULONG CountNextSegments			
 	
### -field IKsAllocatorEx ** NextSegments			
 	
### -field ULONG InsideFactors			
 	
### -field ULONG NumberPins			
 	
## -remarks

## -see-also