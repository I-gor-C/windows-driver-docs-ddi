---
UID: NS.ntifs._MSV1_0_GETCHALLENRESP_RESPONSE
title: MSV1_0_GETCHALLENRESP_RESPONSE
author: windows-driver-content
description: 
ms.assetid: 2c1096ce-cc3e-4bd7-9ad6-a26b542b30e2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MSV1_0_GETCHALLENRESP_RESPONSE, MSV1_0_GETCHALLENRESP_RESPONSE, *PMSV1_0_GETCHALLENRESP_RESPONSE
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

# MSV1_0_GETCHALLENRESP_RESPONSE structure

## -description



## -struct-fields

### -field MSV1_0_PROTOCOL_MESSAGE_TYPE MessageType			
 	
### -field STRING CaseSensitiveChallengeResponse			
 	
### -field STRING CaseInsensitiveChallengeResponse			
 	
### -field UNICODE_STRING UserName			
 	
### -field UNICODE_STRING LogonDomainName			
 	
### -field UCHAR [MSV1_0_USER_SESSION_KEY_LENGTH] UserSessionKey			
 	
### -field UCHAR [MSV1_0_LANMAN_SESSION_KEY_LENGTH] LanmanSessionKey			
 	
## -remarks

## -see-also