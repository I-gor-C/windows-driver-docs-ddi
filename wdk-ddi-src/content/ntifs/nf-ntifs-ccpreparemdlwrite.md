---
UID: NF.ntifs.CcPrepareMdlWrite
title: CcPrepareMdlWrite function
author: windows-driver-content
description: The CcPrepareMdlWrite routine provides direct access to cached file memory so that the caller can write data to the file.
old-location: ifsk\ccpreparemdlwrite.htm
old-project: ifsk
ms.assetid: 84e231ad-50a1-471e-b514-6b769f2a7e1e
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: CcPrepareMdlWrite
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcPrepareMdlWrite
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: < DISPATCH_LEVEL
---

# CcPrepareMdlWrite function



## -description
The <b>CcPrepareMdlWrite</b> routine provides direct access to cached file memory so that the caller can write data to the file.


## -syntax

````
VOID CcPrepareMdlWrite(
  _In_  PFILE_OBJECT     FileObject,
  _In_  PLARGE_INTEGER   FileOffset,
  _In_  ULONG            Length,
  _Out_ PMDL             *MdlChain,
  _Out_ PIO_STATUS_BLOCK IoStatus
);
````


## -parameters

### -param FileObject [in]

Pointer to a file object for the cached file. 

### -param FileOffset [in]

Pointer to a variable that specifies the starting byte offset within the cached file where the data is to be written.

### -param Length [in]

Length in bytes of the data to be written to the system cache.

### -param MdlChain [out]

A chain of one or more memory descriptor lists (MDL) describing the pages to which the data is to be written.

### -param IoStatus [out]

Pointer to an IO_STATUS_BLOCK structure. If the call to <b>CcPrepareMdlWrite</b> succeeds, <i>IoStatus.Status</i> is set to STATUS_SUCCESS. Otherwise, it is set to an appropriate NTSTATUS error code. <i>IoStatus.Information</i> is set to the actual number of bytes that were successfully locked down in the MDL chain.

## -returns
None

## -remarks
<b>CcPrepareMdlWrite</b> is similar to <a href="ifsk.cccopywrite">CcCopyWrite</a>, except that the data is not copied to the cached file. Instead, the physical pages to be overwritten in the system cache are locked in memory, and <b>CcPrepareMdlWrite</b> returns one or more memory descriptor lists (MDL) describing the specified byte range. These pages remain locked in memory until <a href="ifsk.ccmdlwritecomplete">CcMdlWriteComplete</a> or <a href="ifsk.ccmdlwriteabort">CcMdlWriteAbort</a> is called. Thus each call to <b>CcPrepareMdlWrite</b> must be followed by a call to <b>CcMdlWriteComplete</b> or <b>CcMdlWriteAbort</b>.

Note that the pages described by the MDL are locked in memory, but not mapped in system space. The caller can perform this mapping by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff554559">MmGetSystemAddressForMdlSafe</a>.

Note that even if the call to <b>CcPrepareMdlWrite</b> fails, one or more MDLs may have been allocated. The caller can examine the value of <i>IoStatus.Information</i> to determine whether this has occurred. If it has, the caller must call <a href="ifsk.ccmdlwritecomplete">CcMdlWriteComplete</a> to free the allocated MDLs.

If any failure occurs, <b>CcPrepareMdlWrite</b> raises a status exception for that particular failure. For example, if a pool allocation failure occurs, <b>CcPrepareMdlWrite</b> raises a STATUS_INSUFFICIENT_RESOURCES exception; if an I/O error occurs, <b>CcPrepareMdlWrite</b> raises the status exception of the I/O error. Therefore, to gain control if a failure occurs, the driver should wrap the call to <b>CcPrepareMdlWrite</b> in a <b>try-except</b> or <b>try-finally</b> statement.

To cache a file, use <a href="ifsk.ccinitializecachemap">CcInitializeCacheMap</a>.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt; DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.cccopywrite">CcCopyWrite</a>
</dt>
<dt>
<a href="ifsk.ccinitializecachemap">CcInitializeCacheMap</a>
</dt>
<dt>
<a href="ifsk.ccmdlwriteabort">CcMdlWriteAbort</a>
</dt>
<dt>
<a href="ifsk.ccmdlwritecomplete">CcMdlWriteComplete</a>
</dt>
<dt>
<a href="kernel.ioallocatemdl">IoAllocateMdl</a>
</dt>
<dt>
<a href="kernel.iobuildpartialmdl">IoBuildPartialMdl</a>
</dt>
<dt>
<a href="kernel.mmgetmdlbytecount">MmGetMdlByteCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554533">MmGetMdlByteOffset</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554537">MmGetMdlPfnArray</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a>
</dt>
<dt>
<a href="kernel.mmgetsystemaddressformdl">MmGetSystemAddressForMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554559">MmGetSystemAddressForMdlSafe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554568">MmInitializeMdl</a>
</dt>
<dt>
<a href="kernel.mmmaplockedpages">MmMapLockedPages</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554660">MmPrepareMdlForReuse</a>
</dt>
<dt>
<a href="kernel.mmprobeandlockpages">MmProbeAndLockPages</a>
</dt>
<dt>
<a href="kernel.mmunlockpages">MmUnlockPages</a>
</dt>
<dt>
<a href="kernel.mmunmaplockedpages">MmUnmapLockedPages</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcPrepareMdlWrite routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
