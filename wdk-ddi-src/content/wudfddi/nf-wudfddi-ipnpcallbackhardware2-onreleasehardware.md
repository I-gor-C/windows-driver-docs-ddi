---
UID: NF.wudfddi.IPnpCallbackHardware2.OnReleaseHardware
title: IPnpCallbackHardware2::OnReleaseHardware
author: windows-driver-content
description: The OnReleaseHardware method performs operations that are needed when a device is no longer accessible.
old-location: wdf\ipnpcallbackhardware2_onreleasehardware.htm
old-project: wdf
ms.assetid: 652B92C2-EF04-482A-BB57-9F64F947EE4F
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IPnpCallbackHardware2, OnReleaseHardware, IPnpCallbackHardware2::OnReleaseHardware
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IPnpCallbackHardware2.OnReleaseHardware
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
req.iface: IPnpCallbackHardware2
req.product: Windows 10 or later.
---

# IPnpCallbackHardware2::OnReleaseHardware method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnReleaseHardware</b> method performs operations that are needed when a device is no longer accessible.</p>


## -syntax

````
HRESULT OnReleaseHardware(
  [in] IWDFDevice3        *pWdfDevice,
  [in] IWDFCmResourceList *pWdfResourcesTranslated
);
````


## -parameters
<dl>

### -param <i>pWdfDevice</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451197">IWDFDevice3</a> interface for the framework device object.</p>
</dd>

### -param <i>pWdfResourcesTranslated</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439762">IWDFCmResourceList</a> interface for the framework resource-list object that identifies the translated hardware resources that the Plug and Play manager has assigned to the device.</p>
</dd>
</dl>

## -returns
<p><b>OnReleaseHardware</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h. Do not return HRESULT_FROM_NT(STATUS_NOT_SUPPORTED).</p>

## -remarks
<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439727">IPnpCallbackHardware2</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to create a device object.</p>

<p> 
The <b>OnReleaseHardware</b> method must free resources that were allocated during the call to the driver's <a href="wdf.ipnpcallbackhardware2_onpreparehardware">IPnpCallbackHardware2::OnPrepareHardware</a> method, regardless of whether <b>OnPrepareHardware</b> succeeded or failed. As such, <b>OnReleaseHardware</b> must be able to handle the cleanup of partial resources.</p>

<p>For information about deleting an interrupt object, see <a href="wdf.deleting_an_interrupt_object">Deleting an Interrupt Object</a>.</p>

<p>For information about parsing hardware resources, see <a href="wdf.finding_and_mapping_hardware_resources_in_a_umdf_driver">Finding and Mapping Hardware Resources in a UMDF Driver</a>.
</p>

<p>See example code in <a href="wdf.iwdfdevice3_mapiospace">IWDFDevice3::MapIoSpace</a>.</p>

<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439727">IPnpCallbackHardware2</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to create a device object.</p>

<p> 
The <b>OnReleaseHardware</b> method must free resources that were allocated during the call to the driver's <a href="wdf.ipnpcallbackhardware2_onpreparehardware">IPnpCallbackHardware2::OnPrepareHardware</a> method, regardless of whether <b>OnPrepareHardware</b> succeeded or failed. As such, <b>OnReleaseHardware</b> must be able to handle the cleanup of partial resources.</p>

<p>For information about deleting an interrupt object, see <a href="wdf.deleting_an_interrupt_object">Deleting an Interrupt Object</a>.</p>

<p>For information about parsing hardware resources, see <a href="wdf.finding_and_mapping_hardware_resources_in_a_umdf_driver">Finding and Mapping Hardware Resources in a UMDF Driver</a>.
</p>

<p>See example code in <a href="wdf.iwdfdevice3_mapiospace">IWDFDevice3::MapIoSpace</a>.</p>

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
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439727">IPnpCallbackHardware2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439734">OnPrepareHardware</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IPnpCallbackHardware2::OnReleaseHardware method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
