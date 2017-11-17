---
UID: NS.ntifs._SE_ACCESS_REQUEST
title: SE_ACCESS_REQUEST
author: windows-driver-content
description: 
ms.assetid: 995843ce-a663-4ee6-b704-e89bac7bfcf7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SE_ACCESS_REQUEST, SE_ACCESS_REQUEST, *PSE_ACCESS_REQUEST
req.header: ntifs.h
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

# SE_ACCESS_REQUEST structure

## -description



## -struct-fields

### -field ULONG Size			
 	
### -field PSE_SECURITY_DESCRIPTOR SeSecurityDescriptor			
 	
### -field ACCESS_MASK DesiredAccess			
 	
### -field ACCESS_MASK PreviouslyGrantedAccess			
 	
### -field PSID PrincipalSelfSid			
 	
### -field PGENERIC_MAPPING GenericMapping			
 	
### -field ULONG ObjectTypeListCount			
 	
### -field POBJECT_TYPE_LIST ObjectTypeList			
 	
## -remarks

## -see-also