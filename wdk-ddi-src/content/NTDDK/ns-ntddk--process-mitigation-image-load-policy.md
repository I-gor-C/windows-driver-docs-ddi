---
UID: NS.ntddk._PROCESS_MITIGATION_IMAGE_LOAD_POLICY
title: PROCESS_MITIGATION_IMAGE_LOAD_POLICY
author: windows-driver-content
description: 
ms.assetid: 939de9c5-98d1-4bfb-8653-b10a4604a4d0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PROCESS_MITIGATION_IMAGE_LOAD_POLICY, PROCESS_MITIGATION_IMAGE_LOAD_POLICY, *PPROCESS_MITIGATION_IMAGE_LOAD_POLICY
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

# PROCESS_MITIGATION_IMAGE_LOAD_POLICY structure

## -description



## -struct-fields

### -field union DUMMYUNIONNAME			
 	
### -field __unnamed_union_0c2a_39 __unnamed_union_0c2a_39			
 	
### -field ULONG  : 1 NoRemoteImages			
 	
### -field ULONG  : 1 NoLowMandatoryLabelImages			
 	
### -field ULONG  : 1 PreferSystem32Images			
 	
### -field ULONG  : 1 AuditNoRemoteImages			
 	
### -field ULONG  : 1 AuditNoLowMandatoryLabelImages			
 	
### -field ULONG  : 27 ReservedFlags			
 	
### -field ULONG Flags			
 	
## -remarks

## -see-also