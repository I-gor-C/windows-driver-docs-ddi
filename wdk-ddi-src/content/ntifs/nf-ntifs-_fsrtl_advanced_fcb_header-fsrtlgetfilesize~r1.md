---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlGetFileSize~r1
title: FsRtlGetFileSize function
author: windows-driver-content
description: The FsRtlGetFileSize routine is used to get the size of a file.
old-location: ifsk\fsrtlgetfilesize.htm
old-project: ifsk
ms.assetid: 82fcf0da-e945-4cb4-90fc-bb095119ef20
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlGetFileSize
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
req.alt-api: FsRtlGetFileSize
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
req.irql: PASSIVE_LEVEL
---

# FsRtlGetFileSize function



## -description
The <b>FsRtlGetFileSize</b> routine is used to get the size of a file. 



## -syntax

````
NTSTATUS FsRtlGetFileSize(
  _In_  PFILE_OBJECT   FileObject,
  _Out_ PLARGE_INTEGER FileSize
);
````


## -parameters

### -param FileObject [in]

A pointer to the file object to query. 


### -param FileSize [out]

A pointer to a large integer that receives the file size on output.


## -returns
<b>FsRtlGetFileSize</b> returns STATUS_SUCCESS or an appropriate error status representing the final completion status of the operation. Possible error status codes include the following: 
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>The memory required for use by this function could not be allocated. 
<dl>
<dt><b>STATUS_FILE_IS_A_DIRECTORY</b></dt>
</dl>The specified <i>FileObject </i>refers to a directory. 

 


## -remarks
The <b>FsRtlGetFileSize</b> routine is used to retrieve the file size for a file. Unlike <a href="kernel.zwqueryinformationfile">ZwQueryInformationFile</a>, <b>FsRtlGetFileSize</b> does not acquire the file object lock on synchronous file objects. If you already own file system resources, you should call <b>FsRtlGetFileSize</b> instead of <b>ZwQueryInformationFile</b>, because attempting to acquire the file object lock would violate locking order and lead to deadlocks. The <b>ZwQueryInformationFile</b> function should be only if you do not already own file system resources. 

<b>FsRtlGetFileSize</b> will use fast I/O if it is supported or regular IRP-based query to extract the file size. 


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
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fltqueryinformationfile">FltQueryInformationFile</a>
</dt>
<dt>
<a href="kernel.zwqueryinformationfile">ZwQueryInformationFile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlGetFileSize routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

