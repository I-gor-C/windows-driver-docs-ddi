---
UID: NE.wdm._KINTERRUPT_POLARITY
title: KINTERRUPT_POLARITY
author: windows-driver-content
description: The KINTERRUPT_POLARITY enumeration indicates how a device signals an interrupt request on an interrupt line.
old-location: kernel\kinterrupt_polarity.htm
old-project: kernel
ms.assetid: 2fcc4597-b169-43a8-b2bb-dd2dd66f29dc
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KINTERRUPT_POLARITY
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# KINTERRUPT_POLARITY enumeration



## -description
<p>The <b>KINTERRUPT_POLARITY</b> enumeration indicates how a device signals an interrupt request on an interrupt line.</p>


## -syntax

````
typedef enum _KINTERRUPT_POLARITY { 
  InterruptPolarityUnknown,
  InterruptActiveHigh,
  InterruptRisingEdge             = InterruptActiveHigh,
  InterruptActiveLow,
  InterruptFallingEdge            = InterruptActiveLow,
  InterruptActiveBoth,
  InterruptActiveBothTriggerLow   = InterruptActiveBoth,
  InterruptActiveBothTriggerHigh
} KINTERRUPT_POLARITY, *PKINTERRUPT_POLARITY;
````


## -enum-fields
<dl>

### -field <a id="InterruptPolarityUnknown"></a><a id="interruptpolarityunknown"></a><a id="INTERRUPTPOLARITYUNKNOWN"></a><b>InterruptPolarityUnknown</b>

<dd>
<p>The interrupt polarity is unknown.</p>
</dd>

### -field <a id="InterruptActiveHigh"></a><a id="interruptactivehigh"></a><a id="INTERRUPTACTIVEHIGH"></a><b>InterruptActiveHigh</b>

<dd>
<p>Active-high interrupt. The interrupt input type is level-triggered, and an interrupt request is indicated by a high signal level on the interrupt line. The request remains active as long as the line remains high.</p>
</dd>

### -field <a id="InterruptRisingEdge"></a><a id="interruptrisingedge"></a><a id="INTERRUPTRISINGEDGE"></a><b>InterruptRisingEdge</b>

<dd>
<p>Rising-edge-triggered interrupt. The interrupt input type is edge-triggered, and an interrupt request is indicated by a low-to-high transition on the interrupt line.</p>
</dd>

### -field <a id="InterruptActiveLow"></a><a id="interruptactivelow"></a><a id="INTERRUPTACTIVELOW"></a><b>InterruptActiveLow</b>

<dd>
<p>Active-low interrupt. The interrupt input type is level-triggered, and an interrupt request is indicated by a low signal level on the interrupt line. The request remains active as long as the line remains low.</p>
</dd>

### -field <a id="InterruptFallingEdge"></a><a id="interruptfallingedge"></a><a id="INTERRUPTFALLINGEDGE"></a><b>InterruptFallingEdge</b>

<dd>
<p>Falling-edge-triggered interrupt. The interrupt input type is edge-triggered, and an interrupt request is indicated by a high-to-low transition on the interrupt line.</p>
</dd>

### -field <a id="InterruptActiveBoth"></a><a id="interruptactiveboth"></a><a id="INTERRUPTACTIVEBOTH"></a><b>InterruptActiveBoth</b>

<dd>
<p>Active-both interrupt. The interrupt input type is edge-triggered, and an interrupt request is indicated by a low-to-high or a high-to-low transition on the interrupt line. After a low-to-high transition signals an interrupt request, the interrupt line remains high until a high-to-low transition signals the next interrupt request. Similarly, after a high-to-low transition signals an interrupt request, the interrupt line remains low until a low-to-high transition signals the next interrupt request.</p>
</dd>

### -field <a id="InterruptActiveBothTriggerLow"></a><a id="interruptactivebothtriggerlow"></a><a id="INTERRUPTACTIVEBOTHTRIGGERLOW"></a><b>InterruptActiveBothTriggerLow</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>

### -field <a id="InterruptActiveBothTriggerHigh"></a><a id="interruptactivebothtriggerhigh"></a><a id="INTERRUPTACTIVEBOTHTRIGGERHIGH"></a><b>InterruptActiveBothTriggerHigh</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>
</dl>

## -remarks
<p>A <b>KINTERRUPT_POLARITY</b> enumeration constant is frequently used in conjunction with a <a href="..\wdm\ne-wdm--kinterrupt-mode.md">KINTERRUPT_MODE</a> enumeration constant to describe an interrupt signal. A <b>KINTERRUPT_MODE</b> enumeration constant indicates whether the interrupt signal from a device is level-triggered or edge-triggered.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ne-wdm--kinterrupt-mode.md">KINTERRUPT_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KINTERRUPT_POLARITY enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
