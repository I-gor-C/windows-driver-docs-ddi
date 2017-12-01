---
UID: NF.wudfddi.IPnpCallbackRemoteInterfaceNotification.OnRemoteInterfaceArrival
title: IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival
author: windows-driver-content
description: A driver's OnRemoteInterfaceArrival event callback function informs the driver when a device interface is available.
old-location: wdf\ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival.htm
old-project: wdf
ms.assetid: 19a0eec7-1a67-42ad-86d2-20566a2c1268
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPnpCallbackRemoteInterfaceNotification, OnRemoteInterfaceArrival, IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IPnpCallbackRemoteInterfaceNotification.OnRemoteInterfaceArrival
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IPnpCallbackRemoteInterfaceNotification
req.product: Windows 10 or later.
---

# IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A driver's <b>OnRemoteInterfaceArrival</b> event callback function informs the driver when a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> is available. </p>


## -syntax

````
void OnRemoteInterfaceArrival(
  [in] IWDFRemoteInterfaceInitialize *pWdfRemoteInterfaceInit
);
````


## -parameters
<dl>

### -param <i>pWdfRemoteInterfaceInit</i> [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfremoteinterfaceinitialize.md">IWDFRemoteInterfaceInitialize</a> interface that identifies the device interface that has arrived.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>A UMDF-based driver can register its optional <b>OnRemoteInterfaceArrival</b> event callback function by calling <a href="wdf.iwdfdevice2_registerremoteinterfacenotification">IWDFDevice2::RegisterRemoteInterfaceNotification</a>.</p>

<p>The driver can use methods of the <a href="..\wudfddi\nn-wudfddi-iwdfremoteinterfaceinitialize.md">IWDFRemoteInterfaceInitialize</a> interface to determine which device interface has arrived.</p>

<p>Before the driver can send I/O requests to the device interface, the driver must do the following:</p>

<p>Call <a href="wdf.iwdfdevice2_createremoteinterface">IWDFDevice2::CreateRemoteInterface</a> to create a remote interface object.</p>

<p>Call <a href="wdf.iwdfdevice2_createremotetarget">IWDFDevice2::CreateRemoteTarget</a> to create a remote target object.</p>

<p>Call <a href="wdf.iwdfremotetarget_openremoteinterface">IWDFRemoteTarget::OpenRemoteInterface</a> to connect the interface object to the remote target object and open the remote target for I/O operations.</p>

<p>For more information about using remote interface objects to access device interfaces, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF-based Drivers</a>
</p>

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
<p>1.9</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-ipnpcallbackremoteinterfacenotification.md">IPnpCallbackRemoteInterfaceNotification</a>
</dt>
<dt>
<a href="wdf.iwdfdevice2_createremoteinterface">IWDFDevice2::CreateRemoteInterface</a>
</dt>
<dt>
<a href="wdf.iwdfdevice2_createremotetarget">IWDFDevice2::CreateRemoteTarget</a>
</dt>
<dt>
<a href="wdf.iwdfremotetarget_openremoteinterface">IWDFRemoteTarget::OpenRemoteInterface</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfremoteinterfaceinitialize.md">IWDFRemoteInterfaceInitialize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
