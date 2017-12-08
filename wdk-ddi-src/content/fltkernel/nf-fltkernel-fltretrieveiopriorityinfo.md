---
UID: NF.fltkernel.FltRetrieveIoPriorityInfo
title: FltRetrieveIoPriorityInfo function
author: windows-driver-content
description: The FltRetrieveIoPriorityInfo routine is used by a minifilter driver to retrieve priority information from a thread.
old-location: ifsk\fltretrieveiopriorityinfo.htm
old-project: ifsk
ms.assetid: b764e55e-e58b-4a4f-a32f-84e3cfd5f8c4
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltRetrieveIoPriorityInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltRetrieveIoPriorityInfo
req.alt-loc: FltMgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fltmgr.lib
req.dll: FltMgr.sys
req.irql: <= DISPATCH_LEVEL
---

# FltRetrieveIoPriorityInfo function



## -description
The <b>FltRetrieveIoPriorityInfo</b> routine is used by a minifilter driver to retrieve priority information from a thread.


## -syntax

````
NTSTATUS FltRetrieveIoPriorityInfo(
  _In_opt_ PFLT_CALLBACK_DATA Data,
  _In_opt_ PFILE_OBJECT       FileObject,
  _In_opt_ PETHREAD           Thread,
  _Inout_  PIO_PRIORITY_INFO  PriorityInfo
);
````


## -parameters

### -param Data [in, optional]


      An optional pointer to a <a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a> structure, which represents an I/O operation.  This parameter can be <b>NULL</b>.
     

### -param FileObject [in, optional]

An optional pointer to the file object associated with the I/O operation.  This parameter can be <b>NULL</b>.

### -param Thread [in, optional]

An optional pointer to the thread in which to retrieve priority information from.  This parameter can be <b>NULL</b>.

### -param PriorityInfo [in, out]

A pointer to an <a href="ifsk.io_priority_info">IO_PRIORITY_INFO</a> structure used to receive the priority information from the given thread.  The IO_PRIORITY_INFO structure must be initialized by an appropriate routine before it can be used by this routine. See the following Remarks section for more information.

## -returns
The <b>FltRetrieveIoPriorityInfo</b> routine returns STATUS_SUCCESS or an appropriate NTSTATUS value.

## -remarks
The <b>FltRetrieveIoPriorityInfo</b> routine retrieves priority information and saves the information in the structure pointed to by the <i>PriorityInfo</i> parameter.

Typically, the <b>FltRetrieveIoPriorityInfo</b> routine is used in conjunction with the <a href="ifsk.fltapplypriorityinfothread">FltApplyPriorityInfoThread</a> routine to save and then set a thread's I/O priority, paging priority, and thread priority.

If the <i>Thread</i> parameter is non-<b>NULL</b>, the thread's paging priority and thread priority will be retrieved and placed in the <b>PagePriority</b> and <b>ThreadPriority</b> members of the IO_PRIORITY_INFO structure pointed to by the <i>PriorityInfo</i> parameter.  If the <i>Thread</i> parameter is <b>NULL</b>, the <b>ThreadPriority</b> and <b>PagePriority</b> members of the IO_PRIORITY_INFO structure are marked with sentinel values indicating that the thread's paging and thread priorities should not be changed by the system.  Note that these sentinel values stay in effect until explicitly changed.

The following pseudo-code example describes what I/O priority value is retrieved and placed in the <b>IoPriority</b> member of the IO_PRIORITY_INFO structure pointed to by the <i>PriorityInfo </i> parameter.


<div class="alert"><b>Note</b>  
     If the IO_PRIORITY_INFO structure pointed to by the <i>PriorityInfo</i> parameter has not been initialized, you must do so prior to calling this routine, by calling the <a href="ifsk.ioinitializepriorityinfo">IoInitializePriorityInfo</a> routine.</div>
<div> </div>


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
Version
</th>
<td width="70%">
This routine is available starting with Windows Vista.
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
<dt>Fltmgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>FltMgr.sys</dt>
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
<a href="ifsk.fltapplypriorityinfothread">FltApplyPriorityInfoThread</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhint">FltGetIoPriorityHint</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhintfromcallbackdata">FltGetIoPriorityHintFromCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhintfromfileobject">FltGetIoPriorityHintFromFileObject</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhintfromthread">FltGetIoPriorityHintFromThread</a>
</dt>
<dt>
<a href="ifsk.fltretrieveiopriorityinfo">FltRetrieveIoPriorityInfo</a>
</dt>
<dt>
<a href="ifsk.fltsetiopriorityhintintocallbackdata">FltSetIoPriorityHintIntoCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltsetiopriorityhintintofileobject">FltSetIoPriorityHintIntoFileObject</a>
</dt>
<dt>
<a href="ifsk.fltsetiopriorityhintintothread">FltSetIoPriorityHintIntoThread</a>
</dt>
<dt>
<a href="ifsk.io_priority_info">IO_PRIORITY_INFO</a>
</dt>
<dt>
<a href="ifsk.ioinitializepriorityinfo">IoInitializePriorityInfo</a>
</dt>
<dt>
<a href="kernel.psgetcurrentthread">PsGetCurrentThread</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltRetrieveIoPriorityInfo routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
