---
UID: NE.wwan._WWAN_REGISTER_MODE
title: WWAN_REGISTER_MODE
author: windows-driver-content
description: The WWAN_REGISTER_MODE enumeration lists the different network selection modes which defines the way the device should select a network while registering.
old-location: netvista\wwan_register_mode.htm
old-project: netvista
ms.assetid: 608d041c-1034-49cf-b8da-cb3f7769ac55
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
req.alt-api: WWAN_REGISTER_MODE
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

# WWAN_REGISTER_MODE enumeration



## -description
<p>The WWAN_REGISTER_MODE enumeration lists the different network selection modes which defines the way
  the device should select a network while registering.</p>


## -syntax

````
typedef enum _WWAN_REGISTER_MODE { 
  WwanRegisterModeUnknown    = 0,
  WwanRegisterModeAutomatic,
  WwanRegisterModeManual,
  WwanRegisterModeMax
} WWAN_REGISTER_MODE, *PWWAN_REGISTER_MODE;
````


## -enum-fields
<dl>

### -field <a id="WwanRegisterModeUnknown"></a><a id="wwanregistermodeunknown"></a><a id="WWANREGISTERMODEUNKNOWN"></a><b>WwanRegisterModeUnknown</b>

<dd>
<p>It is not specified how the device registers with network providers.</p>
</dd>

### -field <a id="WwanRegisterModeAutomatic"></a><a id="wwanregistermodeautomatic"></a><a id="WWANREGISTERMODEAUTOMATIC"></a><b>WwanRegisterModeAutomatic</b>

<dd>
<p>Device automatically selects a network on which it should register.</p>
</dd>

### -field <a id="WwanRegisterModeManual"></a><a id="wwanregistermodemanual"></a><a id="WWANREGISTERMODEMANUAL"></a><b>WwanRegisterModeManual</b>

<dd>
<p>Device registers to a pre-selected (manually selected) network.</p>
</dd>

### -field <a id="WwanRegisterModeMax"></a><a id="wwanregistermodemax"></a><a id="WWANREGISTERMODEMAX"></a><b>WwanRegisterModeMax</b>

<dd>
<p>The total number of supported registration modes.</p>
</dd>
</dl>

## -remarks
<p><b>WwanRegisterModeAutomatic</b> and 
    <b>WwanRegisterModeManual</b> are the only acceptable values. Miniport drivers can return 
    <b>WwanRegisterModeManual</b> in cases where it is not able to get this value from device.</p>

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
<a href="..\wwan\ns-wwan--wwan-registration-state.md">WWAN_REGISTRATION_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_REGISTER_MODE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
