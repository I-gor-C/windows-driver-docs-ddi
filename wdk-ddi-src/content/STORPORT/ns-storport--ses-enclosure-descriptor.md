---
UID: NS.storport._SES_ENCLOSURE_DESCRIPTOR
title: SES_ENCLOSURE_DESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 59beafb0-b4f3-4c89-b80e-ded1d30c34c1
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SES_ENCLOSURE_DESCRIPTOR, SES_ENCLOSURE_DESCRIPTOR, *PSES_ENCLOSURE_DESCRIPTOR
req.header: storport.h
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

# SES_ENCLOSURE_DESCRIPTOR structure

## -description



## -struct-fields

### -field UCHAR  : 3 NumberOfEnclosureServices			
 	
### -field UCHAR  : 1 Reserved1			
 	
### -field UCHAR  : 3 RelativeEnclosureServicesId			
 	
### -field UCHAR  : 1 Reserved2			
 	
### -field UCHAR SubEnclosureId			
 	
### -field UCHAR NumberOfTypeDescriptorHeaders			
 	
### -field UCHAR EnclosureDescriptorLength			
 	
### -field UCHAR [8] Identifier			
 	
### -field UCHAR [8] VendorId			
 	
### -field UCHAR [16] ProductId			
 	
### -field UCHAR [4] ProductRevisionLevel			
 	
### -field UCHAR [ANYSIZE_ARRAY] VendorSpecific			
 	
## -remarks

## -see-also