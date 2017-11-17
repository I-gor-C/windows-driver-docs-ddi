---
UID: NS.ntifs._SE_AUDIT_INFO
title: SE_AUDIT_INFO
author: windows-driver-content
description: 
ms.assetid: c6e2bdd6-43eb-4b4b-af8d-a840c2737570
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SE_AUDIT_INFO, SE_AUDIT_INFO, *PSE_AUDIT_INFO
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

# SE_AUDIT_INFO structure

## -description



## -struct-fields

### -field ULONG Size			
 	
### -field AUDIT_EVENT_TYPE AuditType			
 	
### -field SE_AUDIT_OPERATION AuditOperation			
 	
### -field ULONG AuditFlags			
 	
### -field UNICODE_STRING SubsystemName			
 	
### -field UNICODE_STRING ObjectTypeName			
 	
### -field UNICODE_STRING ObjectName			
 	
### -field PVOID HandleId			
 	
### -field GUID * TransactionId			
 	
### -field LUID * OperationId			
 	
### -field BOOLEAN ObjectCreation			
 	
### -field BOOLEAN GenerateOnClose			
 	
## -remarks

## -see-also