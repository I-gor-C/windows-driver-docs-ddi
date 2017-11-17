---
UID: NE.bthddi._SCO_DISCONNECT_REASON
title: SCO_DISCONNECT_REASON
author: windows-driver-content
description: The SCO_DISCONNECT_REASON enumeration type gives the reason an SCO channel has been disconnected.
old-location: bltooth\sco_disconnect_reason.htm
ms.assetid: bca4bfc6-d44f-4b10-a30a-ba2acefad7a9
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: bltooth
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SCO_DISCONNECT_REASON
req.alt-loc: bthddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback
   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access
   paged memory)
ms.keywords: IBidiSpl2, UnbindDevice, IBidiSpl2::UnbindDevice
req.iface: IBidiSpl2
---

# SCO_DISCONNECT_REASON enumeration



## -description
<p>The SCO_DISCONNECT_REASON enumeration type gives the reason an SCO channel has been
  disconnected.</p>


## -syntax

````
typedef enum _SCO_DISCONNECT_REASON { 
  ScoHciDisconnect      = 0,
  ScoDisconnectRequest  = 1,
  ScoRadioPoweredDown   = 2,
  ScoHardwareRemoval    = 3
} SCO_DISCONNECT_REASON, *PSCO_DISCONNECT_REASON;
````


## -enum-fields
<dl>

### -field <a id="ScoHciDisconnect"></a><a id="scohcidisconnect"></a><a id="SCOHCIDISCONNECT"></a><b>ScoHciDisconnect</b>

<dd>
<p>This value specifies to the profile driver that the Bluetooth driver stack has received a
     disconnect notification from the host controller interface (HCI) layer.</p>
</dd>

### -field <a id="ScoDisconnectRequest"></a><a id="scodisconnectrequest"></a><a id="SCODISCONNECTREQUEST"></a><b>ScoDisconnectRequest</b>

<dd>
<p>This value specifies to the profile driver that a disconnect request has been received from the
     remote device.</p>
</dd>

### -field <a id="ScoRadioPoweredDown"></a><a id="scoradiopowereddown"></a><a id="SCORADIOPOWEREDDOWN"></a><b>ScoRadioPoweredDown</b>

<dd>
<p>This value specifies to the profile driver that the local radio has been turned off.</p>
</dd>

### -field <a id="ScoHardwareRemoval"></a><a id="scohardwareremoval"></a><a id="SCOHARDWAREREMOVAL"></a><b>ScoHardwareRemoval</b>

<dd>
<p>This value specifies to the profile driver that the local radio has been physically
     removed.</p>
</dd>
</dl>

## -remarks
<p>A value from this enumeration is used as the 
    <b>Reason</b> member of the 
    <a href="https://msdn.microsoft.com/2d3ae219-8a40-476c-b8eb-94f4c0566527">
    SCO_INDICATION_PARAMETERS</a> structure.</p>

<p>Hardware limitations may prevent the Bluetooth driver stack from distinguishing between 
    <b>ScoRadioPoweredDown</b> and 
    <b>ScoHardwareRemoval</b> events.</p>

<p>Currently, 
    <i>ScoHciDisconnect</i> is the only value the Bluetooth driver stack passes to the 
    <a href="https://msdn.microsoft.com/abc9fc88-6852-4bfb-8271-7a73a508c397">SCO Callback Function</a>.</p>

<p>A value from this enumeration is used as the 
    <b>Reason</b> member of the 
    <a href="https://msdn.microsoft.com/2d3ae219-8a40-476c-b8eb-94f4c0566527">
    SCO_INDICATION_PARAMETERS</a> structure.</p>

<p>Hardware limitations may prevent the Bluetooth driver stack from distinguishing between 
    <b>ScoRadioPoweredDown</b> and 
    <b>ScoHardwareRemoval</b> events.</p>

<p>Currently, 
    <i>ScoHciDisconnect</i> is the only value the Bluetooth driver stack passes to the 
    <a href="https://msdn.microsoft.com/abc9fc88-6852-4bfb-8271-7a73a508c397">SCO Callback Function</a>.</p>

<p>A value from this enumeration is used as the 
    <b>Reason</b> member of the 
    <a href="https://msdn.microsoft.com/2d3ae219-8a40-476c-b8eb-94f4c0566527">
    SCO_INDICATION_PARAMETERS</a> structure.</p>

<p>Hardware limitations may prevent the Bluetooth driver stack from distinguishing between 
    <b>ScoRadioPoweredDown</b> and 
    <b>ScoHardwareRemoval</b> events.</p>

<p>Currently, 
    <i>ScoHciDisconnect</i> is the only value the Bluetooth driver stack passes to the 
    <a href="https://msdn.microsoft.com/abc9fc88-6852-4bfb-8271-7a73a508c397">SCO Callback Function</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bthddi.h (include Bthddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536779">SCO_INDICATION_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/abc9fc88-6852-4bfb-8271-7a73a508c397">SCO Callback Function</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20SCO_DISCONNECT_REASON enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
