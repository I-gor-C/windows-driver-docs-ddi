---
UID: NS.ntifs._FILE_INTERNAL_INFORMATION
title: FILE_INTERNAL_INFORMATION
author: windows-driver-content
description: The FILE_INTERNAL_INFORMATION structure is used to query for the file system's 8-byte file reference number for a file.
old-location: ifsk\file_internal_information.htm
old-project: ifsk
ms.assetid: b82bc943-d9f0-451f-a8ac-f89936e866eb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_INTERNAL_INFORMATION, FILE_INTERNAL_INFORMATION, *PFILE_INTERNAL_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_INTERNAL_INFORMATION
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
req.iface: 
---

# FILE_INTERNAL_INFORMATION structure



## -description
<p>The FILE_INTERNAL_INFORMATION structure is used to query for the file system's 8-byte file reference number for a file. </p>


## -syntax

````
typedef struct _FILE_INTERNAL_INFORMATION {
  LARGE_INTEGER IndexNumber;
} FILE_INTERNAL_INFORMATION, *PFILE_INTERNAL_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>IndexNumber</b>

<dd>
<p>The 8-byte file reference number for the file. This number is assigned by the file system and is file-system-specific. (Note that this is not the same as the 16-byte "file object ID" that was added to NTFS for Microsoft Windows 2000.) </p>
</dd>
</dl>

## -remarks
<p>This information can be queried in either of the following ways: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543439">FltQueryInformationFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a>, passing FileInternalInformation as the value of <i>FileInformationClass</i> and passing a caller-allocated, FILE_INTERNAL_INFORMATION-structured buffer as the value of <i>FileInformation</i>. </p>

<p>Create an IRP with major function code <a href="https://msdn.microsoft.com/library/windows/hardware/ff549283">IRP_MJ_QUERY_INFORMATION</a>. </p>

<p>No specific access rights are required to query this information. </p>

<p>The <b>IndexNumber</b> member of the FILE_INTERNAL_INFORMATION structure is the same as the <b>FileId</b> member of the FILE_ID_BOTH_DIR_INFORMATION and FILE_ID_FULL_DIR_INFORMATION structures. </p>

<p>File reference numbers, also called file IDs, are guaranteed to be unique only within a static file system. They are not guaranteed to be unique over time, because file systems are free to reuse them. Nor are they guaranteed to remain constant. For example, the FAT file system generates the file reference number for a file from the byte offset of the file's directory entry record (DIRENT) on the disk. Defragmentation can change this byte offset. Thus a FAT file reference number can change over time. </p>

<p>The size of the buffer passed in the <i>FileInformation</i> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543439">FltQueryInformationFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a> must be at least <b>sizeof</b> (FILE_INTERNAL_INFORMATION). </p>

<p>This structure must be aligned on a LONGLONG (8-byte) boundary. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540303">FILE_ID_BOTH_DIR_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540310">FILE_ID_FULL_DIR_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540335">FILE_OBJECTID_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543439">FltQueryInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_INTERNAL_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
