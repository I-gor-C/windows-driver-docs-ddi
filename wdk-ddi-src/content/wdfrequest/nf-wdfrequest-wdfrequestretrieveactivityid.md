---
UID: NF.wdfrequest.WdfRequestRetrieveActivityId
title: WdfRequestRetrieveActivityId
author: windows-driver-content
description: The WdfRequestRetrieveActivityId method retrieves the current activity identifier associated with an I/O request.
old-location: wdf\wdfrequestretrieveactivityid.htm
old-project: wdf
ms.assetid: 6E38514E-75BD-4F98-AD12-FA4E31654C3E
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfRequestRetrieveActivityId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WdfRequestRetrieveActivityId
req.alt-loc: WUDFx02000.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WUDFx02000.lib
req.dll: WUDFx02000.dll; TBD
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestRetrieveActivityId function



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>WdfRequestRetrieveActivityId</b> method retrieves the current activity identifier associated with an I/O request.</p>


## -syntax

````
NTSTATUS WdfRequestRetrieveActivityId(
  _In_  WDFREQUEST Request,
  _Out_ LPGUID     ActivityId
);
````


## -parameters
<dl>

### -param Request [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>

### -param ActivityId [out]

<dd>
<p>A pointer to a location to store the retrieved GUID.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, <b>WdfRequestRetrieveActivityId</b> returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>No activity ID is associated with the request.</p>

<p> </p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>Requests reflected from kernel mode have an activity identifier available only if the Kernel Trace provider is enabled or if the UMDF driver called <a href="..\wdfrequest\nf-wdfrequest-wdfrequestsetactivityid.md">WdfRequestSetActivityId</a> after receiving the request. For more information about Event Tracing for Windows (ETW), see <a href="etw.event_tracing_portal">Event Tracing</a>.</p>

<p>Requests initiated by the UMDF driver have an activity identifier available only if the UMDF driver previously called  <a href="..\wdfrequest\nf-wdfrequest-wdfrequestsetactivityid.md">WdfRequestSetActivityId</a>.</p>

<p>The framework does not clear a request's activity identifier when the driver calls <a href="..\wdfrequest\nf-wdfrequest-wdfrequestreuse.md">WdfRequestReuse</a>.</p>

<p>For more information about activity identifiers, see <a href="wdf.using_activity_identifiers">Using Activity Identifiers</a>.</p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.dll; </dt>
<dt>TBD</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdfrequestsetactivityid.md">WdfRequestSetActivityId</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestRetrieveActivityId method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
