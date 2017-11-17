---
UID: NS.ntifs._MSV1_0_LM20_LOGON_PROFILE
title: MSV1_0_LM20_LOGON_PROFILE
author: windows-driver-content
description: 
ms.assetid: 039b35ac-2636-4943-9dbf-b45ffab3079a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MSV1_0_LM20_LOGON_PROFILE, MSV1_0_LM20_LOGON_PROFILE, *PMSV1_0_LM20_LOGON_PROFILE
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

# MSV1_0_LM20_LOGON_PROFILE structure

## -description



## -struct-fields

### -field MSV1_0_PROFILE_BUFFER_TYPE MessageType			
 	
### -field LARGE_INTEGER KickOffTime			
 	
### -field LARGE_INTEGER LogoffTime			
 	
### -field ULONG UserFlags			
 	
### -field UCHAR [MSV1_0_USER_SESSION_KEY_LENGTH] UserSessionKey			
 	
### -field UNICODE_STRING LogonDomainName			
 	
### -field UCHAR [MSV1_0_LANMAN_SESSION_KEY_LENGTH] LanmanSessionKey			
 	
### -field UNICODE_STRING LogonServer			
 	
### -field UNICODE_STRING UserParameters			
 	
## -remarks

## -see-also