---
UID: NE.wwan._WWAN_UICCSLOT_STATE
title: WWAN_UICCSLOT_STATE
author: windows-driver-content
description: The WWAN_UICCSLOT_STATE enumeration lists the different states of a UICC (SIM) card slot on a modem. The slot state represents a summary of both the slot state and the card state.
old-location: netvista\wwan_uiccslot_state.htm
old-project: netvista
ms.assetid: 63A3C2AA-6EBF-469D-933A-C51F5EC31C47
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_UICCSLOT_STATE
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

# WWAN_UICCSLOT_STATE enumeration



## -description
<p>The <b>WWAN_UICCSLOT_STATE</b> enumeration lists the different states of a UICC (SIM) card slot on a modem. The slot state represents a summary of both the slot state and the card state.</p>


## -syntax

````
typedef enum _WWAN_UICCSLOT_STATE { 
  UICCSlotStateUnknown,
  UICCSlotStateOffEmpty,
  UICCSlotStateOff,
  UICCSlotStateEmpty,
  UICCSlotStateNotReady,
  UICCSlotStateActive,
  UICCSlotStateError
} WWAN_UICCSLOT_STATE;
````


## -enum-fields
<dl>

### -field <a id="UICCSlotStateUnknown"></a><a id="uiccslotstateunknown"></a><a id="UICCSLOTSTATEUNKNOWN"></a><b>UICCSlotStateUnknown</b>

<dd>
<p>The modem is still in the process of initializing so the SIM slot state is not deterministic.</p>
</dd>

### -field <a id="UICCSlotStateOffEmpty"></a><a id="uiccslotstateoffempty"></a><a id="UICCSLOTSTATEOFFEMPTY"></a><b>UICCSlotStateOffEmpty</b>

<dd>
<p>The card slot is powered off and empty. An implementation that is unable to determine the presence of a card in a slot that is powered off reports its state as <i>Off</i>.</p>
</dd>

### -field <a id="UICCSlotStateOff"></a><a id="uiccslotstateoff"></a><a id="UICCSLOTSTATEOFF"></a><b>UICCSlotStateOff</b>

<dd>
<p>The card slot is powered off and a card is present.</p>
</dd>

### -field <a id="UICCSlotStateEmpty"></a><a id="uiccslotstateempty"></a><a id="UICCSLOTSTATEEMPTY"></a><b>UICCSlotStateEmpty</b>

<dd>
<p>The card slot is powered on but no card is present.</p>
</dd>

### -field <a id="UICCSlotStateNotReady"></a><a id="uiccslotstatenotready"></a><a id="UICCSLOTSTATENOTREADY"></a><b>UICCSlotStateNotReady</b>

<dd>
<p>The card in the slot is not ready; i.e., it has been reset but has not finished initializing. It cannot be used at this time.</p>
</dd>

### -field <a id="UICCSlotStateActive"></a><a id="uiccslotstateactive"></a><a id="UICCSLOTSTATEACTIVE"></a><b>UICCSlotStateActive</b>

<dd>
<p>The card in the slot is available and ready to accept commands. This has no association with the SIM PIN locked state.</p>
</dd>

### -field <a id="UICCSlotStateError"></a><a id="uiccslotstateerror"></a><a id="UICCSLOTSTATEERROR"></a><b>UICCSlotStateError</b>

<dd>
<p>The card in the slot is in an error state and cannot be used.</p>
</dd>
</dl>

## -remarks
<p>The set of reported states is constrained by the capability of the slot hardware. In the most restrictive case, the slot hardware may only be able to determine that a card is present when it is powered on and active; in such a case the <b>OffEmpty</b> and <b>Off</b> states will not be reported.</p>

<p>The set of reported states is constrained by the capability of the slot hardware. In the most restrictive case, the slot hardware may only be able to determine that a card is present when it is powered on and active; in such a case the <b>OffEmpty</b> and <b>Off</b> states will not be reported.</p>

<p>The set of reported states is constrained by the capability of the slot hardware. In the most restrictive case, the slot hardware may only be able to determine that a card is present when it is powered on and active; in such a case the <b>OffEmpty</b> and <b>Off</b> states will not be reported.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
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
<a href="..\wwan\ns-wwan--wwan-slot-info.md">WWAN_SLOT_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_UICCSLOT_STATE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
