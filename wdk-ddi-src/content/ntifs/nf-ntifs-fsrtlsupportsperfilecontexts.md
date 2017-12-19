---
UID: NF.ntifs.FsRtlSupportsPerFileContexts
title: FsRtlSupportsPerFileContexts macro
author: windows-driver-content
description: The FsRtlSupportsPerFileContexts macro checks if per file context information is supported by the file system that is associated with a specified FILE_OBJECT.
old-location: ifsk\fsrtlsupportsperfilecontexts.htm
old-project: ifsk
ms.assetid: 28f0e98f-1f7b-4dcf-8151-e13981634617
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FsRtlSupportsPerFileContexts
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
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
---

# FsRtlSupportsPerFileContexts macro



## -description
The <b>FsRtlSupportsPerFileContexts</b> macro checks if per file context information is supported by the file system that is associated with a specified <a href="kernel.file_object">FILE_OBJECT</a>.



## -syntax

````
BOOLEAN FsRtlSupportsPerFileContexts(
   FILE_OBJECT FileObject
);
````


## -parameters

### -param FileObject 

A FILE_OBJECT that is associated with the file system to be checked.


## -remarks
None


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
IRQL

</th>
<td width="70%">
Any

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.file_object">FILE_OBJECT</a>
</dt>
<dt>
<a href="ifsk.tracking_per_file_context_in_a_legacy_file_system_filter_driver">Tracking Per-File Context in a Legacy File System Filter Driver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlSupportsPerFileContexts  function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

