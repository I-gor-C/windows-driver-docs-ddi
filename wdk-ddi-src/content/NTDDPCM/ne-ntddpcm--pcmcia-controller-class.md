---
UID: NE.ntddpcm._PCMCIA_CONTROLLER_CLASS
title: PCMCIA_CONTROLLER_CLASS
author: windows-driver-content
description: The PCMCIA_CONTROLLER_CLASS enumeration lists the different sorts of PC Card and CardBus controllers.
old-location: pcmcia\pcmcia_controller_class.htm
ms.assetid: d834d97c-cf2d-430b-8f54-b0b47ab1503c
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: PCMCIA
req.header: ntddpcm.h
req.include-header: Ntddpcm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCMCIA_CONTROLLER_CLASS
req.alt-loc: ntddpcm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL (See Remarks section.)
ms.keywords: PARCLASS_NEGOTIATION_MASK, PARCLASS_NEGOTIATION_MASK, *PPARCLASS_NEGOTIATION_MASK
req.iface: 
---

# PCMCIA_CONTROLLER_CLASS enumeration



## -description
<p>The PCMCIA_CONTROLLER_CLASS enumeration lists the different sorts of PC Card and CardBus controllers.</p>


## -syntax

````
typedef enum _PCMCIA_CONTROLLER_CLASS { 
  PcmciaInvalidControllerClass  = -1,
  PcmciaIntelCompatible         = 2,
  PcmciaCardBusCompatible       = 3,
  PcmciaElcController           = 4,
  PcmciaDatabook                = 5,
  PcmciaPciPcmciaBridge         = 6,
  PcmciaCirrusLogic             = 7,
  PcmciaTI                      = 8,
  PcmciaTopic                   = 9,
  PcmciaRicoh                   = 10,
  PcmciaDatabookCB              = 11,
  PcmciaOpti                    = 12,
  PcmciaTrid                    = 13,
  PcmciaO2Micro                 = 14,
  PcmciaNEC                     = 15,
  PcmciaNEC_98                  = 16
} PCMCIA_CONTROLLER_CLASS, *PPCMCIA_CONTROLLER_CLASS;
````


## -enum-fields
<dl>

### -field <a id="PcmciaInvalidControllerClass"></a><a id="pcmciainvalidcontrollerclass"></a><a id="PCMCIAINVALIDCONTROLLERCLASS"></a><b>PcmciaInvalidControllerClass</b>

<dd>
<p>Indicates that the controller class is invalid. </p>
</dd>

### -field <a id="PcmciaIntelCompatible"></a><a id="pcmciaintelcompatible"></a><a id="PCMCIAINTELCOMPATIBLE"></a><b>PcmciaIntelCompatible</b>

<dd>
<p>Indicates an Intel-compatible controller. </p>
</dd>

### -field <a id="PcmciaCardBusCompatible"></a><a id="pcmciacardbuscompatible"></a><a id="PCMCIACARDBUSCOMPATIBLE"></a><b>PcmciaCardBusCompatible</b>

<dd>
<p>Indicates a cardbus-compatible controller. </p>
</dd>

### -field <a id="PcmciaElcController"></a><a id="pcmciaelccontroller"></a><a id="PCMCIAELCCONTROLLER"></a><b>PcmciaElcController</b>

<dd>
<p>Indicates an ELC controller. </p>
</dd>

### -field <a id="PcmciaDatabook"></a><a id="pcmciadatabook"></a><a id="PCMCIADATABOOK"></a><b>PcmciaDatabook</b>

<dd>
<p>Indicates a controller from the Databook TCIC family of controllers. </p>
</dd>

### -field <a id="PcmciaPciPcmciaBridge"></a><a id="pcmciapcipcmciabridge"></a><a id="PCMCIAPCIPCMCIABRIDGE"></a><b>PcmciaPciPcmciaBridge</b>

<dd>
<p>Indicates a PCI to PCMCIA bridge. </p>
</dd>

### -field <a id="PcmciaCirrusLogic"></a><a id="pcmciacirruslogic"></a><a id="PCMCIACIRRUSLOGIC"></a><b>PcmciaCirrusLogic</b>

<dd>
<p>Indicates a CirrusLogic cardbus controller. </p>
</dd>

### -field <a id="PcmciaTI"></a><a id="pcmciati"></a><a id="PCMCIATI"></a><b>PcmciaTI</b>

<dd>
<p>Indicates a TI cardbus controller. </p>
</dd>

### -field <a id="PcmciaTopic"></a><a id="pcmciatopic"></a><a id="PCMCIATOPIC"></a><b>PcmciaTopic</b>

<dd>
<p>Indicates a Toshiba Topic cardbus controller. </p>
</dd>

### -field <a id="PcmciaRicoh"></a><a id="pcmciaricoh"></a><a id="PCMCIARICOH"></a><b>PcmciaRicoh</b>

<dd>
<p>Indicates a Ricoh cardbus controller. </p>
</dd>

### -field <a id="PcmciaDatabookCB"></a><a id="pcmciadatabookcb"></a><a id="PCMCIADATABOOKCB"></a><b>PcmciaDatabookCB</b>

<dd>
<p>Indicates a Databook cardbus controller. </p>
</dd>

### -field <a id="PcmciaOpti"></a><a id="pcmciaopti"></a><a id="PCMCIAOPTI"></a><b>PcmciaOpti</b>

<dd>
<p>Indicates an OPTI cardbus controller. </p>
</dd>

### -field <a id="PcmciaTrid"></a><a id="pcmciatrid"></a><a id="PCMCIATRID"></a><b>PcmciaTrid</b>

<dd>
<p>Indicates a TRID controller. </p>
</dd>

### -field <a id="PcmciaO2Micro"></a><a id="pcmciao2micro"></a><a id="PCMCIAO2MICRO"></a><b>PcmciaO2Micro</b>

<dd>
<p>Indicates an O2Micro cardbus controller. </p>
</dd>

### -field <a id="PcmciaNEC"></a><a id="pcmcianec"></a><a id="PCMCIANEC"></a><b>PcmciaNEC</b>

<dd>
<p>Indicates a Yenta-compliant NEC cardbus controller. </p>
</dd>

### -field <a id="PcmciaNEC_98"></a><a id="pcmcianec_98"></a><a id="PCMCIANEC_98"></a><b>PcmciaNEC_98</b>

<dd>
<p>Indicates a NEC cardbus controller.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddpcm.h (include Ntddpcm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537612">PCMCIA_SOCKET_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCMCIA\buses]:%20PCMCIA_CONTROLLER_CLASS enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
