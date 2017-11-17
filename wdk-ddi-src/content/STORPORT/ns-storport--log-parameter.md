---
UID: NS.storport._LOG_PARAMETER
title: LOG_PARAMETER
author: windows-driver-content
description: 
ms.assetid: 052baf5e-b068-4308-b194-c808341ff39e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: LOG_PARAMETER, LOG_PARAMETER, *PLOG_PARAMETER
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

# LOG_PARAMETER structure

## -description



## -struct-fields

### -field union __unnamed_union_0c6c_27			
 	
### -field LOG_PARAMETER_HEADER Header			
 	
### -field UCHAR [4] ResourceCount			
 	
### -field UCHAR  : 2 Scope			
 	
### -field UCHAR  : 6 Reserved1			
 	
### -field UCHAR [3] Reserved2			
 	
### -field UCHAR Reserved			
 	
### -field UCHAR Temperature			
 	
### -field UCHAR [4] Year			
 	
### -field UCHAR [2] Week			
 	
### -field UCHAR  : 4 SelfTestResults			
 	
### -field UCHAR  : 1 Reserved1			
 	
### -field UCHAR  : 3 SelfTestCode			
 	
### -field UCHAR SelfTestNumber			
 	
### -field UCHAR [2] PowerOnHours			
 	
### -field UCHAR [8] AddressOfFirstFailure			
 	
### -field UCHAR  : 4 SenseKey			
 	
### -field UCHAR  : 4 Reserved2			
 	
### -field UCHAR AdditionalSenseCode			
 	
### -field UCHAR AdditionalSenseCodeQualifier			
 	
### -field UCHAR VendorSpecific			
 	
### -field UCHAR [3] Reserved			
 	
### -field UCHAR PercentageUsed			
 	
### -field UCHAR [4] PowerOnMinutes			
 	
### -field UCHAR Reserved			
 	
### -field UCHAR ScanStatus			
 	
### -field UCHAR [2] ScansPerformed			
 	
### -field UCHAR [2] ScanProgress			
 	
### -field UCHAR [2] MediumScansPerformed			
 	
### -field UCHAR ASC			
 	
### -field UCHAR ASCQ			
 	
### -field UCHAR MostRecentTemperature			
 	
### -field UCHAR [ANYSIZE_ARRAY] VendorSpecific			
 	
### -field UCHAR [0] AsByte			
 	
## -remarks

## -see-also