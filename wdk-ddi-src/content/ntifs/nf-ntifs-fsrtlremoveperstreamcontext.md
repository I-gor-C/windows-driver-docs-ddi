---
UID: NF.ntifs.FsRtlRemovePerStreamContext
title: FsRtlRemovePerStreamContext function
author: windows-driver-content
description: FsRtlRemovePerStreamContext removes a per-stream context structure from the list of per-stream contexts associated with a file stream.
old-location: ifsk\fsrtlremoveperstreamcontext.htm
old-project: ifsk
ms.assetid: 4b046cfa-8f38-4910-8cb3-125395292bd2
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FsRtlRemovePerStreamContext
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
req.alt-api: FsRtlRemovePerStreamContext
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

# FsRtlRemovePerStreamContext function



## -description
<b>FsRtlRemovePerStreamContext</b> removes a per-stream context structure from the list of per-stream contexts associated with a file stream. 



## -syntax

````
PFSRTL_PER_STREAM_CONTEXT FsRtlRemovePerStreamContext(
  _In_     PFSRTL_ADVANCED_FCB_HEADER StreamContext,
  _In_opt_ PVOID                      OwnerId,
  _In_opt_ PVOID                      InstanceId
);
````


## -parameters

### -param StreamContext [in]

Pointer to the FSRTL_ADVANCED_FCB_HEADER structure for the file stream. To get this pointer from a file object, use the <a href="ifsk.fsrtlgetperstreamcontextpointer">FsRtlGetPerStreamContextPointer</a> macro. 


### -param OwnerId [in, optional]

Used to identify context information as belonging to a particular filter driver. 


### -param InstanceId [in, optional]

Used to search for a particular instance of a per-stream context. If not provided, any of the contexts owned by the filter driver is removed and returned. 

If neither the <i>OwnerId</i> nor the <i>InstanceId</i> is provided, any associated per-stream context will be removed and returned.


## -returns
<b>FsRtlRemovePerStreamContext</b> returns a pointer to the per-stream context that is removed. If no match is found, or if the file system does not support filter contexts, <b>FsRtlRemovePerStreamContext</b> returns <b>NULL</b>. 


## -remarks
A file system filter driver calls <b>FsRtlRemovePerStreamContext</b> to remove its own per-stream context structure from the list of per-stream contexts associated with a file stream. 

This routine should only be used when a filter driver needs to discard the context information it has associated with a file stream while the stream is still open. For example, a filter driver might call <b>FsRtlRemovePerStreamContext</b> in the following cases: 

When it receives a request from a user-mode application to stop logging I/O requests on a particular volume. 

When it detects that a file or directory has been renamed. 

When a file stream is closed, the file system is responsible for ensuring that all per-stream contexts associated with that stream are removed and freed. To do this, the file system must call <a href="ifsk.fsrtlteardownperstreamcontexts">FsRtlTeardownPerStreamContexts</a> on the file control block (FCB) or other stream context object for the file stream. <b>FsRtlTeardownPerStreamContexts</b> walks the FilterContexts list, removing each entry and calling its <i>FreeCallback</i> routine. 

Thus, a file system filter driver should not call <b>FsRtlRemovePerStreamContext</b> from within an IRP_MJ_CLOSE or IRP_MJ_PNP dispatch routine. Not only would such a call be unnecessary, but it might also interfere with the file system's call to <a href="ifsk.fsrtlteardownperstreamcontexts">FsRtlTeardownPerStreamContexts</a>. 

To initialize a per-stream context structure, use the <a href="ifsk.fsrtlinitperstreamcontext">FsRtlInitPerStreamContext</a> macro. 

To associate an initialized per-stream context structure with a file stream, call <a href="ifsk.fsrtlinsertperstreamcontext">FsRtlInsertPerStreamContext</a>. 

To retrieve a per-stream context structure that is associated with a file stream, call <a href="ifsk.fsrtllookupperstreamcontext">FsRtlLookupPerStreamContext</a>. 

<b>FsRtlRemovePerStreamContext</b> can only be used on file systems that support filter contexts. 

For more information, see <a href="ifsk.tracking_per_stream_context_in_a_legacy_file_system_filter_driver">Tracking Per-Stream Context in a Legacy File System Filter Driver</a>. 


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
<a href="ifsk.fsrtlsetupadvancedheader">FsRtlSetupAdvancedHeader</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547285">FsRtlSupportsPerStreamContexts</a>
</dt>
<dt>
<a href="ifsk.fsrtlteardownperstreamcontexts">FsRtlTeardownPerStreamContexts</a>
</dt>
<dt>
<a href="ifsk.irp_mj_close">IRP_MJ_CLOSE</a>
</dt>
<dt>
<a href="ifsk.irp_mj_pnp">IRP_MJ_PNP</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlRemovePerStreamContext function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

