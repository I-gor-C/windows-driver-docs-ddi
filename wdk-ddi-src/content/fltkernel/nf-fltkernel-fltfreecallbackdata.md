---
UID: NF.fltkernel.FltFreeCallbackData
title: FltFreeCallbackData function
author: windows-driver-content
description: The FltFreeCallbackData routine frees a callback data structure allocated by the FltAllocateCallbackData routine.
old-location: ifsk\fltfreecallbackdata.htm
old-project: ifsk
ms.assetid: 45cf398f-f7f0-4eb1-b490-4123c6c9f6fa
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltFreeCallbackData
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
req.alt-api: FltFreeCallbackData
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
req.irql: <= DISPATCH_LEVEL
---

# FltFreeCallbackData function



## -description
The <b>FltFreeCallbackData</b> routine frees a callback data structure allocated by the <a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a> routine. 


## -syntax

````
VOID FltFreeCallbackData(
  _In_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters

### -param CallbackData [in]

Pointer to the callback data structure to be freed. This <a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a> structure must have been allocated by a previous call to <a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a>. This parameter is required and cannot be <b>NULL</b>. 

## -returns
None 

## -remarks
A minifilter driver should use <b>FltFreeCallbackData</b> only on a callback data structure (<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>) that it previously allocated with <a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a> and used in a call to <a href="ifsk.fltperformasynchronousio">FltPerformAsynchronousIo</a> or <a href="ifsk.fltperformsynchronousio">FltPerformSynchronousIo</a>. 

In particular, a minifilter driver should not use this routine for any callback data structures that were not allocated by the minifilter driver itself. 

The <b>FltFreeCallbackData</b> routine frees any <a href="kernel.mdl">MDL</a> chain associated with the supplied <i>CallbackData</i> object. A pointer to an MDL chain associated with a <a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a> object will be invalid after a call to <b>FltFreeCallbackData</b> for that object.

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
&lt;= DISPATCH_LEVEL
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
<a href="ifsk.fltperformasynchronousio">FltPerformAsynchronousIo</a>
</dt>
<dt>
<a href="ifsk.fltperformsynchronousio">FltPerformSynchronousIo</a>
</dt>
<dt>
<a href="ifsk.fltreusecallbackdata">FltReuseCallbackData</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltFreeCallbackData routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
