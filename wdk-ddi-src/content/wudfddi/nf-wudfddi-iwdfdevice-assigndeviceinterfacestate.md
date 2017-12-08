---
UID: NF.wudfddi.IWDFDevice.AssignDeviceInterfaceState
title: IWDFDevice::AssignDeviceInterfaceState
author: windows-driver-content
description: The AssignDeviceInterfaceState method enables or disables the specified device interface instance for a device.
old-location: wdf\iwdfdevice_assigndeviceinterfacestate.htm
old-project: wdf
ms.assetid: 466af310-f2a7-4bd7-b927-df644e2e9c24
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFDevice, AssignDeviceInterfaceState, IWDFDevice::AssignDeviceInterfaceState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDevice.AssignDeviceInterfaceState
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
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFDevice
req.product: Windows 10 or later.
---

# IWDFDevice::AssignDeviceInterfaceState method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>AssignDeviceInterfaceState</b> method enables or disables the specified device interface instance for a device.</p>


## -syntax

````
HRESULT AssignDeviceInterfaceState(
  [in]           LPCGUID pDeviceInterfaceGuid,
  [in, optional] PCWSTR  pReferenceString,
  [in]           BOOL    Enable
);
````


## -parameters
<dl>

### -param pDeviceInterfaceGuid [in]

<dd>
<p>A pointer to the GUID for a device interface class.</p>
</dd>

### -param pReferenceString [in, optional]

<dd>
<p>A pointer to a <b>NULL</b>-terminated string that contains the name of the instance of the device interface. This parameter is optional. The driver can pass <b>NULL</b> if the driver does not have to supply a name. If the driver must supply a name, the string that the driver passes must not contain any path separator characters ("/" or "\"). </p>
</dd>

### -param Enable [in]

<dd>
<p>A BOOL value that specifies whether the device interface instance should be enabled or disabled. <b>TRUE</b> indicates to enable; <b>FALSE</b> indicates to disable.</p>
</dd>
</dl>

## -returns
<p><b>AssignDeviceInterfaceState</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>If <a href="wdf.iwdfdevice_createdeviceinterface">IWDFDevice::CreateDeviceInterface</a> succeeds, the framework automatically enables and disables the interface based on the device's PnP state.

Use the <b>AssignDeviceInterfaceState</b> method to disable and re-enable a device interface manually.</p>

<p>

For more information about device interfaces, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF Drivers</a>.</p>

<p>For a code example of how to use the <b>AssignDeviceInterfaceState</b> method, see <a href="wdf.iwdfdevice_createdeviceinterface">IWDFDevice::CreateDeviceInterface</a>.</p>

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
<dt>Wudfddi.h (include Wudfddi.h)</dt>
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
<a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a>
</dt>
<dt>
<a href="wdf.iwdfdevice_createdeviceinterface">IWDFDevice::CreateDeviceInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice::AssignDeviceInterfaceState method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
