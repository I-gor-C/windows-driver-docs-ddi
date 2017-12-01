---
UID: NE.wwan._WWAN_PIN_TYPE
title: WWAN_PIN_TYPE
author: windows-driver-content
description: The WWAN_PIN_TYPE enumeration lists the different types of Personal Identification Numbers (PINs) that are supported by the MB device.
old-location: netvista\wwan_pin_type.htm
old-project: netvista
ms.assetid: f6b8146e-dbe2-4c73-beb2-02868db9fb27
ms.author: windowsdriverdev
ms.date: 11/28/2017
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

### -field <a id="WwanPinTypeNone"></a><a id="wwanpintypenone"></a><a id="WWANPINTYPENONE"></a><b>WwanPinTypeNone</b>

<dd>
<p>No PIN is pending to be entered.</p>
</dd>

### -field <a id="WwanPinTypeCustom"></a><a id="wwanpintypecustom"></a><a id="WWANPINTYPECUSTOM"></a><b>WwanPinTypeCustom</b>

<dd>
<p>The PIN type is a custom type and is none of the other PIN types listed in this
     enumeration.</p>
</dd>

### -field <a id="WwanPinTypePin1"></a><a id="wwanpintypepin1"></a><a id="WWANPINTYPEPIN1"></a><b>WwanPinTypePin1</b>

<dd>
<p>The PIN1 key.</p>
</dd>

### -field <a id="WwanPinTypePin2"></a><a id="wwanpintypepin2"></a><a id="WWANPINTYPEPIN2"></a><b>WwanPinTypePin2</b>

<dd>
<p>The PIN2 key.</p>
</dd>

### -field <a id="WwanPinTypeDeviceSimPin"></a><a id="wwanpintypedevicesimpin"></a><a id="WWANPINTYPEDEVICESIMPIN"></a><b>WwanPinTypeDeviceSimPin</b>

<dd>
<p>The device to SIM key.</p>
</dd>

### -field <a id="WwanPinTypeDeviceFirstSimPin"></a><a id="wwanpintypedevicefirstsimpin"></a><a id="WWANPINTYPEDEVICEFIRSTSIMPIN"></a><b>WwanPinTypeDeviceFirstSimPin</b>

<dd>
<p>The device to very first SIM key.</p>
</dd>

### -field <a id="WwanPinTypeNetworkPin"></a><a id="wwanpintypenetworkpin"></a><a id="WWANPINTYPENETWORKPIN"></a><b>WwanPinTypeNetworkPin</b>

<dd>
<p>The network personalization key.</p>
</dd>

### -field <a id="WwanPinTypeNetworkSubsetPin"></a><a id="wwanpintypenetworksubsetpin"></a><a id="WWANPINTYPENETWORKSUBSETPIN"></a><b>WwanPinTypeNetworkSubsetPin</b>

<dd>
<p>The network subset personalization key.</p>
</dd>

### -field <a id="WwanPinTypeSvcProviderPin"></a><a id="wwanpintypesvcproviderpin"></a><a id="WWANPINTYPESVCPROVIDERPIN"></a><b>WwanPinTypeSvcProviderPin</b>

<dd>
<p>The service provider (SP) personalization key.</p>
</dd>

### -field <a id="WwanPinTypeCorporatePin"></a><a id="wwanpintypecorporatepin"></a><a id="WWANPINTYPECORPORATEPIN"></a><b>WwanPinTypeCorporatePin</b>

<dd>
<p>The corporate personalization key.</p>
</dd>

### -field <a id="WwanPinTypeSubsidyLock"></a><a id="wwanpintypesubsidylock"></a><a id="WWANPINTYPESUBSIDYLOCK"></a><b>WwanPinTypeSubsidyLock</b>

<dd>
<p>The subsidy unlock key.</p>
</dd>

### -field <a id="WwanPinTypePuk1"></a><a id="wwanpintypepuk1"></a><a id="WWANPINTYPEPUK1"></a><b>WwanPinTypePuk1</b>

<dd>
<p>The Personal Identification Number1 Unlock Key (PUK1).</p>
</dd>

### -field <a id="WwanPinTypePuk2"></a><a id="wwanpintypepuk2"></a><a id="WWANPINTYPEPUK2"></a><b>WwanPinTypePuk2</b>

<dd>
<p>The Personal Identification Number2 Unlock Key (PUK2).</p>
</dd>

### -field <a id="WwanPinTypeDeviceFirstSimPuk"></a><a id="wwanpintypedevicefirstsimpuk"></a><a id="WWANPINTYPEDEVICEFIRSTSIMPUK"></a><b>WwanPinTypeDeviceFirstSimPuk</b>

<dd>
<p>The device to very first SIM PIN unlock key.</p>
</dd>

### -field <a id="WwanPinTypeNetworkPuk"></a><a id="wwanpintypenetworkpuk"></a><a id="WWANPINTYPENETWORKPUK"></a><b>WwanPinTypeNetworkPuk</b>

<dd>
<p>The network personalization unlock key.</p>
</dd>

### -field <a id="WwanPinTypeNetworkSubsetPuk"></a><a id="wwanpintypenetworksubsetpuk"></a><a id="WWANPINTYPENETWORKSUBSETPUK"></a><b>WwanPinTypeNetworkSubsetPuk</b>

<dd>
<p>The network subset personalization unlock key.</p>
</dd>

### -field <a id="WwanPinTypeSvcProviderPuk"></a><a id="wwanpintypesvcproviderpuk"></a><a id="WWANPINTYPESVCPROVIDERPUK"></a><b>WwanPinTypeSvcProviderPuk</b>

<dd>
<p>The service provider (SP) personalization unlock key.</p>
</dd>

### -field <a id="WwanPinTypeCorporatePuk"></a><a id="wwanpintypecorporatepuk"></a><a id="WWANPINTYPECORPORATEPUK"></a><b>WwanPinTypeCorporatePuk</b>

<dd>
<p>The corporate personalization unlock key.</p>
</dd>

### -field <a id="WwanPinTypeMax"></a><a id="wwanpintypemax"></a><a id="WWANPINTYPEMAX"></a><b>WwanPinTypeMax</b>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PIN_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
