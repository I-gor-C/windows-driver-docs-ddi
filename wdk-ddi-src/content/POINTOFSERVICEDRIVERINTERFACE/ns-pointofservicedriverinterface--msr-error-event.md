---
UID: NS.pointofservicedriverinterface._MSR_ERROR_EVENT
title: MSR_ERROR_EVENT
author: windows-driver-content
description: 
ms.assetid: 15d29ef5-7c7b-4d32-a279-0be63e552b94
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MSR_ERROR_EVENT, MSR_ERROR_EVENT, *PMSR_ERROR_EVENT
req.header: pointofservicedriverinterface.h
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

# MSR_ERROR_EVENT structure

## -description



## -struct-fields

### -field PosEventDataHeader Header			
 	
### -field MsrTrackErrorType Track1Status			
 	
### -field MsrTrackErrorType Track2Status			
 	
### -field MsrTrackErrorType Track3Status			
 	
### -field MsrTrackErrorType Track4Status			
 	
### -field DriverUnifiedPosErrorSeverity Severity			
 	
### -field DriverUnifiedPosErrorReason Reason			
 	
### -field UINT32 ExtendedReason			
 	
### -field MSR_DATA_RECEIVED CardData			
 	
### -field wchar_t [MSR_ERROR_MAX_MESSAGE_LENGTH] Message			
 	
## -remarks

## -see-also