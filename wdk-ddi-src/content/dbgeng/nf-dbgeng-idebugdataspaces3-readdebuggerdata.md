---
UID: NF.dbgeng.IDebugDataSpaces3.ReadDebuggerData
title: IDebugDataSpaces3::ReadDebuggerData
author: windows-driver-content
description: The ReadDebuggerData method returns information about the target that the debugger engine has queried or determined during the current session.
old-location: debugger\readdebuggerdata.htm
old-project: debugger
ms.assetid: 54e4d3b9-db9d-4844-938f-c8ca8819d182
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugDataSpaces3, ReadDebuggerData, IDebugDataSpaces3::ReadDebuggerData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces.ReadDebuggerData,IDebugDataSpaces2.ReadDebuggerData,IDebugDataSpaces3.ReadDebuggerData,IDebugDataSpaces4.ReadDebuggerData
req.alt-loc: dbgeng.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IDebugDataSpaces3
---

# IDebugDataSpaces3::ReadDebuggerData method



## -description
<p>The <b>ReadDebuggerData</b> method returns information about the target that the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> has queried or determined during the current session.  The available information includes the locations of certain key target kernel locations, specific status values, and a number of other things.</p>


## -syntax

````
HRESULT ReadDebuggerData(
  [in]            ULONG  Index,
  [out]           PVOID  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG DataSize
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index of the data to retrieve.  The following values are valid:</p>
<table>
<tr>
<th>Value</th>
<th>Return Type</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KernBase</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the base address of the kernel image.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_BreakpointWithStatusAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel function <b>BreakpointWithStatusInstruction</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SavedContextAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of saved context record during a bugcheck.  It is only valid after a bugcheck.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KiCallUserModeAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel function <b>KiCallUserMode</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KeUserCallbackDispatcherAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the kernel variable <b>KeUserCallbackDispatcher</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_PsLoadedModuleListAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>PsLoadedModuleList</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_PsActiveProcessHeadAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>PsActiveProcessHead</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_PspCidTableAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>PspCidTable</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_ExpSystemResourcesListAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>ExpSystemResourcesList</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_ExpPagedPoolDescriptorAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>ExpPagedPoolDescriptor</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_ExpNumberOfPagedPoolsAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>ExpNumberOfPagedPools</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KeTimeIncrementAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>KeTimeIncrement</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KeBugCheckCallbackListHeadAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>KeBugCheckCallbackListHead</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KiBugcheckDataAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the kernel variable <b>KiBugCheckData</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_IopErrorLogListHeadAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>IopErrorLogListHead</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_ObpRootDirectoryObjectAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>ObpRootDirectoryObject</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_ObpTypeObjectTypeAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>ObpTypeObjectType</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSystemCacheStartAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmSystemCacheStart</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSystemCacheEndAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmSystemCacheEnd</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSystemCacheWsAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmSystemCacheWs</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmPfnDatabaseAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmPfnDatabase</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSystemPtesStartAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the kernel variable <b>MmSystemPtesStart</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSystemPtesEndAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the kernel variable <b>MmSystemPtesEnd</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSubsectionBaseAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmSubsectionBase</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmNumberOfPagingFilesAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmNumberOfPagingFiles</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmLowestPhysicalPageAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmLowestPhysicalPage</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmHighestPhysicalPageAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmHighestPhysicalPage</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmNumberOfPhysicalPagesAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmNumberOfPhysicalPages</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmMaximumNonPagedPoolInBytesAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmMaximumNonPagedPoolInBytes</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmNonPagedSystemStartAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmNonPagedSystemStart</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmNonPagedPoolStartAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmNonPagedPoolStart</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmNonPagedPoolEndAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmNonPagedPoolEnd</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmPagedPoolStartAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmPagedPoolStart</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmPagedPoolEndAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmPagedPoolEnd</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmPagedPoolInformationAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmPagedPoolInfo</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmPageSize</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the page size.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSizeOfPagedPoolInBytesAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmSizeOfPagedPoolInBytes</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmTotalCommitLimitAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmTotalCommitLimit</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmTotalCommittedPagesAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmTotalCommittedPages</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSharedCommitAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmSharedCommit</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmDriverCommitAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmDriverCommit</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmProcessCommitAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmProcessCommit</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmPagedPoolCommitAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmPagedPoolCommit</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmExtendedCommitAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmExtendedCommit</b>..</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmZeroedPageListHeadAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmZeroedPageListHead</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmFreePageListHeadAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmFreePageListHead</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmStandbyPageListHeadAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmStandbyPageListHead</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmModifiedPageListHeadAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmModifiedPageListHead</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmModifiedNoWritePageListHeadAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmModifiedNoWritePageListHead</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmAvailablePagesAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmAvailablePages</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmResidentAvailablePagesAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmResidentAvailablePages</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_PoolTrackTableAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>PoolTrackTable</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_NonPagedPoolDescriptorAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>NonPagedPoolDescriptor</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmHighestUserAddressAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmHighestUserAddress</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSystemRangeStartAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmSystemRangeStart</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmUserProbeAddressAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmUserProbeAddress</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KdPrintCircularBufferAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the kernel variable <b>KdPrintDefaultCircularBuffer</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KdPrintCircularBufferEndAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the end of the array KdPrintDefaultCircularBuffer</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KdPrintWritePointerAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>KdPrintWritePointer</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KdPrintRolloverCountAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable 
<b>KdPrintRolloverCount</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmLoadedUserImageListAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmLoadedUserImageList</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_PaeEnabled</p>
</td>
<td>
<p>BOOLEAN</p>
</td>
<td>
<p>Returns <b>TRUE</b> when the target system has PAE enabled.</p>
<p>Returns <b>FALSE</b> otherwise.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SharedUserData</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address in the target of the shared user-mode structure, KUSER_SHARED_DATA.  The KUSER_SHARED_DATA structure is defined in ntddk.h (in the Windows Driver Kit) and ntexapi.h (in the Windows SDK).</p>
<p>Some of the information contained in this structure is displayed by the debugger extension <b>!kuser</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_ProductType</p>
</td>
<td>
<p>ULONG</p>
</td>
<td>
<p>Returns the value of the <b>NtProductType</b> field in the shared user-mode page.</p>
<p>This value should be interpreted the same way as the <b>wProductType</b> field of the structure OSVERSIONINFOEX, which is documented in the Windows SDK.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SuiteMask</p>
</td>
<td>
<p>ULONG</p>
</td>
<td>
<p>Returns the value of the <b>SuiteMask</b> field in the shared user-mode page.</p>
<p>This value should be interpreted the same way as the <b>wSuiteMask</b> field of the structure OSVERSIONINFOEX, which is documented in the Windows SDK.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_DumpWriterStatus</p>
</td>
<td>
<p>ULONG</p>
</td>
<td>
<p>Returns the status of the writer of the dump file.  This value is operating system and dump file type specific.</p>
</td>
</tr>
</table>
<p> </p>
<p>The following values are valid for Windows XP and later versions of Windows:</p>
<table>
<tr>
<th>Value</th>
<th>Return Type</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_DATA_NtBuildLabAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>NtBuildLab</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KiNormalSystemCall</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>(Itanium only) Returns the address of the kernel function <b>KiNormalSystemCall</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KiProcessorBlockAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the kernel variable <b>KiProcessorBlock</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmUnloadedDriversAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmUnloadedDrivers</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmLastUnloadedDriverAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmLastUnloadedDriver</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmTriageActionTakenAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>VerifierTriageActionTaken</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSpecialPoolTagAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmSpecialPoolTag</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KernelVerifierAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>KernelVerifier</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmVerifierDataAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmVerifierData</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmAllocatedNonPagedPoolAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmAllocatedNonPagedPool</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmPeakCommitmentAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmPeakCommitment</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmTotalCommitLimitMaximumAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmTotalCommitLimitMaximum</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_CmNtCSDVersionAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>CmNtCSDVersion</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmPhysicalMemoryBlockAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmPhysicalMemoryBlock</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSessionBase</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmSessionBase</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSessionSize</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmSessionSize</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmSystemParentTablePage</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>(Itanium only) Returns the address of the kernel variable <b>MmSystemParentTablePage</b>.</p>
</td>
</tr>
</table>
<p> </p>
<p>The following values are valid for Windows Server 2003 and later versions of Windows:</p>
<table>
<tr>
<th>Value</th>
<th>Return Type</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_DATA_MmVirtualTranslationBase</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>MmVirtualTranslationBase</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetKThreadNextProcessor</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>NextProcessor</b> field in the KTHREAD structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetKThreadTeb</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>Teb</b> field in the KTHREAD structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetKThreadKernelStack</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>KernelStack</b> field in the KTHREAD structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetKThreadInitialStack</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>InitialStack</b> field in the KTHREAD structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetKThreadApcProcess</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the ApcState.Process field in the KTHREAD structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetKThreadState</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>State</b> field in the KTHREAD structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetKThreadBStore</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>(Itanium only) Returns the offset of the <b>InitialBStore</b> field in the KTHREAD structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetKThreadBStoreLimit</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>(Itanium only) Returns the offset of the <b>BStoreLimit</b> field in the KTHREAD structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SizeEProcess</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the size of the EPROCESS structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetEprocessPeb</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>Peb</b> field in the EPROCESS structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetEprocessParentCID</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>InheritedFromUniqueProcessId</b> field in the EPROCESS structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetEprocessDirectoryTableBase</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>DirectoryTableBase</b> field in the EPROCESS structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SizePrcb</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the size of the KPRCB structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetPrcbDpcRoutine</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>DpcRoutineActive</b> field in the KPRCB structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetPrcbCurrentThread</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>CurrentThread</b> field in the KPRCB structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetPrcbMhz</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>MHz</b> field in the KPRCB structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetPrcbCpuType</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p><b>For Itanium processors:</b>  Returns the offset of the <b>ProcessorModel</b> field in the KPRCB structure.</p>
<p><b>For all other processors:</b>  Returns the offset of the <b>CpuType</b> field in the KPRCB structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetPrcbVendorString</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p><b>For Itanium processors:</b>  Returns the offset of the <b>ProcessorVendorString</b> field in the KPRCB structure.</p>
<p><b>For all other processors:</b>  Returns the offset of the <b>VendorString</b> field in the KPRCB structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetPrcbProcessorState</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the ProcessorState.ContextFrame field in the KPRCB structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_OffsetPrcbNumber</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the offset of the <b>Number</b> field in the KPRCB structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_SizeEThread</p>
</td>
<td>
<p>USHORT</p>
</td>
<td>
<p>Returns the size of the ETHREAD structure.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KdPrintCircularBufferPtrAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>KdPrintCircularBuffer</b>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KdPrintBufferSizeAddr</p>
</td>
<td>
<p>ULONG64</p>
</td>
<td>
<p>Returns the address of the kernel variable <b>KdPrintBufferSize</b>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Receives the value of the specified debugger data.  The "Return Type" column in the above table specifies the data type that is returned.  The data can be accessed by casting <i>Buffer</i> to a pointer to that type.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.</p>
</dd>

### -param <i>DataSize</i> [out, optional]

<dd>
<p>Receives the number of bytes used in the buffer <i>Buffer</i>.  If <i>DataSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>Some or all of the values may be unavailable in certain debugging sessions.  For example, some of the values are only available for particular versions of the operating system.</p>

<p>For details on the different values returned by <b>ReadDebuggerData</b>, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich, the Microsoft Windows SDK, and the Windows Driver Kit (WDK).</p>

<p>Some or all of the values may be unavailable in certain debugging sessions.  For example, some of the values are only available for particular versions of the operating system.</p>

<p>For details on the different values returned by <b>ReadDebuggerData</b>, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich, the Microsoft Windows SDK, and the Windows Driver Kit (WDK).</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>