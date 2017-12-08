---
UID: NF.fltkernel.FltReuseCallbackData
title: FltReuseCallbackData function
author: windows-driver-content
description: The FltReuseCallbackData routine reinitializes a callback data structure so that it can be reused.
old-location: ifsk\fltreusecallbackdata.htm
old-project: ifsk
ms.assetid: c8671ba7-6128-4f0f-b5b1-32ce35e31168
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltReuseCallbackData
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
req.alt-api: FltReuseCallbackData
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

# FltReuseCallbackData function



## -description
The <b>FltReuseCallbackData</b> routine reinitializes a callback data structure so that it can be reused. 


## -syntax

````
VOID FltReuseCallbackData(
  _Inout_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters

### -param CallbackData [in, out]

Pointer to the callback data (<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>) structure to be reused. This structure must have been allocated by a previous call to <a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a>. This parameter is required and cannot be <b>NULL</b>. 

## -returns
None 

## -remarks
<b>FltReuseCallbackData</b> reinitializes a callback data (<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>) structure so that it can be used in a new I/O operation. <b>FltReuseCallbackData</b> does not change the <b>TargetInstance</b> field or the <b>TargetFileObject</b> field of the callback data structure's I/O parameter block. 

The <b>FltReuseCallbackData</b> routine frees any <a href="kernel.mdl">MDL</a> chain associated with the supplied <i>CallbackData</i> object. A pointer to an MDL chain associated with a <a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a> object will be invalid after a call to <b>FltReuseCallbackData</b> for that object.

Using <b>FltReuseCallbackData</b> to reuse a callback data structure is faster than freeing the structure and allocating a new one. 

A minifilter driver should use <b>FltReuseCallbackData</b> only on a callback data structure that the minifilter driver previously allocated with <a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a> and used in a call to <a href="ifsk.fltperformsynchronousio">FltPerformSynchronousIo</a> or <a href="ifsk.fltperformasynchronousio">FltPerformAsynchronousIo</a>. 

If the callback data structure was used for asynchronous I/O, the minifilter driver should not call <b>FltReuseCallbackData</b> until the <i>CallbackRoutine</i> specified in the call to <a href="ifsk.fltperformasynchronousio">FltPerformAsynchronousIo</a> is called. 

In particular, a minifilter driver should not use this routine for any callback data structures not allocated by the minifilter driver itself. 

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
<a href="ifsk.fltfreecallbackdata">FltFreeCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltperformasynchronousio">FltPerformAsynchronousIo</a>
</dt>
<dt>
<a href="ifsk.fltperformsynchronousio">FltPerformSynchronousIo</a>
</dt>
<dt>
<a href="ifsk.fltreissuesynchronousio">FltReissueSynchronousIo</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltReuseCallbackData routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
