---
UID: NS.wdm._EXCEPTION_RECORD
title: EXCEPTION_RECORD
author: windows-driver-content
description: 
ms.assetid: de0fcc12-fb22-412d-9ab2-88dbff0c3e37
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: EXCEPTION_RECORD, EXCEPTION_RECORD
req.header: wdm.h
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

# EXCEPTION_RECORD structure

## -description



## -struct-fields

### -field struct _EXCEPTION_RECORD			
 	
### -field _EXCEPTION_RECORD * ExceptionRecord			
 	
### -field NTSTATUS ExceptionCode			
 	
### -field ULONG ExceptionFlags			
 	
### -field PVOID ExceptionAddress			
 	
### -field ULONG NumberParameters			
 	
### -field ULONG_PTR [EXCEPTION_MAXIMUM_PARAMETERS] ExceptionInformation			
 	
## -remarks

## -see-also