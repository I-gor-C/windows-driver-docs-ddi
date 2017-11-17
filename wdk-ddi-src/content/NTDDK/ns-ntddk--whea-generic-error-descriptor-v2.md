---
UID: NS.ntddk._WHEA_GENERIC_ERROR_DESCRIPTOR_V2
title: WHEA_GENERIC_ERROR_DESCRIPTOR_V2
author: windows-driver-content
description: 
ms.assetid: 9550a547-42da-498d-ba84-64b40e8b4e84
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: WHEA_GENERIC_ERROR_DESCRIPTOR_V2, WHEA_GENERIC_ERROR_DESCRIPTOR_V2, *PWHEA_GENERIC_ERROR_DESCRIPTOR_V2
req.header: ntddk.h
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

# WHEA_GENERIC_ERROR_DESCRIPTOR_V2 structure

## -description



## -struct-fields

### -field USHORT Type			
 	
### -field UCHAR Reserved			
 	
### -field UCHAR Enabled			
 	
### -field ULONG ErrStatusBlockLength			
 	
### -field ULONG RelatedErrorSourceId			
 	
### -field UCHAR ErrStatusAddressSpaceID			
 	
### -field UCHAR ErrStatusAddressBitWidth			
 	
### -field UCHAR ErrStatusAddressBitOffset			
 	
### -field UCHAR ErrStatusAddressAccessSize			
 	
### -field WHEA_PHYSICAL_ADDRESS ErrStatusAddress			
 	
### -field WHEA_NOTIFICATION_DESCRIPTOR Notify			
 	
### -field UCHAR ReadAckAddressSpaceID			
 	
### -field UCHAR ReadAckAddressBitWidth			
 	
### -field UCHAR ReadAckAddressBitOffset			
 	
### -field UCHAR ReadAckAddressAccessSize			
 	
### -field WHEA_PHYSICAL_ADDRESS ReadAckAddress			
 	
### -field ULONGLONG ReadAckPreserveMask			
 	
### -field ULONGLONG ReadAckWriteMask			
 	
## -remarks

## -see-also