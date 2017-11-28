---
UID: NF.ntifs.IoStartTimer
title: IoStartTimer
author: windows-driver-content
description: The IoStartTimer routine enables the timer associated with a given device object so the driver-supplied IoTimer routine is called once per second.
old-location: kernel\iostarttimer.htm
old-project: kernel
ms.assetid: 2e13d7da-7ef3-4c2e-b028-f7d37548c208
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoStartTimer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoStartTimer
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
---

# IoStartTimer function



## -description
<p>The <b>IoStartTimer</b> routine enables the timer associated with a given device object so the driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff550381">IoTimer</a> routine is called once per second.</p>


## -syntax

````
VOID IoStartTimer(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to a device object whose timer routine is to be called.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The driver must already have set up the IoTimer routine for the <i>DeviceObject</i> by calling <b>IoInitializeTimer</b>. </p>

<p>The driver must already have set up the IoTimer routine for the <i>DeviceObject</i> by calling <b>IoInitializeTimer</b>. </p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550381">IoTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549344">IoInitializeTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550377">IoStopTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552130">KeInitializeDpc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552168">KeInitializeTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553286">KeSetTimer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoStartTimer routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
