---
UID: NF.wdm.IoGetFunctionCodeFromCtlCode
title: IoGetFunctionCodeFromCtlCode
author: windows-driver-content
description: The IoGetFunctionCodeFromCtlCode macro returns the value of the function code contained in an I/O control code.
old-location: kernel\iogetfunctioncodefromctlcode.htm
ms.assetid: 8bbde78d-49f4-4181-9d92-312010322a7a
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoGetFunctionCodeFromCtlCode
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
ms.keywords: IoGetFunctionCodeFromCtlCode
req.iface: 
req.product: Windows 10 or later.
---

# IoGetFunctionCodeFromCtlCode function



## -description
<p>The <b>IoGetFunctionCodeFromCtlCode</b> macro returns the value of the function code contained in an I/O control code.</p>


## -syntax

````
ULONG IoGetFunctionCodeFromCtlCode(
  _In_ ULONG ControlCode
);
````


## -parameters
<dl>

### -param <i>ControlCode</i> [in]

<dd>
<p>The IOCTL_<i>XXX</i> (or FSCTL_<i>XXX</i>) value, which can be obtained from the driver's I/O stack location of the IRP at <b>Parameters.DeviceIoControl.IoControlCode</b>.</p>
</dd>
</dl>

## -returns
<p><b>IoGetFunctionCodeFromCtlCode</b> returns the value of the <b>Function</b> part of the given IOCTL_<i>XXX</i> code.</p>

## -remarks
<p>For information about the layout of IOCTL codes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565406">Using I/O Control Codes</a>.</p>

<p>For information about the layout of IOCTL codes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565406">Using I/O Control Codes</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548318">IoBuildDeviceIoControlRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoGetFunctionCodeFromCtlCode function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
