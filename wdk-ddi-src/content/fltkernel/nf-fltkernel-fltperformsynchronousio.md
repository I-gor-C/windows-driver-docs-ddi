---
UID: NF.fltkernel.FltPerformSynchronousIo
title: FltPerformSynchronousIo function
author: windows-driver-content
description: A minifilter driver calls FltPerformSynchronousIo to initiate a synchronous I/O operation after calling FltAllocateCallbackData to allocate a callback data structure for the operation.
old-location: ifsk\fltperformsynchronousio.htm
old-project: ifsk
ms.assetid: 14f5260a-b18d-4329-a81e-d24026d9a71d
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
---

# FltPerformSynchronousIo function



## -description
A minifilter driver calls <b>FltPerformSynchronousIo</b> to initiate a synchronous I/O operation after calling <a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a> to allocate a callback data structure for the operation. 



## -syntax

````
VOID FltPerformSynchronousIo(
  _Inout_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters

### -param CallbackData [in, out]

Pointer to a callback data (<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>) structure allocated by a previous call to <a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a>. This parameter is required and cannot be <b>NULL</b>. The caller is responsible for freeing this structure when it is no longer needed by calling <a href="ifsk.fltfreecallbackdata">FltFreeCallbackData</a>. 


## -returns
None 


## -remarks
A minifilter driver calls <b>FltPerformSynchronousIo</b> to initiate a synchronous I/O operation. 

Minifilter drivers can only initiate IRP-based I/O operations. They cannot initiate fast I/O or file system filter (FSFilter) callback operations. 

<b>FltPerformSynchronousIo</b> sends the I/O operation only to the minifilter driver instances attached below the initiating instance (specified in the <i>Instance</i> parameter to <a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a>), and the file system. Minifilter drivers attached above the specified instance do not receive the I/O operation. 

Minifilter drivers should use <b>FltPerformSynchronousIo</b> only in cases where routines such as the following cannot be used: 


<a href="ifsk.fltclose">FltClose</a>



<a href="ifsk.fltcreatefile">FltCreateFile</a>



<a href="ifsk.fltqueryinformationfile">FltQueryInformationFile</a>



<a href="ifsk.fltqueryvolumeinformation">FltQueryVolumeInformation</a>



<a href="ifsk.fltreadfile">FltReadFile</a>



<a href="ifsk.fltsetinformationfile">FltSetInformationFile</a>



<a href="ifsk.fltsetvolumeinformation">FltSetVolumeInformation</a>



<a href="ifsk.flttagfile">FltTagFile</a>



<a href="ifsk.fltuntagfile">FltUntagFile</a>



<a href="ifsk.fltwritefile">FltWriteFile</a>


After <b>FltPerformSynchronousIo</b> returns, the caller can reissue the I/O operation by calling <a href="ifsk.fltreissuesynchronousio">FltReissueSynchronousIo</a>. Alternatively, the caller can free the callback data (<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>) structure by calling <a href="ifsk.fltfreecallbackdata">FltFreeCallbackData</a> or prepare it to be reused by calling <a href="ifsk.fltreusecallbackdata">FltReuseCallbackData</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltclose">FltClose</a>
</dt>
<dt>
<a href="ifsk.fltcreatefile">FltCreateFile</a>
</dt>
<dt>
<a href="ifsk.fltfreecallbackdata">FltFreeCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltperformasynchronousio">FltPerformAsynchronousIo</a>
</dt>
<dt>
<a href="ifsk.fltqueryinformationfile">FltQueryInformationFile</a>
</dt>
<dt>
<a href="ifsk.fltqueryvolumeinformation">FltQueryVolumeInformation</a>
</dt>
<dt>
<a href="ifsk.fltreadfile">FltReadFile</a>
</dt>
<dt>
<a href="ifsk.fltreissuesynchronousio">FltReissueSynchronousIo</a>
</dt>
<dt>
<a href="ifsk.fltreusecallbackdata">FltReuseCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltsetinformationfile">FltSetInformationFile</a>
</dt>
<dt>
<a href="ifsk.fltsetvolumeinformation">FltSetVolumeInformation</a>
</dt>
<dt>
<a href="ifsk.flttagfile">FltTagFile</a>
</dt>
<dt>
<a href="ifsk.fltuntagfile">FltUntagFile</a>
</dt>
<dt>
<a href="ifsk.fltwritefile">FltWriteFile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltPerformSynchronousIo routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

