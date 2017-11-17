---
UID: NS.windot11.DOT11_EXTSTA_ATTRIBUTES~r1
title: DOT11_EXTSTA_ATTRIBUTES
author: windows-driver-content
description: 
ms.assetid: 5f442d2b-0b39-47da-b87d-65a8793abc49
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_EXTSTA_ATTRIBUTES, 
req.header: windot11.h
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

# DOT11_EXTSTA_ATTRIBUTES structure

## -description



## -struct-fields

### -field NDIS_OBJECT_HEADER Header			
 	
### -field ULONG uScanSSIDListSize			
 	
### -field ULONG uDesiredBSSIDListSize			
 	
### -field ULONG uDesiredSSIDListSize			
 	
### -field ULONG uExcludedMacAddressListSize			
 	
### -field ULONG uPrivacyExemptionListSize			
 	
### -field ULONG uKeyMappingTableSize			
 	
### -field ULONG uDefaultKeyTableSize			
 	
### -field ULONG uWEPKeyValueMaxLength			
 	
### -field ULONG uPMKIDCacheSize			
 	
### -field ULONG uMaxNumPerSTADefaultKeyTables			
 	
### -field BOOLEAN bStrictlyOrderedServiceClassImplemented			
 	
### -field UCHAR ucSupportedQoSProtocolFlags			
 	
### -field BOOLEAN bSafeModeImplemented			
 	
### -field ULONG uNumSupportedCountryOrRegionStrings			
 	
### -field PDOT11_COUNTRY_OR_REGION_STRING pSupportedCountryOrRegionStrings			
 	
### -field ULONG uInfraNumSupportedUcastAlgoPairs			
 	
### -field PDOT11_AUTH_CIPHER_PAIR pInfraSupportedUcastAlgoPairs			
 	
### -field ULONG uInfraNumSupportedMcastAlgoPairs			
 	
### -field PDOT11_AUTH_CIPHER_PAIR pInfraSupportedMcastAlgoPairs			
 	
### -field ULONG uAdhocNumSupportedUcastAlgoPairs			
 	
### -field PDOT11_AUTH_CIPHER_PAIR pAdhocSupportedUcastAlgoPairs			
 	
### -field ULONG uAdhocNumSupportedMcastAlgoPairs			
 	
### -field PDOT11_AUTH_CIPHER_PAIR pAdhocSupportedMcastAlgoPairs			
 	
### -field BOOLEAN bAutoPowerSaveMode			
 	
### -field ULONG uMaxNetworkOffloadListSize			
 	
### -field BOOLEAN bMFPCapable			
 	
### -field ULONG uInfraNumSupportedMcastMgmtAlgoPairs			
 	
### -field PDOT11_AUTH_CIPHER_PAIR pInfraSupportedMcastMgmtAlgoPairs			
 	
### -field BOOLEAN bNeighborReportSupported			
 	
### -field BOOLEAN bAPChannelReportSupported			
 	
### -field BOOLEAN bActionFramesSupported			
 	
### -field BOOLEAN bANQPQueryOffloadSupported			
 	
### -field BOOLEAN bHESSIDConnectionSupported			
 	
## -remarks

## -see-also