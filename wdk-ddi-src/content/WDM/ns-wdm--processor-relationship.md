---
UID: NS.wdm._PROCESSOR_RELATIONSHIP
title: PROCESSOR_RELATIONSHIP
author: windows-driver-content
description: 
ms.assetid: 818939eb-eefe-4bc4-aec2-db462d43e183
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PROCESSOR_RELATIONSHIP, PROCESSOR_RELATIONSHIP, *PPROCESSOR_RELATIONSHIP
req.header: wdm.h
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

# PROCESSOR_RELATIONSHIP structure

## -description



## -struct-fields

### -field UCHAR Flags			
 	
### -field UCHAR EfficiencyClass			
 	
### -field UCHAR [20] Reserved			
 	
### -field USHORT GroupCount			
 	
### -field GROUP_AFFINITY [ANYSIZE_ARRAY] GroupMask			
 	
## -remarks

## -see-also