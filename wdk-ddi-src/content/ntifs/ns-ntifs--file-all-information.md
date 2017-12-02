---
UID: NS.ntifs._FILE_ALL_INFORMATION
title: FILE_ALL_INFORMATION
author: windows-driver-content
description: The FILE_ALL_INFORMATION structure is a container for several FILE_XXX_INFORMATION structures.
old-location: kernel\file_all_information.htm
old-project: kernel
ms.assetid: 1b5f314c-6918-4cb8-a4e2-9ca0f4c5ea54
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FILE_ALL_INFORMATION, FILE_ALL_INFORMATION, *PFILE_ALL_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_ALL_INFORMATION
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
req.irql: 
req.iface: 
---

# FILE_ALL_INFORMATION structure



## -description
<p>The <b>FILE_ALL_INFORMATION</b> structure is a container for several <b>FILE_<i>XXX</i>_INFORMATION</b> structures.</p>


## -syntax

````
typedef struct _FILE_ALL_INFORMATION {
  FILE_BASIC_INFORMATION     BasicInformation;
  FILE_STANDARD_INFORMATION  StandardInformation;
  FILE_INTERNAL_INFORMATION  InternalInformation;
  FILE_EA_INFORMATION        EaInformation;
  FILE_ACCESS_INFORMATION    AccessInformation;
  FILE_POSITION_INFORMATION  PositionInformation;
  FILE_MODE_INFORMATION      ModeInformation;
  FILE_ALIGNMENT_INFORMATION AlignmentInformation;
  FILE_NAME_INFORMATION      NameInformation;
} FILE_ALL_INFORMATION, *PFILE_ALL_INFORMATION;
````


## -struct-fields
<dl>

### -field BasicInformation

<dd>
<p>Contains basic information about the file, which includes the file attributes and the file creation time. This member is a <a href="..\wdm\ns-wdm--file-basic-information.md">FILE_BASIC_INFORMATION</a> structure. </p>
</dd>

### -field StandardInformation

<dd>
<p>Contains standard information about a file, which includes the file allocation size, the end-of-file offset, and whether the file is a directory. This member is a <a href="..\wdm\ns-wdm--file-standard-information.md">FILE_STANDARD_INFORMATION</a> structure. </p>
</dd>

### -field InternalInformation

<dd>
<p>Contains the 8-byte file reference number for the file. This member is a <a href="..\ntifs\ns-ntifs--file-internal-information.md">FILE_INTERNAL_INFORMATION</a> structure. </p>
</dd>

### -field EaInformation

<dd>
<p>Specifies the size of the extended attributes of the file. This member is a <a href="..\ntifs\ns-ntifs--file-ea-information.md">FILE_EA_INFORMATION</a> structure. </p>
</dd>

### -field AccessInformation

<dd>
<p>Specifies the client's access rights to the file. This member is a <a href="..\ntifs\ns-ntifs--file-access-information.md">FILE_ACCESS_INFORMATION</a> structure. </p>
</dd>

### -field PositionInformation

<dd>
<p>Specifies the current file position. This member is a <a href="..\wdm\ns-wdm--file-position-information.md">FILE_POSITION_INFORMATION</a> structure. </p>
</dd>

### -field ModeInformation

<dd>
<p>Specifies the access mode in which the file was created or opened. This member is a <a href="..\ntifs\ns-ntifs--file-mode-information.md">FILE_MODE_INFORMATION</a> structure. </p>
</dd>

### -field AlignmentInformation

<dd>
<p>Specifies the device's memory address alignment requirement for data transfers. This member is a <a href="..\ntddk\ns-ntddk--file-alignment-information.md">FILE_ALIGNMENT_INFORMATION</a> structure. </p>
</dd>

### -field NameInformation

<dd>
<p>Contains the file name. This member is a <a href="..\ntddk\ns-ntddk--file-name-information.md">FILE_NAME_INFORMATION</a> structure. This structure contains the first character in the file name string. The additional characters in the file name string immediately follow the structure. To accommodate the full file name, the buffer that is allocated to contain a <b>FILE_ALL_INFORMATION</b> structure must be large enough to contain both the structure and the part of the file name string that follows the structure. </p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a> routine.</p>

<p><b>FILE_ALL_INFORMATION</b> combines several file-information structures into a single structure to reduce the number of queries that are required to obtain information about a file. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows XP and later versions of Windows.</p>
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
<a href="..\ntifs\ns-ntifs--file-access-information.md">FILE_ACCESS_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--file-alignment-information.md">FILE_ALIGNMENT_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--file-basic-information.md">FILE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-ea-information.md">FILE_EA_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-internal-information.md">FILE_INTERNAL_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--file-mode-information.md">FILE_MODE_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--file-name-information.md">FILE_NAME_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--file-position-information.md">FILE_POSITION_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--file-standard-information.md">FILE_STANDARD_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20FILE_ALL_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
