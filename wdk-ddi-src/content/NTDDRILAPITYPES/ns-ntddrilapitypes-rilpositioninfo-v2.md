---
UID: NS.ntddrilapitypes.RILPOSITIONINFO_V2
title: RILPOSITIONINFO_V2
author: windows-driver-content
description: 
ms.assetid: 67fb7b3d-79d1-4397-b5bb-11633b607590
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RILPOSITIONINFO_V2, RILPOSITIONINFO_V2, *LPRILPOSITIONINFO_V2, RILPOSITIONINFO, *LPRILPOSITIONINFO
req.header: ntddrilapitypes.h
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

# RILPOSITIONINFO_V2 structure

## -description



## -struct-fields

### -field DWORD cbSize			
 	
### -field DWORD dwSystemType			
 	
### -field RILPOSITIONINFOGSM stGSMServingCellInfo			
 	
### -field RILPOSITIONINFOUMTS stUMTSServingCellInfo			
 	
### -field RILPOSITIONINFOTDSCDMA stTDSCDMAServingCellInfo			
 	
### -field RILPOSITIONINFOLTE stLTEServingCellInfo			
 	
### -field DWORD dwCntGSMNMR			
 	
### -field RILGSMNMR [15] rgNMR			
 	
### -field DWORD dwCntUMTSMRL			
 	
### -field RILUMTSMRL [15] ruMRL			
 	
### -field DWORD dwCntTDSCDMAMRL			
 	
### -field RILTDSCDMAMRL [15] rtMRL			
 	
### -field DWORD dwCntEUTRAMRL			
 	
### -field RILEUTRAMRL [15] reMRL			
 	
### -field DWORD dwCntC2KMRL			
 	
### -field RILC2KMRL [12] rc2kMRL			
 	
## -remarks

## -see-also