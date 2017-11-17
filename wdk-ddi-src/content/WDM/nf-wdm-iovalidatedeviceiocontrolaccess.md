---
UID: NF.wdm.IoValidateDeviceIoControlAccess
title: IoValidateDeviceIoControlAccess
author: windows-driver-content
description: For more information, see the WdmlibIoValidateDeviceIoControlAccess function.
old-location: kernel\iovalidatedeviceiocontrolaccess.htm
ms.assetid: 45e8279f-b7a5-4b45-92b7-5f740f6c1117
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Server 2003 and later versions of Windows. Drivers that must also work for Windows 2000 and Windows XP can instead link to Wdmsec.lib to use this routine. (The Wdmsec.lib library first shipped with the Windows XP Service Pack 1 [SP1] and Windows Server 2003 editions of the Driver Development Kit [DDK] and now ships with the Windows Driver Kit [WDK].)
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoValidateDeviceIoControlAccess
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
ms.keywords: IoValidateDeviceIoControlAccess
req.iface: 
req.product: Windows 10 or later.
---

# IoValidateDeviceIoControlAccess function



## -description
<p>For more information, see  the <a href="https://msdn.microsoft.com/F986A431-A70D-4488-A792-F37128902C7E">WdmlibIoValidateDeviceIoControlAccess</a> function.</p>


## -syntax

````
NTSTATUS IoValidateDeviceIoControlAccess(
  _In_ PIRP  Irp,
  _In_ ULONG RequiredAccess
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>For more information, see  the <a href="https://msdn.microsoft.com/F986A431-A70D-4488-A792-F37128902C7E">WdmlibIoValidateDeviceIoControlAccess</a> function.</p>
</dd>

### -param <i>RequiredAccess</i> [in]

<dd>
<p>For more information, see  the <a href="https://msdn.microsoft.com/F986A431-A70D-4488-A792-F37128902C7E">WdmlibIoValidateDeviceIoControlAccess</a> function.</p>
</dd>
</dl>

## -returns
<p>For more information, see  the <a href="https://msdn.microsoft.com/F986A431-A70D-4488-A792-F37128902C7E">WdmlibIoValidateDeviceIoControlAccess</a> function.</p>

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
<p>Available in Windows Server 2003 and later versions of Windows. Drivers that must also work for Windows 2000 and Windows XP can instead link to Wdmsec.lib to use this routine. (The Wdmsec.lib library first shipped with the Windows XP Service Pack 1 [SP1] and Windows Server 2003 editions of the Driver Development Kit [DDK] and now ships with the Windows Driver Kit [WDK].)</p>
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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoValidateDeviceIoControlAccess routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
