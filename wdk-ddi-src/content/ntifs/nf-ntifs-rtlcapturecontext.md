---
UID: NF.ntifs.RtlCaptureContext
title: RtlCaptureContext
author: windows-driver-content
description: The RtlCaptureContext function retrieves a context record in the context of the caller.
old-location: ifsk\rtlcapturecontext.htm
old-project: ifsk
ms.assetid: c3edd10c-ea4f-4e2d-96f2-3d1cb3804512
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlCaptureContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later versions of all Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlCaptureContext
req.alt-loc: NtDll.dll,NtosKrnl.exe,API-MS-Win-Core-RTLSupport-l1-1-0.dll,API-MS-Win-Core-RTLSupport-l1-2-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib; OneCoreUAP.lib on Windows 10
req.dll: NtDll.dll (user mode); NtosKrnl.exe (kernel mode)
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# RtlCaptureContext function



## -description
<p>The <b>RtlCaptureContext </b>function retrieves a context record in the context of the caller.</p>


## -syntax

````
VOID RtlCaptureContext(
  _Out_ PCONTEXT ContextRecord
);
````


## -parameters
<dl>

### -param <i>ContextRecord</i> [out]

<dd>
<p>A pointer to a <a href="http://go.microsoft.com/fwlink/p/?linkid=132119">CONTEXT</a> structure.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>The <i>ContextRecord</i> that is captured contains processor-specific register data.  </p>

<p>For kernel-mode code, the CONTEXT structure is defined in <i>Ntddk.h</i>. For more information, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=132119">CONTEXT</a> Structure topic in the SDK documentation.</p>

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
<p>Available in Microsoft Windows XP and later versions of all Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Fltkernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib; </dt>
<dt>OneCoreUAP.lib on Windows 10</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtDll.dll (user mode); </dt>
<dt>NtosKrnl.exe (kernel mode)</dt>
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
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=132119">CONTEXT</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlCaptureContext function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
