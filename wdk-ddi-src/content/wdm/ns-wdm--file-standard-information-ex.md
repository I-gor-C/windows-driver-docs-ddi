---
UID: NS.wdm._FILE_STANDARD_INFORMATION_EX
title: FILE_STANDARD_INFORMATION_EX
author: windows-driver-content
description: The FILE_STANDARD_INFORMATION_EX structure is used as an argument to routines that query or set file information.
old-location: kernel\file_standard_information_ex.htm
old-project: kernel
ms.assetid: 460ADE5A-0302-4695-A9E4-43B309738BE7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FILE_STANDARD_INFORMATION_EX, FILE_STANDARD_INFORMATION_EX, *PFILE_STANDARD_INFORMATION_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_STANDARD_INFORMATION_EX
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# FILE_STANDARD_INFORMATION_EX structure



## -description
<p>The <b>FILE_STANDARD_INFORMATION_EX</b> structure is used as an argument to routines that query or set file information.</p>


## -syntax

````
typedef struct _FILE_STANDARD_INFORMATION_EX {
  LARGE_INTEGER AllocationSize;
  LARGE_INTEGER EndOfFile;
  ULONG         NumberOfLinks;
  BOOLEAN       DeletePending;
  BOOLEAN       Directory;
  BOOLEAN       AlternateStream;
  BOOLEAN       MetadataAttribute;
} FILE_STANDARD_INFORMATION_EX, *PFILE_STANDARD_INFORMATION_EX;
````


## -struct-fields
<dl>

### -field AllocationSize

<dd>
<p>The file allocation size in bytes. Usually, this value is a multiple of the sector or cluster size of the underlying physical device. </p>
</dd>

### -field EndOfFile

<dd>
<p>The end of file location as a byte offset.</p>
</dd>

### -field NumberOfLinks

<dd>
<p>The number of hard links to the file.</p>
</dd>

### -field DeletePending

<dd>
<p>The delete pending status. <b>TRUE</b> indicates that a file deletion has been requested.</p>
</dd>

### -field Directory

<dd>
<p>The file directory status. <b>TRUE</b> indicates the file object represents a directory. </p>
</dd>

### -field AlternateStream

<dd>
<p>The alternate data stream status. <b>TRUE</b> indicates the file object represents an alternate data stream. </p>
</dd>

### -field MetadataAttribute

<dd>
<p>The metadata attribute status. <b>TRUE</b> indicates the file object represents a metadata attribute. </p>
</dd>
</dl>

## -remarks
<p><b>EndOfFile</b> specifies the byte offset to the end of the file. Because this value is zero-based, it actually refers to the first free byte in the file; that is, it is the offset to the byte immediately following the last valid byte in the file. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20FILE_STANDARD_INFORMATION_EX structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
