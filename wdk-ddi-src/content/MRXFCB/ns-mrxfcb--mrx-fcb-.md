---
UID: NS.mrxfcb._MRX_FCB_
title: MRX_FCB_
author: windows-driver-content
description: 
ms.assetid: f17198ac-d332-4904-8682-eab909b19f59
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MRX_FCB_, MRX_FCB, *PMRX_FCB
req.header: mrxfcb.h
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

# MRX_FCB_ structure

## -description



## -struct-fields

### -field FSRTL_ADVANCED_FCB_HEADER Header			
 	
### -field PMRX_NET_ROOT pNetRoot			
 	
### -field PVOID Context			
 	
### -field PVOID Context2			
 	
### -field __volatile ULONG NodeReferenceCount			
 	
### -field ULONG FcbState			
 	
### -field __volatile CLONG UncleanCount			
 	
### -field CLONG UncachedUncleanCount			
 	
### -field __volatile CLONG OpenCount			
 	
### -field __volatile ULONG OutstandingLockOperationsCount			
 	
### -field ULONGLONG ActualAllocationLength			
 	
### -field ULONG Attributes			
 	
### -field BOOLEAN IsFileWritten			
 	
### -field BOOLEAN fShouldBeOrphaned			
 	
### -field BOOLEAN fMiniInited			
 	
### -field UCHAR CachedNetRootType			
 	
### -field LIST_ENTRY SrvOpenList			
 	
### -field ULONG SrvOpenListVersion			
 	
## -remarks

## -see-also