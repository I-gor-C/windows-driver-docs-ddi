---
UID: NS.wwan._WWAN_PIN_ACTION
title: WWAN_PIN_ACTION
author: windows-driver-content
description: The WWAN_PIN_ACTION structure represents actions to perform with a Personal Identification Number (PIN).
old-location: netvista\wwan_pin_action.htm
ms.assetid: 4edd0bc1-cd50-460b-92e1-7b2440ae3861
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_PIN_ACTION
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
ms.keywords: WWAN_PIN_ACTION, WWAN_PIN_ACTION, *PWWAN_PIN_ACTION
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_PIN_ACTION structure



## -description
<p>The WWAN_PIN_ACTION structure represents actions to perform with a Personal Identification Number
  (PIN).</p>


## -syntax

````
typedef struct _WWAN_PIN_ACTION {
  WWAN_PIN_TYPE      PinType;
  WWAN_PIN_OPERATION PinOperation;
  WCHAR              Pin[WWAN_PIN_LEN];
  WCHAR              NewPin[WWAN_PIN_LEN];
} WWAN_PIN_ACTION, *PWWAN_PIN_ACTION;
````


## -struct-fields
<dl>

### -field <b>PinType</b>

<dd>
<p>The type of the PIN on which to perform the action.</p>
</dd>

### -field <b>PinOperation</b>

<dd>
<p>The action to perform with the PIN.</p>
</dd>

### -field <b>Pin</b>

<dd>
<p>A NULL-terminated string that represents the PIN value to perform the action with, or the PIN
     value required to enable/disable PIN settings. This member is a numeric value and applies for all values of 
     <b>PinOperation</b> .</p>
</dd>

### -field <b>NewPin</b>

<dd>
<p>A NULL-terminated string that represents the new PIN value to set when 
     <b>PinOperation</b> is 
     <b>WwanPinOperationChange</b> or 
     <b>WwanPinOperationEnter</b>, for 
     <b>PinType</b><b>WwanPinTypePuk1</b> or 
     <b>WwanPinTypePuk2</b>. This member is a numeric value.</p>
</dd>
</dl>

## -remarks
<p>When 
    <b>PinType</b> is 
    <b>WwanPinTypePuk1</b> or 
    <b>WwanPinTypePuk2</b>, 
    <b>Pin</b> represents the corresponding PUK key.</p>

<p>When 
    <b>PinType</b> is 
    <b>WwanPinTypePuk1</b> or 
    <b>WwanPinTypePuk2, WwanPinOperationEnter</b> is the only supported value for 
    <b>PinOperation</b> .</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571221">WWAN_PIN_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571219">WWAN_PIN_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567922">NDIS_WWAN_SET_PIN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PIN_ACTION structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
