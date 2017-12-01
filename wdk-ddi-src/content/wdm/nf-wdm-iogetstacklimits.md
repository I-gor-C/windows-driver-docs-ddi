---
UID: NF.wdm.IoGetStackLimits
title: IoGetStackLimits
author: windows-driver-content
description: The IoGetStackLimits routine returns the boundaries of the current thread's stack frame.
old-location: kernel\iogetstacklimits.htm
old-project: kernel
ms.assetid: aaa10cb2-16cb-40a8-ad72-9715da311957
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoGetStackLimits
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
req.alt-api: IoGetStackLimits
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
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# IoGetStackLimits function



## -description
<p>The <b>IoGetStackLimits</b> routine returns the boundaries of the current thread's stack frame.</p>


## -syntax

````
VOID IoGetStackLimits(
  _Out_ PULONG_PTR LowLimit,
  _Out_ PULONG_PTR HighLimit
);
````


## -parameters
<dl>

### -param <i>LowLimit</i> [out]

<dd>
<p>Pointer to a caller-supplied variable in which this routine returns the lower offset of the current thread's stack frame.</p>
</dd>

### -param <i>HighLimit</i> [out]

<dd>
<p>Pointer to a caller-supplied variable in which this routine returns the higher offset of the current thread's stack frame.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Highest-level drivers can call this routine, particularly file systems that have been passed a pointer to a location on the current thread's stack.</p>

<p>In Windows Server 2003 Service Pack 1 (SP1) and later versions of Windows, callers of <b>IoGetStackLimits</b> can be running at any IRQL. For earlier operating systems, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

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
<p>See Remarks section.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-iogetinitialstack.md">IoGetInitialStack</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iogetremainingstacksize.md">IoGetRemainingStackSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoGetStackLimits routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
