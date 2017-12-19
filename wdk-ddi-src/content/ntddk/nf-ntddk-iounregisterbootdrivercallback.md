---
UID: NF.ntddk.IoUnregisterBootDriverCallback
title: IoUnregisterBootDriverCallback function
author: windows-driver-content
description: The IoUnRegisterBootDriverCallback routine unregisters a previously registered BOOT_DRIVER_CALLBACK_FUNCTION routine.
old-location: kernel\iounregisterbootdrivercallback.htm
old-project: kernel
ms.assetid: 6199672C-A4A4-4ED8-B91E-95D96A472449
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IoUnregisterBootDriverCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoUnRegisterBootDriverCallback
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
---

# IoUnregisterBootDriverCallback function



## -description
The <b>IoUnRegisterBootDriverCallback</b> routine unregisters a previously registered <b>BOOT_DRIVER_CALLBACK_FUNCTION</b> routine.



## -syntax

````
void IoUnRegisterBootDriverCallback(
  _In_ PVOID CallbackHandle
);
````


## -parameters

### -param CallbackHandle [in]

A handle returned from a previous call to <a href="kernel.ioregisterbootdrivercallback">IoRegisterBootDriverCallback</a>.


## -returns
None


## -remarks
A driver that calls <a href="kernel.ioregisterbootdrivercallback">IoRegisterBootDriverCallback</a> must call <b>IoUnRegisterBootDriverCallback</b> before being unloaded.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with  Windows 8.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioregisterbootdrivercallback">IoRegisterBootDriverCallback</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoUnRegisterBootDriverCallback routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

