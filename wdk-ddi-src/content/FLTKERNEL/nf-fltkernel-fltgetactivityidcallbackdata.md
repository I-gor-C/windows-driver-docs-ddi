---
UID: NF.fltkernel.FltGetActivityIdCallbackData
title: FltGetActivityIdCallbackData
author: windows-driver-content
description: The FltGetActivityIdCallbackData routine retrieves the current activity ID associated with a request in a minifilter's callback data.
old-location: ifsk\fltgetactivityidcallbackdata.htm
ms.assetid: 3DAA2135-768E-4A37-B2FD-9915F16D8A66
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetActivityIdCallbackData
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
ms.keywords: FltGetActivityIdCallbackData
req.iface: 
---

# FltGetActivityIdCallbackData function



## -description
<p>The <b>FltGetActivityIdCallbackData</b> routine retrieves the current activity ID associated with a request in a minifilter's callback data.</p>


## -syntax

````
NTSTATUS FltGetActivityIdCallbackData(
  _In_  PFLT_CALLBACK_DATA CallbackData,
  _Out_ LPGUID             Guid
);
````


## -parameters
<dl>

### -param <i>CallbackData</i> [in]

<dd>
<p>A pointer to the callback data containing the request with an associated activity ID.</p>
</dd>

### -param <i>Guid</i> [out]

<dd>
<p>A pointer to the GUID structure receiving the activity ID.</p>
</dd>
</dl>

## -returns
<p><b>FltGetActivityIdCallbackData</b> returns one of the following <b>NTSTATUS</b> values.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The callback data does not contain a request for an IRP operation.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>No activity ID is associated with the request in <i>CallbackData</i>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>An activity ID was returned in the <b>GUID</b> value pointed to by <i>Guid</i>.</p>

<p> </p>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967702">FltSetActivityIdCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967700">FltPropagateActivityIdToThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetActivityIdCallbackData routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
