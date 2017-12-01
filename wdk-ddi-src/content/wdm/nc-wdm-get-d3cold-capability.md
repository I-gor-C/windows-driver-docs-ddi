---
UID: NC.wdm.GET_D3COLD_CAPABILITY
title: GET_D3COLD_CAPABILITY
author: windows-driver-content
description: The GetBusDriverD3ColdSupport routine enables the driver for a device to query whether the enumerating bus driver supports the D3cold device power state.
old-location: kernel\getbusdriverd3coldsupport.htm
old-project: kernel
ms.assetid: FE756171-327B-40E7-92A4-9159C509FD5E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetBusDriverD3ColdSupport
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# GET_D3COLD_CAPABILITY callback



## -description
<p>The <i>GetBusDriverD3ColdSupport</i> routine enables the driver for a device to query whether the enumerating bus driver supports the D3cold device power state.</p>


## -prototype

````
GET_D3COLD_CAPABILITY GetBusDriverD3ColdSupport;

NTSTATUS GetBusDriverD3ColdSupport(
  _In_opt_ PVOID    Context,
  _Out_    PBOOLEAN D3ColdSupported
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in, optional]

<dd>
<p>A pointer to interface-specific context information. The caller sets this parameter to the value of the <b>Context</b> member of the <a href="..\wdm\ns-wdm--d3cold-support-interface.md">D3COLD_SUPPORT_INTERFACE</a> structure for the interface.</p>
</dd>

### -param <i>D3ColdSupported</i> [out]

<dd>
<p>A pointer to a BOOLEAN variable to which the routine writes a value to indicate whether the bus driver supports the D3cold. If this value is <b>TRUE</b>, the bus driver supports D3cold. If <b>FALSE</b>, the bus driver does not support D3cold. If the call fails, the routine returns an error status code and does not write anything to this variable.</p>
</dd>
</dl>

## -returns
<p>The <i>GetBusDriverD3ColdSupport</i> routine returns STATUS_SUCCESS if it is successful. Otherwise, it returns an appropriate error status code.</p>

## -remarks
<p>The driver for the device calls the version of this routine that is implemented by the <a href="https://msdn.microsoft.com/38ca54e0-defe-48b2-ab00-a5f688c2eb01">Windows ACPI driver</a>, Acpi.sys. This routine checks the parent bus driver for the device to determine whether this bus driver supports the D3cold power state.</p>

<p>For example, starting with Windows 8, Microsoft supplies an inbox USB 3.0 eXtensible Host Controller Interface (xHCI) driver that supports D3cold. Some third-party hardware vendors supply Windows drivers for their xHCI controllers, but these drivers might not support D3cold. The driver for a USB 3.0 device can call the <i>GetBusDriverD3ColdSupport</i> routine to determine whether the parent xHCI controller driver supports D3cold.</p>

<p>A bus driver supports D3cold if all of the following are true:</p>

<p>The driver for a device can call the <a href="..\wdm\nc-wdm-get-idle-wake-info.md">GetIdleWakeInfo</a> routine to determine whether the underlying bus drivers and ACPI system firmware support D3cold for the device. If this call fails and returns an error status code, the device driver can call the <i>GetBusDriverD3ColdSupport</i> routine to determine whether the failure is caused by lack of D3cold support by the parent bus driver.</p>

<p>A device on a bus can make a transition to the D3cold substate only if the bus driver supports this transition. If the bus driver does not support D3cold, the device never enters D3cold, even if the function driver for the device calls the <a href="..\wdm\nc-wdm-set-d3cold-support.md">SetD3ColdSupport</a> routine to enable the transition to D3cold. In this case, <i>SetD3ColdSupport</i> calls have no effect, but are harmless.</p>

<p>For this reason, most device drivers never need to call the <i>GetBusDriverD3ColdSupport</i> routine.</p>

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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--d3cold-support-interface.md">D3COLD_SUPPORT_INTERFACE</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-get-idle-wake-info.md">GetIdleWakeInfo</a>
</dt>
<dt>
<a href="kernel.guid_d3cold_support_interface">GUID_D3COLD_SUPPORT_INTERFACE</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-set-d3cold-support.md">SetD3ColdSupport</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20GET_D3COLD_CAPABILITY routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
