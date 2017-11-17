---
UID: NS.fcb._FCB
title: FCB
author: windows-driver-content
description: 
ms.assetid: dfac079f-18b9-4ff9-9105-510591b9ec71
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: FCB, FCB, *PFCB
req.header: fcb.h
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

# FCB structure

## -description



## -struct-fields

### -field union __unnamed_union_0bd5_7			
 	
### -field PV_NET_ROOT VNetRoot			
 	
### -field PNON_PAGED_FCB NonPaged			
 	
### -field LIST_ENTRY ScavengerFinalizationList			
 	
### -field PKEVENT pBufferingStateChangeCompletedEvent			
 	
### -field LONG NumberOfBufferingStateChangeWaiters			
 	
### -field RX_FCB_TABLE_ENTRY FcbTableEntry			
 	
### -field UNICODE_STRING PrivateAlreadyPrefixedName			
 	
### -field BOOLEAN UpperFinalizationDone			
 	
### -field RX_BLOCK_CONDITION Condition			
 	
### -field PRX_FSD_DISPATCH_VECTOR PrivateDispatchVector			
 	
### -field PRDBSS_DEVICE_OBJECT RxDeviceObject			
 	
### -field PMINIRDR_DISPATCH MRxDispatch			
 	
### -field PFAST_IO_DISPATCH MRxFastIoDispatch			
 	
### -field PSRV_OPEN InternalSrvOpen			
 	
### -field PFOBX InternalFobx			
 	
### -field SHARE_ACCESS ShareAccess			
 	
### -field SHARE_ACCESS ShareAccessPerSrvOpens			
 	
### -field ULONG NumberOfLinks			
 	
### -field LARGE_INTEGER CreationTime			
 	
### -field LARGE_INTEGER LastAccessTime			
 	
### -field LARGE_INTEGER LastWriteTime			
 	
### -field LARGE_INTEGER LastChangeTime			
 	
### -field ULONG ulFileSizeVersion			
 	
### -field FILE_LOCK FileLock			
 	
### -field PFAST_MUTEX FileSizeLock			
 	
### -field ULONG EaModificationCount			
 	
### -field FCB_BUFFERED_LOCKS BufferedLocks			
 	
### -field PNON_PAGED_FCB CopyOfNonPaged			
 	
### -field ULONG [RX_FCBTRACKER_CASE_MAXIMUM] FcbAcquires			
 	
### -field ULONG [RX_FCBTRACKER_CASE_MAXIMUM] FcbReleases			
 	
### -field PCHAR PagingIoResourceFile			
 	
### -field ULONG PagingIoResourceLine			
 	
### -field LOWIO_PER_FCB_INFO LowIoPerFcbInfo			
 	
## -remarks

## -see-also