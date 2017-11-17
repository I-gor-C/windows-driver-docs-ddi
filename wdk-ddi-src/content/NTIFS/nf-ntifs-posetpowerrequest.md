---
UID: NF.ntifs.PoSetPowerRequest
title: PoSetPowerRequest
author: windows-driver-content
description: The PoSetPowerRequest routine increments the count for the specified power request type.
old-location: kernel\posetpowerrequest.htm
ms.assetid: 5670a4dd-3804-4532-8765-2fdffe1c4a0b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoSetPowerRequest
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
ms.keywords: PoSetPowerRequest
req.iface: 
---

# PoSetPowerRequest function



## -description
<p>The <b>PoSetPowerRequest</b> routine increments the count for the specified power request type.</p>


## -syntax

````
NTSTATUS PoSetPowerRequest(
  _Inout_ PVOID              PowerRequest,
  _In_    POWER_REQUEST_TYPE Type
);
````


## -parameters
<dl>

### -param <i>PowerRequest</i> [in, out]

<dd>
<p>A pointer to a power request object that was created by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559663">PoCreatePowerRequest</a> routine.</p>
</dd>

### -param <i>Type</i> [in]

<dd>
<p>The type of power request. Set this parameter to the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff559840">POWER_REQUEST_TYPE</a> enumeration value:</p>
<ul>
<li>
<p><b>PowerRequestSystemRequired</b></p>
</li>
</ul>
</dd>
</dl>

## -returns
<p><b>PoSetPowerRequest</b> returns STATUS_SUCCESS if the call is successful. If the call fails, possible error return codes include the following:</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The <i>Type</i> parameter is set to an unsupported value.</p>

<p> </p>

## -remarks
<p>A driver can call the <b>PoSetPowerRequest</b> routine to request that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559829">power manager</a> override several types of default power behavior, which are specified as <a href="https://msdn.microsoft.com/library/windows/hardware/ff559840">POWER_REQUEST_TYPE</a> enumeration values. To restore the default behavior, the driver cancels the request by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559658">PoClearPowerRequest</a> routine.</p>

<p>The power manager maintains a count of the active requests for each power request type. The <b>PoSetPowerRequest</b> routine increments the count for the specified power request type by one. The <b>PoClearPowerRequest</b> routine decrements the count by one. A nonzero count indicates that requests from one or more components are active. After the count decrements to zero, the computer reverts to the default behavior for the specified power request type.</p>

<p>A driver can call the <b>PoSetPowerRequest</b> routine to request that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559829">power manager</a> override several types of default power behavior, which are specified as <a href="https://msdn.microsoft.com/library/windows/hardware/ff559840">POWER_REQUEST_TYPE</a> enumeration values. To restore the default behavior, the driver cancels the request by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559658">PoClearPowerRequest</a> routine.</p>

<p>The power manager maintains a count of the active requests for each power request type. The <b>PoSetPowerRequest</b> routine increments the count for the specified power request type by one. The <b>PoClearPowerRequest</b> routine decrements the count by one. A nonzero count indicates that requests from one or more components are active. After the count decrements to zero, the computer reverts to the default behavior for the specified power request type.</p>

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
<p>Available starting with Windows 7.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559658">PoClearPowerRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559663">PoCreatePowerRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559840">POWER_REQUEST_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoSetPowerRequest routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
