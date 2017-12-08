---
UID: NF.wudfddi.IPnpCallbackHardware.OnPrepareHardware
title: IPnpCallbackHardware::OnPrepareHardware
author: windows-driver-content
description: The OnPrepareHardware method notifies a driver to make the specified hardware accessible.
old-location: wdf\ipnpcallbackhardware_onpreparehardware.htm
old-project: wdf
ms.assetid: c821231a-446d-45dd-9c12-9ab05aeb1108
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IPnpCallbackHardware, OnPrepareHardware, IPnpCallbackHardware::OnPrepareHardware
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
req.alt-api: IPnpCallbackHardware.OnPrepareHardware
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
req.iface: IPnpCallbackHardware
req.product: Windows 10 or later.
---

# IPnpCallbackHardware::OnPrepareHardware method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnPrepareHardware</b> method notifies a driver to make the specified hardware accessible.</p>


## -syntax

````
HRESULT OnPrepareHardware(
  [in] IWDFDevice *pWdfDevice
);
````


## -parameters
<dl>

### -param pWdfDevice [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a> interface for the device object of the device to make accessible.</p>
</dd>
</dl>

## -returns
<p><b>OnPrepareHardware</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes defined in Winerror.h. Do not return HRESULT_FROM_NT(STATUS_NOT_SUPPORTED).</p>

<p>If <b>OnPrepareHardware</b> returns an error code, the framework will still call the <a href="wdf.ipnpcallbackhardware_onreleasehardware">IPnpCallbackHardware::OnReleaseHardware</a> method. The <b>OnReleaseHardware</b> method can then free resources that were allocated during the call to <b>OnPrepareHardware</b>. Because <b>OnReleaseHardware</b> must free resources for both success and failure cases of <b>OnPrepareHardware</b>,  it must be able to handle the cleanup of partial resources. 

</p>

<p>This method must use the HRESULT_FROM_NT macro to return a specific HRESULT value to  return status to a kernel-mode client. For more information, see <a href="wdf.supporting_kernel_mode_clients">Supporting Kernel-mode Clients</a>.</p>

## -remarks
<p>A driver registers the <a href="..\wudfddi\nn-wudfddi-ipnpcallbackhardware.md">IPnpCallbackHardware</a> interface when it calls the <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> method to create a device object. </p>

<p>Receiving a call to the <b>OnPrepareHardware</b> method is equivalent to a Microsoft Windows Driver Model (WDM) driver receiving an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a> IRP.</p>

<p>For more information, see <a href="wdf.finding_and_mapping_hardware_resources_in_a_umdf_driver">Finding and Mapping Hardware Resources in a UMDF Driver</a>.</p>

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
<a href="..\wudfddi\nn-wudfddi-ipnpcallbackhardware.md">IPnpCallbackHardware</a>
</dt>
<dt>
<a href="wdf.ipnpcallbackhardware_onreleasehardware">IPnpCallbackHardware::OnReleaseHardware</a>
</dt>
<dt>
<a href="wdf.ipnpcallbackhardware2_onpreparehardware">IPnpCallbackHardware2::OnPrepareHardware</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IPnpCallbackHardware::OnPrepareHardware method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
