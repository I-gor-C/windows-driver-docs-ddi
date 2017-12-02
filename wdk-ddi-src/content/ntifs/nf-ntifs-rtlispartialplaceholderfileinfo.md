---
UID: NF.ntifs.RtlIsPartialPlaceholderFileInfo
title: RtlIsPartialPlaceholderFileInfo
author: windows-driver-content
description: The RtlIsPartialPlaceholderFileInfo routine determines if a file is a known type of placeholder, based on the information returned by NtQueryInformationFile or NtQueryDirectoryFile.
old-location: ifsk\rtlispartialplaceholderfileinfo.htm
old-project: ifsk
ms.assetid: B84CC8C1-639D-45B4-A2A4-03BA2F1FF04B
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlIsPartialPlaceholderFileInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlIsPartialPlaceholderFileInfo
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

# RtlIsPartialPlaceholderFileInfo function



## -description
<p>The <b>RtlIsPartialPlaceholderFileInfo</b> routine determines if a file is a known type of placeholder, based on the information
    returned by <b>NtQueryInformationFile</b> or <b>NtQueryDirectoryFile</b>.</p>


## -syntax

````
NTSTATUS RtlIsPartialPlaceholderFileInfo(
  _In_   CONST VOID            *InfoBuffer,
  _In_  FILE_INFORMATION_CLASS InfoClass,
  _Out_ PBOOLEAN               IsPartialPlaceholder
);
````


## -parameters
<dl>

### -param InfoBuffer [in]

<dd>
<p>Specifies a pointer to a caller-allocated buffer which contains information about the file object. If this is from a call
        to <b>NtQueryDirectoryFile</b>, this may point to the first or any subsequent
        subsequent entry in the buffer (found by walking the buffer).</p>
</dd>

### -param InfoClass [in]

<dd>
<p> Specifies which File Information class to use to query InfoBuffer.</p>
</dd>

### -param IsPartialPlaceholder [out]

<dd>
<p><b>IsPartialPlaceholder</b> is a pointer to a boolean which returns <b>TRUE</b> if the file or directory is a placeholder. It  returns <b>FALSE</b> if either the
        file or directory is not a placeholder or is a full placeholder. Returns undefined on failure.</p>
</dd>
</dl>

## -returns
<p>Returns<b> STATUS_SUCCESS</b> if IsPartialPlaceholder is valid and not undefined.</p>

## -remarks
<p> If <b>InfoBuffer</b> is from a call
        to <b>NtQueryDirectoryFile</b>, this may point to the first or any subsequent
        subsequent entry in the buffer which is found by walking the buffer.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10, version 1709.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-rtlispartialplaceholder.md">RtlIsPartialPlaceholder</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlIsPartialPlaceholderFileInfo routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
