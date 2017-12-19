---
UID: NF.ntifs.FsRtlLookupPerStreamContext
title: FsRtlLookupPerStreamContext macro
author: windows-driver-content
description: The FsRtlLookupPerStreamContext macro retrieves a per-stream context structure for a file stream.
old-location: ifsk\fsrtllookupperstreamcontext.htm
old-project: ifsk
ms.assetid: 8f8c47c3-1917-4252-b812-711ef52d22d7
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FsRtlLookupPerStreamContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: This routine is available on Update Rollup for Windows 2000 Service Pack 4 (SP4) and on Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlLookupPerStreamContext
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

# FsRtlLookupPerStreamContext macro



## -description
The <b>FsRtlLookupPerStreamContext</b> macro retrieves a per-stream context structure for a file stream. 



## -syntax

````
PFSRTL_PER_STREAM_CONTEXT FsRtlLookupPerStreamContext(
  _In_     PFSRTL_ADVANCED_FCB_HEADER StreamContext,
  _In_opt_ PVOID                      OwnerId,
  _In_opt_ PVOID                      InstanceId
);
````


## -parameters

### -param StreamContext [in]

Pointer to the FSRTL_ADVANCED_FCB_HEADER structure for the file stream. To get this pointer from a file object, use the <a href="ifsk.fsrtlgetperstreamcontextpointer">FsRtlGetPerStreamContextPointer</a> macro. 


### -param OwnerId [in, optional]

Pointer to a caller-allocated variable that uniquely identifies the owner of the per-stream context structure. The format of this variable is filter driver − specific. Must be non-<b>NULL</b> if a non-<b>NULL</b> value is supplied for <i>InstanceId</i>. 


### -param InstanceId [in, optional]

Pointer to a filter driver − allocated variable that can be used to distinguish among per-stream context structures created by the same filter driver. The format of this variable is filter driver − specific. 

If <i>OwnerId</i> and <i>InstanceId</i> are both <b>NULL</b>, <b>FsRtlLookupPerStreamContext</b> returns the first per-stream context found. 

If a non-<b>NULL</b> value is supplied for <i>OwnerId</i> and <i>InstanceId</i> is <b>NULL</b>, <b>FsRtlLookupPerStreamContext</b> returns the first per-stream context found whose <b>OwnerId</b> member matches the <i>OwnerId</i> parameter. 


## -remarks
A file system filter driver calls <b>FsRtlLookupPerStreamContext</b> to retrieve its per-stream context structure for a file stream. The per-stream context structure contains context information that the filter driver maintains for the file stream. 

To initialize a per-stream context structure, use the <a href="ifsk.fsrtlinitperstreamcontext">FsRtlInitPerStreamContext</a> macro. 

To associate an initialized per-stream context structure with a file stream, call <a href="ifsk.fsrtlinsertperstreamcontext">FsRtlInsertPerStreamContext</a>. 

To remove a per-stream context structure that is associated with a file stream, call <a href="ifsk.fsrtlremoveperstreamcontext">FsRtlRemovePerStreamContext</a>. 

For more information, see <a href="ifsk.tracking_per_stream_context_in_a_legacy_file_system_filter_driver">Tracking Per-Stream Context in a Legacy File System Filter Driver</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
This routine is available on Update Rollup for Windows 2000 Service Pack 4 (SP4) and on Windows XP and later. 

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
<a href="ifsk.fsrtlremoveperstreamcontext">FsRtlRemovePerStreamContext</a>
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
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlLookupPerStreamContext function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

