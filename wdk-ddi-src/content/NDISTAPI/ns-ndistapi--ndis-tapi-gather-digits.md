---
UID: NS.ndistapi._NDIS_TAPI_GATHER_DIGITS
title: NDIS_TAPI_GATHER_DIGITS
author: windows-driver-content
description: 
ms.assetid: b5ecaae5-e13d-4aff-b201-fad44a3a311f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_TAPI_GATHER_DIGITS, NDIS_TAPI_GATHER_DIGITS, *PNDIS_TAPI_GATHER_DIGITS
req.header: ndistapi.h
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

# NDIS_TAPI_GATHER_DIGITS structure

## -description



## -struct-fields

### -field ULONG ulRequestID			
 	
### -field IN HDRV_CALL hdCall			
 	
### -field IN ULONG ulEndToEndID			
 	
### -field IN ULONG ulDigitModes			
 	
### -field IN LPWSTR lpsOrigDigitsBuffer			
 	
### -field IN ULONG ulDigitsBufferOffset			
 	
### -field IN ULONG ulNumDigitsNeeded			
 	
### -field OUT ULONG ulNumDigitsRead			
 	
### -field OUT ULONG ulTickCount			
 	
### -field OUT ULONG ulTerminationReason			
 	
### -field IN ULONG ulTerminationDigitsMask			
 	
### -field IN ULONG ulFirstDigitTimeout			
 	
### -field IN ULONG ulInterDigitTimeout			
 	
## -remarks

## -see-also