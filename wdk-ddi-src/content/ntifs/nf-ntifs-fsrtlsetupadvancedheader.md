---
UID: NF.ntifs.FsRtlSetupAdvancedHeader
title: FsRtlSetupAdvancedHeader function
author: windows-driver-content
description: The FsRtlSetupAdvancedHeader macro is used by file systems to initialize an FSRTL_ADVANCED_FCB_HEADER structure for use with filter contexts.
old-location: ifsk\fsrtlsetupadvancedheader.htm
old-project: ifsk
ms.assetid: 8bcf7bbf-6c41-4683-9a62-d408b120c7b9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlSetupAdvancedHeader
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Desktop
req.target-min-winverclnt: Available on Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlSetupAdvancedHeader
req.alt-loc: ntifs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
---

# FsRtlSetupAdvancedHeader function



## -description
The <b>FsRtlSetupAdvancedHeader</b> macro is used by file systems to initialize an <a href="ifsk.fsrtl_advanced_fcb_header">FSRTL_ADVANCED_FCB_HEADER</a> structure for use with filter contexts. 



## -syntax

````
VOID FsRtlSetupAdvancedHeader(
  _In_ PVOID       AdvancedHeader,
  _In_ PFAST_MUTEX FastMutex
);
````


## -parameters

### -param AdvancedHeader [in]

A pointer to the <a href="ifsk.fsrtl_advanced_fcb_header">FSRTL_ADVANCED_FCB_HEADER</a> structure to be initialized. 


### -param FastMutex [in]

A pointer to an initialized fast mutex that will be used to synchronize access to the <a href="ifsk.fsrtl_advanced_fcb_header">FSRTL_ADVANCED_FCB_HEADER</a> structure. The fast mutex must be allocated from nonpaged pool. 

This parameter can be <b>NULL</b>. Callers should set this parameter to <b>NULL</b> if they intend to use an already existing fast mutex object. If <i>FastMutex</i> is <b>NULL</b>, the caller must explicitly set the <i>FastMutex</i> member of the stream context object to point to the existing fast mutex. (This can be done before or after calling <b>FsRtlSetupAdvancedHeader</b>.) 


## -returns
None


## -remarks
File systems use the <b>FsRtlSetupAdvancedHeader</b> macro to initialize an <a href="ifsk.fsrtl_advanced_fcb_header">FSRTL_ADVANCED_FCB_HEADER</a> structure for use with filter contexts. 

When the advanced FCB header structure is no longer required, the file system must call <a href="ifsk.fsrtlteardownperstreamcontexts">FsRtlTeardownPerStreamContexts</a> to free all associated per-stream context structures. 

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
Available on Microsoft Windows XP and later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547285">FsRtlSupportsPerStreamContexts</a>
</dt>
<dt>
<a href="ifsk.fsrtlteardownperstreamcontexts">FsRtlTeardownPerStreamContexts</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlSetupAdvancedHeader function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

