---
UID: NF.wudfddi.IWDFDevice2.RegisterRemoteInterfaceNotification
title: IWDFDevice2::RegisterRemoteInterfaceNotification method
author: windows-driver-content
description: The RegisterRemoteInterfaceNotification method registers a driver to receive a notification when a specified device interface becomes available.
old-location: wdf\iwdfdevice2_registerremoteinterfacenotification.htm
old-project: wdf
ms.assetid: 48e1fc20-03e7-42ef-b57c-9246a56df4ef
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFDevice2, IWDFDevice2::RegisterRemoteInterfaceNotification, RegisterRemoteInterfaceNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFDevice2.RegisterRemoteInterfaceNotification
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
req.product: Windows 10 or later.
---

# IWDFDevice2::RegisterRemoteInterfaceNotification method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>RegisterRemoteInterfaceNotification</b> method registers a driver to receive a notification when a specified <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> becomes available.



## -syntax

````
HRESULT RegisterRemoteInterfaceNotification(
  [in] LPCGUID pDeviceInterfaceGuid,
  [in] BOOL    IncludeExistingInterfaces
);
````


## -parameters

### -param pDeviceInterfaceGuid [in]

A pointer to a GUID that identifies a device interface.


### -param IncludeExistingInterfaces [in]

A Boolean value. If the driver sets this value to <b>TRUE</b>, the framework notifies the driver if the specified device interface becomes available after the driver calls <b>RegisterRemoteInterfaceNotification</b>, and it also notifies the driver if the device interface was available before the driver called <b>RegisterRemoteInterfaceNotification</b>. 

If the driver sets this value to <b>FALSE</b>, the framework notifies the driver only if the device interface becomes available after the driver calls <b>RegisterRemoteInterfaceNotification</b>.


## -returns
<b>RegisterRemoteInterfaceNotification</b> returns S_OK of the operation succeeds. Otherwise, this method returns another value that Winerror.h contains.


## -remarks
Your driver can call <b>RegisterRemoteInterfaceNotification</b> only if the callback interface that the driver previously passed to <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> supports the <a href="..\wudfddi\nn-wudfddi-ipnpcallbackremoteinterfacenotification.md">IPnpCallbackRemoteInterfaceNotification</a> interface.

For more information, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF-based Drivers</a>.

The following code example shows how an <a href="wdf.idriverentry_ondeviceadd">IDriverEntry::OnDeviceAdd</a> callback function can register for notification of the arrival of a device interface.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.9

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

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
<a href="..\wudfddi\nn-wudfddi-iwdfdevice2.md">IWDFDevice2</a>
</dt>
<dt>
<a href="wdf.ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival">IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice2::RegisterRemoteInterfaceNotification method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

