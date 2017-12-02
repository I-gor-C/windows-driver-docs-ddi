---
UID: NF.wdm.ClfsSetLogFileInformation
title: ClfsSetLogFileInformation
author: windows-driver-content
description: The ClfsSetLogFileInformation routine sets metadata and state information for a specified stream and its underlying physical log.
old-location: kernel\clfssetlogfileinformation.htm
old-project: kernel
ms.assetid: 9f44b1ce-25d4-438f-b4eb-cff7bbfb5e0a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ClfsSetLogFileInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsSetLogFileInformation
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

# ClfsSetLogFileInformation function



## -description
<p>The <b>ClfsSetLogFileInformation</b> routine sets metadata and state information for a specified stream and its underlying physical log.</p>


## -syntax

````
NTSTATUS ClfsSetLogFileInformation(
  _In_ PLOG_FILE_OBJECT           plfoLog,
  _In_ CLFS_LOG_INFORMATION_CLASS eInformationClass,
  _In_ PVOID                      pinfoBuffer,
  _In_ ULONG                      cbBuffer
);
````


## -parameters
<dl>

### -param plfoLog [in]

<dd>
<p>A pointer to a <a href="kernel.log_file_object">LOG_FILE_OBJECT</a> structure that represents a CLFS stream. The caller previously obtained this pointer by calling <a href="..\wdm\nf-wdm-clfscreatelogfile.md">ClfsCreateLogFile</a>.</p>
</dd>

### -param eInformationClass [in]

<dd>
<p>A <a href="kernel.clfs_log_information_class">CLFS_LOG_INFORMATION_CLASS</a> value that specifies the class of information being set.</p>
</dd>

### -param pinfoBuffer [in]

<dd>
<p>A pointer to a buffer that supplies the log information. The structure of this buffer varies according to the class of information specified by <i>eInformationClass</i>. The following table shows the relationship between the information class and the buffer type.</p>
<table>
<tr>
<th>Value of eInformationClass</th>
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

### -param cbBuffer [in]

<dd>
<p>The size, in bytes, of the buffer pointed to by <i>pinfoBuffer</i>.</p>
</dd>
</dl>

## -returns
<p><b>ClfsSetLogFileInformation</b> returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h.</p>

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
<p>Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
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
<a href="kernel.clfs_information">CLFS_INFORMATION</a>
</dt>
<dt>
<a href="kernel.clfs_log_information_class">CLFS_LOG_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--clfs-stream-id-information.md">CLFS_STREAM_ID_INFORMATION</a>
</dt>
<dt>
<a href="kernel.log_file_object">LOG_FILE_OBJECT</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-clfscreatelogfile.md">ClfsCreateLogFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-clfsquerylogfileinformation.md">ClfsQueryLogFileInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsSetLogFileInformation routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
