---
UID: NE.udecxusbdevice._UDECX_ENDPOINTS_CONFIGURE_TYPE
title: UDECX_ENDPOINTS_CONFIGURE_TYPE
author: windows-driver-content
description: Defines values for endpoint configuration options.
old-location: buses\udecx_endpoints_configure_type.htm
old-project: usbref
ms.assetid: F13C7D8D-C134-432A-904B-7435894B07E5
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UdecxUrbSetBytesCompleted
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UDECX_ENDPOINTS_CONFIGURE_TYPE
req.alt-loc: udecxusbdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UDECX_ENDPOINTS_CONFIGURE_TYPE enumeration



## -description
<p>Defines values for endpoint configuration options. </p>


## -syntax

````
typedef enum _UDECX_ENDPOINTS_CONFIGURE_TYPE { 
  UdecxEndpointsConfigureTypeDeviceInitialize           = 0,
  UdecxEndpointsConfigureTypeDeviceConfigurationChange  = ,
  UdecxEndpointsConfigureTypeInterfaceSettingChange     = ,
  UdecxEndpointsConfigureTypeEndpointsReleasedOnly      = 
} UDECX_ENDPOINTS_CONFIGURE_TYPE, *PUDECX_ENDPOINTS_CONFIGURE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="UdecxEndpointsConfigureTypeDeviceInitialize"></a><a id="udecxendpointsconfiguretypedeviceinitialize"></a><a id="UDECXENDPOINTSCONFIGURETYPEDEVICEINITIALIZE"></a><b>UdecxEndpointsConfigureTypeDeviceInitialize</b>

<dd>
<p>Reserved for internal use.</p>
</dd>

### -field <a id="UdecxEndpointsConfigureTypeDeviceConfigurationChange"></a><a id="udecxendpointsconfiguretypedeviceconfigurationchange"></a><a id="UDECXENDPOINTSCONFIGURETYPEDEVICECONFIGURATIONCHANGE"></a><b>UdecxEndpointsConfigureTypeDeviceConfigurationChange</b>

<dd>
<p>The requested change applies to the USB device configuration.</p>
</dd>

### -field <a id="UdecxEndpointsConfigureTypeInterfaceSettingChange"></a><a id="udecxendpointsconfiguretypeinterfacesettingchange"></a><a id="UDECXENDPOINTSCONFIGURETYPEINTERFACESETTINGCHANGE"></a><b>UdecxEndpointsConfigureTypeInterfaceSettingChange</b>

<dd>
<p>The requested change applies to an alternate setting of a USB interface.</p>
</dd>

### -field <a id="UdecxEndpointsConfigureTypeEndpointsReleasedOnly"></a><a id="udecxendpointsconfiguretypeendpointsreleasedonly"></a><a id="UDECXENDPOINTSCONFIGURETYPEENDPOINTSRELEASEDONLY"></a><b>UdecxEndpointsConfigureTypeEndpointsReleasedOnly</b>

<dd>
<p>The requested change applies to an endpoint of an interface setting.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Udecxusbdevice.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt595913">EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt627993">UDECX_ENDPOINTS_CONFIGURE_PARAMS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UDECX_ENDPOINTS_CONFIGURE_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
