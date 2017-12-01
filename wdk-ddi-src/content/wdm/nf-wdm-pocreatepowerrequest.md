---
UID: NF.wdm.PoCreatePowerRequest
title: PoCreatePowerRequest
author: windows-driver-content
description: The PoCreatePowerRequest routine creates a power request object.
old-location: kernel\pocreatepowerrequest.htm
old-project: kernel
ms.assetid: 67986bf8-b070-44e9-95a2-eea35100b0e7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PoCreatePowerRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoCreatePowerRequest
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
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PoCreatePowerRequest function



## -description
<p>The <b>PoCreatePowerRequest</b> routine creates a power request object.</p>


## -syntax

````
NTSTATUS PoCreatePowerRequest(
  _Out_ PVOID                   *PowerRequest,
  _In_  PDEVICE_OBJECT          DeviceObject,
  _In_  PCOUNTED_REASON_CONTEXT Context
);
````


## -parameters
<dl>

### -param <i>PowerRequest</i> [out]

<dd>
<p>A pointer to a location into which the routine writes a pointer to the newly created power request object. If the call fails, the routine writes <b>NULL</b> to this location.</p>
</dd>

### -param <i>DeviceObject</i> [in]

<dd>
<p>A pointer to the device object of the caller (a <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure).</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to a <a href="..\wdm\ns-wdm--counted-reason-context.md">COUNTED_REASON_CONTEXT</a> structure that describes why the caller is creating the power request object. This parameter is optional and can be set to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>PoCreatePowerRequest</b> returns STATUS_SUCCESS if the call is successful. If the call fails, possible error return codes include the following:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>DeviceObject</i> parameter is <b>NULL</b>.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There is not enough memory available to create a power request object.</p>

<p> </p>

## -remarks
<p>This routine creates a power request object. To enable power requests, the caller should create one power request object and use that object for all calls to the <a href="..\ntifs\nf-ntifs-posetpowerrequest.md">PoSetPowerRequest</a> and <a href="..\ntifs\nf-ntifs-poclearpowerrequest.md">PoClearPowerRequest</a> routines.</p>

<p>A driver can use power requests to override certain aspects of the computer's default power behavior. For example, a driver for a TV receiver device can use power requests to prevent the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559829">power manager</a> from automatically blanking the display during extended periods of time in which no user interaction occurs.</p>

<p>When the power request object is no longer needed, the caller must delete the object by calling the <a href="..\ntifs\nf-ntifs-podeletepowerrequest.md">PoDeletePowerRequest</a> routine. The driver must delete the power request object before it deletes the device object that was used to create the power request object.</p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-poclearpowerrequest.md">PoClearPowerRequest</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-podeletepowerrequest.md">PoDeletePowerRequest</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-posetpowerrequest.md">PoSetPowerRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoCreatePowerRequest routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
