---
UID: NS.ntifs._FILE_ID_BOTH_DIR_INFORMATION
title: FILE_ID_BOTH_DIR_INFORMATION
author: windows-driver-content
description: The FILE_ID_BOTH_DIR_INFORMATION structure is used to query file reference number information for the files in a directory.
old-location: ifsk\file_id_both_dir_information.htm
ms.assetid: 57a66b41-f9f6-42e1-95d7-010cacd1374a
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
req.alt-api: FILE_ID_BOTH_DIR_INFORMATION
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
ms.keywords: FILE_ID_BOTH_DIR_INFORMATION, FILE_ID_BOTH_DIR_INFORMATION, *PFILE_ID_BOTH_DIR_INFORMATION
req.iface: 
---

# FILE_ID_BOTH_DIR_INFORMATION structure



## -description
<p>The FILE_ID_BOTH_DIR_INFORMATION structure is used to query file reference number information for the files in a directory. </p>


## -syntax

````
typedef struct _FILE_ID_BOTH_DIR_INFORMATION {
  ULONG         NextEntryOffset;
  ULONG         FileIndex;
  LARGE_INTEGER CreationTime;
  LARGE_INTEGER LastAccessTime;
  LARGE_INTEGER LastWriteTime;
  LARGE_INTEGER ChangeTime;
  LARGE_INTEGER EndOfFile;
  LARGE_INTEGER AllocationSize;
  ULONG         FileAttributes;
  ULONG         FileNameLength;
  ULONG         EaSize;
  CCHAR         ShortNameLength;
  WCHAR         ShortName[12];
  LARGE_INTEGER FileId;
  WCHAR         FileName[1];
} FILE_ID_BOTH_DIR_INFORMATION, *PFILE_ID_BOTH_DIR_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>NextEntryOffset</b>

<dd>
<p>Byte offset of the next FILE_ID_BOTH_DIR_INFORMATION entry, if multiple entries are present in a buffer. This member is zero if no other entries follow this one. </p>
</dd>

### -field <b>FileIndex</b>

<dd>
<p>Byte offset of the file within the parent directory. This member is undefined for file systems, such as NTFS, in which the position of a file within the parent directory is not fixed and can be changed at any time to maintain sort order. </p>
</dd>

### -field <b>CreationTime</b>

<dd>
<p>Time when the file was created. </p>
</dd>

### -field <b>LastAccessTime</b>

<dd>
<p>Last time the file was accessed. </p>
</dd>

### -field <b>LastWriteTime</b>

<dd>
<p>Last time information was written to the file. </p>
</dd>

### -field <b>ChangeTime</b>

<dd>
<p>Last time the file was changed. </p>
</dd>

### -field <b>EndOfFile</b>

<dd>
<p>Absolute new end-of-file position as a byte offset from the start of the file. <b>EndOfFile</b> specifies the byte offset to the end of the file. Because this value is zero-based, it actually refers to the first free byte in the file. In other words, <b>EndOfFile</b> is the offset to the byte immediately following the last valid byte in the file.</p>
</dd>

### -field <b>AllocationSize</b>

<dd>
<p>File allocation size, in bytes. Usually, this value is a multiple of the sector or cluster size of the underlying physical device. </p>
</dd>

### -field <b>FileAttributes</b>

<dd>
<p>File attributes, which can be any valid combination of the following: </p>
<p>
<dl>
<dd>FILE_ATTRIBUTE_READONLY</dd>
<dd>FILE_ATTRIBUTE_HIDDEN</dd>
<dd>FILE_ATTRIBUTE_SYSTEM</dd>
<dd>FILE_ATTRIBUTE_DIRECTORY</dd>
<dd>FILE_ATTRIBUTE_ARCHIVE</dd>
<dd>FILE_ATTRIBUTE_NORMAL</dd>
<dd>FILE_ATTRIBUTE_TEMPORARY</dd>
<dd>FILE_ATTRIBUTE_COMPRESSED</dd>
</dl>
</p>
</dd>

### -field <b>FileNameLength</b>

<dd>
<p>Specifies the length of the file name string. </p>
</dd>

### -field <b>EaSize</b>

<dd>
<p>Combined length, in bytes, of the extended attributes (EA) for the file. </p>
</dd>

### -field <b>ShortNameLength</b>

<dd>
<p>Specifies the length of the short file name string. </p>
</dd>

### -field <b>ShortName</b>

<dd>
<p>Unicode string containing the short (8.3) name for the file. </p>
</dd>

### -field <b>FileId</b>

<dd>
<p>The 8-byte file reference number for the file. This number is generated and assigned to the file by the file system. (Note that the <b>FileId</b> is not the same as the 16-byte "file object ID" that was added to NTFS for Microsoft Windows 2000.) </p>
</dd>

### -field <b>FileName</b>

<dd>
<p>Specifies the first character of the file name string. This is followed in memory by the remainder of the string. </p>
</dd>
</dl>

## -remarks
<p>This information can be queried in either of the following ways: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff567047">ZwQueryDirectoryFile</a>, passing FileIdBothDirectoryInformation as the value of <i>FileInformationClass</i> and passing a caller-allocated, FILE_ID_BOTH_DIR_INFORMATION-structured buffer as the value of <i>FileInformation</i>. </p>

<p>Create an IRP with major function code IRP_MJ_DIRECTORY_CONTROL and minor function code IRP_MN_QUERY_DIRECTORY. </p>

<p>No specific access rights are required to query this information. </p>

<p>File reference numbers, also called file IDs, are guaranteed to be unique only within a static file system. They are not guaranteed to be unique over time, because file systems are free to reuse them. Nor are they guaranteed to remain constant. For example, the FAT file system generates the file reference number for a file from the byte offset of the file's directory entry record (DIRENT) on the disk. Defragmentation can change this byte offset. Thus a FAT file reference number can change over time. </p>

<p>All dates and times are in absolute system-time format. Absolute system time is the number of 100-nanosecond intervals since the start of the year 1601. </p>

<p>This structure must be aligned on a LONGLONG (8-byte) boundary. If a buffer contains two or more of these structures, the <b>NextEntryOffset</b> value in each entry, except the last, falls on an 8-byte boundary. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547026">FsRtlNotifyFullChangeDirectory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567047">ZwQueryDirectoryFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_ID_BOTH_DIR_INFORMATION structure%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
