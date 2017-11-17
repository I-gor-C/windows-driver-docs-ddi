---
UID: NF.wdm.SeEtwWriteKMCveEvent
title: SeEtwWriteKMCveEvent
author: windows-driver-content
description: The SeEtwWriteKMCveEvent function is a tracing function for publishing events when an attempted security vulnerability exploit is detected in your kernel-mode drivers.
old-location: devtest\seetwwritekmcveevent.htm
ms.assetid: 9CF6C8FC-869A-4667-9859-845BFF093549
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: devtest
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10 and later versions of Windows
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SeEtwWriteKMCveEvent
req.alt-loc: Ntoskrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: Ntoskrnl.exe
req.irql: 
ms.keywords: SeEtwWriteKMCveEvent
req.iface: 
req.product: Windows 10 or later.
---

# SeEtwWriteKMCveEvent function



## -description
<p>The <b> 	SeEtwWriteKMCveEvent</b> function is a tracing function for publishing events when an attempted security vulnerability exploit is detected in your kernel-mode drivers.   </p>


## -syntax

````
__checkReturn HRESULT NTStatus SeEtwWriteKMCveEvent(
  _In_     PCUNICODE_STRING CveId,
  _In_opt_ PCUNICODE_STRING AdditionalDetails
);
````


## -parameters
<dl>

### -param <i>CveId</i> [in]

<dd>
<p>A pointer to a string mentioning the CVE-ID associated with the vulnerability for which this event is being raised. Technical guidance for handling the CVE-ID is shared <a href="ttp://go.microsoft.com/fwlink/?LinkId=798519">here</a></p>
</dd>

### -param <i>AdditionalDetails</i> [in, optional]

<dd>
<p>A pointer to a string giving additional details that the event producer may want to provide to the consumer of this event.</p>
</dd>
</dl>

## -returns
<p><b>SeEtwWriteKMCveEvent</b> returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The driver was successfully published</p><dl>
<dt><b>ERROR_INVALID_PARAMETER</b></dt>
</dl><p>Invalid pointer to CVE-ID passed</p>

<p> </p>

## -remarks
<p>The <b> 	SeEtwWriteKMCveEvent</b> function publishes a CVE-based event. This function should be called only in scenarios where an attempt to exploit a known, patched vulnerability is detected by the application. Ideally, this function call should be added as part of the fix (update) itself. 
 The default consumer for this event is EventLog-System. To enable another consumer, the provider can be added to the consumer session.
</p>

<p>Provider GUID: 85a62a0d-7e17-485f-9d4f-749a287193a6</p>

<p>Source Name: Microsoft-Windows-Audit-CVE or CVE-Audit</p>

<p>The <b> 	SeEtwWriteKMCveEvent</b> function publishes a CVE-based event. This function should be called only in scenarios where an attempt to exploit a known, patched vulnerability is detected by the application. Ideally, this function call should be added as part of the fix (update) itself. 
 The default consumer for this event is EventLog-System. To enable another consumer, the provider can be added to the consumer session.
</p>

<p>Provider GUID: 85a62a0d-7e17-485f-9d4f-749a287193a6</p>

<p>Source Name: Microsoft-Windows-Audit-CVE or CVE-Audit</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 10 and later versions of Windows</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.exe</dt>
</dl>
</td>
</tr>
</table>