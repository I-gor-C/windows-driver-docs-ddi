---
UID: NE.wwan._WWAN_ACTIVATION_STATE
title: WWAN_ACTIVATION_STATE
author: windows-driver-content
description: The WWAN_ACTIVATION_STATE enumeration lists the different Packet Data Protocol (PDP) context activation states that are supported by the MB device.
old-location: netvista\wwan_activation_state.htm
ms.assetid: ca5caf9d-5c73-4516-bbc9-ee3ff9511e99
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
req.alt-api: WWAN_ACTIVATION_STATE
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

# WWAN_ACTIVATION_STATE enumeration



## -description
<p>The WWAN_ACTIVATION_STATE enumeration lists the different Packet Data Protocol (PDP) context
  activation states that are supported by the MB device.</p>


## -syntax

````
typedef enum _WWAN_ACTIVATION_STATE { 
  WwanActivationStateUnknown       = 0,
  WwanActivationStateActivated,
  WwanActivationStateActivating,
  WwanActivationStateDeactivated,
  WwanActivationStateDeactivating,
  WwanActivationStateMax
} WWAN_ACTIVATION_STATE, *PWWAN_ACTIVATION_STATE;
````


## -enum-fields
<dl>

### -field <a id="WwanActivationStateUnknown"></a><a id="wwanactivationstateunknown"></a><a id="WWANACTIVATIONSTATEUNKNOWN"></a><b>WwanActivationStateUnknown</b>

<dd>
<p>The activation state is unknown.</p>
</dd>

### -field <a id="WwanActivationStateActivated"></a><a id="wwanactivationstateactivated"></a><a id="WWANACTIVATIONSTATEACTIVATED"></a><b>WwanActivationStateActivated</b>

<dd>
<p>The packet context is activated.</p>
</dd>

### -field <a id="WwanActivationStateActivating"></a><a id="wwanactivationstateactivating"></a><a id="WWANACTIVATIONSTATEACTIVATING"></a><b>WwanActivationStateActivating</b>

<dd>
<p>The packet context is currently in the process of getting activated.</p>
</dd>

### -field <a id="WwanActivationStateDeactivated"></a><a id="wwanactivationstatedeactivated"></a><a id="WWANACTIVATIONSTATEDEACTIVATED"></a><b>WwanActivationStateDeactivated</b>

<dd>
<p>The packet context is not activated.</p>
</dd>

### -field <a id="WwanActivationStateDeactivating"></a><a id="wwanactivationstatedeactivating"></a><a id="WWANACTIVATIONSTATEDEACTIVATING"></a><b>WwanActivationStateDeactivating</b>

<dd>
<p>The packet context is currently in the process of getting deactivated.</p>
</dd>

### -field <a id="WwanActivationStateMax"></a><a id="wwanactivationstatemax"></a><a id="WWANACTIVATIONSTATEMAX"></a><b>WwanActivationStateMax</b>

<dd>
<p>The total number of PDP activation states.</p>
</dd>
</dl>

## -remarks
<p>Miniport drivers use the 
    <b>WwanActivationStateActivating</b> and 
    <b>WwanActivationStateDeactivating</b> transient states when responding to 
    <i>query</i> requests. Miniport driver should not return these states when processing 
    <i>set</i> requests. Miniport drivers must only send 
    <i>set</i> indications after they have successfully activated or deactivated a PDP context, and not
    immediately after receiving the request.</p>

<p>Miniport drivers use the 
    <b>WwanActivationStateActivating</b> and 
    <b>WwanActivationStateDeactivating</b> transient states when responding to 
    <i>query</i> requests. Miniport driver should not return these states when processing 
    <i>set</i> requests. Miniport drivers must only send 
    <i>set</i> indications after they have successfully activated or deactivated a PDP context, and not
    immediately after receiving the request.</p>

<p>Miniport drivers use the 
    <b>WwanActivationStateActivating</b> and 
    <b>WwanActivationStateDeactivating</b> transient states when responding to 
    <i>query</i> requests. Miniport driver should not return these states when processing 
    <i>set</i> requests. Miniport drivers must only send 
    <i>set</i> indications after they have successfully activated or deactivated a PDP context, and not
    immediately after receiving the request.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571235">WWAN_SET_CONTEXT_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_ACTIVATION_STATE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
