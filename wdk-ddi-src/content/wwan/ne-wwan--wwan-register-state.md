---
UID: NE.wwan._WWAN_REGISTER_STATE
title: WWAN_REGISTER_STATE
author: windows-driver-content
description: The WWAN_REGISTER_STATE enumeration lists the different provider network registration states that are supported by the MB device.
old-location: netvista\wwan_register_state.htm
old-project: netvista
ms.assetid: fba4e60e-c247-4466-9b0f-c8e7ffa594d2
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
req.alt-api: WWAN_REGISTER_STATE
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

# WWAN_REGISTER_STATE enumeration



## -description
<p>The WWAN_REGISTER_STATE enumeration lists the different provider network registration states that are
  supported by the MB device.</p>


## -syntax

````
typedef enum _WWAN_REGISTER_STATE { 
  WwanRegisterStateUnknown       = 0,
  WwanRegisterStateDeregistered,
  WwanRegisterStateSearching,
  WwanRegisterStateHome,
  WwanRegisterStateRoaming,
  WwanRegisterStatePartner,
  WwanRegisterStateDenied,
  WwanRegisterStateMax
} WWAN_REGISTER_STATE, *PWWAN_REGISTER_STATE;
````


## -enum-fields
<dl>

### -field <a id="WwanRegisterStateUnknown"></a><a id="wwanregisterstateunknown"></a><a id="WWANREGISTERSTATEUNKNOWN"></a><b>WwanRegisterStateUnknown</b>

<dd>
<p>The current registration state is unknown. The miniport driver may specify this state on a failure
     to set an appropriate 
     <i>WwanRegisterActionXxx</i>.</p>
</dd>

### -field <a id="WwanRegisterStateDeregistered"></a><a id="wwanregisterstatederegistered"></a><a id="WWANREGISTERSTATEDEREGISTERED"></a><b>WwanRegisterStateDeregistered</b>

<dd>
<p>The device is not registered and is not searching for network providers.</p>
</dd>

### -field <a id="WwanRegisterStateSearching"></a><a id="wwanregisterstatesearching"></a><a id="WWANREGISTERSTATESEARCHING"></a><b>WwanRegisterStateSearching</b>

<dd>
<p>The device is searching for a network provider.</p>
</dd>

### -field <a id="WwanRegisterStateHome"></a><a id="wwanregisterstatehome"></a><a id="WWANREGISTERSTATEHOME"></a><b>WwanRegisterStateHome</b>

<dd>
<p>The device is using the home network provider.</p>
</dd>

### -field <a id="WwanRegisterStateRoaming"></a><a id="wwanregisterstateroaming"></a><a id="WWANREGISTERSTATEROAMING"></a><b>WwanRegisterStateRoaming</b>

<dd>
<p>The device is using a network provider that supports roaming.</p>
</dd>

### -field <a id="WwanRegisterStatePartner"></a><a id="wwanregisterstatepartner"></a><a id="WWANREGISTERSTATEPARTNER"></a><b>WwanRegisterStatePartner</b>

<dd>
<p>The device is using a roaming network partner.</p>
</dd>

### -field <a id="WwanRegisterStateDenied"></a><a id="wwanregisterstatedenied"></a><a id="WWANREGISTERSTATEDENIED"></a><b>WwanRegisterStateDenied</b>

<dd>
<p>Registration of the device on visible networks has been denied. However, emergency voice calls may
     still be made. This value applies only to voice connections, and not to data connections.</p>
</dd>

### -field <a id="WwanRegisterStateMax"></a><a id="wwanregisterstatemax"></a><a id="WWANREGISTERSTATEMAX"></a><b>WwanRegisterStateMax</b>

<dd>
<p>The total number of supported registration states.</p>
</dd>
</dl>

## -remarks
<p>The current registration state is typically reflected in the device's user interface.</p>

<p>The 
    <b>WwanRegisterStatePartner</b> value indicates that the device is roaming on a preferred partner network,
    whereas 
    <b>WwanRegisterStateRoaming</b> value indicates that the device is just roaming. If the partner
    characterization of the roaming state is not available, the miniport driver should report 
    <b>WwanRegisterStateRoaming</b>.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_REGISTER_STATE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
