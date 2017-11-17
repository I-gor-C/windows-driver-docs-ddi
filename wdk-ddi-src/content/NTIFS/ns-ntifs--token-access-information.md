---
UID: NS.ntifs._TOKEN_ACCESS_INFORMATION
title: TOKEN_ACCESS_INFORMATION
author: windows-driver-content
description: 
ms.assetid: 102d9f6c-3030-4d9a-bc47-63e5dbca9b57
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: TOKEN_ACCESS_INFORMATION, TOKEN_ACCESS_INFORMATION, *PTOKEN_ACCESS_INFORMATION
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

# TOKEN_ACCESS_INFORMATION structure

## -description



## -struct-fields

### -field PSID_AND_ATTRIBUTES_HASH SidHash			
 	
### -field PSID_AND_ATTRIBUTES_HASH RestrictedSidHash			
 	
### -field PTOKEN_PRIVILEGES Privileges			
 	
### -field LUID AuthenticationId			
 	
### -field TOKEN_TYPE TokenType			
 	
### -field SECURITY_IMPERSONATION_LEVEL ImpersonationLevel			
 	
### -field TOKEN_MANDATORY_POLICY MandatoryPolicy			
 	
### -field ULONG Flags			
 	
### -field ULONG AppContainerNumber			
 	
### -field PSID PackageSid			
 	
### -field PSID_AND_ATTRIBUTES_HASH CapabilitiesHash			
 	
### -field PSID TrustLevelSid			
 	
### -field PSECURITY_ATTRIBUTES_OPAQUE SecurityAttributes			
 	
## -remarks

## -see-also