---
UID: NS.ntddk._FILE_NAME_INFORMATION
title: FILE_NAME_INFORMATION
author: windows-driver-content
description: The FILE_NAME_INFORMATION structure is used as argument to the ZwQueryInformationFile and ZwSetInformationFile routines.
old-location: kernel\file_name_information.htm
old-project: kernel
ms.assetid: 04ec8e82-d74d-4827-8533-aa57e3638a45
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: FILE_NAME_INFORMATION, FILE_NAME_INFORMATION, *PFILE_NAME_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_NAME_INFORMATION
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FILE_NAME_INFORMATION structure



## -description
<p>The <b>FILE_NAME_INFORMATION</b> structure is used as argument to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a> routines.</p>


## -syntax

````
typedef struct _FILE_NAME_INFORMATION {
  ULONG FileNameLength;
  WCHAR FileName[1];
} FILE_NAME_INFORMATION, *PFILE_NAME_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>FileNameLength</b>

<dd>
<p>Specifies the length, in bytes, of the file name string.</p>
</dd>

### -field <b>FileName</b>

<dd>
<p>Specifies the first character of the file name string. This is followed in memory by the remainder of the string.</p>
</dd>
</dl>

## -remarks
<p>The <b>ZwQueryInformationFile</b> routine uses this structure to return the file name string to the caller. For more information about the form of the name returned, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a>.</p>

<p>Callers of <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a> can use this structure to specify a new short name for a file.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20FILE_NAME_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
