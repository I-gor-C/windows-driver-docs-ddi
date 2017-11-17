---
UID: NE.wwan._WWAN_PIN_OPERATION
title: WWAN_PIN_OPERATION
author: windows-driver-content
description: The WWAN_PIN_OPERATION enumeration lists the different Personal Identification Number (PIN) operations that are supported by the MB device.
old-location: netvista\wwan_pin_operation.htm
ms.assetid: 1b21b4b4-a35d-47c4-9cd6-e31e2dfbe59f
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_PIN_OPERATION
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
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_PIN_OPERATION enumeration



## -description
<p>The WWAN_PIN_OPERATION enumeration lists the different Personal Identification Number (PIN)
  operations that are supported by the MB device.</p>


## -syntax

````
typedef enum _WWAN_PIN_OPERATION { 
  WwanPinOperationEnter    = 0,
  WwanPinOperationEnable,
  WwanPinOperationDisable,
  WwanPinOperationChange,
  WwanPinOperationMax
} WWAN_PIN_OPERATION, *PWWAN_PIN_OPERATION;
````


## -enum-fields
<dl>

### -field <a id="WwanPinOperationEnter"></a><a id="wwanpinoperationenter"></a><a id="WWANPINOPERATIONENTER"></a><b>WwanPinOperationEnter</b>

<dd>
<p>Enter the specified PIN into the device.</p>
</dd>

### -field <a id="WwanPinOperationEnable"></a><a id="wwanpinoperationenable"></a><a id="WWANPINOPERATIONENABLE"></a><b>WwanPinOperationEnable</b>

<dd>
<p>Enable the specified PIN.</p>
</dd>

### -field <a id="WwanPinOperationDisable"></a><a id="wwanpinoperationdisable"></a><a id="WWANPINOPERATIONDISABLE"></a><b>WwanPinOperationDisable</b>

<dd>
<p>Disable the specified PIN.</p>
</dd>

### -field <a id="WwanPinOperationChange"></a><a id="wwanpinoperationchange"></a><a id="WWANPINOPERATIONCHANGE"></a><b>WwanPinOperationChange</b>

<dd>
<p>Change the specified PIN.</p>
</dd>

### -field <a id="WwanPinOperationMax"></a><a id="wwanpinoperationmax"></a><a id="WWANPINOPERATIONMAX"></a><b>WwanPinOperationMax</b>

<dd>
<p>The total number of supported PIN operations.</p>
</dd>
</dl>

## -remarks
<p>If a PIN disable operation for a given PIN type is tried when that PIN type is locked, miniport
    drivers can either fail the request with WWAN_STATUS_PIN_REQUIRED or they can successfully complete the
    request. If miniport drivers complete the request successfully, the disable operation should also unlock
    the PIN.</p>

<p>If a PIN disable operation for a given PIN type is tried when that PIN type is locked, miniport
    drivers can either fail the request with WWAN_STATUS_PIN_REQUIRED or they can successfully complete the
    request. If miniport drivers complete the request successfully, the disable operation should also unlock
    the PIN.</p>

<p>If a PIN disable operation for a given PIN type is tried when that PIN type is locked, miniport
    drivers can either fail the request with WWAN_STATUS_PIN_REQUIRED or they can successfully complete the
    request. If miniport drivers complete the request successfully, the disable operation should also unlock
    the PIN.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571213">WWAN_PIN_ACTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PIN_OPERATION enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
