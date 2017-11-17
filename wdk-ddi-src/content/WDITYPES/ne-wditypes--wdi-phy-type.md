---
UID: NE.wditypes._WDI_PHY_TYPE
title: WDI_PHY_TYPE
author: windows-driver-content
description: The WDI_PHY_TYPE enumeration defines the PHY types.
old-location: netvista\wdi_phy_type.htm
ms.assetid: BDA90056-6DAA-4FC8-82EC-3062087E02C4
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_PHY_TYPE
req.alt-loc: wditypes.hpp
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
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WDI_PHY_TYPE enumeration



## -description
<p>The WDI_PHY_TYPE enumeration defines the PHY types.</p>


## -syntax

````
typedef enum _WDI_PHY_TYPE { 
  WDI_PHY_TYPE_UNKNOWN     = 0,
  WDI_PHY_TYPE_ANY         = 0,
  WDI_PHY_TYPE_FHSS        = 1,
  WDI_PHY_TYPE_DSSS        = 2,
  WDI_PHY_TYPE_IRBASEBAND  = 3,
  WDI_PHY_TYPE_OFDM        = 4,
  WDI_PHY_TYPE_HRDSSS      = 5,
  WDI_PHY_TYPE_ERP         = 6,
  WDI_PHY_TYPE_HT          = 7,
  WDI_PHY_TYPE_VHT         = 8,
  WDI_PHY_TYPE_DMG         = 9,
  WDI_PHY_TYPE_IHV_START   = 0x80000000,
  WDI_PHY_TYPE_IHV_END     = 0xffffffff
} WDI_PHY_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WDI_PHY_TYPE_UNKNOWN"></a><a id="wdi_phy_type_unknown"></a><b>WDI_PHY_TYPE_UNKNOWN</b>

<dd>
<p>Specifies an unknown or uninitialized PHY type.</p>
</dd>

### -field <a id="WDI_PHY_TYPE_ANY"></a><a id="wdi_phy_type_any"></a><b>WDI_PHY_TYPE_ANY</b>

<dd>
<p>Specifies an unknown or uninitialized PHY type.</p>
</dd>

### -field <a id="WDI_PHY_TYPE_FHSS"></a><a id="wdi_phy_type_fhss"></a><b>WDI_PHY_TYPE_FHSS</b>

<dd>
<p>Specifies a frequency-hopping spread-spectrum (FHSS) PHY.</p>
</dd>

### -field <a id="WDI_PHY_TYPE_DSSS"></a><a id="wdi_phy_type_dsss"></a><b>WDI_PHY_TYPE_DSSS</b>

<dd>
<p>Specifies a direct sequence spread spectrum (DSSS) PHY.</p>
</dd>

### -field <a id="WDI_PHY_TYPE_IRBASEBAND"></a><a id="wdi_phy_type_irbaseband"></a><b>WDI_PHY_TYPE_IRBASEBAND</b>

<dd>
<p>Specifies an infrared (IR) baseband PHY.</p>
</dd>

### -field <a id="WDI_PHY_TYPE_OFDM"></a><a id="wdi_phy_type_ofdm"></a><b>WDI_PHY_TYPE_OFDM</b>

<dd>
<p>Specifies an orthogonal frequency division multiplexing (OFDM) 802.11a PHY.</p>
</dd>

### -field <a id="WDI_PHY_TYPE_HRDSSS"></a><a id="wdi_phy_type_hrdsss"></a><b>WDI_PHY_TYPE_HRDSSS</b>

<dd>
<p>Specifies a high-rate DSSS (HRDSSS) 802.11b PHY.</p>
</dd>

### -field <a id="WDI_PHY_TYPE_ERP"></a><a id="wdi_phy_type_erp"></a><b>WDI_PHY_TYPE_ERP</b>

<dd>
<p>Specifies an extended-rate 802.11g PHY (ERP).</p>
</dd>

### -field <a id="WDI_PHY_TYPE_HT"></a><a id="wdi_phy_type_ht"></a><b>WDI_PHY_TYPE_HT</b>

<dd>
<p>Specifies a high-throughput (HT) 802.11n PHY. Each 802.11n PHY, whether dual-band or not, is specified as this PHY type.

</p>
</dd>

### -field <a id="WDI_PHY_TYPE_VHT"></a><a id="wdi_phy_type_vht"></a><b>WDI_PHY_TYPE_VHT</b>

<dd>
<p>Specifies a very high-throughput (VHT) 802.11ac PHY.</p>
</dd>

### -field <a id="WDI_PHY_TYPE_DMG"></a><a id="wdi_phy_type_dmg"></a><b>WDI_PHY_TYPE_DMG</b>

<dd>
<p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
<p>Specifies an 802.11ad PHY.</p>
</dd>

### -field <a id="WDI_PHY_TYPE_IHV_START"></a><a id="wdi_phy_type_ihv_start"></a><b>WDI_PHY_TYPE_IHV_START</b>

<dd>
<p>Specifies the start of the range that is used to define proprietary PHY types that are developed by an independent hardware vendor (IHV). 

</p>
</dd>

### -field <a id="WDI_PHY_TYPE_IHV_END"></a><a id="wdi_phy_type_ihv_end"></a><b>WDI_PHY_TYPE_IHV_END</b>

<dd>
<p>Specifies the end of the range that is used to define proprietary PHY types that are developed by an IHV. 

</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>