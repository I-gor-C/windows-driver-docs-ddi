---
UID: NE.wdfusb._WdfUsbTargetDeviceSelectConfigType
title: WdfUsbTargetDeviceSelectConfigType
author: windows-driver-content
description: The WdfUsbTargetDeviceSelectConfigType enumeration defines types of configuration operations for USB devices.
old-location: wdf\wdfusbtargetdeviceselectconfigtype.htm
ms.assetid: d3637f5e-d4c1-430c-8511-8aac18fceee2
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfUsbTargetDeviceSelectConfigType
req.alt-loc: wdfusb.h
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
ms.keywords: WDF_TIMER_CONFIG, WDF_TIMER_CONFIG, *PWDF_TIMER_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetDeviceSelectConfigType enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfUsbTargetDeviceSelectConfigType</b> enumeration defines types of configuration operations for USB devices.</p>


## -syntax

````
typedef enum _WdfUsbTargetDeviceSelectConfigType { 
  WdfUsbTargetDeviceSelectConfigTypeInvalid               = 0,
  WdfUsbTargetDeviceSelectConfigTypeDeconfig              = 1,
  WdfUsbTargetDeviceSelectConfigTypeSingleInterface       = 2,
  WdfUsbTargetDeviceSelectConfigTypeMultiInterface        = 3,
  WdfUsbTargetDeviceSelectConfigTypeInterfacesPairs       = 4,
  WdfUsbTargetDeviceSelectConfigTypeInterfacesDescriptor  = 5,
  WdfUsbTargetDeviceSelectConfigTypeUrb                   = 6
} WdfUsbTargetDeviceSelectConfigType;
````


## -enum-fields
<dl>

### -field <a id="WdfUsbTargetDeviceSelectConfigTypeInvalid"></a><a id="wdfusbtargetdeviceselectconfigtypeinvalid"></a><a id="WDFUSBTARGETDEVICESELECTCONFIGTYPEINVALID"></a><b>WdfUsbTargetDeviceSelectConfigTypeInvalid</b>

<dd>
<p>For internal use only.</p>
</dd>

### -field <a id="WdfUsbTargetDeviceSelectConfigTypeDeconfig"></a><a id="wdfusbtargetdeviceselectconfigtypedeconfig"></a><a id="WDFUSBTARGETDEVICESELECTCONFIGTYPEDECONFIG"></a><b>WdfUsbTargetDeviceSelectConfigTypeDeconfig</b>

<dd>
<p>Deconfigure the device. This value applies to KMDF only.</p>
</dd>

### -field <a id="WdfUsbTargetDeviceSelectConfigTypeSingleInterface"></a><a id="wdfusbtargetdeviceselectconfigtypesingleinterface"></a><a id="WDFUSBTARGETDEVICESELECTCONFIGTYPESINGLEINTERFACE"></a><b>WdfUsbTargetDeviceSelectConfigTypeSingleInterface</b>

<dd>
<p>Configure the device to use a single, specified interface. This value applies to KMDF and UMDF.</p>
</dd>

### -field <a id="WdfUsbTargetDeviceSelectConfigTypeMultiInterface"></a><a id="wdfusbtargetdeviceselectconfigtypemultiinterface"></a><a id="WDFUSBTARGETDEVICESELECTCONFIGTYPEMULTIINTERFACE"></a><b>WdfUsbTargetDeviceSelectConfigTypeMultiInterface</b>

<dd>
<p>Configure the device to use multiple interfaces. This value applies to KMDF and UMDF.</p>
</dd>

### -field <a id="WdfUsbTargetDeviceSelectConfigTypeInterfacesPairs"></a><a id="wdfusbtargetdeviceselectconfigtypeinterfacespairs"></a><a id="WDFUSBTARGETDEVICESELECTCONFIGTYPEINTERFACESPAIRS"></a><b>WdfUsbTargetDeviceSelectConfigTypeInterfacesPairs</b>

<dd>
<p>Configure the device to use multiple interfaces, possibly with alternate settings. Alternate settings are described in the USB specification.  This value applies to KMDF and UMDF.</p>
</dd>

### -field <a id="WdfUsbTargetDeviceSelectConfigTypeInterfacesDescriptor"></a><a id="wdfusbtargetdeviceselectconfigtypeinterfacesdescriptor"></a><a id="WDFUSBTARGETDEVICESELECTCONFIGTYPEINTERFACESDESCRIPTOR"></a><b>WdfUsbTargetDeviceSelectConfigTypeInterfacesDescriptor</b>

<dd>
<p>Configure the device by using configuration parameters that are contained in USB descriptors. This value applies to KMDF only.</p>
</dd>

### -field <a id="WdfUsbTargetDeviceSelectConfigTypeUrb"></a><a id="wdfusbtargetdeviceselectconfigtypeurb"></a><a id="WDFUSBTARGETDEVICESELECTCONFIGTYPEURB"></a><b>WdfUsbTargetDeviceSelectConfigTypeUrb</b>

<dd>
<p>Configure the device by using configuration parameters that are contained in a driver-supplied URB structure. This value applies to KMDF only.</p>
</dd>
</dl>

## -remarks
<p>The <b>WdfUsbTargetDeviceSelectConfigType</b> enumeration is used to specify the <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552600">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure. That structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550101">WdfUsbTargetDeviceSelectConfig</a> method.</p>

<p>The <b>WdfUsbTargetDeviceSelectConfigType</b> enumeration is used to specify the <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552600">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure. That structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550101">WdfUsbTargetDeviceSelectConfig</a> method.</p>

<p>The <b>WdfUsbTargetDeviceSelectConfigType</b> enumeration is used to specify the <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552600">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure. That structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550101">WdfUsbTargetDeviceSelectConfig</a> method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552600">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550101">WdfUsbTargetDeviceSelectConfig</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetDeviceSelectConfigType enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
