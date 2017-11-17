---
UID: NE.wudfddi_types._WDF_PNP_CAPABILITY
title: WDF_PNP_CAPABILITY
author: windows-driver-content
description: The WDF_PNP_CAPABILITY enumeration contains values that identify Plug and Play (PnP) capabilities for a device.
old-location: wdf\wdf_pnp_capability.htm
ms.assetid: adcc5f64-b49c-47ca-8ef9-276537a0d7c6
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi_types.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDF_PNP_CAPABILITY
req.alt-loc: Wudfddi_types.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: WRITE_REGISTER_USHORT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_PNP_CAPABILITY enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>WDF_PNP_CAPABILITY</b> enumeration contains values that identify Plug and Play (PnP) capabilities for a device.</p>


## -syntax

````
typedef enum _WDF_PNP_CAPABILITY { 
  WdfPnpCapInvalid            = 0,
  WdfPnpCapLockSupported      = 1,
  WdfPnpCapEjectSupported     = 2,
  WdfPnpCapRemovable          = 3,
  WdfPnpCapDockDevice         = 4,
  WdfPnpCapSurpriseRemovalOk  = 5,
  WdfPnpCapNoDisplayInUI      = 6,
  WdfPnpCapMaximum            = ( WdfPnpCapNoDisplayInUI + 1 )
} WDF_PNP_CAPABILITY;
````


## -enum-fields
<dl>

### -field <a id="WdfPnpCapInvalid"></a><a id="wdfpnpcapinvalid"></a><a id="WDFPNPCAPINVALID"></a><b>WdfPnpCapInvalid</b>

<dd>
<p>Indicates whether PnP capabilities of the device are invalid.</p>
</dd>

### -field <a id="WdfPnpCapLockSupported"></a><a id="wdfpnpcaplocksupported"></a><a id="WDFPNPCAPLOCKSUPPORTED"></a><b>WdfPnpCapLockSupported</b>

<dd>
<p>Indicates whether the device can be locked in its slot to prevent ejection. (Setting this capability disables ejecting a device from its slot and does not disable ejecting media from a device.) </p>
</dd>

### -field <a id="WdfPnpCapEjectSupported"></a><a id="wdfpnpcapejectsupported"></a><a id="WDFPNPCAPEJECTSUPPORTED"></a><b>WdfPnpCapEjectSupported</b>

<dd>
<p>Indicates whether the device can be ejected from its slot. (Setting this capability enables ejecting a device from its slot and does not enable ejecting media from a device.) </p>
</dd>

### -field <a id="WdfPnpCapRemovable"></a><a id="wdfpnpcapremovable"></a><a id="WDFPNPCAPREMOVABLE"></a><b>WdfPnpCapRemovable</b>

<dd>
<p>Indicates whether the device can be removed while the computer is running. If <b>WdfPnpCapRemovable</b> is set to <b>WdfTrue</b> and <b>WdfPnpCapSurpriseRemovalOk</b> is set to <b>WdfFalse</b>, users should use the system's Unplug or Eject Hardware application. </p>
</dd>

### -field <a id="WdfPnpCapDockDevice"></a><a id="wdfpnpcapdockdevice"></a><a id="WDFPNPCAPDOCKDEVICE"></a><b>WdfPnpCapDockDevice</b>

<dd>
<p>Indicates whether the device is a docking station. </p>
</dd>

### -field <a id="WdfPnpCapSurpriseRemovalOk"></a><a id="wdfpnpcapsurpriseremovalok"></a><a id="WDFPNPCAPSURPRISEREMOVALOK"></a><b>WdfPnpCapSurpriseRemovalOk</b>

<dd>
<p>Indicates whether users can remove the device without using the computer's Unplug or Eject Hardware application.</p>
</dd>

### -field <a id="WdfPnpCapNoDisplayInUI"></a><a id="wdfpnpcapnodisplayinui"></a><a id="WDFPNPCAPNODISPLAYINUI"></a><b>WdfPnpCapNoDisplayInUI</b>

<dd>
<p>Indicates whether the device can be hidden (not displayed) in Device Manager.</p>
</dd>

### -field <a id="WdfPnpCapMaximum"></a><a id="wdfpnpcapmaximum"></a><a id="WDFPNPCAPMAXIMUM"></a><b>WdfPnpCapMaximum</b>

<dd>
<p>Valid enumeration values were exceeded.</p>
</dd>
</dl>

## -remarks
<p>A UMDF driver supplies one of the values of <b>WDF_PNP_CAPABILITY</b> to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556974">IWDFDeviceInitialize::GetPnpCapability</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff556993">IWDFDeviceInitialize::SetPnpCapability</a> method to identify the PnP capability to retrieve or set status for.</p>

<p>A UMDF driver supplies one of the values of <b>WDF_PNP_CAPABILITY</b> to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556974">IWDFDeviceInitialize::GetPnpCapability</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff556993">IWDFDeviceInitialize::SetPnpCapability</a> method to identify the PnP capability to retrieve or set status for.</p>

<p>A UMDF driver supplies one of the values of <b>WDF_PNP_CAPABILITY</b> to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556974">IWDFDeviceInitialize::GetPnpCapability</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff556993">IWDFDeviceInitialize::SetPnpCapability</a> method to identify the PnP capability to retrieve or set status for.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi_types.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556974">IWDFDeviceInitialize::GetPnpCapability</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556993">IWDFDeviceInitialize::SetPnpCapability</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_PNP_CAPABILITY enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
