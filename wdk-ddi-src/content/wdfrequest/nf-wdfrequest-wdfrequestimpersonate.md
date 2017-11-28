---
UID: NF.wdfrequest.WdfRequestImpersonate
title: WdfRequestImpersonate
author: windows-driver-content
description: The WdfRequestImpersonate method registers a driver-supplied event callback function that the framework should call for impersonation.
old-location: wdf\wdfrequestimpersonate.htm
old-project: wdf
ms.assetid: E5267F04-D693-453B-BAD2-C61F89B07F6E
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfRequestImpersonate
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
req.alt-api: WdfRequestImpersonate
req.alt-loc: WUDFx02000.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WUDFx02000.lib
req.dll: WUDFx02000.dll; 
TBD
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestImpersonate function



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>WdfRequestImpersonate</b> method registers a driver-supplied event callback function  that the framework should call for impersonation.</p>


## -syntax

````
NTSTATUS WdfRequestImpersonate(
  _In_     WDFREQUEST                   Request,
  _In_     SECURITY_IMPERSONATION_LEVEL ImpersonationLevel,
  _In_     PFN_WDF_REQUEST_IMPERSONATE  EvtRequestImpersonate,
  _In_opt_ PVOID                        Context
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to the framework request object that represents the I/O request that is being completed.</p>
</dd>

### -param <i>ImpersonationLevel</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff556631">SECURITY_IMPERSONATION_LEVEL</a>-typed value that identifies the level of impersonation.</p>
</dd>

### -param <i>EvtRequestImpersonate</i> [in]

<dd>
<p>A pointer to the driver's <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-impersonate.md">EvtRequestImpersonate</a> event callback function.</p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>A pointer to a buffer that contains context information that is related to the impersonation call. The framework passes this context information in a call to the <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-impersonate.md">EvtRequestImpersonate</a> event callback function. This parameter is optional and can be <b>NULL</b></p>
</dd>
</dl>

## -returns
<p>If the <b>WdfRequestImpersonate</b> method encounters no errors, it returns STATUS_SUCCESS.</p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>The <b>WdfRequestImpersonate</b> method does not return until the <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-impersonate.md">EvtRequestImpersonate</a> event callback function completes.</p>

<p>For more information, see <a href="wdf.handling_client_impersonation_in_umdf_drivers">Handling Client Impersonation in UMDF Drivers</a>.</p>

<p>The <b>WdfRequestImpersonate</b> method does not return until the <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-impersonate.md">EvtRequestImpersonate</a> event callback function completes.</p>

<p>For more information, see <a href="wdf.handling_client_impersonation_in_umdf_drivers">Handling Client Impersonation in UMDF Drivers</a>.</p>

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
<a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-impersonate.md">EvtRequestImpersonate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559136">IWDFIoRequest::Impersonate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestImpersonate method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
