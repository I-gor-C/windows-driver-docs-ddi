---
UID: NS.storport._PERFORMANCE_DESCRIPTOR
title: PERFORMANCE_DESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 1bc963d2-8cd2-44f1-ad37-c410701cba2d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PERFORMANCE_DESCRIPTOR, PERFORMANCE_DESCRIPTOR, *PPERFORMANCE_DESCRIPTOR
req.header: storport.h
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

# PERFORMANCE_DESCRIPTOR structure

## -description



## -struct-fields

### -field UCHAR  : 1 RandomAccess			
 	
### -field UCHAR  : 1 Exact			
 	
### -field UCHAR  : 1 RestoreDefaults			
 	
### -field UCHAR  : 2 WriteRotationControl			
 	
### -field UCHAR  : 3 Reserved1			
 	
### -field UCHAR [3] Reserved			
 	
### -field UCHAR [4] StartLba			
 	
### -field UCHAR [4] EndLba			
 	
### -field UCHAR [4] ReadSize			
 	
### -field UCHAR [4] ReadTime			
 	
### -field UCHAR [4] WriteSize			
 	
### -field UCHAR [4] WriteTime			
 	
## -remarks

## -see-also