---
UID: NS.ntifs._FILE_RENAME_INFORMATION
title: FILE_RENAME_INFORMATION
author: windows-driver-content
description: The FILE_RENAME_INFORMATION structure is used to rename a file.
old-location: ifsk\file_rename_information.htm
old-project: ifsk
ms.assetid: 25a195ab-faf1-488d-a9b2-65ae88b57ebd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_RENAME_INFORMATION, FILE_RENAME_INFORMATION, *PFILE_RENAME_INFORMATION
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
req.alt-api: FILE_RENAME_INFORMATION
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

# FILE_RENAME_INFORMATION structure



## -description
<p>The <b>FILE_RENAME_INFORMATION</b> structure is used to rename a file.</p>


## -syntax

````
typedef struct _FILE_RENAME_INFORMATION {
  BOOLEAN ReplaceIfExists;
  HANDLE  RootDirectory;
  ULONG   FileNameLength;
  WCHAR   FileName[1];
} FILE_RENAME_INFORMATION, *PFILE_RENAME_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>ReplaceIfExists</b>

<dd>
<p>Set to <b>TRUE</b> to specify that if a file with the given name already exists, it should be replaced with the given file. Set to <b>FALSE</b> if the rename operation should fail if a file with the given name already exists. </p>
</dd>

### -field <b>RootDirectory</b>

<dd>
<p>If the file is not being moved to a different directory, or if the <b>FileName</b> member contains the full pathname, this member is <b>NULL</b>. Otherwise, it is a handle for the root directory under which the file will reside after it is renamed. </p>
</dd>

### -field <b>FileNameLength</b>

<dd>
<p>Length, in bytes, of the new name for the file. </p>
</dd>

### -field <b>FileName</b>

<dd>
<p>The first character of a wide-character string containing the new name for the file. This is followed in memory by the remainder of the string. If the <b>RootDirectory</b> member is <b>NULL</b>, and the file is being moved to a different directory, this member specifies the full pathname to be assigned to the file. Otherwise, it specifies only the file name or a relative pathname. </p>
</dd>
</dl>

## -remarks
<p>The <b>FILE_RENAME_INFORMATION</b> structure is used to rename a file. This operation can be performed in either of the following ways: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>, passing <b>FileRenameInformation</b> as the value of <i>FileInformationClass</i> and passing a caller-allocated buffer formatted as a <b>FILE_RENAME_INFORMATION</b> structure for the value of <i>FileInformation</i>. The <i>FileHandle</i> parameter specifies the file to be renamed. </p>

<p>Create an IRP with major function code IRP_MJ_SET_INFORMATION. </p>

<p>File system minifilters must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>, not <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>, to rename a file. </p>

<p>Renaming a file requires DELETE access to the file so that the directory entry may be removed from the current parent directory, as well as the appropriate access to create the new entry in the new parent directory file. </p>

<p>The file name string in the <b>FileName</b> member must be specified in one of the following forms. </p>

<p>A simple file name. (The <b>RootDirectory</b> member is <b>NULL</b>.) In this case, the file is simply renamed within the same directory. That is, the rename operation changes the name of the file but not its location. </p>

<p>A fully qualified file name. (The <b>RootDirectory</b> member is <b>NULL</b>.) In this case, the rename operation changes the name and location of the file. </p>

<p>A relative file name. In this case, the <b>RootDirectory</b> member contains a handle to the target directory for the rename operation. The file name itself must be a simple file name. </p>

<p>General rules for rename operations: </p>

<p>A file or directory can only be renamed within a volume. In other words, a rename operation cannot cause a file or directory to be moved to a different volume. </p>

<p>A volume's root directory cannot be renamed. </p>

<p>If <b>ReplaceIfExists</b> is set to <b>FALSE</b>, and the target exists, the rename operation will fail. </p>

<p>Even if <b>ReplaceIfExists</b> is set to <b>TRUE</b>, the rename operation will still fail if a file with the same name already exists and is a directory, a read-only file, or a currently executing file. </p>

<p>A volume's files and directories cannot be renamed if the volume is a read-only volume, such as a CDFS volume or a read-only NTFS volume. </p>

<p>Special rules for renaming open files: </p>

<p>A file cannot be renamed if it has any open handles, unless it is only open because of a batch opportunistic lock (oplock) and the batch oplock can be broken immediately. </p>

<p>A file cannot be renamed if a file with the same name exists and has open handles (except in the batch-oplock case described earlier). </p>

<p>A directory cannot be renamed if it or any of its subdirectories contains a file that has open handles (except in the batch-oplock case described earlier). </p>

<p>Special rules for renaming NTFS data streams: </p>

<p>The source handle cannot be opened with FILE_DIRECTORY_FILE. </p>

<p>The source handle cannot be a directory opened without either FILE_DIRECTORY_FILE or FILE_NON_DIRECTORY_FILE. </p>

<p>The new name for the stream must begin with a colon (:). </p>

<p>A data stream can only be renamed within a file. In other words, a rename operation cannot cause a data stream to be moved to a different file. </p>

<p>A stream on a directory cannot be renamed to the default data stream. </p>

<p>If <b>ReplaceIfExists</b> is set to <b>TRUE</b>, the rename operation will succeed only if a stream with the same name exists and is a zero-length data stream. </p>

<p>"Renaming" the default data stream is allowed, but this is not a true rename, because it leaves behind a zero-length default data stream. </p>

<p>The size of the <i>FileInformation</i> buffer passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a> must be &gt;= <b>sizeof</b>(FILE_RENAME_INFORMATION) plus the size in bytes of the <b>FileName</b> string. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549366">IRP_MJ_SET_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_RENAME_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
