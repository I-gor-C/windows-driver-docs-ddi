---
UID: NF.wdm.ClfsQueryLogFileInformation
title: ClfsQueryLogFileInformation
author: windows-driver-content
description: The ClfsQueryLogFileInformation routine returns metadata and state information for a specified CLFS stream or its underlying physical log or both.
old-location: kernel\clfsquerylogfileinformation.htm
old-project: kernel
ms.assetid: a907f219-9e4a-415f-821c-d419b7fde729
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ClfsQueryLogFileInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsQueryLogFileInformation
req.alt-loc: Clfs.sys,Ext-MS-Win-fs-clfs-l1-1-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Clfs.lib
req.dll: Clfs.sys
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ClfsQueryLogFileInformation function



## -description
<p>The <b>ClfsQueryLogFileInformation</b> routine returns metadata and state information for a specified CLFS stream or its underlying physical log or both.</p>


## -syntax

````
NTSTATUS  ClfsQueryLogFileInformation(
  _In_    PLOG_FILE_OBJECT           plfoLog,
  _In_    CLFS_LOG_INFORMATION_CLASS eInformationClass,
  _Out_   PVOID                      pinfoBuffer,
  _Inout_ PULONG                     pcbBuffer
);
````


## -parameters
<dl>

### -param <i>plfoLog</i> [in]

<dd>
<p>A pointer to a <a href="kernel.log_file_object">LOG_FILE_OBJECT</a> structure that represents a CLFS stream. The caller previously obtained this pointer by calling <a href="..\wdm\nf-wdm-clfscreatelogfile.md">ClfsCreateLogFile</a>.</p>
</dd>

### -param <i>eInformationClass</i> [in]

<dd>
<p>A value from the <a href="kernel.clfs_log_information_class">CLFS_LOG_INFORMATION_CLASS</a> enumeration that specifies the type of information being requested.</p>
</dd>

### -param <i>pinfoBuffer</i> [out]

<dd>
<p>A pointer to a buffer that receives the log information. The structure of this buffer depends on the value of <i>eInformationClass</i>. The following table shows the relationship between the information class and the data type of the buffer.</p>
<table>
<tr>
<th>Value of <i>eInformationClass</i></th>
<th>Type of buffer pointed to by <i>pinfoBuffer</i></th>
</tr>
<tr>
<td>
<p><b>ClfsLogBasicInformation</b></p>
</td>
<td>
<p>
<a href="kernel.clfs_information">CLFS_INFORMATION</a>
</p>
</td>
</tr>
<tr>
<td>
<p><b>ClfsLogBasicInformationPhysical</b></p>
</td>
<td>
<p>
<a href="kernel.clfs_information">CLFS_INFORMATION</a>
</p>
</td>
</tr>
<tr>
<td>
<p><b>ClfsLogNameInformation</b></p>
</td>
<td>
<p>
<a href="..\wdm\ns-wdm--clfs-log-name-information.md">CLFS_LOG_NAME_INFORMATION</a>
</p>
</td>
</tr>
<tr>
<td>
<p><b>ClfsLogPhysicalNameInformation</b></p>
</td>
<td>
<p>
<a href="..\wdm\ns-wdm--clfs-log-name-information.md">CLFS_LOG_NAME_INFORMATION</a>
</p>
</td>
</tr>
<tr>
<td>
<p><b>ClfsLogStreamIdentifierInformation</b></p>
</td>
<td>
<p>
<a href="..\wdm\ns-wdm--clfs-stream-id-information.md">CLFS_STREAM_ID_INFORMATION</a>
</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pcbBuffer</i> [in, out]

<dd>
<p>The size, in bytes, of the buffer pointed to by <i>pinfoBuffer</i>.</p>
</dd>
</dl>

## -returns
<p><b>ClfsQueryLogFileInformation</b> returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h.</p>

## -remarks
<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.</p>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-clfssetlogfileinformation.md">ClfsSetLogFileInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsQueryLogFileInformation routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
