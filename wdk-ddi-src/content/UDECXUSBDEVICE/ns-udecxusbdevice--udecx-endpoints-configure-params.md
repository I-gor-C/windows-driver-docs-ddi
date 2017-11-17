---
UID: NS.udecxusbdevice._UDECX_ENDPOINTS_CONFIGURE_PARAMS
title: UDECX_ENDPOINTS_CONFIGURE_PARAMS
author: windows-driver-content
description: Contains the configuration options specified by USB device emulation class extension (UdeCx) to the client driver when the class extension invokes EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE.
old-location: buses\udecx_endpoints_configure_params.htm
ms.assetid: C31AE3A8-CD3C-4270-BA5C-A61C0F386701
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UDECX_ENDPOINTS_CONFIGURE_PARAMS
req.alt-loc: UdecxUsbDevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: UDECX_ENDPOINTS_CONFIGURE_PARAMS, UDECX_ENDPOINTS_CONFIGURE_PARAMS, *PUDECX_ENDPOINTS_CONFIGURE_PARAMS
req.iface: 
req.product: Windows 10 or later.
---

# UDECX_ENDPOINTS_CONFIGURE_PARAMS structure



## -description
<p>Contains the configuration options specified by USB device emulation class extension (UdeCx) to the client driver when the class extension invokes <a href="https://msdn.microsoft.com/library/windows/hardware/mt595913">EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE</a>.</p>


## -syntax

````
typedef struct _UDECX_ENDPOINTS_CONFIGURE_PARAMS {
  ULONG                                                    Size;
  UDECX_ENDPOINTS_CONFIGURE_TYPE                           ConfigureType;
  UCHAR                                                    NewConfigurationValue;
  UCHAR                                                    InterfaceNumber;
  ULONG                                                    NewInterfaceSetting;
  UCHAR                                                    EndpointsToConfigureCount;
  _Field_size_(EndpointsToConfigureCount) UDECXUSBENDPOINT *EndpointsToConfigure;
  UCHAR                                                    ReleasedEndpointsCount;
  _Field_size_(ReleasedEndpointsCount) UDECXUSBENDPOINT    *EndpointsToConfigure;
} UDECX_ENDPOINTS_CONFIGURE_PARAMS, *PUDECX_ENDPOINTS_CONFIGURE_PARAMS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size of this structure.</p>
</dd>

### -field <b>ConfigureType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt627994">UDECX_ENDPOINTS_CONFIGURE_TYPE</a>-typed value that indicates whether the configuration, interface setting, or endpoint must be configured. </p>
</dd>

### -field <b>NewConfigurationValue</b>

<dd>
<p>If <b>ConfigureType</b> is <b>UdecxEndpointsConfigureTypeDeviceConfigurationChange</b>, this value is <b>bConfigurationValue</b> of the new configuration descriptor (<a href="https://msdn.microsoft.com/library/windows/hardware/ff539241">USB_CONFIGURATION_DESCRIPTOR</a>).</p>
</dd>

### -field <b>InterfaceNumber</b>

<dd>
<p>If <b>ConfigureType</b> is <b>UdecxEndpointsConfigureTypeInterfaceSettingChange</b>, this value is <b>bInterfaceNumber</b> of the current interface descriptor (<a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a>).</p>
</dd>

### -field <b>NewInterfaceSetting</b>

<dd>
<p>If <b>ConfigureType</b> is <b>UdecxEndpointsConfigureTypeInterfaceSettingChange</b>, this value is <b>bAlternateSetting</b> of the interface descriptor (<a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a>) to set.</p>
</dd>

### -field <b>EndpointsToConfigureCount</b>

<dd>
<p>The number entries in the array pointed to by <i>EndpointsToConfigure</i>. This value indicates number of endpoints that must be configured.</p>
</dd>

### -field <b>EndpointsToConfigure</b>

<dd>
<p>A pointer to an array of UDECXUSBENDPOINT handles that indicates the endpoint objects to be configured.</p>
</dd>

### -field <b>ReleasedEndpointsCount</b>

<dd>
<p>The number entries in the array pointed to by <i>EndpointsToConfigure</i>. This value indicates number of endpoints to release.</p>
</dd>

### -field <b>EndpointsToConfigure</b>

<dd>
<p>A pointer to an array of UDECXUSBENDPOINT handles that indicates the endpoint objects that must be released.</p>
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
<dt>UdecxUsbDevice.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt595913">EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UDECX_ENDPOINTS_CONFIGURE_PARAMS structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
