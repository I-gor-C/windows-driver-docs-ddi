---
UID: NE.windot11._DOT11_PHY_TYPE~r1
title: DOT11_PHY_TYPE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_phy_type.htm
ms.assetid: 45ef8085-512e-4f9b-a7ea-e4f445555cf8
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_PHY_TYPE
req.alt-loc: windot11.h
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
ms.keywords: PRINTER_EVENT_ATTRIBUTES_INFO, PRINTER_EVENT_ATTRIBUTES_INFO, *PPRINTER_EVENT_ATTRIBUTES_INFO
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_PHY_TYPE enumeration



## -description

## -syntax

````
typedef enum _DOT11_PHY_TYPE { 
  dot11_phy_type_unknown     = 0,
  dot11_phy_type_any         = dot11_phy_type_unknown,
  dot11_phy_type_fhss        = 1,
  dot11_phy_type_dsss        = 2,
  dot11_phy_type_irbaseband  = 3,
  dot11_phy_type_ofdm        = 4,
  dot11_phy_type_hrdsss      = 5,
  dot11_phy_type_erp         = 6,
  dot11_phy_type_ht          = 7,
  dot11_phy_type_vht         = 8,
  dot11_phy_type_IHV_start   = 0x80000000,
  dot11_phy_type_IHV_end     = 0xffffffff
} DOT11_PHY_TYPE, *PDOT11_PHY_TYPE;
````


## -enum-fields
<dl>

### -field <a id="dot11_phy_type_unknown"></a><a id="DOT11_PHY_TYPE_UNKNOWN"></a><b>dot11_phy_type_unknown</b>

<dd>
<p>Specifies an unknown or uninitialized PHY type.</p>
</dd>

### -field <a id="dot11_phy_type_any"></a><a id="DOT11_PHY_TYPE_ANY"></a><b>dot11_phy_type_any</b>

<dd>
<p>Specifies an unknown or uninitialized PHY type.</p>
</dd>

### -field <a id="dot11_phy_type_fhss"></a><a id="DOT11_PHY_TYPE_FHSS"></a><b>dot11_phy_type_fhss</b>

<dd>
<p>Specifies a frequency-hopping spread-spectrum (FHSS) PHY.</p>
</dd>

### -field <a id="dot11_phy_type_dsss"></a><a id="DOT11_PHY_TYPE_DSSS"></a><b>dot11_phy_type_dsss</b>

<dd>
<p>Specifies a direct sequence spread spectrum (DSSS) PHY.</p>
</dd>

### -field <a id="dot11_phy_type_irbaseband"></a><a id="DOT11_PHY_TYPE_IRBASEBAND"></a><b>dot11_phy_type_irbaseband</b>

<dd>
<p>Specifies an infrared (IR) baseband PHY.</p>
</dd>

### -field <a id="dot11_phy_type_ofdm"></a><a id="DOT11_PHY_TYPE_OFDM"></a><b>dot11_phy_type_ofdm</b>

<dd>
<p>Specifies an orthogonal frequency division multiplexing (OFDM) 802.11a PHY.</p>
</dd>

### -field <a id="dot11_phy_type_hrdsss"></a><a id="DOT11_PHY_TYPE_HRDSSS"></a><b>dot11_phy_type_hrdsss</b>

<dd>
<p>Specifies a high-rate DSSS (HRDSSS) 802.11b PHY.</p>
</dd>

### -field <a id="dot11_phy_type_erp"></a><a id="DOT11_PHY_TYPE_ERP"></a><b>dot11_phy_type_erp</b>

<dd>
<p>Specifies an extended-rate 802.11g PHY (ERP).</p>
</dd>

### -field <a id="dot11_phy_type_ht"></a><a id="DOT11_PHY_TYPE_HT"></a><b>dot11_phy_type_ht</b>

<dd>
<p>Specifies a high-throughput (HT) 802.11n PHY. Each 802.11n PHY, whether dual-band or not, is
     specified as this PHY type.</p>
</dd>

### -field <a id="dot11_phy_type_vht"></a><a id="DOT11_PHY_TYPE_VHT"></a><b>dot11_phy_type_vht</b>

<dd>
<p>Specifies a very high-throughput (VHT) 802.11ac PHY.</p>
</dd>

### -field <a id="dot11_phy_type_IHV_start"></a><a id="dot11_phy_type_ihv_start"></a><a id="DOT11_PHY_TYPE_IHV_START"></a><b>dot11_phy_type_IHV_start</b>

<dd>
<p>Specifies the start of the range that is used to define proprietary PHY types that are developed
     by an independent hardware vendor (IHV).
     </p>
<p>The 
     <b>dot11_phy_type_IHV_start</b> enumerator value is valid only when the miniport driver is operating in
     Extensible Station (ExtSTA) mode.</p>
</dd>

### -field <a id="dot11_phy_type_IHV_end"></a><a id="dot11_phy_type_ihv_end"></a><a id="DOT11_PHY_TYPE_IHV_END"></a><b>dot11_phy_type_IHV_end</b>

<dd>
<p>Specifies the end of the range that is used to define proprietary PHY types that are developed by
     an IHV.
     </p>
<p>The 
     <b>dot11_phy_type_IHV_end</b> enumerator value is valid only when the miniport driver is operating in
     ExtSTA mode.</p>
</dd>
</dl>

## -remarks
<p>An IHV can assign a value for its proprietary PHY types from 
    <b>dot11_phy_type_IHV_start</b> through 
    <b>dot11_phy_type_IHV_end</b>. The IHV must assign a unique number from this range for each of its
    proprietary PHY types.</p>

<p>An IHV can assign a value for its proprietary PHY types from 
    <b>dot11_phy_type_IHV_start</b> through 
    <b>dot11_phy_type_IHV_end</b>. The IHV must assign a unique number from this range for each of its
    proprietary PHY types.</p>

<p>An IHV can assign a value for its proprietary PHY types from 
    <b>dot11_phy_type_IHV_start</b> through 
    <b>dot11_phy_type_IHV_end</b>. The IHV must assign a unique number from this range for each of its
    proprietary PHY types.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/770962e3-0339-46f8-a789-7c9bbf9e058f">
   DOT11_ASSOCIATION_COMPLETION_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569407">OID_DOT11_RECV_SENSITIVITY_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569413">OID_DOT11_SCAN_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569426">OID_DOT11_SUPPORTED_PHY_TYPES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_PHY_TYPE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
