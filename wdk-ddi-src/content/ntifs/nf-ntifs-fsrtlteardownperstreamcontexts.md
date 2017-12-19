---
UID: NF.ntifs.FsRtlTeardownPerStreamContexts
title: FsRtlTeardownPerStreamContexts function
author: windows-driver-content
description: The FsRtlTeardownPerStreamContexts routine frees all per-stream context structures associated with a given FSRTL_ADVANCED_FCB_HEADER structure.
old-location: ifsk\fsrtlteardownperstreamcontexts.htm
old-project: ifsk
ms.assetid: a37a921c-748a-4ac2-99c7-a6cf987a8f54
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FsRtlTeardownPerStreamContexts
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Update Rollup for Windows 2000 Service Pack 4 (SP4) and on Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlTeardownPerStreamContexts
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
req.irql: <= APC_LEVEL
---

# FsRtlTeardownPerStreamContexts function



## -description
The <b>FsRtlTeardownPerStreamContexts</b> routine frees all per-stream context structures associated with a given FSRTL_ADVANCED_FCB_HEADER structure. 



## -syntax

````
VOID FsRtlTeardownPerStreamContexts(
  _In_ PFSRTL_ADVANCED_FCB_HEADER AdvancedHeader
);
````


## -parameters

### -param AdvancedHeader [in]

Pointer to the FSRTL_ADVANCED_FCB_HEADER structure. 


## -returns
None


## -remarks
File systems call <b>FsRtlTeardownPerStreamContexts</b> to free all per-stream context structures associated with a given FSRTL_ADVANCED_FCB_HEADER structure. When a file system tears down the stream context object for a file stream, it must call <b>FsRtlTeardownPerStreamContexts</b>, which in turn calls the <i>FreeCallback</i> routines of all per-stream context structures associated with the file stream. 

To avoid conflicts in synchronization, the <b>FsRtlTeardownPerStreamContexts</b> routine releases the lock for the per file context objects before calling <i>FreeCallback</i>. This avoids blocking access to the to the per file context objects by the filter for own list operations, such as removal with <a href="ifsk.fsrtlremoveperstreamcontext">FsRtlRemovePerStreamContext</a>.


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
Version

</th>
<td width="70%">
This routine is available on Update Rollup for Windows 2000 Service Pack 4 (SP4) and on Microsoft Windows XP and later. 

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
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsrtl_advanced_fcb_header">FSRTL_ADVANCED_FCB_HEADER</a>
</dt>
<dt>
<a href="ifsk.fsrtl_per_stream_context">FSRTL_PER_STREAM_CONTEXT</a>
</dt>
<dt>
<a href="ifsk.fsrtlgetperstreamcontextpointer">FsRtlGetPerStreamContextPointer</a>
</dt>
<dt>
<a href="ifsk.fsrtlinitperstreamcontext">FsRtlInitPerStreamContext</a>
</dt>
<dt>
<a href="ifsk.fsrtlinsertperstreamcontext">FsRtlInsertPerStreamContext</a>
</dt>
<dt>
<a href="ifsk.fsrtllookupperstreamcontext">FsRtlLookupPerStreamContext</a>
</dt>
<dt>
<a href="ifsk.fsrtlremoveperstreamcontext">FsRtlRemovePerStreamContext</a>
</dt>
<dt>
<a href="ifsk.fsrtlsetupadvancedheader">FsRtlSetupAdvancedHeader</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547285">FsRtlSupportsPerStreamContexts</a>
</dt>
<dt>
<a href="ifsk.tracking_per_stream_context_in_a_legacy_file_system_filter_driver">Tracking Per-Stream Context in a Legacy File System Filter Driver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlTeardownPerStreamContexts routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

