---
UID: NF.ntifs.FsRtlGetPerStreamContextPointer
title: FsRtlGetPerStreamContextPointer
author: windows-driver-content
description: The FsRtlGetPerStreamContextPointer macro returns the file system's stream context for a file stream.
old-location: ifsk\fsrtlgetperstreamcontextpointer.htm
old-project: ifsk
ms.assetid: f3f9294a-23c0-450a-ae29-22add8176540
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlGetPerStreamContextPointer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: The FsRtlGetPerStreamContextPointer macro is available on Microsoft Windows XP and later, and on the Update Rollup for Windows 2000 Service Pack 4 (SP4).
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlGetPerStreamContextPointer
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
req.iface: 
---

# FsRtlGetPerStreamContextPointer function



## -description
<p>The <b>FsRtlGetPerStreamContextPointer</b> macro returns the file system's stream context for a file stream. </p>


## -syntax

````
PFSRTL_ADVANCED_FCB_HEADER FsRtlGetPerStreamContextPointer(
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to a file object for the file stream. </p>
</dd>
</dl>

## -returns
<p>The <b>FsRtlGetPerStreamContextPointer</b> macro returns a pointer to the file system's stream context for the file stream represented by the given file object. </p>

## -remarks
<p>File system filter drivers can use the <b>FsRtlGetPerStreamContextPointer</b> macro to obtain a stream context pointer for the file stream that is represented by a given file object. A stream context pointer is a pointer to the file system's stream context for the file stream. This pointer can be passed as a parameter to <a href="..\ntifs\nf-ntifs-fsrtlinsertperstreamcontext.md">FsRtlInsertPerStreamContext</a>, <a href="..\ntifs\nf-ntifs-fsrtllookupperstreamcontext.md">FsRtlLookupPerStreamContext</a>, and <a href="..\ntifs\nf-ntifs-fsrtlremoveperstreamcontext.md">FsRtlRemovePerStreamContext</a>. </p>

<p>The stream context pointer points to a <a href="..\ntifs\ns-ntifs--fsrtl-advanced-fcb-header.md">FSRTL_ADVANCED_FCB_HEADER</a> structure that uniquely identifies the file stream to the file system. This structure is usually embedded in a stream context object, such as a file control block (FCB) or stream control block (SCB). When the file stream is opened, the file system stores a pointer to the FCB or SCB in the file object's <b>FsContext</b> member. </p>

<p>For more information, see <a href="ifsk.tracking_per_stream_context_in_a_legacy_file_system_filter_driver">Tracking Per-Stream Context in a Legacy File System Filter Driver</a>. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>The FsRtlGetPerStreamContextPointer macro is available on Microsoft Windows XP and later, and on the Update Rollup for Windows 2000 Service Pack 4 (SP4). </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ns-ntifs--fsrtl-advanced-fcb-header.md">FSRTL_ADVANCED_FCB_HEADER</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlinitperstreamcontext.md">FsRtlInitPerStreamContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlinsertperstreamcontext.md">FsRtlInsertPerStreamContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtllookupperstreamcontext.md">FsRtlLookupPerStreamContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlremoveperstreamcontext.md">FsRtlRemovePerStreamContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlsetupadvancedheader.md">FsRtlSetupAdvancedHeader</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547285">FsRtlSupportsPerStreamContexts</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlteardownperstreamcontexts.md">FsRtlTeardownPerStreamContexts</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlGetPerStreamContextPointer function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
