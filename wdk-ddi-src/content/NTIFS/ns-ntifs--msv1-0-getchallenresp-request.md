---
UID: NS.ntifs._MSV1_0_GETCHALLENRESP_REQUEST
title: MSV1_0_GETCHALLENRESP_REQUEST
author: windows-driver-content
description: 
ms.assetid: e9e3baad-2482-4323-a511-13df40ac45d6
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MSV1_0_GETCHALLENRESP_REQUEST, MSV1_0_GETCHALLENRESP_REQUEST, *PMSV1_0_GETCHALLENRESP_REQUEST
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

# MSV1_0_GETCHALLENRESP_REQUEST structure

## -description



## -struct-fields

### -field MSV1_0_PROTOCOL_MESSAGE_TYPE MessageType			
 	
### -field ULONG ParameterControl			
 	
### -field LUID LogonId			
 	
### -field UNICODE_STRING Password			
 	
### -field UCHAR [MSV1_0_CHALLENGE_LENGTH] ChallengeToClient			
 	
### -field UNICODE_STRING UserName			
 	
### -field UNICODE_STRING LogonDomainName			
 	
### -field UNICODE_STRING ServerName			
 	
## -remarks

## -see-also