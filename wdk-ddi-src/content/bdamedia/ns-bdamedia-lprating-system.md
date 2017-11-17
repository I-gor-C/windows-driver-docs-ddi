---
UID: NS.bdamedia.LPRATING_SYSTEM
title: LPRATING_SYSTEM
author: windows-driver-content
description: 
ms.assetid: f8cb50fa-8b06-42a0-973c-c85a5fdfc0de
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: LPRATING_SYSTEM, RATING_SYSTEM, *LPRATING_SYSTEM
req.header: bdamedia.h
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

# LPRATING_SYSTEM structure

## -description



## -struct-fields

### -field GUID rating_system_id			
 	
### -field BYTE  : 1 rating_system_is_age_type			
 	
### -field BYTE  : 7 reserved			
 	
### -field BYTE [MAX_COUNTRY_CODE_STRING] country_code			
 	
### -field DWORD rating_attribute_count			
 	
### -field RATING_ATTRIBUTE * lpratingattrib			
 	
## -remarks

## -see-also