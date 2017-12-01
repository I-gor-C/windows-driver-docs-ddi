---
UID: NF.wudfusb.IWDFUsbTargetDevice.SetPowerPolicy
title: IWDFUsbTargetDevice::SetPowerPolicy
author: windows-driver-content
description: The SetPowerPolicy method sets the WinUsb power policy.
old-location: wdf\iwdfusbtargetdevice_setpowerpolicy.htm
old-project: wdf
ms.assetid: e1b31df0-d383-43a3-bf9f-8874689cbf58
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFUsbTargetDevice, SetPowerPolicy, IWDFUsbTargetDevice::SetPowerPolicy
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfusb.h
req.include-header: Wudfusb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbTargetDevice.SetPowerPolicy
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: 
req.iface: IWDFUsbTargetDevice
req.product: Windows 10 or later.
---

# IWDFUsbTargetDevice::SetPowerPolicy method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>SetPowerPolicy</b> method sets the WinUsb power policy.</p>


## -syntax

````
HRESULT SetPowerPolicy(
  [in] ULONG PolicyType,
  [in] ULONG ValueLength,
  [in] PVOID Value
);
````


## -parameters
<dl>

### -param <i>PolicyType</i> [in]

<dd>
<p>The type of WinUsb power policy that the UMDF driver sets.</p>
</dd>

### -param <i>ValueLength</i> [in]

<dd>
<p>The size, in bytes, of the buffer that <b>SetPowerPolicy</b> supplies in <i>Value</i>.</p>
</dd>

### -param <i>Value</i> [in]

<dd>
<p>A pointer to the buffer that contains the WinUsb power policy.</p>
</dd>
</dl>

## -returns
<p><b>SetPowerPolicy</b> returns one of the following values: </p><dl>
<dt><b>S_OK </b></dt>
</dl><p>
<a href="wdf.iwdfusbtargetdevice_setpowerpolicy">SetPowerPolicy</a> successfully set the WinUsb power policy. </p><dl>
<dt><b>E_OUTOFMEMORY </b></dt>
</dl><p>
<a href="wdf.iwdfusbtargetdevice_setpowerpolicy">SetPowerPolicy</a> encountered an allocation failure.</p><dl>
<dt><b>An error code that is defined in Winerror.h</b></dt>
</dl><p>This value corresponds to the error code that the WinUsb API returned.</p>

<p> </p>

## -remarks
<p>Power policy controls the power management that WinUsb for the device performs.</p>

<p>For information about valid policy types and values that a UMDF driver can pass for the <i>PolicyType</i> and <i>Value</i> parameters, see the <a href="buses.winusb_setpowerpolicy">WinUsb_SetPowerPolicy</a> function.</p>

<p>For more information about the power behavior of WinUSB, see <a href="buses.winusb_power_management">WinUSB Power Management</a>.</p>

<p>The <b>SetPowerPolicy</b> method generates a UMDF request and synchronously sends the request to the I/O target.</p>

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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfusb.h (include Wudfusb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfusb\nn-wudfusb-iwdfusbtargetdevice.md">IWDFUsbTargetDevice</a>
</dt>
<dt>
<a href="buses.winusb_setpowerpolicy">WinUsb_SetPowerPolicy</a>
</dt>
<dt>
<a href="wdf.iwdfusbtargetdevice_retrievepowerpolicy">IWDFUsbTargetDevice::RetrievePowerPolicy</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUsbTargetDevice::SetPowerPolicy method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
