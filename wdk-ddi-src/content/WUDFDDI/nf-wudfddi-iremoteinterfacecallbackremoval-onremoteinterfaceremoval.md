---
UID: NF.wudfddi.IRemoteInterfaceCallbackRemoval.OnRemoteInterfaceRemoval
title: IRemoteInterfaceCallbackRemoval::OnRemoteInterfaceRemoval
author: windows-driver-content
description: A UMDF-based driver's OnRemoteInterfaceRemoval event callback function notifies the driver that it cannot use a device interface because the interface has been removed.
old-location: wdf\iremoteinterfacecallbackremoval_onremoteinterfaceremoval.htm
ms.assetid: 0dfa2eb8-a7f6-46d9-9599-5e2aaf583f78
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IRemoteInterfaceCallbackRemoval.OnRemoteInterfaceRemoval
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
ms.keywords: IRemoteInterfaceCallbackRemoval, OnRemoteInterfaceRemoval, IRemoteInterfaceCallbackRemoval::OnRemoteInterfaceRemoval
req.iface: IRemoteInterfaceCallbackRemoval
req.product: Windows 10 or later.
---

# IRemoteInterfaceCallbackRemoval::OnRemoteInterfaceRemoval method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A UMDF-based driver's <b>OnRemoteInterfaceRemoval</b> event callback function notifies the driver that it cannot use a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> because the interface has been removed.</p>


## -syntax

````
void OnRemoteInterfaceRemoval(
  [in] IWDFRemoteInterface *pWdfRemoteInterface
);
````


## -parameters
<dl>

### -param <i>pWdfRemoteInterface</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/10d4cd20-c797-455c-b16d-00982be5c1b7">IWDFRemoteInterface</a> interface of a remote interface object that represents a device interface. The driver obtains this pointer when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff556925">IWDFDevice2::CreateRemoteInterface</a>.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>A driver's <b>OnRemoteInterfaceRemoval</b> event callback function must do whatever driver-specific tasks are necessary to handle removal of the device interface. In addition, the callback must delete the remote interface object that <a href="https://msdn.microsoft.com/library/windows/hardware/ff556925">IWDFDevice2::CreateRemoteInterface</a> created and call the interface's <b>Release</b> function if it has previously called the interface's <b>AddRef</b> function.</p>

<p>If the driver does not provide this callback function, the framework deletes the remote interface object that <a href="https://msdn.microsoft.com/library/windows/hardware/ff556925">IWDFDevice2::CreateRemoteInterface</a> created. </p>

<p>For more information about a driver's <b>OnRemoteInterfaceRemoval</b> event callback function, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF-based Drivers</a>.</p>

<p>A driver's <b>OnRemoteInterfaceRemoval</b> event callback function must do whatever driver-specific tasks are necessary to handle removal of the device interface. In addition, the callback must delete the remote interface object that <a href="https://msdn.microsoft.com/library/windows/hardware/ff556925">IWDFDevice2::CreateRemoteInterface</a> created and call the interface's <b>Release</b> function if it has previously called the interface's <b>AddRef</b> function.</p>

<p>If the driver does not provide this callback function, the framework deletes the remote interface object that <a href="https://msdn.microsoft.com/library/windows/hardware/ff556925">IWDFDevice2::CreateRemoteInterface</a> created. </p>

<p>For more information about a driver's <b>OnRemoteInterfaceRemoval</b> event callback function, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF-based Drivers</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556891">IRemoteInterfaceCallbackRemoval</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556775">IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556889">IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IRemoteInterfaceCallbackRemoval::OnRemoteInterfaceRemoval method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
