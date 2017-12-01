---
UID: NF.wdm.EtwProviderEnabled
title: EtwProviderEnabled
author: windows-driver-content
description: The EtwProviderEnabled function verifies that a provider is enabled for event logging at a specified level and keyword.
old-location: devtest\etwproviderenabled.htm
old-project: devtest
ms.assetid: 28b0a40e-e8e8-4953-8a3a-f3f1b58ad80f
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: EtwProviderEnabled
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EtwProviderEnabled
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# EtwProviderEnabled function



## -description
<p>The <b>EtwProviderEnabled</b> function verifies that a provider is enabled for event logging at a specified level and keyword. </p>


## -syntax

````
BOOLEAN EtwProviderEnabled(
  _In_ REGHANDLE RegHandle,
  _In_ UCHAR     Level,
  _In_ ULONGLONG Keyword
);
````


## -parameters
<dl>

### -param <i>RegHandle</i> [in]

<dd>
<p>A pointer to the event provider registration handle, which is returned by the <b>EtwRegister</b> function if the event provider registration is successful.</p>
</dd>

### -param <i>Level</i> [in]

<dd>
<p>The level at which the provider is enabled.</p>
</dd>

### -param <i>Keyword</i> [in]

<dd>
<p>The keyword that indicates whether the provider is enabled.</p>
</dd>
</dl>

## -returns
<p>The function returns <b>TRUE</b> if the provider is enabled and <b>FALSE</b> if the provider is not enabled. </p>

## -remarks
<p>You can use the <b>EtwProviderEnabled</b> function to verify that the registered provider is enabled for any event by passing in zeros for the <i>Level</i> and <i>Keyword</i> values when you call the function. If any event is enabled, the provider is enabled. </p>

<p>If an event descriptor is already available, use the <a href="..\wdm\nf-wdm-etweventenabled.md">EtwEventEnabled</a> function.</p>

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
<p>Available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-etweventenabled.md">EtwEventEnabled</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [devtest\devtest]:%20EtwProviderEnabled function%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
