---
UID: NS.ntifs._FILE_OBJECTID_INFORMATION
title: FILE_OBJECTID_INFORMATION
author: windows-driver-content
description: The FILE_OBJECTID_INFORMATION structure is used to query for object ID information for the files in a directory on an NTFS volume.
old-location: ifsk\file_objectid_information.htm
old-project: ifsk
ms.assetid: bbbaf48b-78c3-4a4b-801b-2fe3c0112a68
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FILE_OBJECTID_INFORMATION, FILE_OBJECTID_INFORMATION, *PFILE_OBJECTID_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available on Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_OBJECTID_INFORMATION
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

# FILE_OBJECTID_INFORMATION structure



## -description
<p>The FILE_OBJECTID_INFORMATION structure is used to query for object ID information for the files in a directory on an NTFS volume. </p>


## -syntax

````
typedef struct _FILE_OBJECTID_INFORMATION {
  LONGLONG FileReference;
  UCHAR    ObjectId[16];
  union {
    struct {
      UCHAR BirthVolumeId[16];
      UCHAR BirthObjectId[16];
      UCHAR DomainId[16];
    };
    UCHAR  ExtendedInfo[48];
  };
} FILE_OBJECTID_INFORMATION, *PFILE_OBJECTID_INFORMATION;
````


## -struct-fields
<dl>

### -field FileReference

<dd>
<p>The 8-byte file reference number for the file. NTFS generates this number and assigns it to the file automatically when the file is created. </p>
</dd>

### -field ObjectId

<dd>
<p>The 16-byte file object ID for the file. NTFS generates this number and assigns it to the file at the request of a driver or application. File object IDs are guaranteed to be unique only within the volume where the file resides. </p>
</dd>

### -field ( unnamed struct )

<dd>
<p> </p>
<dl>

### -field BirthVolumeId

<dd>
<p>The object identifier of the volume on which the file resided when the object identifier was created, or zero if the volume had no object identifier at that time. After copy operations, move operations, or other file operations, this may not be the same as the object identifier of the volume on which the object currently resides. </p>
</dd>

### -field BirthObjectId

<dd>
<p>The object identifier of the file at the time it was created. After copy operations, move operations, or other file operations, this may not be the same as the current value of the <b>ObjectId</b> member. </p>
</dd>

### -field DomainId

<dd>
<p>Reserved; must be zero. </p>
</dd>
</dl>
</dd>

### -field ExtendedInfo

<dd>
<p>User-provided data. You can use it to contain the <b>BirthVolumeID</b>, <b>BirthObjectID</b>, and <b>DomainID</b> members, or you can define a different data structure. </p>
</dd>
</dl>

## -remarks
<p>This information can be queried in either of the following ways: </p>

<p>Call <a href="..\ntifs\nf-ntifs-zwquerydirectoryfile.md">ZwQueryDirectoryFile</a>, passing FileObjectIdInformation as the value of <i>FileInformationClass</i> and passing a caller-allocated, FILE_OBJECTID_INFORMATION-structured buffer as the value of <i>FileInformation</i>. </p>

<p>Create an IRP with major function code IRP_MJ_DIRECTORY_CONTROL and minor function code IRP_MN_QUERY_DIRECTORY. </p>

<p>No special access rights are required to query for this information. </p>

<p>Support for file reference numbers and file object IDs is file system-specific. File object IDs are supported only on NTFS volumes on Microsoft Windows 2000 and later. NTFS allows files to be opened by object ID as well as by file reference number. </p>

<p>File system filter drivers that use file object IDs should be tested for interoperability with DFS, the Replicator service, and the Distributed Link Tracking service, all of which use and manipulate file object IDs. </p>

<p>This structure must be aligned on a LONG (4-byte) boundary. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available on Microsoft Windows 2000 and later. </p>
</td>
</tr>
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
<a href="..\ntifs\ns-ntifs--file-internal-information.md">FILE_INTERNAL_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.irp_mj_directory_control">IRP_MJ_DIRECTORY_CONTROL</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwquerydirectoryfile.md">ZwQueryDirectoryFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_OBJECTID_INFORMATION structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
