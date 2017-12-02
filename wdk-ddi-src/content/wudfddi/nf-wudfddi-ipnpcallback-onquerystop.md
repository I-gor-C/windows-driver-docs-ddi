---
UID: NF.wudfddi.IPnpCallback.OnQueryStop
title: IPnpCallback::OnQueryStop
author: windows-driver-content
description: The OnQueryStop method notifies a driver before a device is stopped.
old-location: wdf\ipnpcallback_onquerystop.htm
old-project: wdf
ms.assetid: e0cb14fa-82d0-4ce3-8672-801e7f04d522
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IPnpCallback, OnQueryStop, IPnpCallback::OnQueryStop
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPnpCallback.OnQueryStop
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IPnpCallback
req.product: Windows 10 or later.
---

# IPnpCallback::OnQueryStop method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnQueryStop</b> method notifies a driver before a device is stopped. </p>


## -syntax

````
HRESULT OnQueryStop(
  [in] IWDFDevice *pWdfDevice
);
````


## -parameters
<dl>

### -param pWdfDevice [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a> interface for the device object of the device that will be stopped.</p>
</dd>
</dl>

## -returns
<p>If the driver determines that the device can be stopped, the <b>OnQueryStop</b> callback method must return S_OK or another status code for which SUCCEEDED(status) equals <b>TRUE</b>. Otherwise it must return a status code for which SUCCEEDED(status) equals <b>FALSE</b>.   HRESULT error codes are defined in Winerror.h. Do not return HRESULT_FROM_NT(STATUS_NOT_SUPPORTED).</p>

<p>This method must use the HRESULT_FROM_NT macro to return a specific HRESULT value to  return status to a kernel-mode client. For more information, see <a href="wdf.supporting_kernel_mode_clients">Supporting Kernel-mode Clients</a>.</p>

## -remarks
<p>A driver registers the <a href="..\wudfddi\nn-wudfddi-ipnpcallback.md">IPnpCallback</a> interface when it calls the <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> method to create a device object. </p>

<p>The framework does not synchronize the <b>OnQueryStop</b> callback function with other PnP and power management callback functions.  </p>

<p><b>OnQueryStop</b> is not called in framework versions 1.7 and earlier.</p>

<p>For more information about the <b>OnQueryStop</b> callback method, see <a href="wdf.the_pnp_manager_redistributes_system_resources">The PnP Manager Redistributes System Resources</a>.</p>

## -requirements
<table>
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
<a href="..\wudfddi\nn-wudfddi-ipnpcallback.md">IPnpCallback</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a>
</dt>
<dt>
<a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IPnpCallback::OnQueryStop method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
