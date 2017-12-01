---
UID: NF.wdm.IoGetDriverObjectExtension
title: IoGetDriverObjectExtension
author: windows-driver-content
description: The IoGetDriverObjectExtension routine retrieves a previously allocated per-driver context area.
old-location: kernel\iogetdriverobjectextension.htm
old-project: kernel
ms.assetid: ce983953-53fc-4a32-8072-8a9f74d11ae3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoGetDriverObjectExtension
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoGetDriverObjectExtension
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoGetDriverObjectExtension function



## -description
<p>The <b>IoGetDriverObjectExtension</b> routine retrieves a previously allocated per-driver context area.</p>


## -syntax

````
PVOID IoGetDriverObjectExtension(
  _In_ PDRIVER_OBJECT DriverObject,
  _In_ PVOID          ClientIdentificationAddress
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>Specifies the driver object with which the context area is associated.</p>
</dd>

### -param <i>ClientIdentificationAddress</i> [in]

<dd>
<p>Specifies the unique identifier, provided when it was allocated, of the context area to be retrieved.</p>
</dd>
</dl>

## -returns
<p><b>IoGetDriverObjectExtension</b> returns a pointer to the context area, if any or returns <b>NULL</b>.</p>

## -remarks
<p>Drivers call <b>IoGetDriverObjectExtension</b> to retrieve a pointer to a previously allocated extension area. </p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-ioallocatedriverobjectextension.md">IoAllocateDriverObjectExtension</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoGetDriverObjectExtension routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
