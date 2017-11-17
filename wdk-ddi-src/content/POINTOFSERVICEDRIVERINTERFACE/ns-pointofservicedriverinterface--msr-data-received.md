---
UID: NS.pointofservicedriverinterface._MSR_DATA_RECEIVED
title: MSR_DATA_RECEIVED
author: windows-driver-content
description: 
ms.assetid: e4e596e1-28ae-4162-90f5-d5ef7eab5ac9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MSR_DATA_RECEIVED, MSR_DATA_RECEIVED, *PMSR_DATA_RECEIVED
req.header: pointofservicedriverinterface.h
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

# MSR_DATA_RECEIVED structure

## -description



## -struct-fields

### -field MsrCardType CardType			
 	
### -field unsigned char Track1EncryptedDataLength			
 	
### -field unsigned char Track2EncryptedDataLength			
 	
### -field unsigned char Track3EncryptedDataLength			
 	
### -field unsigned char Track4EncryptedDataLength			
 	
### -field unsigned char [MSR_TRACK_SIZE] Track1EncryptedData			
 	
### -field unsigned char [MSR_TRACK_SIZE] Track2EncryptedData			
 	
### -field unsigned char [MSR_TRACK_SIZE] Track3EncryptedData			
 	
### -field unsigned char [MSR_TRACK_SIZE] Track4EncryptedData			
 	
### -field unsigned char Track1MaskedDataLength			
 	
### -field unsigned char Track2MaskedDataLength			
 	
### -field unsigned char Track3MaskedDataLength			
 	
### -field unsigned char Track4MaskedDataLength			
 	
### -field unsigned char [MSR_TRACK_SIZE] Track1MaskedData			
 	
### -field unsigned char [MSR_TRACK_SIZE] Track2MaskedData			
 	
### -field unsigned char [MSR_TRACK_SIZE] Track3MaskedData			
 	
### -field unsigned char [MSR_TRACK_SIZE] Track4MaskedData			
 	
### -field unsigned char Track1DiscretionaryDataLength			
 	
### -field unsigned char Track2DiscretionaryDataLength			
 	
### -field unsigned char [MSR_TRACK_SIZE] Track1DiscretionaryData			
 	
### -field unsigned char [MSR_TRACK_SIZE] Track2DiscretionaryData			
 	
### -field unsigned char CardAuthenicationDataLength			
 	
### -field unsigned char CardAuthenticationDataAbsoluteLength			
 	
### -field unsigned char [MSR_CARD_AUTHENTICATION_DATA_SIZE] CardAuthenicationData			
 	
### -field unsigned char AdditionalSecurityInformationLength			
 	
### -field unsigned char [MSR_ADDITIONAL_SECURITY_INFORMATION_SIZE] AdditionalSecurityInformation			
 	
## -remarks

## -see-also