---
UID: NF.wudfusb.IWDFUsbInterface.GetConfiguredSettingIndex
title: IWDFUsbInterface::GetConfiguredSettingIndex
author: windows-driver-content
description: The GetConfiguredSettingIndex method retrieves the current setting index for a USB interface.
old-location: wdf\iwdfusbinterface_getconfiguredsettingindex.htm
old-project: wdf
ms.assetid: 0deccfee-34e3-47ee-b141-9758cffcd0c2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFUsbInterface, GetConfiguredSettingIndex, IWDFUsbInterface::GetConfiguredSettingIndex
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
req.alt-api: IWDFUsbInterface.GetConfiguredSettingIndex
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
req.iface: IWDFUsbInterface
req.product: Windows 10 or later.
---

# IWDFUsbInterface::GetConfiguredSettingIndex method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetConfiguredSettingIndex</b> method retrieves the current setting index for a USB interface.</p>


## -syntax

````
UCHAR GetConfiguredSettingIndex();
````


## -parameters


## -returns
<p><b>GetConfiguredSettingIndex</b> returns the current setting index for the USB interface.</p>

<p><b>GetConfiguredSettingIndex</b> returns the current setting index for the USB interface.</p>

<p><b>GetConfiguredSettingIndex</b> returns the current setting index for the USB interface.</p>

## -remarks
<p>The <b>GetConfiguredSettingIndex</b> method is provided for convenience because a UMDF driver can obtain the current setting index from the <b>bAlternateSetting</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a> structure that the driver retrieves when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560320">IWDFUsbInterface::GetInterfaceDescriptor</a> method. </p>

<p>The <b>GetConfiguredSettingIndex</b> method is provided for convenience because a UMDF driver can obtain the current setting index from the <b>bAlternateSetting</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a> structure that the driver retrieves when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560320">IWDFUsbInterface::GetInterfaceDescriptor</a> method. </p>

<p>The <b>GetConfiguredSettingIndex</b> method is provided for convenience because a UMDF driver can obtain the current setting index from the <b>bAlternateSetting</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a> structure that the driver retrieves when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560320">IWDFUsbInterface::GetInterfaceDescriptor</a> method. </p>

<p>The <b>GetConfiguredSettingIndex</b> method is provided for convenience because a UMDF driver can obtain the current setting index from the <b>bAlternateSetting</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a> structure that the driver retrieves when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560320">IWDFUsbInterface::GetInterfaceDescriptor</a> method. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560312">IWDFUsbInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560320">IWDFUsbInterface::GetInterfaceDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUsbInterface::GetConfiguredSettingIndex method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
