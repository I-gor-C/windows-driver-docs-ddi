---
UID: NS.ntifs._FILE_FS_ATTRIBUTE_INFORMATION
title: FILE_FS_ATTRIBUTE_INFORMATION
author: windows-driver-content
description: The FILE_FS_ATTRIBUTE_INFORMATION structure is used to query attribute information for a file system.
old-location: ifsk\file_fs_attribute_information.htm
old-project: ifsk
ms.assetid: 373788d8-4963-4319-82ae-3a0675c9fff4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_FS_ATTRIBUTE_INFORMATION, FILE_FS_ATTRIBUTE_INFORMATION, *PFILE_FS_ATTRIBUTE_INFORMATION
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
req.alt-api: FILE_FS_ATTRIBUTE_INFORMATION
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

# FILE_FS_ATTRIBUTE_INFORMATION structure



## -description
<p>The <b>FILE_FS_ATTRIBUTE_INFORMATION</b> 
   structure is used to query attribute information for a file system.</p>


## -syntax

````
typedef struct _FILE_FS_ATTRIBUTE_INFORMATION {
  ULONG FileSystemAttributes;
  LONG  MaximumComponentNameLength;
  ULONG FileSystemNameLength;
  WCHAR FileSystemName[1];
} FILE_FS_ATTRIBUTE_INFORMATION, *PFILE_FS_ATTRIBUTE_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>FileSystemAttributes</b>

<dd>
<p>Bitmask of flags specifying attributes of the specified file system, as a compatible combination of the 
       following flags.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>FILE_CASE_PRESERVED_NAMES</b></p>
</td>
<td>
<p>The file system preserves the case of file names when it places a name on disk.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_CASE_SENSITIVE_SEARCH</b></p>
</td>
<td>
<p>The file system supports case-sensitive file names.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_FILE_COMPRESSION</b></p>
</td>
<td>
<p>The file system supports file-based compression. This flag is incompatible with the 
          <b>FILE_VOLUME_IS_COMPRESSED</b> flag.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_NAMED_STREAMS</b></p>
</td>
<td>
<p>The file system supports named streams.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_PERSISTENT_ACLS</b></p>
</td>
<td>
<p>The file system preserves and enforces access control lists 
          (<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>).</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_READ_ONLY_VOLUME</b></p>
</td>
<td>
<p><b>Microsoft Windows XP and later:</b> The specified volume is read-only.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_SUPPORTS_ENCRYPTION</b></p>
</td>
<td>
<p>The file system supports the Encrypted File System (EFS).</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_SUPPORTS_OBJECT_IDS</b></p>
</td>
<td>
<p>The file system supports object identifiers.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_SUPPORTS_REMOTE_STORAGE</b></p>
</td>
<td>
<p>The file system supports remote storage.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_SUPPORTS_REPARSE_POINTS</b></p>
</td>
<td>
<p>The file system supports reparse points.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_SUPPORTS_SPARSE_FILES</b></p>
</td>
<td>
<p>The file system supports sparse files.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_UNICODE_ON_DISK</b></p>
</td>
<td>
<p>The file system supports Unicode in file names.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_VOLUME_IS_COMPRESSED</b></p>
</td>
<td>
<p>The specified volume is a compressed volume. This flag is incompatible with the 
          <b>FILE_FILE_COMPRESSION</b> flag.</p>
</td>
</tr>
<tr>
<td>
<p><b>FILE_VOLUME_QUOTAS</b></p>
</td>
<td>
<p>The file system supports per-user quotas.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>MaximumComponentNameLength</b>

<dd>
<p>Maximum file name component length, in bytes, supported by the specified file system. A file name component 
      is that portion of a file name between backslashes.</p>
</dd>

### -field <b>FileSystemNameLength</b>

<dd>
<p>Length, in bytes, of the file system name.</p>
</dd>

### -field <b>FileSystemName</b>

<dd>
<p>File system name.</p>
</dd>
</dl>

## -remarks
<p>This information can be queried in either of the following ways:</p>

<p>Call <a href="..\fltkernel\nf-fltkernel-fltqueryvolumeinformation.md">FltQueryVolumeInformation</a> or 
       <a href="..\ntifs\nf-ntifs-zwqueryvolumeinformationfile.md">ZwQueryVolumeInformationFile</a>, passing 
       <b>FileFsAttributeInformation</b> as the value of 
       <i>FileInformationClass</i> and passing a caller-allocated, 
       <b>FILE_FS_ATTRIBUTE_INFORMATION</b>-structured 
       buffer as the value of <i>FileInformation</i>.</p>

<p>On CSVFS <b>FileFsAttributeInformation</b> returns 
       <b>FILE_FS_ATTRIBUTE_INFORMATION</b> for the 
       CSVFS file system. If you want to query <b>FileFsAttributeInformation</b> for the file 
       system CSVFS is layered on then you should use 
       <a href="fs.fsctl_csv_query_down_level_file_system_characteristics">FSCTL_CSV_QUERY_DOWN_LEVEL_FILE_SYSTEM_CHARACTERISTICS</a>.</p>

<p>Create an IRP with major function code 
       <a href="ifsk.irp_mj_query_volume_information">IRP_MJ_QUERY_VOLUME_INFORMATION</a>.</p>

<p>No specific access rights are required to query this information. Thus this information is available as long as 
     the volume is accessed through an open handle to the volume itself, or to a file or directory on the volume.</p>

<p>The size of the buffer passed in the <i>FileInformation</i> parameter to 
     <a href="..\fltkernel\nf-fltkernel-fltqueryvolumeinformation.md">FltQueryVolumeInformation</a> or 
     <a href="..\ntifs\nf-ntifs-zwqueryvolumeinformationfile.md">ZwQueryVolumeInformationFile</a> must be at 
     least <code>sizeof(FILE_FS_ATTRIBUTE_INFORMATION)</code>.</p>

<p>This structure must be aligned on a <b>LONG</b> (4-byte) boundary.</p>

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
<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltqueryvolumeinformation.md">FltQueryVolumeInformation</a>
</dt>
<dt>
<a href="ifsk.irp_mj_query_volume_information">IRP_MJ_QUERY_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwqueryvolumeinformationfile.md">ZwQueryVolumeInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_FS_ATTRIBUTE_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
