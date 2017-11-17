---
UID: NS.rimext.RIMCOMPLETEFRAME
title: RIMCOMPLETEFRAME
author: windows-driver-content
description: 
ms.assetid: f6073719-dd46-4b0c-a231-cc28bb326600
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RIMCOMPLETEFRAME, 
req.header: rimext.h
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

# RIMCOMPLETEFRAME structure

## -description



## -struct-fields

### -field DWORD cbSize			
 	
### -field LIST_ENTRY nextFrame			
 	
### -field DWORD cPointers			
 	
### -field DWORD cRawDataBlocks			
 	
### -field HANDLE hRimDev			
 	
### -field UINT64 qpcArrivalTime			
 	
### -field BOOL bDevInjection			
 	
### -field BOOL bButtonOnly			
 	
### -field BOOL bAutoRepeatFrame			
 	
### -field DWORD dwRimTickCount			
 	
### -field ULONGLONG ullRimQpc			
 	
### -field RIMPOINTERINFONODE * pPrimaryPointerInfoNode			
 	
### -field RIMPOINTERRAWDATA * pRawDataList			
 	
### -field RIMPOINTERINFONODE * pPointerInfoList			
 	
## -remarks

## -see-also