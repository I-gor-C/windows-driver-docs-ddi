---
UID: NE.usb._USB_CONTROLLER_FLAVOR
title: USB_CONTROLLER_FLAVOR
author: windows-driver-content
description: The USB_CONTROLLER_FLAVOR enumeration specifies the type of USB host controller.
old-location: buses\usb_controller_flavor.htm
old-project: usbref
ms.assetid: c732fe90-50fb-4f6e-b42e-cb35c1ed0091
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: URS_CONFIG, URS_CONFIG, *PURS_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: usb.h
req.include-header: Usb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_CONTROLLER_FLAVOR
req.alt-loc: usb.h
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

# USB_CONTROLLER_FLAVOR enumeration



## -description
<p>The <b>USB_CONTROLLER_FLAVOR</b> enumeration specifies the type of USB host controller.</p>


## -syntax

````
typedef enum _USB_CONTROLLER_FLAVOR { 
  USB_HcGeneric        = 0,
  OHCI_Generic         = 100,
  OHCI_Hydra           = 101,
  OHCI_NEC             = 102,
  UHCI_Generic         = 200,
  UHCI_Piix4           = 201,
  UHCI_Piix3           = 202,
  UHCI_Ich2            = 203,
  UHCI_Ich1            = 205,
  UHCI_Ich3m           = 206,
  UHCI_Ich4            = 207,
  UHCI_Ich5            = 208,
  UHCI_Ich6            = 209,
  UHCI_Intel           = 249,
  UHCI_VIA             = 250,
  UHCI_VIA_x01         = 251,
  UHCI_VIA_x02         = 252,
  UHCI_VIA_x03         = 253,
  UHCI_VIA_x04         = 254,
  UHCI_VIA_x0E_FIFO    = 264,
  EHCI_Generic         = 1000,
  EHCI_NEC             = 2000,
  EHCI_Lucent          = 3000,
  EHCI_NVIDIA_Tegra2   = 4000,
  EHCI_NVIDIA_Tegra3   = 4001,
  EHCI_Intel_Medfield  = 5001
} USB_CONTROLLER_FLAVOR;
````


## -enum-fields
<dl>

### -field <a id="USB_HcGeneric"></a><a id="usb_hcgeneric"></a><a id="USB_HCGENERIC"></a><b>USB_HcGeneric</b>

<dd>
<p>Indicates a generic host controller.</p>
</dd>

### -field <a id="OHCI_Generic"></a><a id="ohci_generic"></a><a id="OHCI_GENERIC"></a><b>OHCI_Generic</b>

<dd>
<p>Indicates a generic OHCI host controller.</p>
</dd>

### -field <a id="OHCI_Hydra"></a><a id="ohci_hydra"></a><a id="OHCI_HYDRA"></a><b>OHCI_Hydra</b>

<dd>
<p>Indicates a Hydra host controller.</p>
</dd>

### -field <a id="OHCI_NEC"></a><a id="ohci_nec"></a><b>OHCI_NEC</b>

<dd>
<p>Indicates a NEC host controller.</p>
</dd>

### -field <a id="UHCI_Generic"></a><a id="uhci_generic"></a><a id="UHCI_GENERIC"></a><b>UHCI_Generic</b>

<dd>
<p>Indicates a generic UHCI host controller.</p>
</dd>

### -field <a id="UHCI_Piix4"></a><a id="uhci_piix4"></a><a id="UHCI_PIIX4"></a><b>UHCI_Piix4</b>

<dd>
<p>Indicates an Intel PIIX4 UHCI host controller.</p>
</dd>

### -field <a id="UHCI_Piix3"></a><a id="uhci_piix3"></a><a id="UHCI_PIIX3"></a><b>UHCI_Piix3</b>

<dd>
<p>Indicates an Intel PIIX3 UHCI host controller.</p>
</dd>

### -field <a id="UHCI_Ich2"></a><a id="uhci_ich2"></a><a id="UHCI_ICH2"></a><b>UHCI_Ich2</b>

<dd>
<p>Indicates an Intel ICH2 UHCI host controller.</p>
</dd>

### -field <a id="UHCI_Ich1"></a><a id="uhci_ich1"></a><a id="UHCI_ICH1"></a><b>UHCI_Ich1</b>

<dd>
<p>Indicates an Intel 815 ICH1 UHCI host controller.</p>
</dd>

### -field <a id="UHCI_Ich3m"></a><a id="uhci_ich3m"></a><a id="UHCI_ICH3M"></a><b>UHCI_Ich3m</b>

<dd>
<p>Indicates an Intel ICH3m UHCI host controller.</p>
</dd>

### -field <a id="UHCI_Ich4"></a><a id="uhci_ich4"></a><a id="UHCI_ICH4"></a><b>UHCI_Ich4</b>

<dd>
<p>Indicates an Intel ICH4m UHCI host controller.</p>
</dd>

### -field <a id="UHCI_Ich5"></a><a id="uhci_ich5"></a><a id="UHCI_ICH5"></a><b>UHCI_Ich5</b>

<dd>
<p>Indicates an Intel ICH5m UHCI host controller.</p>
</dd>

### -field <a id="UHCI_Ich6"></a><a id="uhci_ich6"></a><a id="UHCI_ICH6"></a><b>UHCI_Ich6</b>

<dd>
<p>Indicates an Intel ICH6m UHCI host controller.</p>
</dd>

### -field <a id="UHCI_Intel"></a><a id="uhci_intel"></a><a id="UHCI_INTEL"></a><b>UHCI_Intel</b>

<dd>
<p>Indicates a generic Intel UHCI host controller.</p>
</dd>

### -field <a id="UHCI_VIA"></a><a id="uhci_via"></a><b>UHCI_VIA</b>

<dd>
<p>Indicates a generic VIA UHCI host controller.</p>
</dd>

### -field <a id="UHCI_VIA_x01"></a><a id="uhci_via_x01"></a><a id="UHCI_VIA_X01"></a><b>UHCI_VIA_x01</b>

<dd>
<p>Indicates a Revision 1 VIA UHCI host controller.</p>
</dd>

### -field <a id="UHCI_VIA_x02"></a><a id="uhci_via_x02"></a><a id="UHCI_VIA_X02"></a><b>UHCI_VIA_x02</b>

<dd>
<p>Indicates a Revision 2 VIA UHCI host controller.</p>
</dd>

### -field <a id="UHCI_VIA_x03"></a><a id="uhci_via_x03"></a><a id="UHCI_VIA_X03"></a><b>UHCI_VIA_x03</b>

<dd>
<p>Indicates a Revision 3 VIA UHCI host controller.</p>
</dd>

### -field <a id="UHCI_VIA_x04"></a><a id="uhci_via_x04"></a><a id="UHCI_VIA_X04"></a><b>UHCI_VIA_x04</b>

<dd>
<p>Indicates a Revision 4 VIA UHCI host controller.</p>
</dd>

### -field <a id="UHCI_VIA_x0E_FIFO"></a><a id="uhci_via_x0e_fifo"></a><a id="UHCI_VIA_X0E_FIFO"></a><b>UHCI_VIA_x0E_FIFO</b>

<dd>
<p>Indicates a FIFO Revision VIA UHCI host controller.</p>
</dd>

### -field <a id="EHCI_Generic"></a><a id="ehci_generic"></a><a id="EHCI_GENERIC"></a><b>EHCI_Generic</b>

<dd>
<p>Indicates a generic EHCI host controller.</p>
</dd>

### -field <a id="EHCI_NEC"></a><a id="ehci_nec"></a><b>EHCI_NEC</b>

<dd>
<p>Indicates an NEC EHCI host controller.</p>
</dd>

### -field <a id="EHCI_Lucent"></a><a id="ehci_lucent"></a><a id="EHCI_LUCENT"></a><b>EHCI_Lucent</b>

<dd>
<p>Indicates an EHCI Lucent host controller.</p>
</dd>

### -field <a id="EHCI_NVIDIA_Tegra2"></a><a id="ehci_nvidia_tegra2"></a><a id="EHCI_NVIDIA_TEGRA2"></a><b>EHCI_NVIDIA_Tegra2</b>

<dd>
<p>Indicates a Revision 2 NVIDIA Tegra EHCI host controller.</p>
</dd>

### -field <a id="EHCI_NVIDIA_Tegra3"></a><a id="ehci_nvidia_tegra3"></a><a id="EHCI_NVIDIA_TEGRA3"></a><b>EHCI_NVIDIA_Tegra3</b>

<dd>
<p>Indicates a Revision 3 NVIDIA Tegra EHCI host controller.</p>
</dd>

### -field <a id="EHCI_Intel_Medfield"></a><a id="ehci_intel_medfield"></a><a id="EHCI_INTEL_MEDFIELD"></a><b>EHCI_Intel_Medfield</b>

<dd>
<p>Indicates an Intel Medfield host controller.</p>
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
<dt>Usb.h (include Usb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_controller_info_0">USB_CONTROLLER_INFO_0</a>
</dt>
<dt>
<a href="buses.usb_enumerations">USB Constants and Enumerations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_CONTROLLER_FLAVOR enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
