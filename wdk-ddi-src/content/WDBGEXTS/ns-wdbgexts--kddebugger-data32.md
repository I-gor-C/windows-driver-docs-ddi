---
UID: NS.wdbgexts._KDDEBUGGER_DATA32
title: KDDEBUGGER_DATA32
author: windows-driver-content
description: 
ms.assetid: 5b43f55f-51e8-4038-a8b8-859988d42302
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KDDEBUGGER_DATA32, KDDEBUGGER_DATA32, *PKDDEBUGGER_DATA32
req.header: wdbgexts.h
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

# KDDEBUGGER_DATA32 structure

## -description



## -struct-fields

### -field DBGKD_DEBUG_DATA_HEADER32 Header			
 	
### -field ULONG KernBase			
 	
### -field ULONG BreakpointWithStatus			
 	
### -field ULONG SavedContext			
 	
### -field USHORT ThCallbackStack			
 	
### -field USHORT NextCallback			
 	
### -field USHORT FramePointer			
 	
### -field USHORT  : 1 PaeEnabled			
 	
### -field ULONG KiCallUserMode			
 	
### -field ULONG KeUserCallbackDispatcher			
 	
### -field ULONG PsLoadedModuleList			
 	
### -field ULONG PsActiveProcessHead			
 	
### -field ULONG PspCidTable			
 	
### -field ULONG ExpSystemResourcesList			
 	
### -field ULONG ExpPagedPoolDescriptor			
 	
### -field ULONG ExpNumberOfPagedPools			
 	
### -field ULONG KeTimeIncrement			
 	
### -field ULONG KeBugCheckCallbackListHead			
 	
### -field ULONG KiBugcheckData			
 	
### -field ULONG IopErrorLogListHead			
 	
### -field ULONG ObpRootDirectoryObject			
 	
### -field ULONG ObpTypeObjectType			
 	
### -field ULONG MmSystemCacheStart			
 	
### -field ULONG MmSystemCacheEnd			
 	
### -field ULONG MmSystemCacheWs			
 	
### -field ULONG MmPfnDatabase			
 	
### -field ULONG MmSystemPtesStart			
 	
### -field ULONG MmSystemPtesEnd			
 	
### -field ULONG MmSubsectionBase			
 	
### -field ULONG MmNumberOfPagingFiles			
 	
### -field ULONG MmLowestPhysicalPage			
 	
### -field ULONG MmHighestPhysicalPage			
 	
### -field ULONG MmNumberOfPhysicalPages			
 	
### -field ULONG MmMaximumNonPagedPoolInBytes			
 	
### -field ULONG MmNonPagedSystemStart			
 	
### -field ULONG MmNonPagedPoolStart			
 	
### -field ULONG MmNonPagedPoolEnd			
 	
### -field ULONG MmPagedPoolStart			
 	
### -field ULONG MmPagedPoolEnd			
 	
### -field ULONG MmPagedPoolInformation			
 	
### -field ULONG MmPageSize			
 	
### -field ULONG MmSizeOfPagedPoolInBytes			
 	
### -field ULONG MmTotalCommitLimit			
 	
### -field ULONG MmTotalCommittedPages			
 	
### -field ULONG MmSharedCommit			
 	
### -field ULONG MmDriverCommit			
 	
### -field ULONG MmProcessCommit			
 	
### -field ULONG MmPagedPoolCommit			
 	
### -field ULONG MmExtendedCommit			
 	
### -field ULONG MmZeroedPageListHead			
 	
### -field ULONG MmFreePageListHead			
 	
### -field ULONG MmStandbyPageListHead			
 	
### -field ULONG MmModifiedPageListHead			
 	
### -field ULONG MmModifiedNoWritePageListHead			
 	
### -field ULONG MmAvailablePages			
 	
### -field ULONG MmResidentAvailablePages			
 	
### -field ULONG PoolTrackTable			
 	
### -field ULONG NonPagedPoolDescriptor			
 	
### -field ULONG MmHighestUserAddress			
 	
### -field ULONG MmSystemRangeStart			
 	
### -field ULONG MmUserProbeAddress			
 	
### -field ULONG KdPrintCircularBuffer			
 	
### -field ULONG KdPrintCircularBufferEnd			
 	
### -field ULONG KdPrintWritePointer			
 	
### -field ULONG KdPrintRolloverCount			
 	
### -field ULONG MmLoadedUserImageList			
 	
## -remarks

## -see-also