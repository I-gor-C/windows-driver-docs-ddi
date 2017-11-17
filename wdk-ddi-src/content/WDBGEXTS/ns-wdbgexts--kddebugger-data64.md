---
UID: NS.wdbgexts._KDDEBUGGER_DATA64
title: KDDEBUGGER_DATA64
author: windows-driver-content
description: 
ms.assetid: ef1cdf54-b76d-4ac2-bde1-dc1ef23067e2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KDDEBUGGER_DATA64, KDDEBUGGER_DATA64, *PKDDEBUGGER_DATA64
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

# KDDEBUGGER_DATA64 structure

## -description



## -struct-fields

### -field DBGKD_DEBUG_DATA_HEADER64 Header			
 	
### -field ULONG64 KernBase			
 	
### -field ULONG64 BreakpointWithStatus			
 	
### -field ULONG64 SavedContext			
 	
### -field USHORT ThCallbackStack			
 	
### -field USHORT NextCallback			
 	
### -field USHORT FramePointer			
 	
### -field USHORT  : 1 PaeEnabled			
 	
### -field ULONG64 KiCallUserMode			
 	
### -field ULONG64 KeUserCallbackDispatcher			
 	
### -field ULONG64 PsLoadedModuleList			
 	
### -field ULONG64 PsActiveProcessHead			
 	
### -field ULONG64 PspCidTable			
 	
### -field ULONG64 ExpSystemResourcesList			
 	
### -field ULONG64 ExpPagedPoolDescriptor			
 	
### -field ULONG64 ExpNumberOfPagedPools			
 	
### -field ULONG64 KeTimeIncrement			
 	
### -field ULONG64 KeBugCheckCallbackListHead			
 	
### -field ULONG64 KiBugcheckData			
 	
### -field ULONG64 IopErrorLogListHead			
 	
### -field ULONG64 ObpRootDirectoryObject			
 	
### -field ULONG64 ObpTypeObjectType			
 	
### -field ULONG64 MmSystemCacheStart			
 	
### -field ULONG64 MmSystemCacheEnd			
 	
### -field ULONG64 MmSystemCacheWs			
 	
### -field ULONG64 MmPfnDatabase			
 	
### -field ULONG64 MmSystemPtesStart			
 	
### -field ULONG64 MmSystemPtesEnd			
 	
### -field ULONG64 MmSubsectionBase			
 	
### -field ULONG64 MmNumberOfPagingFiles			
 	
### -field ULONG64 MmLowestPhysicalPage			
 	
### -field ULONG64 MmHighestPhysicalPage			
 	
### -field ULONG64 MmNumberOfPhysicalPages			
 	
### -field ULONG64 MmMaximumNonPagedPoolInBytes			
 	
### -field ULONG64 MmNonPagedSystemStart			
 	
### -field ULONG64 MmNonPagedPoolStart			
 	
### -field ULONG64 MmNonPagedPoolEnd			
 	
### -field ULONG64 MmPagedPoolStart			
 	
### -field ULONG64 MmPagedPoolEnd			
 	
### -field ULONG64 MmPagedPoolInformation			
 	
### -field ULONG64 MmPageSize			
 	
### -field ULONG64 MmSizeOfPagedPoolInBytes			
 	
### -field ULONG64 MmTotalCommitLimit			
 	
### -field ULONG64 MmTotalCommittedPages			
 	
### -field ULONG64 MmSharedCommit			
 	
### -field ULONG64 MmDriverCommit			
 	
### -field ULONG64 MmProcessCommit			
 	
### -field ULONG64 MmPagedPoolCommit			
 	
### -field ULONG64 MmExtendedCommit			
 	
### -field ULONG64 MmZeroedPageListHead			
 	
### -field ULONG64 MmFreePageListHead			
 	
### -field ULONG64 MmStandbyPageListHead			
 	
### -field ULONG64 MmModifiedPageListHead			
 	
### -field ULONG64 MmModifiedNoWritePageListHead			
 	
### -field ULONG64 MmAvailablePages			
 	
### -field ULONG64 MmResidentAvailablePages			
 	
### -field ULONG64 PoolTrackTable			
 	
### -field ULONG64 NonPagedPoolDescriptor			
 	
### -field ULONG64 MmHighestUserAddress			
 	
### -field ULONG64 MmSystemRangeStart			
 	
### -field ULONG64 MmUserProbeAddress			
 	
### -field ULONG64 KdPrintCircularBuffer			
 	
### -field ULONG64 KdPrintCircularBufferEnd			
 	
### -field ULONG64 KdPrintWritePointer			
 	
### -field ULONG64 KdPrintRolloverCount			
 	
### -field ULONG64 MmLoadedUserImageList			
 	
### -field ULONG64 NtBuildLab			
 	
### -field ULONG64 KiNormalSystemCall			
 	
### -field ULONG64 KiProcessorBlock			
 	
### -field ULONG64 MmUnloadedDrivers			
 	
### -field ULONG64 MmLastUnloadedDriver			
 	
### -field ULONG64 MmTriageActionTaken			
 	
### -field ULONG64 MmSpecialPoolTag			
 	
### -field ULONG64 KernelVerifier			
 	
### -field ULONG64 MmVerifierData			
 	
### -field ULONG64 MmAllocatedNonPagedPool			
 	
### -field ULONG64 MmPeakCommitment			
 	
### -field ULONG64 MmTotalCommitLimitMaximum			
 	
### -field ULONG64 CmNtCSDVersion			
 	
### -field ULONG64 MmPhysicalMemoryBlock			
 	
### -field ULONG64 MmSessionBase			
 	
### -field ULONG64 MmSessionSize			
 	
### -field ULONG64 MmSystemParentTablePage			
 	
### -field ULONG64 MmVirtualTranslationBase			
 	
### -field USHORT OffsetKThreadNextProcessor			
 	
### -field USHORT OffsetKThreadTeb			
 	
### -field USHORT OffsetKThreadKernelStack			
 	
### -field USHORT OffsetKThreadInitialStack			
 	
### -field USHORT OffsetKThreadApcProcess			
 	
### -field USHORT OffsetKThreadState			
 	
### -field USHORT OffsetKThreadBStore			
 	
### -field USHORT OffsetKThreadBStoreLimit			
 	
### -field USHORT SizeEProcess			
 	
### -field USHORT OffsetEprocessPeb			
 	
### -field USHORT OffsetEprocessParentCID			
 	
### -field USHORT OffsetEprocessDirectoryTableBase			
 	
### -field USHORT SizePrcb			
 	
### -field USHORT OffsetPrcbDpcRoutine			
 	
### -field USHORT OffsetPrcbCurrentThread			
 	
### -field USHORT OffsetPrcbMhz			
 	
### -field USHORT OffsetPrcbCpuType			
 	
### -field USHORT OffsetPrcbVendorString			
 	
### -field USHORT OffsetPrcbProcStateContext			
 	
### -field USHORT OffsetPrcbNumber			
 	
### -field USHORT SizeEThread			
 	
### -field ULONG64 KdPrintCircularBufferPtr			
 	
### -field ULONG64 KdPrintBufferSize			
 	
### -field ULONG64 KeLoaderBlock			
 	
### -field USHORT SizePcr			
 	
### -field USHORT OffsetPcrSelfPcr			
 	
### -field USHORT OffsetPcrCurrentPrcb			
 	
### -field USHORT OffsetPcrContainedPrcb			
 	
### -field USHORT OffsetPcrInitialBStore			
 	
### -field USHORT OffsetPcrBStoreLimit			
 	
### -field USHORT OffsetPcrInitialStack			
 	
### -field USHORT OffsetPcrStackLimit			
 	
### -field USHORT OffsetPrcbPcrPage			
 	
### -field USHORT OffsetPrcbProcStateSpecialReg			
 	
### -field USHORT GdtR0Code			
 	
### -field USHORT GdtR0Data			
 	
### -field USHORT GdtR0Pcr			
 	
### -field USHORT GdtR3Code			
 	
### -field USHORT GdtR3Data			
 	
### -field USHORT GdtR3Teb			
 	
### -field USHORT GdtLdt			
 	
### -field USHORT GdtTss			
 	
### -field USHORT Gdt64R3CmCode			
 	
### -field USHORT Gdt64R3CmTeb			
 	
### -field ULONG64 IopNumTriageDumpDataBlocks			
 	
### -field ULONG64 IopTriageDumpDataBlocks			
 	
### -field ULONG64 VfCrashDataBlock			
 	
### -field ULONG64 MmBadPagesDetected			
 	
### -field ULONG64 MmZeroedPageSingleBitErrorsDetected			
 	
### -field ULONG64 EtwpDebuggerData			
 	
### -field USHORT OffsetPrcbContext			
 	
### -field USHORT OffsetPrcbMaxBreakpoints			
 	
### -field USHORT OffsetPrcbMaxWatchpoints			
 	
### -field ULONG OffsetKThreadStackLimit			
 	
### -field ULONG OffsetKThreadStackBase			
 	
### -field ULONG OffsetKThreadQueueListEntry			
 	
### -field ULONG OffsetEThreadIrpList			
 	
### -field USHORT OffsetPrcbIdleThread			
 	
### -field USHORT OffsetPrcbNormalDpcState			
 	
### -field USHORT OffsetPrcbDpcStack			
 	
### -field USHORT OffsetPrcbIsrStack			
 	
### -field USHORT SizeKDPC_STACK_FRAME			
 	
### -field USHORT OffsetKPriQueueThreadListHead			
 	
### -field USHORT OffsetKThreadWaitReason			
 	
### -field USHORT Padding			
 	
### -field ULONG64 PteBase			
 	
## -remarks

## -see-also