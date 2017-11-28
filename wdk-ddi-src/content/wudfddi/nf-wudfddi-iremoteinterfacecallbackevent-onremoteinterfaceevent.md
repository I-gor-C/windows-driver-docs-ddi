---
UID: NF.wudfddi.IRemoteInterfaceCallbackEvent.OnRemoteInterfaceEvent
title: IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent
author: windows-driver-content
description: A UMDF-based driver's OnRemoteInterfaceEvent event callback function handles device events that are associated with a device interface.
old-location: wdf\iremoteinterfacecallbackevent_onremoteinterfaceevent.htm
old-project: wdf
ms.assetid: 6cee6662-2eef-4caf-ab70-780748521ba9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IRemoteInterfaceCallbackEvent, OnRemoteInterfaceEvent, IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent
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
req.alt-api: IRemoteInterfaceCallbackEvent.OnRemoteInterfaceEvent
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
req.iface: IRemoteInterfaceCallbackEvent
req.product: Windows 10 or later.
---

# IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A UMDF-based driver's <b>OnRemoteInterfaceEvent</b> event callback function handles device events that are associated with a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.</p>


## -syntax

````
void OnRemoteInterfaceEvent(
  [in]           IWDFRemoteInterface *pWdfRemoteInterface,
  [in]           REFGUID             EventGuid,
  [in, optional] BYTE                *pbData,
  [in]           DWORD               cbDataSize,
  [in]           DWORD               NameBufferOffset
);
````


## -parameters
<dl>

### -param <i>pWdfRemoteInterface</i> [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfremoteinterface.md">IWDFRemoteInterface</a> interface of a remote interface object that represents a device interface. The driver obtains this pointer when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff556925">IWDFDevice2::CreateRemoteInterface</a>.</p>
</dd>

### -param <i>EventGuid</i> [in]

<dd>
<p>A GUID that identifies the event type. Event GUIDs are defined by the components that support such GUIDs. Some <a href="NULL">device interface classes</a> provide event GUIDs, and some driver provide custom events.</p>
</dd>

### -param <i>pbData</i> [in, optional]

<dd>
<p>A pointer to a buffer that contains event-specific data. Typically, components that define event GUIDs also define event-specific structures for event buffers.</p>
</dd>

### -param <i>cbDataSize</i> [in]

<dd>
<p>The size, in bytes, of the buffer that <i>pbData</i> points to.</p>
</dd>

### -param <i>NameBufferOffset</i> [in]

<dd>
<p>An offset, in bytes, from the beginning of the buffer that <i>pbData</i> points to. Bytes from 0 to <i>NameBufferOffset</i>-1 of the buffer contain binary data. Bytes from <i>NameBufferOffset</i> to the end of the buffer contain Unicode string data. </p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>A driver's <b>OnRemoteInterfaceEvent</b> event callback function handles all device events except arrival and removal events. Such events can originate from a UMDF-based driver's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558835">IWDFDevice::PostEvent</a> or from a kernel-mode driver's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549625">IoReportTargetDeviceChange</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549634">IoReportTargetDeviceChangeAsynchronous</a>.</p>

<p>The framework begins calling the <b>OnRemoteInterfaceEvent</b> event callback function after the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff560276">IWDFRemoteTarget::OpenRemoteInterface</a> and continues to call the callback function until the device interface's <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> is closed.</p>

<p>For more information about a driver's <b>OnRemoteInterfaceEvent</b> event callback function, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF-based Drivers</a>.</p>

<p>A driver's <b>OnRemoteInterfaceEvent</b> event callback function handles all device events except arrival and removal events. Such events can originate from a UMDF-based driver's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558835">IWDFDevice::PostEvent</a> or from a kernel-mode driver's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549625">IoReportTargetDeviceChange</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549634">IoReportTargetDeviceChangeAsynchronous</a>.</p>

<p>The framework begins calling the <b>OnRemoteInterfaceEvent</b> event callback function after the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff560276">IWDFRemoteTarget::OpenRemoteInterface</a> and continues to call the callback function until the device interface's <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> is closed.</p>

<p>For more information about a driver's <b>OnRemoteInterfaceEvent</b> event callback function, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF-based Drivers</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556887">IRemoteInterfaceCallbackEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556775">IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556893">IRemoteInterfaceCallbackRemoval::OnRemoteInterfaceRemoval</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
