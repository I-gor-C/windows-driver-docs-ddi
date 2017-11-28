---
UID: NE.wdm._KINTERRUPT_MODE
title: KINTERRUPT_MODE
author: windows-driver-content
description: The KINTERRUPT_MODE enumeration type indicates whether an interrupt is level-triggered or edge-triggered.
old-location: kernel\kinterrupt_mode.htm
old-project: kernel
ms.assetid: 2f00fe3f-d73d-4f0f-a1dd-ae72fa57e55d
ms.author: windowsdriverdev
ms.date: 11/20/2017
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
req.alt-api: KINTERRUPT_MODE
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# KINTERRUPT_MODE enumeration



## -description
<p>The <b>KINTERRUPT_MODE</b> enumeration type indicates whether an interrupt is level-triggered or edge-triggered.</p>


## -syntax

````
typedef enum _KINTERRUPT_MODE { 
  LevelSensitive  = 0,
  Latched         = 1
} KINTERRUPT_MODE;
````


## -enum-fields
<dl>

### -field <a id="LevelSensitive"></a><a id="levelsensitive"></a><a id="LEVELSENSITIVE"></a><b>LevelSensitive</b>

<dd>
<p>The interrupt is level-triggered. This is the mode for traditional PCI line-based interrupts.</p>
</dd>

### -field <a id="Latched"></a><a id="latched"></a><a id="LATCHED"></a><b>Latched</b>

<dd>
<p>The interrupt is edge-triggered. This is the mode for PCI message-signaled interrupts. </p>
</dd>
</dl>

## -remarks
<p>The interrupt mode is an electrical characteristic of the interrupt. A device signals a level-triggered interrupt by changing the voltage on the interrupt pin, and holding it there until the processor signals that the interrupt is received. In contrast, to signal an edge-triggered interrupt, the device changes the voltage state for a fixed period of time, before reverting to the original voltage state.</p>

<p>The interrupt mode is an electrical characteristic of the interrupt. A device signals a level-triggered interrupt by changing the voltage on the interrupt pin, and holding it there until the processor signals that the interrupt is received. In contrast, to signal an edge-triggered interrupt, the device changes the voltage state for a fixed period of time, before reverting to the original voltage state.</p>

<p>The interrupt mode is an electrical characteristic of the interrupt. A device signals a level-triggered interrupt by changing the voltage on the interrupt pin, and holding it there until the processor signals that the interrupt is received. In contrast, to signal an edge-triggered interrupt, the device changes the voltage state for a fixed period of time, before reverting to the original voltage state.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554243">KINTERRUPT_POLARITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548378">IoConnectInterruptEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KINTERRUPT_MODE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
