---
UID: NF.wudfddi.IWDFDeviceInitialize.AutoForwardCreateCleanupClose
title: IWDFDeviceInitialize::AutoForwardCreateCleanupClose
author: windows-driver-content
description: The AutoForwardCreateCleanupClose method controls when create, cleanup, and close notifications are forwarded to the next lower driver in the device stack.
old-location: wdf\iwdfdeviceinitialize_autoforwardcreatecleanupclose.htm
old-project: wdf
ms.assetid: b9c8e54e-7cd5-48a9-b948-5327900c8a99
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFDeviceInitialize, AutoForwardCreateCleanupClose, IWDFDeviceInitialize::AutoForwardCreateCleanupClose
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
req.alt-api: IWDFDeviceInitialize.AutoForwardCreateCleanupClose
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
req.iface: IWDFDeviceInitialize
req.product: Windows 10 or later.
---

# IWDFDeviceInitialize::AutoForwardCreateCleanupClose method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>AutoForwardCreateCleanupClose</b> method controls when create, cleanup, and close notifications are forwarded to the next lower driver in the device stack.</p>


## -syntax

````
void AutoForwardCreateCleanupClose(
  [in] WDF_TRI_STATE State
);
````


## -parameters
<dl>

### -param <i>State</i> [in]

<dd>
<p>A WDF_TRI_STATE-typed value that identifies the state of automatic forwarding. The following table shows the possible values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>WdfUseDefault</b> (0)</p>
</td>
<td>
<p>The framework uses the default forwarding scheme. For more information, see the following Remarks section.</p>
</td>
</tr>
<tr>
<td>
<p><b>WdfFalse</b> (1)</p>
</td>
<td>
<p>The framework does not forward create, cleanup, and close notifications to the next lower driver.</p>
</td>
</tr>
<tr>
<td>
<p><b>WdfTrue</b> (2)</p>
</td>
<td>
<p>The framework synchronously forwards create, cleanup, and close notifications to the next lower driver.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If the UMDF driver passes <b>WdfUseDefault</b> for the <i>State</i> parameter in a call to <b>AutoForwardCreateCleanupClose</b>, the framework uses a default forwarding scheme for create, cleanup, and close notifications that depends on whether the driver is a filter or function driver:</p>

<p>If the driver is a filter driver, the default forwarding scheme is to synchronously forward notifications to the next lower driver.</p>

<p>If the driver is a function driver, the default forwarding scheme is not to forward notifications to the next lower driver.</p>

<p>If the framework is set up for forwarding, it forwards cleanup and close notifications regardless of whether the driver supports the <a href="wdf.ifilecallbackcleanup_oncleanupfile">IFileCallbackCleanup::OnCleanupFile</a> and <a href="wdf.ifilecallbackclose_onclosefile">IFileCallbackClose::OnCloseFile</a> interface methods. However, the framework automatically forwards create requests only if the driver does not support the <a href="wdf.iqueuecallbackcreate_oncreatefile">IQueueCallbackCreate::OnCreateFile</a> method. If the driver supports <b>IQueueCallbackCreate::OnCreateFile</b>, the framework forwards create requests only if the driver explicitly set up forwarding (<b>WdfTrue</b>) to the next lower driver. </p>

<p>For more information about how a UMDF driver uses <b>AutoForwardCreateCleanupClose</b>, see <a href="wdf.preventing_an_imbalance_of_create_and_close_notifications_to_a_driver">Preventing an Imbalance of Create and Close Notifications to a Driver</a>. </p>

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
<a href="..\wudfddi\nn-wudfddi-iwdfdeviceinitialize.md">IWDFDeviceInitialize</a>
</dt>
<dt>
<a href="wdf.ifilecallbackcleanup_oncleanupfile">IFileCallbackCleanup::OnCleanupFile</a>
</dt>
<dt>
<a href="wdf.ifilecallbackclose_onclosefile">IFileCallbackClose::OnCloseFile</a>
</dt>
<dt>
<a href="wdf.iqueuecallbackcreate_oncreatefile">IQueueCallbackCreate::OnCreateFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDeviceInitialize::AutoForwardCreateCleanupClose method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
