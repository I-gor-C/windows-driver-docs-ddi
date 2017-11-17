---
UID: NS.ntifs._MSV1_0_SUBAUTH_LOGON
title: MSV1_0_SUBAUTH_LOGON
author: windows-driver-content
description: 
ms.assetid: 6c34f6d7-c91b-47a5-9981-fcfa57b7d2ab
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MSV1_0_SUBAUTH_LOGON, MSV1_0_SUBAUTH_LOGON, *PMSV1_0_SUBAUTH_LOGON
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

# MSV1_0_SUBAUTH_LOGON structure

## -description



## -struct-fields

### -field MSV1_0_LOGON_SUBMIT_TYPE MessageType			
 	
### -field UNICODE_STRING LogonDomainName			
 	
### -field UNICODE_STRING UserName			
 	
### -field UNICODE_STRING Workstation			
 	
### -field UCHAR [MSV1_0_CHALLENGE_LENGTH] ChallengeToClient			
 	
### -field STRING AuthenticationInfo1			
 	
### -field STRING AuthenticationInfo2			
 	
### -field ULONG ParameterControl			
 	
### -field ULONG SubAuthPackageId			
 	
## -remarks

## -see-also