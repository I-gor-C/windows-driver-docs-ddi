---
UID: NF.ntifs.FsRtlInsertPerFileContext
title: FsRtlInsertPerFileContext function
author: windows-driver-content
description: The FsRtlInsertPerFileContext routine associates a FSRTL_PER_FILE_CONTEXT object with a driver-specified context object for a file.
old-location: ifsk\fsrtlinsertperfilecontext.htm
old-project: ifsk
ms.assetid: accc3600-9614-48e0-912d-1e8b324e659f
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FsRtlInsertPerFileContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlInsertPerFileContext
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
req.irql: <=APC_LEVEL
---

# FsRtlInsertPerFileContext function



## -description
The <b>FsRtlInsertPerFileContext</b> routine associates a <a href="ifsk.fsrtl_per_file_context">FSRTL_PER_FILE_CONTEXT</a> object with a driver-specified context object for a file.



## -syntax

````
NTSTATUS FsRtlInsertPerFileContext(
  _In_ PVOID                   *PerFileContextPointer,
  _In_ PFSRTL_PER_FILE_CONTEXT Ptr
);
````


## -parameters

### -param PerFileContextPointer [in]

A pointer to an opaque pointer used by the file system runtime library (FSRTL) package to track file contexts. To retrieve this pointer from a file object, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546051">FsRtlGetPerFileContextPointer</a> macro.


### -param Ptr [in]

A pointer to the driver-specific context structure. 


## -returns
The <b>FsRtlInsertPerFileContext</b> routine returns STATUS_SUCCESS, or an appropriate error code, such as:
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>The underlying file system does not support filter file contexts. You can use the <a href="ifsk.fsrtlsupportsperfilecontexts">FsRtlSupportsPerFileContexts</a> macro to check whether a file system supports per file context objects.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>The system could not allocate resources (typically memory).

 


## -remarks
The FsRtlGetPerFileContextPointer macro returns a <i>FileContextSupportPointer</i> for an open file. 

Parameters


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
Available in Windows Vista and later versions of the Windows operating system.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
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
&lt;=APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsrtl_per_file_context">FSRTL_PER_FILE_CONTEXT</a>
</dt>
<dt>
<a href="ifsk.fsrtllookupperfilecontext">FsRtlLookupPerFileContext</a>
</dt>
<dt>
<a href="ifsk.fsrtlremoveperfilecontext">FsRtlRemovePerFileContext</a>
</dt>
<dt>
<a href="ifsk.tracking_per_file_context_in_a_legacy_file_system_filter_driver">Tracking Per-File Context in a Legacy File System Filter Driver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlInsertPerFileContext routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

