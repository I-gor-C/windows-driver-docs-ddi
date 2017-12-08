---
UID: NF.fltkernel.FltAllocateCallbackData
title: FltAllocateCallbackData function
author: windows-driver-content
description: FltAllocateCallbackData allocates a callback data structure that a minifilter driver can use to initiate an I/O request.
old-location: ifsk\fltallocatecallbackdata.htm
old-project: ifsk
ms.assetid: a2afb8b8-b0e2-4d22-9d93-33ba2b2f8933
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltAllocateCallbackData
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
req.alt-api: FltAllocateCallbackData
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL
---

# FltAllocateCallbackData function



## -description
<b>FltAllocateCallbackData</b> allocates a callback data structure that a minifilter driver can use to initiate an I/O request. 


## -syntax

````
NTSTATUS FltAllocateCallbackData(
  _In_     PFLT_INSTANCE      Instance,
  _In_opt_ PFILE_OBJECT       FileObject,
  _Out_    PFLT_CALLBACK_DATA *RetNewCallbackData
);
````


## -parameters

### -param Instance [in]

Opaque instance pointer for the minifilter driver instance that is initiating the I/O operation. This parameter is required and cannot be <b>NULL</b>. 

### -param FileObject [in, optional]

File object pointer to be used in the I/O operation. This parameter is optional and can be <b>NULL</b>. 

### -param RetNewCallbackData [out]

Pointer to a caller-allocated variable that receives the address of the newly allocated callback data (<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>) structure. 

## -returns
<b>FltAllocateCallbackData</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: 
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>
<a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a> encountered a pool allocation failure when attempting to allocate the callback data structure. This is an error code. 

 

## -remarks
A minifilter driver can call <b>FltAllocateCallbackData</b> to allocate a callback data (<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>) structure for an I/O operation initiated by the minifilter driver. 

Callback data structures are allocated from nonpaged pool. 

After initializing the parameters of the callback data structure returned by <b>FltAllocateCallbackData</b>, the caller initiates the I/O operation by passing the structure to <a href="ifsk.fltperformsynchronousio">FltPerformSynchronousIo</a> or <a href="ifsk.fltperformasynchronousio">FltPerformAsynchronousIo</a>. These routines send the I/O operation only to the minifilter driver instances attached below the initiating instance (specified in the <i>Instance</i> parameter) and to the file system. Minifilter drivers attached above the specified instance do not receive the I/O operation. 

Minifilter drivers can only initiate IRP-based I/O operations. They cannot initiate fast I/O or file system filter (FSFilter) callback operations. 

Minifilter drivers should use <b>FltAllocateCallbackData</b>, <a href="ifsk.fltperformasynchronousio">FltPerformAsynchronousIo</a>, and <a href="ifsk.fltperformsynchronousio">FltPerformSynchronousIo</a> only for I/O operations for which routines such as the following cannot be used: 


<a href="ifsk.fltclose">FltClose</a>



<a href="ifsk.fltcreatefile">FltCreateFile</a>



<a href="ifsk.fltqueryvolumeinformation">FltQueryVolumeInformation</a>



<a href="ifsk.fltreadfile">FltReadFile</a>



<a href="ifsk.fltsetvolumeinformation">FltSetVolumeInformation</a>



<a href="ifsk.flttagfile">FltTagFile</a>



<a href="ifsk.fltuntagfile">FltUntagFile</a>



<a href="ifsk.fltwritefile">FltWriteFile</a>


When the callback data structure allocated by <b>FltAllocateCallbackData</b> is no longer needed, the caller is responsible for freeing it by calling <a href="ifsk.fltfreecallbackdata">FltFreeCallbackData</a>. 

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
<a href="ifsk.fltperformsynchronousio">FltPerformSynchronousIo</a>
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
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltAllocateCallbackData routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
