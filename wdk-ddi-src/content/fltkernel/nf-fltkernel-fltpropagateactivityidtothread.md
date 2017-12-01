---
UID: NF.fltkernel.FltPropagateActivityIdToThread
title: FltPropagateActivityIdToThread
author: windows-driver-content
description: The FltPropagateActivityIdToThread routine associates the activity ID from the IRP in the minifilter's callback data with the current thread.
old-location: ifsk\fltpropagateactivityidtothread.htm
old-project: ifsk
ms.assetid: 7453EEB1-F974-4AEB-93C4-A75A79E1FE19
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltPropagateActivityIdToThread
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltPropagateActivityIdToThread
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# FltPropagateActivityIdToThread function



## -description
<p>The <b>FltPropagateActivityIdToThread</b> routine associates the activity ID from the  IRP in the minifilter's callback data with the current thread.</p>


## -syntax

````
NTSTATUS FltPropagateActivityIdToThread(
  _In_    PFLT_CALLBACK_DATA CallbackData,
  _Inout_ LPGUID             PropagatedId,
  _Out_   LPGUID             *OriginalId
);
````


## -parameters
<dl>

### -param <i>CallbackData</i> [in]

<dd>
<p>A pointer to the callback data containing the request with an associated activity ID.</p>
</dd>

### -param <i>PropagatedId</i> [in, out]

<dd>
<p>A pointer to a caller allocated <b>GUID</b> which stores the activity ID for the current thread.</p>
</dd>

### -param <i>OriginalId</i> [out]

<dd>
<p>On return, the <b>GUID</b> pointer referenced by <i>OriginalId</i> points to the activity ID that was previously set for the thread.</p>
</dd>
</dl>

## -returns
<p><b>FltPropagateActivityIdToThread</b> returns one of the following <b>NTSTATUS</b> values.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The callback data does not contain a request for an IRP operation.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>No activity ID is associated with the request in <i>CallbackData</i>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>An activity ID was returned in the <b>GUID</b> value pointed to by <i>Guid</i>.</p>

<p> </p>

## -remarks
<p>The <b>FltPropagateActivityIdToThread</b> routine is  used by trace aware minifilters. A minifilter will use this routine to attach the activity ID from an IRP   to a worker thread processing I/O for the request.

    A minifilter must call <b>IoClearActivityIdThread</b> with the pointer in <i>OriginalId</i> before
    returning control from the worker thread if the call to <b>FltPropagateActivityIdToThread</b> was successful.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with  Windows 8.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetactivityidcallbackdata.md">FltGetActivityIdCallbackData</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsetactivityidcallbackdata.md">FltSetActivityIdCallbackData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltPropagateActivityIdToThread routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
