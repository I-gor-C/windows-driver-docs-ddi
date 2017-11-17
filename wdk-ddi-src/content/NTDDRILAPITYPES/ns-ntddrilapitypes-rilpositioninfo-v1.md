---
UID: NS.ntddrilapitypes.RILPOSITIONINFO_V1
title: RILPOSITIONINFO_V1
author: windows-driver-content
description: 
ms.assetid: 30ffedc8-70ca-4651-ab57-a0366784b264
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RILPOSITIONINFO_V1, RILPOSITIONINFO_V1, *LPRILPOSITIONINFO_V1
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

# RILPOSITIONINFO_V1 structure

## -description



## -struct-fields

### -field DWORD cbSize			
 	
### -field DWORD dwSystemType			
 	
### -field RILPOSITIONINFOGSM stGSMServingCellInfo			
 	
### -field RILPOSITIONINFOUMTS stUMTSServingCellInfo			
 	
### -field RILPOSITIONINFOLTE stLTEServingCellInfo			
 	
### -field DWORD dwCntGSMNMR			
 	
### -field RILGSMNMR [15] rgNMR			
 	
### -field DWORD dwCntUMTSMRL			
 	
### -field RILUMTSMRL [15] ruMRL			
 	
### -field DWORD dwCntEUTRAMRL			
 	
### -field RILEUTRAMRL [15] reMRL			
 	
### -field DWORD dwCntC2KMRL			
 	
### -field RILC2KMRL [12] rc2kMRL			
 	
## -remarks

## -see-also