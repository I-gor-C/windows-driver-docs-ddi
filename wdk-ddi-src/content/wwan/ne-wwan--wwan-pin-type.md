---
UID: NE.wwan._WWAN_PIN_TYPE
title: WWAN_PIN_TYPE
author: windows-driver-content
description: The WWAN_PIN_TYPE enumeration lists the different types of Personal Identification Numbers (PINs) that are supported by the MB device.
old-location: netvista\wwan_pin_type.htm
old-project: netvista
ms.assetid: f6b8146e-dbe2-4c73-beb2-02868db9fb27
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_PIN_TYPE
req.alt-loc: wwan.h
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
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_PIN_TYPE enumeration



## -description
<p>The WWAN_PIN_TYPE enumeration lists the different types of Personal Identification Numbers (PINs)
  that are supported by the MB device.</p>


## -syntax

````
typedef enum _WWAN_PIN_TYPE { 
  WwanPinTypeNone               = 0,
  WwanPinTypeCustom,
  WwanPinTypePin1,
  WwanPinTypePin2,
  WwanPinTypeDeviceSimPin,
  WwanPinTypeDeviceFirstSimPin,
  WwanPinTypeNetworkPin,
  WwanPinTypeNetworkSubsetPin,
  WwanPinTypeSvcProviderPin,
  WwanPinTypeCorporatePin,
  WwanPinTypeSubsidyLock,
  WwanPinTypePuk1,
  WwanPinTypePuk2,
  WwanPinTypeDeviceFirstSimPuk,
  WwanPinTypeNetworkPuk,
  WwanPinTypeNetworkSubsetPuk,
  WwanPinTypeSvcProviderPuk,
  WwanPinTypeCorporatePuk,
  WwanPinTypeMax
} WWAN_PIN_TYPE, *PWWAN_PIN_TYPE;
````


## -enum-fields
<dl>

### -field WwanPinTypeNone

<dd>
<p>No PIN is pending to be entered.</p>
</dd>

### -field WwanPinTypeCustom

<dd>
<p>The PIN type is a custom type and is none of the other PIN types listed in this
     enumeration.</p>
</dd>

### -field WwanPinTypePin1

<dd>
<p>The PIN1 key.</p>
</dd>

### -field WwanPinTypePin2

<dd>
<p>The PIN2 key.</p>
</dd>

### -field WwanPinTypeDeviceSimPin

<dd>
<p>The device to SIM key.</p>
</dd>

### -field WwanPinTypeDeviceFirstSimPin

<dd>
<p>The device to very first SIM key.</p>
</dd>

### -field WwanPinTypeNetworkPin

<dd>
<p>The network personalization key.</p>
</dd>

### -field WwanPinTypeNetworkSubsetPin

<dd>
<p>The network subset personalization key.</p>
</dd>

### -field WwanPinTypeSvcProviderPin

<dd>
<p>The service provider (SP) personalization key.</p>
</dd>

### -field WwanPinTypeCorporatePin

<dd>
<p>The corporate personalization key.</p>
</dd>

### -field WwanPinTypeSubsidyLock

<dd>
<p>The subsidy unlock key.</p>
</dd>

### -field WwanPinTypePuk1

<dd>
<p>The Personal Identification Number1 Unlock Key (PUK1).</p>
</dd>

### -field WwanPinTypePuk2

<dd>
<p>The Personal Identification Number2 Unlock Key (PUK2).</p>
</dd>

### -field WwanPinTypeDeviceFirstSimPuk

<dd>
<p>The device to very first SIM PIN unlock key.</p>
</dd>

### -field WwanPinTypeNetworkPuk

<dd>
<p>The network personalization unlock key.</p>
</dd>

### -field WwanPinTypeNetworkSubsetPuk

<dd>
<p>The network subset personalization unlock key.</p>
</dd>

### -field WwanPinTypeSvcProviderPuk

<dd>
<p>The service provider (SP) personalization unlock key.</p>
</dd>

### -field WwanPinTypeCorporatePuk

<dd>
<p>The corporate personalization unlock key.</p>
</dd>

### -field WwanPinTypeMax

<dd>
<p>The total number of supported PIN types.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wwan\ns-wwan--wwan-pin-info.md">WWAN_PIN_INFO</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-pin-action.md">WWAN_PIN_ACTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PIN_TYPE enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
