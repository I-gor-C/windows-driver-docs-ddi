---
UID: NS.minitape._SES_STATUS_DIAGNOSTIC_PAGE
title: SES_STATUS_DIAGNOSTIC_PAGE
author: windows-driver-content
description: 
ms.assetid: 4ced4e1a-b224-41ca-9ac9-45fdb13b2a92
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SES_STATUS_DIAGNOSTIC_PAGE, SES_STATUS_DIAGNOSTIC_PAGE, *PSES_STATUS_DIAGNOSTIC_PAGE
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

# SES_STATUS_DIAGNOSTIC_PAGE structure

## -description



## -struct-fields

### -field UCHAR PageCode			
 	
### -field UCHAR  : 1 Unrecoverable			
 	
### -field UCHAR  : 1 Critical			
 	
### -field UCHAR  : 1 NonCritical			
 	
### -field UCHAR  : 1 Informational			
 	
### -field UCHAR  : 1 InvalidOperation			
 	
### -field UCHAR  : 3 Reserved			
 	
### -field UCHAR [2] PageLength			
 	
### -field UCHAR [4] GenerationCode			
 	
### -field SES_STATUS_DESCRIPTOR [ANYSIZE_ARRAY] Descriptors			
 	
## -remarks

## -see-also