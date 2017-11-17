---
UID: NS.minitape._SES_CONTROL_DIAGNOSTIC_PAGE
title: SES_CONTROL_DIAGNOSTIC_PAGE
author: windows-driver-content
description: 
ms.assetid: 83c1cee3-a524-4d51-b39e-fc06b223562e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SES_CONTROL_DIAGNOSTIC_PAGE, SES_CONTROL_DIAGNOSTIC_PAGE, *PSES_CONTROL_DIAGNOSTIC_PAGE
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

# SES_CONTROL_DIAGNOSTIC_PAGE structure

## -description



## -struct-fields

### -field UCHAR PageCode			
 	
### -field UCHAR  : 1 Unrecoverable			
 	
### -field UCHAR  : 1 Critical			
 	
### -field UCHAR  : 1 NonCritical			
 	
### -field UCHAR  : 1 Informational			
 	
### -field UCHAR  : 4 Reserved			
 	
### -field UCHAR [2] PageLength			
 	
### -field UCHAR [4] ExpectedGenerationCode			
 	
### -field SES_CONTROL_DESCRIPTOR [ANYSIZE_ARRAY] Descriptors			
 	
## -remarks

## -see-also