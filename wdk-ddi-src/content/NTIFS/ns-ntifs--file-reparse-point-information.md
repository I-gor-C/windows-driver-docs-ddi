---
UID: NS.ntifs._FILE_REPARSE_POINT_INFORMATION
title: FILE_REPARSE_POINT_INFORMATION
author: windows-driver-content
description: The FILE_REPARSE_POINT_INFORMATION structure is used to query for information about a reparse point.
old-location: ifsk\file_reparse_point_information.htm
ms.assetid: de6e8b39-9e0c-4817-82b4-d64e81a95e79
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_REPARSE_POINT_INFORMATION
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
req.irql: 
ms.keywords: FILE_REPARSE_POINT_INFORMATION, FILE_REPARSE_POINT_INFORMATION, *PFILE_REPARSE_POINT_INFORMATION
req.iface: 
---

# FILE_REPARSE_POINT_INFORMATION structure



## -description
<p>The FILE_REPARSE_POINT_INFORMATION structure is used to query for information about a reparse point. </p>


## -syntax

````
typedef struct _FILE_REPARSE_POINT_INFORMATION {
  LONGLONG FileReference;
  ULONG    Tag;
} FILE_REPARSE_POINT_INFORMATION, *PFILE_REPARSE_POINT_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>FileReference</b>

<dd>
<p>The 8-byte file reference number for the file. This number is generated and assigned to the file by the NTFS file system. (Note that the <i>FileId</i> is not the same as the 16-byte "file object ID" that was added to NTFS for Microsoft Windows 2000.) </p>
</dd>

### -field <b>Tag</b>

<dd>
<p>Reparse point tag. The <b>ReparseTag</b> member indicates the structure of the user-defined reparse data. For more information about reparse point tags, see the Microsoft Windows SDK documentation. </p>
</dd>
</dl>

## -remarks
<p>This information can be queried in either of the following ways: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff567047">ZwQueryDirectoryFile</a>, passing FileReparsePointInformation as the value of <i>FileInformationClass</i> and passing a caller-allocated, FILE_REPARSE_POINT_INFORMATION-structured buffer as the value of <i>FileInformation</i>. </p>

<p>Create an IRP with major function code <a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a> and minor function code IRP_MN_QUERY_DIRECTORY. </p>

<p>For more information about reparse points, see the Windows SDK documentation. </p>

<p>No specific access rights are required to query this information. </p>

<p>This structure must be LONG-aligned. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567047">ZwQueryDirectoryFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_REPARSE_POINT_INFORMATION structure%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
