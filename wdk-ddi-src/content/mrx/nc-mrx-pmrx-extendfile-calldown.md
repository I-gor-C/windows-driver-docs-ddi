---
UID: NC.mrx.PMRX_EXTENDFILE_CALLDOWN
title: PMRX_EXTENDFILE_CALLDOWN
author: windows-driver-content
description: The MRxExtendForCache routine is called by RDBSS to request that a network mini-redirector extend a file when the file is being cached by the cache manager.
old-location: ifsk\mrxextendforcache.htm
old-project: ifsk
ms.assetid: 2fde7925-040b-4a8c-8a95-29321f1ae474
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SetDSMCounters_IN, SetDSMCounters_IN, *PSetDSMCounters_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: mrx.h
req.include-header: Mrx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MRxExtendForCache
req.alt-loc: mrx.h
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
req.iface: 
---

# PMRX_EXTENDFILE_CALLDOWN callback



## -description
<p>The<i> MRxExtendForCache</i> routine is called by <a href="ifsk.the_rdbss_driver_and_library">RDBSS</a> to request that a network mini-redirector extend a file when the file is being cached by the cache manager. </p>


## -prototype

````
PMRX_EXTENDFILE_CALLDOWN MRxExtendForCache;

ULONG MRxExtendForCache(
  _Inout_ PRX_CONTEXT    RxContext,
  _Inout_ PLARGE_INTEGER pNewFileSize,
  _Out_   PLARGE_INTEGER pNewAllocationSize
)
{ ... }
````


## -parameters
<dl>

### -param <i>RxContext</i> [in, out]

<dd>
<p>A pointer to the RX_CONTEXT structure. This parameter contains the IRP that is requesting the operation. </p>
</dd>

### -param <i>pNewFileSize</i> [in, out]

<dd>
<p>A pointer to the LARGE_INTEGER structure indicating the byte count of the new file size. </p>
</dd>

### -param <i>pNewAllocationSize</i> [out]

<dd>
<p>A pointer to the LARGE_INTEGER structure for storing the new allocation size when <i>MRxExtendForCache</i> returns. </p>
</dd>
</dl>

## -returns
<p><i>MRxExtendForCache</i> returns STATUS_SUCCESS on success or an error code on failure. </p>

## -remarks
<p><i>MRxExtendForCache</i> handles network requests to extend the file for cached I/O.</p>

<p>Before calling<i> MRxExtendForCache</i>, RDBSS modifies the following members in the RX_CONTEXT structure pointed to by the <i>RxContext</i> parameter:</p><dl>
<dd>
<p><b>LowIoContext.Operation </b>is set to LOWIO_OP_WRITE</p>
</dd>
<dd>
<p><b>LowIoContext.ParamsFor.ReadWrite.Flags</b> has the LOWIO_READWRITEFLAG_EXTENDING_FILESIZE bit set</p>
</dd>
</dl><p><b>LowIoContext.Operation </b>is set to LOWIO_OP_WRITE</p>

<p><b>LowIoContext.ParamsFor.ReadWrite.Flags</b> has the LOWIO_READWRITEFLAG_EXTENDING_FILESIZE bit set</p>

<p>A network mini-redirector that caches file or directory information may need to invalidate its cache information when the file is extended.</p>

<p><i>MRxExtendForCache</i> handles network requests to extend the file for cached I/O.</p>

<p>Before calling<i> MRxExtendForCache</i>, RDBSS modifies the following members in the RX_CONTEXT structure pointed to by the <i>RxContext</i> parameter:</p><dl>
<dd>
<p><b>LowIoContext.Operation </b>is set to LOWIO_OP_WRITE</p>
</dd>
<dd>
<p><b>LowIoContext.ParamsFor.ReadWrite.Flags</b> has the LOWIO_READWRITEFLAG_EXTENDING_FILESIZE bit set</p>
</dd>
</dl><p><b>LowIoContext.Operation </b>is set to LOWIO_OP_WRITE</p>

<p><b>LowIoContext.ParamsFor.ReadWrite.Flags</b> has the LOWIO_READWRITEFLAG_EXTENDING_FILESIZE bit set</p>

<p>A network mini-redirector that caches file or directory information may need to invalidate its cache information when the file is extended.</p>

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
<dt>Mrx.h (include Mrx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549838">MRxAreFilesAliased</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549841">MRxCleanupFobx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549845">MRxCloseSrvOpen</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549847">MRxCollapseOpen</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549862">MRxCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549871">MRxDeallocateForFcb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549872">MRxDeallocateForFobx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549879">MRxExtendForNonCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550669">MRxFlush</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550677">MRxForceClosed</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550691">MRxIsLockRealizable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550817">MRxShouldTryToCollapseThisOpen</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550839">MRxTruncate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550844">MRxZeroExtend</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxExtendForCache routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
