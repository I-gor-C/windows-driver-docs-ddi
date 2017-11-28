---
UID: NF.ntifs.FsRtlSupportsPerFileContexts
title: FsRtlSupportsPerFileContexts
author: windows-driver-content
description: The FsRtlSupportsPerFileContexts macro checks if per file context information is supported by the file system that is associated with a specified FILE_OBJECT.
old-location: ifsk\fsrtlsupportsperfilecontexts.htm
old-project: ifsk
ms.assetid: 28f0e98f-1f7b-4dcf-8151-e13981634617
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlSupportsPerFileContexts
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlSupportsPerFileContexts
req.alt-loc: Ntifs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any
req.iface: 
---

# FsRtlSupportsPerFileContexts function



## -description
<p>The <b>FsRtlSupportsPerFileContexts</b> macro checks if per file context information is supported by the file system that is associated with a specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a>.</p>


## -syntax

````
BOOLEAN FsRtlSupportsPerFileContexts(
   FILE_OBJECT FileObject
);
````


## -parameters
<dl>

### -param <i>FileObject</i> 

<dd>
<p>A FILE_OBJECT that is associated with the file system to be checked.</p>
</dd>
</dl>

## -returns
<p>The macro returns <b>TRUE</b> if the associated file system does support per file context objects. The macro returns <b>FALSE</b> if the file system does not support per file context objects.</p>

## -remarks
<p>None</p>

<p>None</p>

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
<p>Available in Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a>
</dt>
<dt>
<a href="ifsk.tracking_per_file_context_in_a_legacy_file_system_filter_driver">Tracking Per-File Context in a Legacy File System Filter Driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlSupportsPerFileContexts  function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
