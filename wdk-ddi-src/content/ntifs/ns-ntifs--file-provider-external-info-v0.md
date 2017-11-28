---
UID: NS.ntifs._FILE_PROVIDER_EXTERNAL_INFO_V0
title: FILE_PROVIDER_EXTERNAL_INFO_V0
author: windows-driver-content
description: This structure may be altered or unavailable. Instead, use FILE_PROVIDER_EXTERNAL_INFO_V1.
old-location: ifsk\file_provider_external_info_v0.htm
old-project: ifsk
ms.assetid: E2368589-9F75-4743-9D38-323221B20EF8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_PROVIDER_EXTERNAL_INFO_V0, FILE_PROVIDER_EXTERNAL_INFO_V0, *PFILE_PROVIDER_EXTERNAL_INFO_V0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Windows.h, WinIoCtl.h, Ntifs.h, Windows.h, WinIoCtl.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_PROVIDER_EXTERNAL_INFO_V0
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

# FILE_PROVIDER_EXTERNAL_INFO_V0 structure



## -description
<p>This structure may be altered or unavailable. Instead, use <a href="https://msdn.microsoft.com/library/windows/hardware/mt426732">FILE_PROVIDER_EXTERNAL_INFO_V1</a>.</p>


## -syntax

````
typedef struct _FILE_PROVIDER_EXTERNAL_INFO_V0 {
  ULONG Version;
  ULONG Algorithm;
} FILE_PROVIDER_EXTERNAL_INFO_V0, *PFILE_PROVIDER_EXTERNAL_INFO_V0;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of the provider to use. Specify FILE_PROVIDER_CURRENT_VERSION.</p>
</dd>

### -field <b>Algorithm</b>

<dd>
<p>Specifies the compression algorithm that is used to compress this file. Currently defined algorithms are: </p>
<ul>
<li>FILE_PROVIDER_COMPRESSION_XPRESS4K: Indicates that the data for the file should be compressed in 4kb chunks with the XPress algorithm. This algorithm is designed to be computationally lightweight, and provides for rapid access to data.</li>
<li>FILE_PROVIDER_COMPRESSION_LZX: Indicates that the data for the file should be compressed in 32kb chunks with the LZX algorithm. This algorithm is designed to be highly compact, and provides for small footprint for infrequently accessed data.</li>
<li>FILE_PROVIDER_COMPRESSION_XPRESS8K: Indicates that the data for the file should be compressed in 8kb chunks with the XPress algorithm. </li>
<li>FILE_PROVIDER_COMPRESSION_XPRESS16K: Indicates that the data for the file should be compressed in 16kb chunks with the XPress algorithm.</li>
</ul>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Windows.h, WinIoCtl.h, Ntifs.h, Windows.h, WinIoCtl.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt426732">FILE_PROVIDER_EXTERNAL_INFO_V1</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_PROVIDER_EXTERNAL_INFO_V0 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
