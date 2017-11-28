---
UID: NF.fltkernel.FltPerformSynchronousIo
title: FltPerformSynchronousIo
author: windows-driver-content
description: A minifilter driver calls FltPerformSynchronousIo to initiate a synchronous I/O operation after calling FltAllocateCallbackData to allocate a callback data structure for the operation.
old-location: ifsk\fltperformsynchronousio.htm
old-project: ifsk
ms.assetid: 14f5260a-b18d-4329-a81e-d24026d9a71d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltPerformSynchronousIo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltPerformSynchronousIo
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
req.iface: 
---

# FltPerformSynchronousIo function



## -description
<p>A minifilter driver calls <b>FltPerformSynchronousIo</b> to initiate a synchronous I/O operation after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541703">FltAllocateCallbackData</a> to allocate a callback data structure for the operation. </p>


## -syntax

````
VOID FltPerformSynchronousIo(
  _Inout_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters
<dl>

### -param <i>CallbackData</i> [in, out]

<dd>
<p>Pointer to a callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure allocated by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541703">FltAllocateCallbackData</a>. This parameter is required and cannot be <b>NULL</b>. The caller is responsible for freeing this structure when it is no longer needed by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff542949">FltFreeCallbackData</a>. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>A minifilter driver calls <b>FltPerformSynchronousIo</b> to initiate a synchronous I/O operation. </p>

<p>Minifilter drivers can only initiate IRP-based I/O operations. They cannot initiate fast I/O or file system filter (FSFilter) callback operations. </p>

<p><b>FltPerformSynchronousIo</b> sends the I/O operation only to the minifilter driver instances attached below the initiating instance (specified in the <i>Instance</i> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541703">FltAllocateCallbackData</a>), and the file system. Minifilter drivers attached above the specified instance do not receive the I/O operation. </p>

<p>Minifilter drivers should use <b>FltPerformSynchronousIo</b> only in cases where routines such as the following cannot be used: </p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541863">FltClose</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541935">FltCreateFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543439">FltQueryInformationFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544589">FltTagFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544608">FltUntagFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541863">FltClose</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541935">FltCreateFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543439">FltQueryInformationFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544589">FltTagFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544608">FltUntagFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a>
</p>

<p>After <b>FltPerformSynchronousIo</b> returns, the caller can reissue the I/O operation by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544311">FltReissueSynchronousIo</a>. Alternatively, the caller can free the callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff542949">FltFreeCallbackData</a> or prepare it to be reused by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544358">FltReuseCallbackData</a>. </p>

<p>A minifilter driver calls <b>FltPerformSynchronousIo</b> to initiate a synchronous I/O operation. </p>

<p>Minifilter drivers can only initiate IRP-based I/O operations. They cannot initiate fast I/O or file system filter (FSFilter) callback operations. </p>

<p><b>FltPerformSynchronousIo</b> sends the I/O operation only to the minifilter driver instances attached below the initiating instance (specified in the <i>Instance</i> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541703">FltAllocateCallbackData</a>), and the file system. Minifilter drivers attached above the specified instance do not receive the I/O operation. </p>

<p>Minifilter drivers should use <b>FltPerformSynchronousIo</b> only in cases where routines such as the following cannot be used: </p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541863">FltClose</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541935">FltCreateFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543439">FltQueryInformationFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544589">FltTagFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544608">FltUntagFile</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541863">FltClose</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541935">FltCreateFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543439">FltQueryInformationFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544589">FltTagFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544608">FltUntagFile</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a>
</p>

<p>After <b>FltPerformSynchronousIo</b> returns, the caller can reissue the I/O operation by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544311">FltReissueSynchronousIo</a>. Alternatively, the caller can free the callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff542949">FltFreeCallbackData</a> or prepare it to be reused by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544358">FltReuseCallbackData</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541703">FltAllocateCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541863">FltClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541935">FltCreateFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542949">FltFreeCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543420">FltPerformAsynchronousIo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543439">FltQueryInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544311">FltReissueSynchronousIo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544358">FltReuseCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544516">FltSetInformationFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544564">FltSetVolumeInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544589">FltTagFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544608">FltUntagFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltPerformSynchronousIo routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
